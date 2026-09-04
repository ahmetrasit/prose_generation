import { dashboardConfig, firebaseConfig } from "./firebase-config.js";

const FIREBASE_VERSION = "12.18.0";
const PAGE_SIZE = 50;
const ACTIVE_STAGE_STATES = new Set(["active", "composing", "editing"]);
const ATTENTION_STATES = new Set(["failed", "attention", "stalled"]);
const ARTIFACT_ORDER = ["micro", "macro", "global", "consolidated", "editorial"];
const stageNames = {
  micro: "Micro scope",
  macro: "Macro scope",
  global: "Global scope",
  canonical: "Canonical",
  validator: "Validation",
};

const elements = Object.fromEntries(
  [
    "connection-dot", "connection-label", "sign-in", "manage-passcodes", "app-version", "run-id",
    "orchestrator-select", "refresh", "resume", "pause", "control-note",
    "metric-total", "metric-pending", "metric-active", "metric-agents",
    "metric-completed", "metric-attention", "metric-reruns",
    "attention-strip", "attention-title", "attention-detail", "show-attention",
    "queue-caption", "search", "status-filter", "task-rows", "empty-state",
    "previous-page", "next-page", "page-label", "reader-heading",
    "artifact-tabs", "reader-meta", "reader-content", "close-reader",
    "passcode-admin", "close-passcodes", "passcode-form", "passcode-label",
    "passcode-value", "generate-passcode", "allow-passcode", "created-passcode",
    "created-passcode-value", "copy-passcode", "passcode-result", "passcode-rows",
    "passcode-empty", "version-banner", "version-banner-text", "update-app",
  ].map((id) => [id, document.getElementById(id)])
);

const params = new URLSearchParams(window.location.search);
elements["app-version"].textContent = `v${dashboardConfig.appVersion}`;
document.title = `V5 Commentary Operations v${dashboardConfig.appVersion}`;
const state = {
  mode: firebaseConfig && params.get("local") !== "1" ? "firebase" : "local",
  runId: params.get("run") || dashboardConfig.defaultRunId,
  snapshot: emptySnapshot(),
  firebase: null,
  unsubscribe: [],
  selectedTaskId: null,
  selectedArtifact: null,
  page: 1,
  lastLoadAt: null,
  contentCache: new Map(),
  passcodes: {},
  adminOpen: false,
};

