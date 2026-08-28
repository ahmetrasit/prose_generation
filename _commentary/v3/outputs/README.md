# Generated outputs

The v3 workflow accepts model responses only in typed paths beneath this tree:

- `adjudication/sNNN/`: structured candidate decisions;
- `synthesis/sNNN/`: raw synthesis responses and validated synthesis manifests;
- `sNNN/`: deterministically rendered prose, evidence, index, and friction files.

Validators bind every response to the exact prompt manifest as well as source,
docket, adjudication, and packet hashes before a later stage may consume it.
Validated adjudication also retains a complete focus and nominated-branch
review ledger, including exact candidate-owned contact excerpts, which the
final friction file renders deterministically.
