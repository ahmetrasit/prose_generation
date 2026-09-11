import { dashboardConfig, firebaseConfig } from "./firebase-config.js";

const FIREBASE_VERSION = "12.18.0";
const ACTIVE_STAGE_STATES = new Set(["active", "composing", "editing"]);
const ATTENTION_STATES = new Set(["failed", "attention", "interrupted", "stalled"]);
const ARTIFACT_ORDER = ["micro", "macro", "global", "consolidated", "editorial", "invitation"];
const READER_WIDTH_STORAGE_KEY = "v5-monitor-reader-width";
const STAGE_NAMES = {
  micro: "Micro scope",
  macro: "Macro scope",
  global: "Global scope",
  canonical: "Canonical",
  invitation: "Invitation",
  validator: "Validation",
};
const STATUS_ORDER = {
  failed: 0,
  attention: 1,
  stalled: 2,
  active: 3,
  awaiting_validation: 4,
  pending: 5,
  completed: 6,
};

const elements = Object.fromEntries(
  [
    "connection-dot", "connection-label", "sign-in", "manage-passcodes", "app-version",
    "run-id", "run-options", "orchestrator-select", "refresh", "resume", "pause",
    "control-note", "metric-total", "metric-pending", "metric-active", "metric-agents",
    "metric-completed", "metric-attention", "metric-reruns", "progress-fill", "progress-label",
    "attention-strip", "attention-title", "attention-detail", "show-attention", "workspace",
    "queue-caption", "search", "status-filter", "surah-filter", "orchestrator-filter",
    "reset-filters", "task-rows", "empty-state", "page-size", "page-range",
    "previous-page", "next-page", "page-label", "reader", "reader-heading", "previous-task",
    "next-task", "artifact-tabs", "reader-meta", "reader-content", "close-reader",
    "reader-resizer",
    "cell-tooltip", "passcode-admin", "close-passcodes", "passcode-form", "passcode-label",
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
  runs: {},
  firebase: null,
  unsubscribeGlobal: [],
  unsubscribeRun: [],
  selectedTaskId: null,
  selectedArtifact: null,
  visibleTasks: [],
  loadedArtifactVersions: new Map(),
  page: 1,
  pageSize: 50,
  sort: { key: "surah", direction: "asc" },
  contentCache: new Map(),
  readerWidth: readStoredReaderWidth(),
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

function readStoredReaderWidth() {
  try {
    const value = Number(window.localStorage.getItem(READER_WIDTH_STORAGE_KEY));
    return Number.isFinite(value) && value > 0 ? value : null;
  } catch (_error) {
    return null;
  }
}

function storeReaderWidth(width) {
  try {
    window.localStorage.setItem(READER_WIDTH_STORAGE_KEY, String(Math.round(width)));
  } catch (_error) {
    // Pane size persistence is a convenience; monitoring should continue without it.
  }
}

function applyReaderWidth(width) {
  if (!width) return;
  elements.workspace.style.setProperty("--reader-width", `${Math.round(width)}px`);
}

function updateReaderResizerValue(width, maxWidth) {
  elements["reader-resizer"].setAttribute("aria-valuemax", String(Math.round(maxWidth)));
  elements["reader-resizer"].setAttribute("aria-valuenow", String(Math.round(width)));
}

function readerWidthBounds() {
  const bounds = elements.workspace.getBoundingClientRect();
  const minReader = 320;
  const minQueue = 420;
  const maxReader = Math.max(minReader, bounds.width - minQueue);
  return { minReader, maxReader };
}

function setReaderWidth(width, { persist = true } = {}) {
  const { minReader, maxReader } = readerWidthBounds();
  const next = Math.min(maxReader, Math.max(minReader, width));
  applyReaderWidth(next);
  updateReaderResizerValue(next, maxReader);
  if (persist) {
    state.readerWidth = next;
    storeReaderWidth(next);
  }
}

function syncReaderWidth() {
  const { minReader, maxReader } = readerWidthBounds();
  if (!state.readerWidth && !elements.workspace.classList.contains("reader-open")) {
    updateReaderResizerValue(minReader, maxReader);
    return;
  }
  const current = state.readerWidth || elements.reader.getBoundingClientRect().width || minReader;
  setReaderWidth(current, { persist: false });
}

function readerWidthFromPointer(event) {
  const bounds = elements.workspace.getBoundingClientRect();
  return bounds.right - event.clientX;
}

function artifactLabel(kind) {
  return kind === "invitation" ? "invitation summary" : kind;
}

function refNumbers(taskOrRef) {
  const ref = typeof taskOrRef === "string" ? taskOrRef : taskOrRef.ayah_ref;
  const [surah, ayah] = String(ref || "0:0").split(":").map(Number);
  return { surah: surah || 0, ayah: Number.isFinite(ayah) ? ayah : 0 };
}

function compareRefs(first, second) {
  const a = refNumbers(first);
  const b = refNumbers(second);
  return a.surah - b.surah || a.ayah - b.ayah;
}

function taskId(orchestratorId, ayahRef) {
  const { surah, ayah } = refNumbers(ayahRef);
  return `${orchestratorId}--s${String(surah).padStart(3, "0")}-a${String(ayah).padStart(3, "0")}`;
}

function blankStages() {
  return Object.fromEntries(
    Object.keys(STAGE_NAMES).map((stage) => [
      stage,
      { status: "pending", attempt: 0, agent_id: null, updated_at: null },
    ])
  );
}

function tasksForRun() {
  const orchestrators = Object.values(state.snapshot.orchestrators || {})
    .filter((item) => !item.run_id || item.run_id === state.runId);
  const tasks = [];
  const seen = new Set();
  for (const orchestrator of orchestrators) {
    for (const ayahRef of orchestrator.scope_refs || []) {
      const id = taskId(orchestrator.orchestrator_id, ayahRef);
      const task = state.snapshot.tasks[id] || {
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
      };
      tasks.push(task);
      seen.add(id);
    }
  }
  for (const task of Object.values(state.snapshot.tasks || {})) {
    if ((!task.run_id || task.run_id === state.runId) && !seen.has(task.task_id)) tasks.push(task);
  }
  return tasks;
}

function activeStages(task) {
  return Object.entries(task.stages || {}).filter(([, stage]) => ACTIVE_STAGE_STATES.has(stage.status));
}

function isStalled(task) {
  const threshold = dashboardConfig.staleAfterMinutes * 60 * 1000;
  return activeStages(task).some(([, stage]) => {
    const timestamp = new Date(stage.updated_at).getTime();
    return Number.isFinite(timestamp) && Date.now() - timestamp > threshold;
  });
}

function displayStatus(task) {
  if (["failed", "attention"].includes(task.status)) return task.status;
  if (task.status === "active" && isStalled(task)) return "stalled";
  return task.status || "pending";
}

function currentStep(task) {
  const active = activeStages(task);
  if (active.length) return active.map(([name]) => STAGE_NAMES[name] || name).join(", ");
  const failed = Object.entries(task.stages || {})
    .find(([, value]) => ATTENTION_STATES.has(value.status));
  if (failed) return STAGE_NAMES[failed[0]] || failed[0];
  if (task.status === "awaiting_validation") return "Validation";
  if (task.status === "completed") return "Done";
  const ready = Object.entries(task.stages || {}).find(([, value]) => value.status === "ready");
  return ready ? STAGE_NAMES[ready[0]] || ready[0] : "Not started";
}

function agentsForTask(task) {
  return [...new Set(Object.values(task.stages || {}).map((stage) => stage.agent_id).filter(Boolean))];
}

function attemptCount(task) {
  return Math.max(0, ...Object.values(task.stages || {}).map((stage) => Number(stage.attempt || 0)));
}

function relativeTime(value) {
  if (!value) return "Never";
  const timestamp = new Date(value).getTime();
  if (!Number.isFinite(timestamp)) return "Unknown";
  const seconds = Math.max(0, Math.floor((Date.now() - timestamp) / 1000));
  if (seconds < 60) return `${seconds}s ago`;
  if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
  if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
  return `${Math.floor(seconds / 86400)}d ago`;
}

function absoluteTime(value) {
  if (!value) return "No update recorded";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? String(value) : date.toLocaleString();
}

function timestampValue(value) {
  const timestamp = new Date(value || 0).getTime();
  return Number.isFinite(timestamp) ? timestamp : 0;
}

function statusGroup(task) {
  const status = displayStatus(task);
  if (ATTENTION_STATES.has(status)) return "attention";
  if (["active", "awaiting_validation"].includes(status)) return "active";
  return status;
}

function searchText(task) {
  const { surah, ayah } = refNumbers(task);
  const attention = (task.attention || []).flatMap((item) => [item.stage, item.status, item.message]);
  return [
    task.ayah_ref, surah, ayah, displayStatus(task), currentStep(task), task.analysis_id,
    task.orchestrator_id, task.worker_id, ...agentsForTask(task), ...attention,
  ].filter(Boolean).join(" ").toLocaleLowerCase();
}

function matchesStatus(task, filter) {
  if (filter === "all") return true;
  if (filter === "attention") return statusGroup(task) === "attention";
  if (filter === "active") return statusGroup(task) === "active";
  return displayStatus(task) === filter;
}

function filteredTasks(tasks) {
  const needle = elements.search.value.trim().toLocaleLowerCase();
  const status = elements["status-filter"].value;
  const surah = elements["surah-filter"].value;
  const orchestrator = elements["orchestrator-filter"].value;
  return tasks.filter((task) => (
    (!needle || searchText(task).includes(needle))
    && matchesStatus(task, status)
    && (surah === "all" || String(refNumbers(task).surah) === surah)
    && (orchestrator === "all" || task.orchestrator_id === orchestrator)
  ));
}

function sortValue(task, key) {
  const ref = refNumbers(task);
  if (key === "surah") return ref.surah;
  if (key === "ayah") return ref.ayah;
  if (key === "state") return STATUS_ORDER[displayStatus(task)] ?? 99;
  if (key === "step") return currentStep(task).toLocaleLowerCase();
  if (key === "agent") return agentsForTask(task).join(", ").toLocaleLowerCase();
  if (key === "attempts") return attemptCount(task);
  if (key === "analysis") return String(task.analysis_id || "").toLocaleLowerCase();
  if (key === "orchestrator") return String(task.orchestrator_id || "").toLocaleLowerCase();
  if (key === "updated") return new Date(task.updated_at || 0).getTime() || 0;
  return "";
}

function sortedTasks(tasks) {
  const direction = state.sort.direction === "asc" ? 1 : -1;
  return [...tasks].sort((first, second) => {
    const a = sortValue(first, state.sort.key);
    const b = sortValue(second, state.sort.key);
    const primary = typeof a === "number" && typeof b === "number"
      ? a - b
      : String(a).localeCompare(String(b), undefined, { numeric: true });
    return primary * direction
      || compareRefs(first, second)
      || String(first.orchestrator_id).localeCompare(String(second.orchestrator_id));
  });
}

function updateMetrics(tasks) {
  const active = tasks.filter((task) => statusGroup(task) === "active");
  const attention = tasks.filter((task) => statusGroup(task) === "attention");
  const completed = tasks.filter((task) => task.status === "completed");
  const agents = new Set(active.flatMap(agentsForTask));
  const reruns = tasks.filter((task) => attemptCount(task) > 1).length;
  elements["metric-total"].textContent = tasks.length.toLocaleString();
  elements["metric-pending"].textContent = tasks.filter((task) => statusGroup(task) === "pending").length.toLocaleString();
  elements["metric-active"].textContent = active.length.toLocaleString();
  elements["metric-agents"].textContent = agents.size.toLocaleString();
  elements["metric-completed"].textContent = completed.length.toLocaleString();
  elements["metric-attention"].textContent = attention.length.toLocaleString();
  elements["metric-reruns"].textContent = reruns.toLocaleString();
  const percentage = tasks.length ? Math.round((completed.length / tasks.length) * 100) : 0;
  elements["progress-fill"].style.width = `${percentage}%`;
  elements["progress-label"].textContent = `${percentage}% complete`;
  elements["attention-strip"].hidden = attention.length === 0;
  const failures = attention.filter((task) => displayStatus(task) === "failed").length;
  const stalled = attention.filter((task) => displayStatus(task) === "stalled").length;
  elements["attention-title"].textContent = `${attention.length} ayah${attention.length === 1 ? " needs" : "s need"} attention`;
  elements["attention-detail"].textContent = `${failures} failed, ${stalled} potentially stalled`;
}

function setCell(cell, value, tooltip = value) {
  const text = String(value ?? "-");
  cell.textContent = text;
  if (tooltip && text !== "-") {
    cell.dataset.tooltip = String(tooltip);
    cell.title = String(tooltip);
  }
}

function attentionSummary(task) {
  const latest = (task.attention || []).at(-1);
  if (!latest) return displayStatus(task).replaceAll("_", " ");
  return [latest.stage, latest.status, latest.message].filter(Boolean).join(" / ");
}

function renderSortHeaders() {
  for (const header of document.querySelectorAll("th[data-sort]")) {
    const active = header.dataset.sort === state.sort.key;
    header.setAttribute("aria-sort", active ? (state.sort.direction === "asc" ? "ascending" : "descending") : "none");
    header.querySelector(".sort-indicator").textContent = active
      ? (state.sort.direction === "asc" ? "▲" : "▼")
      : "";
  }
}

function renderTable(tasks) {
  state.visibleTasks = sortedTasks(filteredTasks(tasks));
  const pageCount = Math.max(1, Math.ceil(state.visibleTasks.length / state.pageSize));
  state.page = Math.max(1, Math.min(state.page, pageCount));
  const first = (state.page - 1) * state.pageSize;
  const visible = state.visibleTasks.slice(first, first + state.pageSize);
  elements["task-rows"].replaceChildren();
  for (const task of visible) {
    const row = document.getElementById("task-row-template").content.firstElementChild.cloneNode(true);
    const status = displayStatus(task);
    const agents = agentsForTask(task);
    const ref = refNumbers(task);
    const attempts = attemptCount(task);
    row.dataset.taskId = task.task_id;
    row.classList.toggle("selected", task.task_id === state.selectedTaskId);
    setCell(row.querySelector(".surah-cell"), ref.surah);
    setCell(row.querySelector(".ayah-cell"), ref.ayah, `Surah ${ref.surah}, ayah ${ref.ayah}`);
    const stateCell = row.querySelector(".state-cell");
    stateCell.dataset.tooltip = attentionSummary(task);
    stateCell.title = attentionSummary(task);
    const badge = row.querySelector(".status-badge");
    badge.textContent = status.replaceAll("_", " ");
    badge.classList.add(status);
    setCell(row.querySelector(".step-cell"), currentStep(task));
    setCell(row.querySelector(".agent-cell"), agents.join(", ") || "-");
    setCell(row.querySelector(".attempt-cell"), attempts || "-");
    row.querySelector(".attempt-cell").classList.toggle("rerun", attempts > 1);
    setCell(row.querySelector(".analysis-cell"), task.analysis_id || "-");
    setCell(row.querySelector(".orchestrator-cell"), task.orchestrator_id || "-");
    setCell(row.querySelector(".updated-cell"), relativeTime(task.updated_at), absoluteTime(task.updated_at));
    row.addEventListener("click", () => selectTask(task));
    row.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        selectTask(task);
      }
    });
    elements["task-rows"].append(row);
  }
  elements["empty-state"].hidden = visible.length !== 0;
  elements["queue-caption"].textContent = `${state.visibleTasks.length.toLocaleString()} shown of ${tasks.length.toLocaleString()} ayat`;
  elements["page-label"].textContent = `Page ${state.page} of ${pageCount}`;
  elements["page-range"].textContent = state.visibleTasks.length
    ? `${first + 1}-${first + visible.length} of ${state.visibleTasks.length.toLocaleString()}`
    : "0 rows";
  elements["previous-page"].disabled = state.page <= 1;
  elements["next-page"].disabled = state.page >= pageCount;
  renderSortHeaders();
  updateReaderNavigation();
}