function emptySnapshot() {
  return { workers: {}, orchestrators: {}, tasks: {}, artifacts: {} };
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderInline(value) {
  return escapeHtml(value)
    .replace(
      /\{ar:([^,{}]*),\s*tr:([^,{}]*),\s*gloss:([^{}]*)\}/g,
      '<span class="markup-token"><span class="markup-ar" lang="ar" dir="rtl">$1</span><span class="markup-tr">$2</span><span class="markup-gloss">$3</span></span>'
    )
    .replace(/\{ar:([^{}]*)\}/g, '<span class="markup-ar" lang="ar" dir="rtl">$1</span>')
    .replace(/\{tr:([^{}]*)\}/g, '<span class="markup-tr">$1</span>')
    .replace(/\{gloss:([^{}]*)\}/g, '<span class="markup-gloss">$1</span>')
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

function renderMarkup(markdown) {
  const lines = String(markdown || "").replaceAll("\r\n", "\n").split("\n");
  const output = [];
  let paragraph = [];
  let list = [];
  const flushParagraph = () => {
    if (paragraph.length) output.push(`<p>${renderInline(paragraph.join(" "))}</p>`);
    paragraph = [];
  };
  const flushList = () => {
    if (list.length) output.push(`<ul>${list.map((item) => `<li>${renderInline(item)}</li>`).join("")}</ul>`);
    list = [];
  };
  for (const line of lines) {
    const heading = line.match(/^(#{1,3})\s+(.+)$/);
    const listItem = line.match(/^[-*]\s+(.+)$/);
    const quote = line.match(/^>\s?(.+)$/);
    if (heading) {
      flushParagraph();
      flushList();
      output.push(`<h${heading[1].length}>${renderInline(heading[2])}</h${heading[1].length}>`);
    } else if (listItem) {
      flushParagraph();
      list.push(listItem[1]);
    } else if (quote) {
      flushParagraph();
      flushList();
      output.push(`<blockquote>${renderInline(quote[1])}</blockquote>`);
    } else if (!line.trim()) {
      flushParagraph();
      flushList();
    } else {
      flushList();
      paragraph.push(line.trim());
    }
  }
  flushParagraph();
  flushList();
  return output.join("");
}

function compareRefs(first, second) {
  const a = first.split(":").map(Number);
  const b = second.split(":").map(Number);
  return a[0] - b[0] || a[1] - b[1];
}

function taskId(orchestratorId, ayahRef) {
  const [surah, ayah] = ayahRef.split(":").map(Number);
  return `${orchestratorId}--s${String(surah).padStart(3, "0")}-a${String(ayah).padStart(3, "0")}`;
}

function blankStages() {
  return Object.fromEntries(
    ["micro", "macro", "global", "canonical", "validator"].map((stage) => [
      stage,
      { status: "pending", attempt: 0, agent_id: null, updated_at: null },
    ])
  );
}

function tasksForRun() {
  const orchestrators = Object.values(state.snapshot.orchestrators || {})
    .filter((item) => item.run_id === state.runId);
  const tasks = [];
  for (const orchestrator of orchestrators) {
    for (const ayahRef of orchestrator.scope_refs || []) {
      const id = taskId(orchestrator.orchestrator_id, ayahRef);
      tasks.push(state.snapshot.tasks[id] || {
        task_id: id,
        run_id: state.runId,
        worker_id: orchestrator.worker_id,
        orchestrator_id: orchestrator.orchestrator_id,
        analysis_id: orchestrator.analysis_id,
        ayah_ref: ayahRef,
        status: "pending",
        stages: blankStages(),
        attention: [],
        artifact_kinds: [],
        updated_at: orchestrator.started_at,
      });
    }
  }
  return tasks.sort((a, b) => compareRefs(a.ayah_ref, b.ayah_ref) || a.orchestrator_id.localeCompare(b.orchestrator_id));
}

function displayStatus(task) {
  if (["failed", "attention"].includes(task.status)) return task.status;
  if (task.status === "active" && isStalled(task)) return "stalled";
  return task.status;
}

function isStalled(task) {
  const threshold = dashboardConfig.staleAfterMinutes * 60 * 1000;
  return activeStages(task).some(([, stage]) => (
    stage.updated_at && Date.now() - new Date(stage.updated_at).getTime() > threshold
  ));
}

function activeStages(task) {
  return Object.entries(task.stages || {}).filter(([, stage]) => ACTIVE_STAGE_STATES.has(stage.status));
}

function currentStep(task) {
  const active = activeStages(task);
  if (active.length) return active.map(([name]) => stageNames[name]).join(", ");
  const failed = Object.entries(task.stages || {}).find(([, value]) => ATTENTION_STATES.has(value.status));
  if (failed) return stageNames[failed[0]];
  if (task.status === "awaiting_validation") return "Validation";
  if (task.status === "completed") return "Done";
  const ready = Object.entries(task.stages || {}).find(([, value]) => value.status === "ready");
  return ready ? stageNames[ready[0]] : "Not started";
}

function agentsForTask(task) {
  return [...new Set(Object.values(task.stages || {}).map((stage) => stage.agent_id).filter(Boolean))];
}

function attemptCount(task) {
  return Math.max(0, ...Object.values(task.stages || {}).map((stage) => Number(stage.attempt || 0)));
}

function relativeTime(value) {
  if (!value) return "Never";
  const seconds = Math.max(0, Math.floor((Date.now() - new Date(value).getTime()) / 1000));
  if (seconds < 60) return `${seconds}s ago`;
  if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
  if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
  return `${Math.floor(seconds / 86400)}d ago`;
}

function statusGroup(task) {
  const status = displayStatus(task);
  if (ATTENTION_STATES.has(status)) return "attention";
  if (["active", "awaiting_validation"].includes(status)) return "active";
  return status;
}

function filteredTasks(tasks) {
  const needle = elements.search.value.trim().toLowerCase();
  const filter = elements["status-filter"].value;
  return tasks.filter((task) => {
    const text = [task.ayah_ref, task.orchestrator_id, ...agentsForTask(task)].join(" ").toLowerCase();
    return (!needle || text.includes(needle)) && (filter === "all" || statusGroup(task) === filter);
  });
}

function updateMetrics(tasks) {
  const active = tasks.filter((task) => statusGroup(task) === "active");
  const attention = tasks.filter((task) => statusGroup(task) === "attention");
  const agents = new Set(active.flatMap(agentsForTask));
  const reruns = tasks.filter((task) => attemptCount(task) > 1).length;
  elements["metric-total"].textContent = tasks.length.toLocaleString();
  elements["metric-pending"].textContent = tasks.filter((task) => task.status === "pending").length.toLocaleString();
  elements["metric-active"].textContent = active.length.toLocaleString();
  elements["metric-agents"].textContent = agents.size.toLocaleString();
  elements["metric-completed"].textContent = tasks.filter((task) => task.status === "completed").length.toLocaleString();
  elements["metric-attention"].textContent = attention.length.toLocaleString();
  elements["metric-reruns"].textContent = reruns.toLocaleString();
  elements["attention-strip"].hidden = attention.length === 0;
  const failures = attention.filter((task) => task.status === "failed").length;
  const stalled = attention.filter((task) => displayStatus(task) === "stalled").length;
  elements["attention-title"].textContent = `${attention.length} ayah${attention.length === 1 ? " needs" : "s need"} attention`;
  elements["attention-detail"].textContent = `${failures} failed, ${stalled} potentially stalled`;
}

function renderTable(tasks) {
  const filtered = filteredTasks(tasks);
  const pageCount = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
  state.page = Math.min(state.page, pageCount);
  const first = (state.page - 1) * PAGE_SIZE;
  const visible = filtered.slice(first, first + PAGE_SIZE);
  elements["task-rows"].replaceChildren();
  for (const task of visible) {
    const row = document.getElementById("task-row-template").content.firstElementChild.cloneNode(true);
    const status = displayStatus(task);
    const agents = agentsForTask(task);
    row.dataset.taskId = task.task_id;
    row.classList.toggle("selected", task.task_id === state.selectedTaskId);
    row.querySelector(".ayah-cell").textContent = task.ayah_ref;
    const badge = row.querySelector(".status-badge");
    badge.textContent = status.replaceAll("_", " ");
    badge.classList.add(status);
    row.querySelector(".step-cell").textContent = currentStep(task);
    row.querySelector(".agent-cell").textContent = agents.join(", ") || "-";
    row.querySelector(".attempt-cell").textContent = attemptCount(task) || "-";
    row.querySelector(".updated-cell").textContent = relativeTime(task.updated_at);
    row.addEventListener("click", () => selectTask(task));
    row.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") selectTask(task);
    });
    elements["task-rows"].append(row);
  }
  elements["empty-state"].hidden = visible.length !== 0;
  elements["queue-caption"].textContent = `${filtered.length.toLocaleString()} shown of ${tasks.length.toLocaleString()} ayat`;
  elements["page-label"].textContent = `Page ${state.page} of ${pageCount}`;
  elements["previous-page"].disabled = state.page <= 1;
  elements["next-page"].disabled = state.page >= pageCount;
}

function orchestratorsForRun() {
  return Object.values(state.snapshot.orchestrators || {}).filter((item) => item.run_id === state.runId);
}

function renderControls() {
  const previous = elements["orchestrator-select"].value;
  const orchestrators = orchestratorsForRun();
  elements["orchestrator-select"].replaceChildren();
  for (const orchestrator of orchestrators) {
    const option = document.createElement("option");
    option.value = orchestrator.orchestrator_id;
    option.textContent = `${orchestrator.orchestrator_id} (${orchestrator.scope_count || 0})`;
    elements["orchestrator-select"].append(option);
  }
  if (orchestrators.some((item) => item.orchestrator_id === previous)) {
    elements["orchestrator-select"].value = previous;
  }
  const selected = orchestrators.find((item) => item.orchestrator_id === elements["orchestrator-select"].value);
  const canControl = state.mode === "firebase" && Boolean(selected) && Boolean(state.firebase?.user);
  elements.resume.disabled = !canControl;
  elements.pause.disabled = !canControl;
  elements.resume.classList.toggle("selected", selected?.desired_state === "running");
  elements.pause.classList.toggle("selected", selected?.desired_state === "paused");
  elements["control-note"].textContent = state.mode === "local" ? "Cloud controls disabled in local view" : selected ? `${selected.worker_id} / ${selected.monitor_state || "unknown"}` : "No orchestrator";
}

function render() {
  const tasks = tasksForRun();
  updateMetrics(tasks);
  renderControls();
  renderTable(tasks);
}

async function selectTask(task) {
  state.selectedTaskId = task.task_id;
  state.selectedArtifact = null;
  elements["reader-heading"].textContent = `Ayah ${task.ayah_ref}`;
  elements["reader-content"].innerHTML = '<p class="reader-placeholder">Loading prose...</p>';
  document.querySelector(".reader").classList.add("open");
  renderTable(tasksForRun());
  if (state.mode === "firebase") await loadFirebaseArtifacts(task);
  renderReader(task);
}

function renderReader(task) {
  const artifacts = state.snapshot.artifacts?.[task.task_id] || {};
  const currentKinds = new Set(task.artifact_kinds || []);
  const available = ARTIFACT_ORDER.filter((kind) => artifacts[kind] && currentKinds.has(kind));
  elements["artifact-tabs"].replaceChildren();
  if (!state.selectedArtifact || !available.includes(state.selectedArtifact)) {
    state.selectedArtifact = available.includes("editorial") ? "editorial" : available.at(-1) || null;
  }
  for (const kind of available) {
    const button = document.createElement("button");
    button.type = "button";
    button.role = "tab";
    button.textContent = kind;
    button.classList.toggle("selected", kind === state.selectedArtifact);
    button.setAttribute("aria-selected", String(kind === state.selectedArtifact));
    button.addEventListener("click", () => {
      state.selectedArtifact = kind;
      renderReader(task);
    });
    elements["artifact-tabs"].append(button);
  }
  if (!state.selectedArtifact) {
    elements["reader-meta"].textContent = `${task.orchestrator_id} / no reader-visible output yet`;
    elements["reader-content"].innerHTML = '<p class="reader-placeholder">Scope and consolidated prose will appear here when written.</p>';
    return;
  }
  const artifact = artifacts[state.selectedArtifact];
  elements["reader-meta"].textContent = `${artifact.path} / ${Number(artifact.size || 0).toLocaleString()} bytes / ${relativeTime(artifact.modified_at)}`;
  if (artifact.oversize) {
    elements["reader-content"].innerHTML = '<p class="reader-placeholder">This artifact exceeds the inline reader limit.</p>';
  } else if (artifact.content == null && state.mode === "local") {
    elements["reader-content"].innerHTML = '<p class="reader-placeholder">Loading prose...</p>';
    loadLocalArtifact(task, artifact);
  } else if (artifact.content == null) {
    elements["reader-content"].innerHTML = '<p class="reader-placeholder">Prose content is unavailable.</p>';
  } else {
    elements["reader-content"].innerHTML = renderMarkup(artifact.content);
  }
}

async function loadLocalArtifact(task, artifact) {
  const cacheKey = artifact.sha256 || `${artifact.path}:${artifact.modified_at}`;
  try {
    if (!state.contentCache.has(cacheKey)) {
      const path = artifact.path.split("/").map(encodeURIComponent).join("/");
      const response = await fetch(`/${path}`, { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      state.contentCache.set(cacheKey, await response.text());
    }
    artifact.content = state.contentCache.get(cacheKey);
    if (state.selectedTaskId === task.task_id) renderReader(task);
  } catch (error) {
    elements["reader-content"].innerHTML = `<p class="reader-placeholder">Could not load prose: ${escapeHtml(error.message)}</p>`;
  }
}

function setConnection(label, kind = "online") {
  elements["connection-label"].textContent = label;
  elements["connection-dot"].className = `connection-dot ${kind}`;
}

async function checkForUpdate() {
  try {
    const configUrl = new URL("./firebase-config.js", import.meta.url);
    configUrl.searchParams.set("check", Date.now());
    const latest = await import(configUrl.href);
    const latestVersion = latest.dashboardConfig?.appVersion;
    if (latestVersion && latestVersion !== dashboardConfig.appVersion) {
      elements["version-banner-text"].textContent = `Version v${latestVersion} is available`;
      elements["version-banner"].hidden = false;
    }
  } catch (_error) {
    // A failed update check should not interrupt monitoring.
  }
}

function setAdminOpen(open) {
  state.adminOpen = open;
  elements["passcode-admin"].hidden = !open;
  document.querySelector(".commandbar").hidden = open;
  document.querySelector("main").hidden = open;
}

function generatePasscode() {
  const bytes = crypto.getRandomValues(new Uint8Array(18));
  return [...bytes].map((value) => value.toString(16).padStart(2, "0")).join("");
}

async function hashPasscode(passcode) {
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(passcode));
  return [...new Uint8Array(digest)]
    .map((value) => value.toString(16).padStart(2, "0"))
    .join("");
}

function firestoreDate(value) {
  if (value?.toDate) return value.toDate();
  return value ? new Date(value) : null;
}

function renderPasscodes() {
  const entries = Object.values(state.passcodes).sort((first, second) => {
    if (Boolean(first.active) !== Boolean(second.active)) return first.active ? -1 : 1;
    return String(first.label || "").localeCompare(String(second.label || ""));
  });
  elements["passcode-rows"].replaceChildren();
  elements["passcode-empty"].hidden = entries.length !== 0;
  for (const passcode of entries) {
    const row = document.createElement("tr");
    const created = firestoreDate(passcode.created_at);
    const values = [
      passcode.label || "Unnamed",
      `${String(passcode.fingerprint || "").slice(0, 12)}...`,
      passcode.active ? "Allowed" : "Revoked",
      created && !Number.isNaN(created.getTime()) ? created.toLocaleString() : "Pending",
    ];
    for (const value of values) {
      const cell = document.createElement("td");
      cell.textContent = value;
      row.append(cell);
    }
    const actionCell = document.createElement("td");
    const action = document.createElement("button");
    action.type = "button";
    action.className = "button";
    action.textContent = passcode.active ? "Revoke" : "Allow";
    action.addEventListener("click", () => setPasscodeActive(passcode.fingerprint, !passcode.active));
    actionCell.append(action);
    row.append(actionCell);
    elements["passcode-rows"].append(row);
  }
}

async function setPasscodeActive(fingerprint, active) {
  if (!state.firebase?.user) return;
  const { storeApi, db } = state.firebase;
  try {
    await storeApi.updateDoc(storeApi.doc(db, "passcodes", fingerprint), {
      active,
      updated_at: storeApi.serverTimestamp(),
    });
  } catch (error) {
    elements["passcode-result"].textContent = error.message;
  }
}

async function allowPasscode(event) {
  event.preventDefault();
  if (!state.firebase?.user) return;
  const label = elements["passcode-label"].value.trim();
  const passcode = elements["passcode-value"].value.trim();
  if (passcode.length < 12) {
    elements["passcode-value"].setCustomValidity("Use at least 12 characters.");
    elements["passcode-value"].reportValidity();
    return;
  }
  elements["passcode-value"].setCustomValidity("");
  const fingerprint = await hashPasscode(passcode);
  const { storeApi, db, user } = state.firebase;
  elements["allow-passcode"].disabled = true;
  try {
    await storeApi.setDoc(storeApi.doc(db, "passcodes", fingerprint), {
      fingerprint,
      label,
      active: true,
      created_at: storeApi.serverTimestamp(),
      updated_at: storeApi.serverTimestamp(),
      created_by: user.email,
    }, { merge: true });
    elements["created-passcode-value"].value = passcode;
    elements["created-passcode"].hidden = false;
    elements["passcode-result"].textContent = "Allowed";
    elements["passcode-value"].value = "";
    elements["passcode-value"].type = "password";
  } catch (error) {
    elements["passcode-result"].textContent = error.message;
    elements["created-passcode"].hidden = false;
  } finally {
    elements["allow-passcode"].disabled = false;
  }
}

async function loadLocal() {
  try {
    const response = await fetch(`${dashboardConfig.localSnapshotUrl}?t=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.snapshot = await response.json();
    state.lastLoadAt = new Date();
    setConnection(`Local snapshot / ${relativeTime(state.snapshot.generated_at)}`);
  } catch (error) {
    state.snapshot = demoSnapshot();
    setConnection("Local preview data", "error");
  }
  render();
  if (state.selectedTaskId) {
    const task = state.snapshot.tasks[state.selectedTaskId];
    if (task) renderReader(task);
  }
}

async function initializeFirebase() {
  const base = `https://www.gstatic.com/firebasejs/${FIREBASE_VERSION}`;
  const [appApi, authApi, storeApi] = await Promise.all([
    import(`${base}/firebase-app.js`),
    import(`${base}/firebase-auth.js`),
    import(`${base}/firebase-firestore.js`),
  ]);
  const app = appApi.initializeApp(firebaseConfig);
  const auth = authApi.getAuth(app);
  const db = storeApi.getFirestore(app);
  state.firebase = { authApi, storeApi, auth, db, user: null };
  elements["sign-in"].hidden = false;
  authApi.onAuthStateChanged(auth, (user) => {
    state.firebase.user = user;
    elements["sign-in"].textContent = user ? "Sign out" : "Sign in";
    elements["manage-passcodes"].hidden = !user;
    if (user) subscribeFirebase();
    else {
      unsubscribeFirebase();
      setAdminOpen(false);
      state.passcodes = {};
      state.snapshot = emptySnapshot();
      setConnection("Sign in required", "error");
      render();
    }
  });
}

function unsubscribeFirebase() {
  for (const unsubscribe of state.unsubscribe) unsubscribe();
  state.unsubscribe = [];
}

function subscribeFirebase() {
  unsubscribeFirebase();
  const { storeApi, db } = state.firebase;
  state.snapshot = emptySnapshot();
  const onError = (error) => setConnection(`Firebase error: ${error.code || error.message}`, "error");
  const orchestratorsRef = storeApi.collection(db, "runs", state.runId, "orchestrators");
  const tasksRef = storeApi.collection(db, "runs", state.runId, "tasks");
  const passcodesRef = storeApi.collection(db, "passcodes");
  state.unsubscribe.push(storeApi.onSnapshot(orchestratorsRef, (result) => {
    state.snapshot.orchestrators = Object.fromEntries(result.docs.map((doc) => [doc.id, doc.data()]));
    setConnection(`Firebase / ${state.firebase.user.email}`);
    render();
  }, onError));
  state.unsubscribe.push(storeApi.onSnapshot(tasksRef, (result) => {
    state.snapshot.tasks = Object.fromEntries(result.docs.map((doc) => [doc.id, doc.data()]));
    render();
  }, onError));
  state.unsubscribe.push(storeApi.onSnapshot(passcodesRef, (result) => {
    state.passcodes = Object.fromEntries(result.docs.map((document) => [document.id, document.data()]));
    renderPasscodes();
  }, onError));
}

async function loadFirebaseArtifacts(task) {
  const { storeApi, db } = state.firebase;
  const reference = storeApi.collection(db, "runs", state.runId, "tasks", task.task_id, "artifacts");
  const result = await storeApi.getDocs(reference);
  state.snapshot.artifacts[task.task_id] = Object.fromEntries(result.docs.map((doc) => [doc.id, doc.data()]));
}

async function setRemoteControl(desiredState) {
  const orchestratorId = elements["orchestrator-select"].value;
  if (!orchestratorId || !state.firebase?.user) return;
  const { storeApi, db } = state.firebase;
  const controlId = `${state.runId}--${orchestratorId}`;
  const reference = storeApi.doc(db, "controls", controlId);
  try {
    await storeApi.setDoc(reference, {
      control_id: controlId,
      run_id: state.runId,
      orchestrator_id: orchestratorId,
      desired_state: desiredState,
      control_requested_at: storeApi.serverTimestamp(),
    }, { merge: true });
    const orchestrator = state.snapshot.orchestrators[orchestratorId];
    if (orchestrator) orchestrator.desired_state = desiredState;
    renderControls();
  } catch (error) {
    setConnection(`Control failed: ${error.code || error.message}`, "error");
  }
}

function changeRun() {
  state.runId = elements["run-id"].value.trim() || dashboardConfig.defaultRunId;
  state.page = 1;
  state.selectedTaskId = null;
  const url = new URL(window.location.href);
  url.searchParams.set("run", state.runId);
  window.history.replaceState({}, "", url);
  if (state.mode === "firebase" && state.firebase?.user) subscribeFirebase();
  else render();
}

function demoSnapshot() {
  const now = Date.now();
  const orchestrator = {
    run_id: state.runId,
    worker_id: "studio-mac",
    orchestrator_id: "orch-s029",
    analysis_id: "native",
    scope_refs: ["29:38", "29:39", "29:40", "29:41", "29:42"],
    scope_count: 5,
    started_at: new Date(now - 75 * 60000).toISOString(),
    desired_state: "running",
    monitor_state: "online",
  };
  const task = (ayahRef, status, stage, attempt, minutes, agent, artifactKinds = []) => ({
    task_id: taskId(orchestrator.orchestrator_id, ayahRef),
    run_id: state.runId,
    worker_id: orchestrator.worker_id,
    orchestrator_id: orchestrator.orchestrator_id,
    analysis_id: "native",
    ayah_ref: ayahRef,
    status,
    stages: {
      ...blankStages(),
      [stage]: { status: status === "failed" ? "failed" : "active", attempt, agent_id: agent, updated_at: new Date(now - minutes * 60000).toISOString() },
    },
    artifact_kinds: artifactKinds,
    updated_at: new Date(now - minutes * 60000).toISOString(),
  });
  const tasks = [
    task("29:38", "completed", "validator", 1, 4, "agent-31", ["micro", "macro", "global", "consolidated", "editorial"]),
    task("29:39", "active", "macro", 2, 3, "agent-42", ["micro"]),
    task("29:40", "failed", "global", 1, 8, "agent-19"),
    task("29:41", "active", "micro", 1, 48, "agent-08"),
  ];
  tasks[0].stages.validator.status = "passed";
  const sample = "# Ayah 29:38\n\n{ar:وَوَصَّيْنَا الْإِنسَانَ بِوَالِدَيْهِ حُسْنًا}\n\n**Editorial prose.** The command joins moral clarity to lived obligation. The expression {gloss:husnan} is read here through its immediate argument and the wider discourse.\n\n- {tr:Scope evidence} remains visible.\n- Consolidation resolves competing observations.";
  return {
    generated_at: new Date().toISOString(),
    workers: {},
    orchestrators: { [orchestrator.orchestrator_id]: orchestrator },
    tasks: Object.fromEntries(tasks.map((item) => [item.task_id, item])),
    artifacts: {
      [tasks[0].task_id]: Object.fromEntries(ARTIFACT_ORDER.map((kind) => [kind, {
        kind,
        path: `_commentary/v5/${kind === "editorial" ? "editorial" : "raw"}/native/s029/29_38/${kind}.md`,
        size: sample.length,
        modified_at: tasks[0].updated_at,
        content: `${sample}\n\n## ${kind[0].toUpperCase() + kind.slice(1)} view\n\nThis is local preview content for the markup reader.`,
      }])),
    },
  };
}

elements["run-id"].value = state.runId;
elements["run-id"].addEventListener("change", changeRun);
elements.refresh.addEventListener("click", () => state.mode === "local" ? loadLocal() : subscribeFirebase());
elements.search.addEventListener("input", () => { state.page = 1; renderTable(tasksForRun()); });
elements["status-filter"].addEventListener("change", () => { state.page = 1; renderTable(tasksForRun()); });
elements["show-attention"].addEventListener("click", () => {
  elements["status-filter"].value = elements["status-filter"].value === "attention" ? "all" : "attention";
  state.page = 1;
  renderTable(tasksForRun());
});
elements["previous-page"].addEventListener("click", () => { state.page -= 1; renderTable(tasksForRun()); });
elements["next-page"].addEventListener("click", () => { state.page += 1; renderTable(tasksForRun()); });
elements["orchestrator-select"].addEventListener("change", renderControls);
elements.resume.addEventListener("click", () => setRemoteControl("running"));
elements.pause.addEventListener("click", () => setRemoteControl("paused"));
elements["close-reader"].addEventListener("click", () => document.querySelector(".reader").classList.remove("open"));
elements["manage-passcodes"].addEventListener("click", () => setAdminOpen(true));
elements["close-passcodes"].addEventListener("click", () => setAdminOpen(false));
elements["generate-passcode"].addEventListener("click", () => {
  elements["passcode-value"].value = generatePasscode();
  elements["passcode-value"].type = "text";
});
elements["passcode-value"].addEventListener("input", () => {
  elements["passcode-value"].setCustomValidity("");
});
elements["passcode-form"].addEventListener("submit", allowPasscode);
elements["copy-passcode"].addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(elements["created-passcode-value"].value);
    elements["passcode-result"].textContent = "Copied";
  } catch (error) {
    elements["passcode-result"].textContent = error.message;
  }
});
elements["update-app"].addEventListener("click", () => window.location.reload());
elements["sign-in"].addEventListener("click", async () => {
  const { authApi, auth, user } = state.firebase;
  if (user) await authApi.signOut(auth);
  else await authApi.signInWithPopup(auth, new authApi.GoogleAuthProvider());
});

if (state.mode === "local") {
  loadLocal();
  window.setInterval(loadLocal, 10000);
} else {
  initializeFirebase().catch((error) => setConnection(`Firebase startup failed: ${error.message}`, "error"));
}
window.setInterval(checkForUpdate, 60000);