function replaceFilterOptions(select, firstLabel, values) {
  const previous = select.value || "all";
  select.replaceChildren();
  const all = document.createElement("option");
  all.value = "all";
  all.textContent = firstLabel;
  select.append(all);
  for (const { value, label } of values) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    select.append(option);
  }
  select.value = [...select.options].some((option) => option.value === previous) ? previous : "all";
}

function updateFilterOptions(tasks) {
  const surahs = [...new Set(tasks.map((task) => refNumbers(task).surah))].sort((a, b) => a - b);
  replaceFilterOptions(
    elements["surah-filter"],
    "All surahs",
    surahs.map((surah) => ({ value: String(surah), label: `Surah ${surah}` }))
  );
  const orchestrators = [...new Set(tasks.map((task) => task.orchestrator_id).filter(Boolean))].sort();
  replaceFilterOptions(
    elements["orchestrator-filter"],
    "All orchestrators",
    orchestrators.map((value) => ({ value, label: value }))
  );
}

function orchestratorsForRun() {
  return Object.values(state.snapshot.orchestrators || {})
    .filter((item) => !item.run_id || item.run_id === state.runId)
    .sort((a, b) => {
      const created = timestampValue(b.started_at || b.registered_at) - timestampValue(a.started_at || a.registered_at);
      return created || String(a.orchestrator_id).localeCompare(String(b.orchestrator_id));
    });
}

function renderRuns() {
  const runIds = new Set([dashboardConfig.defaultRunId, state.runId, ...Object.keys(state.runs)]);
  elements["run-options"].replaceChildren();
  for (const runId of [...runIds].filter(Boolean).sort()) {
    const option = document.createElement("option");
    option.value = runId;
    const timestamp = state.runs[runId]?.last_registered_at;
    option.label = timestamp ? `${runId} / ${relativeTime(timestamp)}` : runId;
    elements["run-options"].append(option);
  }
}

function renderControls() {
  const previous = elements["orchestrator-select"].value;
  const orchestrators = orchestratorsForRun();
  elements["orchestrator-select"].replaceChildren();
  if (!orchestrators.length) {
    const option = document.createElement("option");
    option.textContent = "No orchestrators";
    option.value = "";
    elements["orchestrator-select"].append(option);
  }
  for (const orchestrator of orchestrators) {
    const option = document.createElement("option");
    const createdAt = orchestrator.started_at || orchestrator.registered_at;
    option.value = orchestrator.orchestrator_id;
    option.textContent = [
      orchestrator.orchestrator_id,
      createdAt ? relativeTime(createdAt) : null,
      `${Number(orchestrator.scope_count || 0).toLocaleString()} ayat`,
    ].filter(Boolean).join(" / ");
    option.title = createdAt ? `Created ${absoluteTime(createdAt)}` : "Creation time unavailable";
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
  elements["control-note"].textContent = state.mode === "local"
    ? "Cloud controls disabled in local view"
    : selected
      ? `${selected.worker_id || "unknown worker"} / ${selected.monitor_state || "unknown"}`
      : "No orchestrator";
}

function render() {
  const tasks = tasksForRun();
  updateFilterOptions(tasks);
  updateMetrics(tasks);
  renderRuns();
  renderControls();
  renderTable(tasks);
}

async function selectTask(task) {
  state.selectedTaskId = task.task_id;
  state.selectedArtifact = null;
  elements.reader.hidden = false;
  elements.workspace.classList.add("reader-open");
  syncReaderWidth();
  elements["reader-heading"].textContent = `Surah ${refNumbers(task).surah}, ayah ${refNumbers(task).ayah}`;
  setReaderHtml('<p class="reader-placeholder">Loading prose...</p>');
  renderTable(tasksForRun());
  if (state.mode === "firebase") {
    try {
      await loadFirebaseArtifacts(task);
    } catch (error) {
      if (state.selectedTaskId === task.task_id) {
        setReaderHtml(`<p class="reader-placeholder">Could not load prose: ${escapeHtml(error.message)}</p>`);
      }
      return;
    }
  }
  if (state.selectedTaskId === task.task_id) renderReader(task);
}

function closeReader() {
  state.selectedTaskId = null;
  state.selectedArtifact = null;
  elements["reader-content"].dataset.viewKey = "";
  elements["reader-content"].dataset.contentKey = "";
  elements.reader.hidden = true;
  elements.workspace.classList.remove("reader-open");
  renderTable(tasksForRun());
}

function updateReaderNavigation() {
  const index = state.visibleTasks.findIndex((task) => task.task_id === state.selectedTaskId);
  elements["previous-task"].disabled = index <= 0;
  elements["next-task"].disabled = index < 0 || index >= state.visibleTasks.length - 1;
}

function navigateReader(offset) {
  const index = state.visibleTasks.findIndex((task) => task.task_id === state.selectedTaskId);
  const task = state.visibleTasks[index + offset];
  if (task) selectTask(task);
}

function startReaderResize(event) {
  if (event.button !== 0 || window.matchMedia("(max-width: 920px)").matches) return;
  event.preventDefault();
  elements["reader-resizer"].setPointerCapture(event.pointerId);
  elements.workspace.classList.add("reader-resizing");
  setReaderWidth(readerWidthFromPointer(event));
}

function moveReaderResize(event) {
  if (!elements.workspace.classList.contains("reader-resizing")) return;
  setReaderWidth(readerWidthFromPointer(event));
}

function finishReaderResize(event) {
  if (!elements.workspace.classList.contains("reader-resizing")) return;
  elements.workspace.classList.remove("reader-resizing");
  if (elements["reader-resizer"].hasPointerCapture(event.pointerId)) {
    elements["reader-resizer"].releasePointerCapture(event.pointerId);
  }
}

function adjustReaderWidth(event) {
  if (!["ArrowLeft", "ArrowRight"].includes(event.key)) return;
  event.preventDefault();
  const current = state.readerWidth || elements.reader.getBoundingClientRect().width;
  setReaderWidth(current + (event.key === "ArrowLeft" ? 40 : -40));
}

function artifactCacheKey(artifact) {
  return artifact.sha256 || `${artifact.path}:${artifact.modified_at}:${artifact.size}`;
}

function setReaderHtml(html, { viewKey = "", contentKey = "", preserveScroll = false } = {}) {
  const reader = elements["reader-content"];
  const scrollTop = preserveScroll ? reader.scrollTop : 0;
  reader.innerHTML = html;
  reader.dataset.viewKey = viewKey;
  reader.dataset.contentKey = contentKey;
  reader.scrollTop = Math.min(scrollTop, Math.max(0, reader.scrollHeight - reader.clientHeight));
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
    button.textContent = artifactLabel(kind);
    button.classList.toggle("selected", kind === state.selectedArtifact);
    button.setAttribute("aria-selected", String(kind === state.selectedArtifact));
    button.addEventListener("click", () => {
      state.selectedArtifact = kind;
      renderReader(task);
    });
    elements["artifact-tabs"].append(button);
  }
  updateReaderNavigation();
  if (!state.selectedArtifact) {
    elements["reader-meta"].textContent = `${task.orchestrator_id} / no reader-visible output yet`;
    setReaderHtml('<p class="reader-placeholder">Scope and consolidated prose will appear here when written.</p>');
    return;
  }
  const artifact = artifacts[state.selectedArtifact];
  const viewKey = `${task.task_id}:${state.selectedArtifact}`;
  const sameView = elements["reader-content"].dataset.viewKey === viewKey;
  const cacheKey = artifactCacheKey(artifact);
  if (artifact.content == null && state.mode === "local" && state.contentCache.has(cacheKey)) {
    artifact.content = state.contentCache.get(cacheKey);
  }
  elements["reader-meta"].textContent = `${artifact.path} / ${Number(artifact.size || 0).toLocaleString()} bytes / ${relativeTime(artifact.modified_at)}`;
  elements["reader-meta"].title = `${artifact.path} / ${absoluteTime(artifact.modified_at)}`;
  if (artifact.oversize) {
    setReaderHtml('<p class="reader-placeholder">This artifact exceeds the inline reader limit.</p>', { viewKey, contentKey: cacheKey, preserveScroll: sameView });
  } else if (artifact.content == null && state.mode === "local") {
    if (!sameView || !elements["reader-content"].textContent.trim()) {
      setReaderHtml('<p class="reader-placeholder">Loading prose...</p>', { viewKey, contentKey: cacheKey });
    }
    loadLocalArtifact(task, artifact);
  } else if (artifact.content == null) {
    setReaderHtml('<p class="reader-placeholder">Prose content is unavailable.</p>', { viewKey, contentKey: cacheKey, preserveScroll: sameView });
  } else {
    const contentKey = `${cacheKey}:${artifact.content.length}`;
    if (sameView && elements["reader-content"].dataset.contentKey === contentKey) return;
    setReaderHtml(renderMarkup(artifact.content), { viewKey, contentKey, preserveScroll: sameView });
  }
}

async function loadLocalArtifact(task, artifact) {
  const cacheKey = artifactCacheKey(artifact);
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
    if (state.selectedTaskId === task.task_id) {
      setReaderHtml(`<p class="reader-placeholder">Could not load prose: ${escapeHtml(error.message)}</p>`, {
        viewKey: `${task.task_id}:${artifact.kind}`,
        contentKey: artifactCacheKey(artifact),
      });
    }
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
    // An update check must not interrupt monitoring.
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
      setCell(cell, value);
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
  if (params.get("demo") === "1") {
    state.snapshot = demoSnapshot();
    setConnection("Local preview data");
    render();
    return;
  }
  try {
    const response = await fetch(`${dashboardConfig.localSnapshotUrl}?t=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.snapshot = await response.json();
    setConnection(`Local snapshot / ${relativeTime(state.snapshot.generated_at)}`);
  } catch (_error) {
    state.snapshot = demoSnapshot();
    setConnection("Local preview data", "error");
  }
  render();
  if (state.selectedTaskId) {
    const task = tasksForRun().find((item) => item.task_id === state.selectedTaskId);
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
    if (user) {
      subscribeFirebaseGlobal();
      subscribeFirebaseRun();
    } else {
      unsubscribeFirebase();
      setAdminOpen(false);
      state.passcodes = {};
      state.runs = {};
      state.snapshot = emptySnapshot();
      setConnection("Sign in required", "error");
      render();
    }
  });
}

function unsubscribeCallbacks(callbacks) {
  for (const unsubscribe of callbacks) unsubscribe();
  callbacks.length = 0;
}

function unsubscribeFirebase() {
  unsubscribeCallbacks(state.unsubscribeGlobal);
  unsubscribeCallbacks(state.unsubscribeRun);
}

function subscribeFirebaseGlobal() {
  unsubscribeCallbacks(state.unsubscribeGlobal);
  const { storeApi, db } = state.firebase;
  const onError = (error) => setConnection(`Firebase error: ${error.code || error.message}`, "error");
  state.unsubscribeGlobal.push(storeApi.onSnapshot(storeApi.collection(db, "runs"), (result) => {
    state.runs = Object.fromEntries(result.docs.map((document) => [document.id, document.data()]));
    renderRuns();
  }, onError));
  state.unsubscribeGlobal.push(storeApi.onSnapshot(storeApi.collection(db, "passcodes"), (result) => {
    state.passcodes = Object.fromEntries(result.docs.map((document) => [document.id, document.data()]));
    renderPasscodes();
  }, onError));
}

function subscribeFirebaseRun() {
  unsubscribeCallbacks(state.unsubscribeRun);
  const { storeApi, db } = state.firebase;
  state.snapshot = emptySnapshot();
  state.loadedArtifactVersions.clear();
  const onError = (error) => setConnection(`Firebase error: ${error.code || error.message}`, "error");
  const orchestratorsRef = storeApi.collection(db, "runs", state.runId, "orchestrators");
  const tasksRef = storeApi.collection(db, "runs", state.runId, "tasks");
  state.unsubscribeRun.push(storeApi.onSnapshot(orchestratorsRef, (result) => {
    state.snapshot.orchestrators = Object.fromEntries(result.docs.map((document) => [document.id, document.data()]));
    setConnection(`Firebase / ${state.firebase.user.email}`);
    render();
  }, onError));
  state.unsubscribeRun.push(storeApi.onSnapshot(tasksRef, (result) => {
    state.snapshot.tasks = Object.fromEntries(result.docs.map((document) => [document.id, document.data()]));
    render();
    const selected = state.snapshot.tasks[state.selectedTaskId];
    if (selected && !elements.reader.hidden) {
      loadFirebaseArtifacts(selected).then(() => {
        if (state.selectedTaskId === selected.task_id) renderReader(selected);
      }).catch(onError);
    }
  }, onError));
}

async function loadFirebaseArtifacts(task) {
  const version = String(task.updated_at || "");
  if (state.loadedArtifactVersions.get(task.task_id) === version) return;
  const { storeApi, db } = state.firebase;
  const reference = storeApi.collection(db, "runs", state.runId, "tasks", task.task_id, "artifacts");
  const result = await storeApi.getDocs(reference);
  state.snapshot.artifacts[task.task_id] = Object.fromEntries(
    result.docs.map((document) => [document.id, document.data()])
  );
  state.loadedArtifactVersions.set(task.task_id, version);
}

async function setRemoteControl(desiredState) {
  const orchestratorId = elements["orchestrator-select"].value;
  if (!orchestratorId || !state.firebase?.user) return;
  const { storeApi, db } = state.firebase;
  const controlId = `${state.runId}--${orchestratorId}`;
  try {
    await storeApi.setDoc(storeApi.doc(db, "controls", controlId), {
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
  elements["run-id"].value = state.runId;
  state.page = 1;
  closeReader();
  const url = new URL(window.location.href);
  url.searchParams.set("run", state.runId);
  window.history.replaceState({}, "", url);
  if (state.mode === "firebase" && state.firebase?.user) subscribeFirebaseRun();
  else render();
}

function demoSnapshot() {
  const now = Date.now();
  const definitions = [
    { surah: 2, id: "orch-s002-office", worker: "office-mac", analysis: "native" },
    { surah: 12, id: "orch-s012-research", worker: "research-laptop", analysis: "focus-trace" },
    { surah: 29, id: "orch-s029-evening", worker: "studio-mac", analysis: "native" },
  ];
  const orchestrators = {};
  const tasks = {};
  const artifacts = {};
  let index = 0;
  for (const definition of definitions) {
    const refs = Array.from({ length: 60 }, (_, offset) => `${definition.surah}:${offset + 1}`);
    orchestrators[definition.id] = {
      run_id: state.runId,
      worker_id: definition.worker,
      orchestrator_id: definition.id,
      analysis_id: definition.analysis,
      scope_refs: refs,
      scope_count: refs.length,
      started_at: new Date(now - (180 - index) * 60000).toISOString(),
      desired_state: definition.surah === 12 ? "paused" : "running",
      monitor_state: "online",
    };
    for (const ayahRef of refs) {
      index += 1;
      const stages = blankStages();
      const cycle = index % 20;
      const attempt = index % 17 === 0 ? 2 : 1;
      const minutes = cycle === 14 ? 52 : (index % 19) + 1;
      const updatedAt = new Date(now - minutes * 60000).toISOString();
      let status = "pending";
      let artifactKinds = [];
      if (cycle < 11) {
        status = "completed";
        for (const stage of ["micro", "macro", "global", "canonical", "invitation"]) {
          stages[stage] = { status: "completed", attempt, agent_id: `agent-${stage}-${String(index).padStart(3, "0")}`, updated_at: updatedAt };
        }
        stages.validator = { status: "passed", attempt, agent_id: `agent-canonical-${String(index).padStart(3, "0")}`, updated_at: updatedAt };
        artifactKinds = [...ARTIFACT_ORDER];
      } else if (cycle < 15) {
        status = "active";
        const lane = ["micro", "macro", "global", "canonical"][cycle - 11];
        stages[lane] = { status: lane === "canonical" ? "editing" : "active", attempt, agent_id: `agent-${lane}-long-session-${String(index).padStart(3, "0")}`, updated_at: updatedAt };
        artifactKinds = lane === "canonical" ? ["micro", "macro", "global", "consolidated"] : [];
      } else if (cycle === 15) {
        status = "failed";
        stages.global = { status: "failed", attempt, agent_id: `agent-global-${index}`, updated_at: updatedAt };
      } else if (cycle === 16) {
        status = "attention";
        stages.canonical = { status: "attention", attempt, agent_id: `agent-canonical-${index}`, updated_at: updatedAt };
      } else if (cycle === 17) {
        stages.micro.status = "ready";
      }
      const id = taskId(definition.id, ayahRef);
      const task = {
        task_id: id,
        run_id: state.runId,
        worker_id: definition.worker,
        orchestrator_id: definition.id,
        analysis_id: definition.analysis,
        ayah_ref: ayahRef,
        status,
        stages,
        attention: status === "failed" || status === "attention" ? [{
          stage: status === "failed" ? "global" : "canonical",
          status,
          message: status === "failed" ? "Agent exited before producing valid scope prose" : "Editorial validation needs operator review",
          at: updatedAt,
        }] : [],
        artifact_kinds: artifactKinds,
        updated_at: updatedAt,
      };
      tasks[id] = task;
      if (artifactKinds.length) {
        const { surah, ayah } = refNumbers(task);
        const sample = `# Ayah ${task.ayah_ref}\n\n{ar:وَوَصَّيْنَا الْإِنسَانَ بِوَالِدَيْهِ حُسْنًا}\n\n**Editorial prose.** This preview shows how a completed ayah reads inside the operations inspector. The expression {gloss:husnan} remains connected to its immediate argument and wider discourse.\n\n- {tr:Scope evidence} remains visible.\n- Consolidation resolves competing observations.\n\n## Review note\n\nThe reader keeps prose separate from the operational queue, so long sessions remain easy to scan.`;
        artifacts[id] = Object.fromEntries(artifactKinds.map((kind) => [kind, {
          kind,
          path: `_commentary/v5/${kind === "editorial" ? "editorial" : "raw"}/${definition.analysis}/s${String(surah).padStart(3, "0")}/${surah}_${ayah}/${kind}.md`,
          size: sample.length,
          modified_at: updatedAt,
          content: `${sample}\n\n### ${kind[0].toUpperCase() + kind.slice(1)} view`,
        }]));
      }
    }
  }
  return {
    generated_at: new Date().toISOString(),
    workers: {},
    orchestrators,
    tasks,
    artifacts,
  };
}

function showTooltip(owner) {
  if (!owner?.dataset.tooltip) return;
  const clipped = owner.scrollWidth > owner.clientWidth || owner.scrollHeight > owner.clientHeight;
  if (!clipped && owner.closest(".task-table") && !owner.classList.contains("state-cell")) return;
  elements["cell-tooltip"].textContent = owner.dataset.tooltip;
  elements["cell-tooltip"].hidden = false;
  const rect = owner.getBoundingClientRect();
  const tooltip = elements["cell-tooltip"];
  const left = Math.min(Math.max(12, rect.left), window.innerWidth - tooltip.offsetWidth - 12);
  const below = rect.bottom + 8;
  const top = below + tooltip.offsetHeight < window.innerHeight
    ? below
    : Math.max(8, rect.top - tooltip.offsetHeight - 8);
  tooltip.style.left = `${left}px`;
  tooltip.style.top = `${top}px`;
}

function hideTooltip() {
  elements["cell-tooltip"].hidden = true;
}

for (const header of document.querySelectorAll("th[data-sort]")) {
  header.querySelector("button").addEventListener("click", () => {
    const key = header.dataset.sort;
    state.sort = state.sort.key === key
      ? { key, direction: state.sort.direction === "asc" ? "desc" : "asc" }
      : { key, direction: "asc" };
    state.page = 1;
    renderTable(tasksForRun());
  });
}

elements["run-id"].value = state.runId;
elements["run-id"].addEventListener("change", changeRun);
elements.refresh.addEventListener("click", () => state.mode === "local" ? loadLocal() : subscribeFirebaseRun());
for (const id of ["search", "status-filter", "surah-filter", "orchestrator-filter"]) {
  elements[id].addEventListener(id === "search" ? "input" : "change", () => {
    state.page = 1;
    renderTable(tasksForRun());
  });
}
elements["reset-filters"].addEventListener("click", () => {
  elements.search.value = "";
  elements["status-filter"].value = "all";
  elements["surah-filter"].value = "all";
  elements["orchestrator-filter"].value = "all";
  state.page = 1;
  renderTable(tasksForRun());
});
elements["show-attention"].addEventListener("click", () => {
  elements["status-filter"].value = elements["status-filter"].value === "attention" ? "all" : "attention";
  state.page = 1;
  renderTable(tasksForRun());
});
elements["page-size"].addEventListener("change", () => {
  state.pageSize = Number(elements["page-size"].value) || 50;
  state.page = 1;
  renderTable(tasksForRun());
});
elements["previous-page"].addEventListener("click", () => { state.page -= 1; renderTable(tasksForRun()); });
elements["next-page"].addEventListener("click", () => { state.page += 1; renderTable(tasksForRun()); });
elements["orchestrator-select"].addEventListener("change", renderControls);
elements.resume.addEventListener("click", () => setRemoteControl("running"));
elements.pause.addEventListener("click", () => setRemoteControl("paused"));
elements["close-reader"].addEventListener("click", closeReader);
elements["previous-task"].addEventListener("click", () => navigateReader(-1));
elements["next-task"].addEventListener("click", () => navigateReader(1));
elements["reader-resizer"].addEventListener("pointerdown", startReaderResize);
elements["reader-resizer"].addEventListener("pointermove", moveReaderResize);
elements["reader-resizer"].addEventListener("pointerup", finishReaderResize);
elements["reader-resizer"].addEventListener("pointercancel", finishReaderResize);
elements["reader-resizer"].addEventListener("keydown", adjustReaderWidth);
elements["manage-passcodes"].addEventListener("click", () => setAdminOpen(true));
elements["close-passcodes"].addEventListener("click", () => setAdminOpen(false));
elements["generate-passcode"].addEventListener("click", () => {
  elements["passcode-value"].value = generatePasscode();
  elements["passcode-value"].type = "text";
});
elements["passcode-value"].addEventListener("input", () => elements["passcode-value"].setCustomValidity(""));
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
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !elements.reader.hidden) closeReader();
});
document.addEventListener("pointerover", (event) => showTooltip(event.target.closest("[data-tooltip]")));
document.addEventListener("pointerout", (event) => {
  const owner = event.target.closest("[data-tooltip]");
  if (!owner || !(event.relatedTarget instanceof Node) || !owner.contains(event.relatedTarget)) hideTooltip();
});
document.addEventListener("focusin", (event) => showTooltip(event.target.closest("[data-tooltip]")));
document.addEventListener("focusout", hideTooltip);
window.addEventListener("scroll", hideTooltip, true);
window.addEventListener("resize", () => {
  hideTooltip();
  if (
    state.readerWidth
    && elements.workspace.classList.contains("reader-open")
    && !window.matchMedia("(max-width: 920px)").matches
  ) {
    syncReaderWidth();
  }
});
syncReaderWidth();

if (state.mode === "local") {
  loadLocal();
  window.setInterval(loadLocal, 10000);
} else {
  initializeFirebase().catch((error) => setConnection(`Firebase startup failed: ${error.message}`, "error"));
}
window.setInterval(checkForUpdate, 60000);
