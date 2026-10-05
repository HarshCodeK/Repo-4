# MegaProject — sandboxed tool agent

Small tool-calling boundary where the model is untrusted input and file access is constrained to a resolved workspace.

`Workspace.path()` rejects absolute paths, parent traversal, home expansion, and resolved paths outside the workspace. Only `list` and bounded `read` tools are exposed.

This is a **path sandbox**, not OS-level isolation. Hostile workloads need container/VM and OS restrictions.

## Test
`pip install -e . && pytest -q`

## Interview notes
Resolve before checking; allowlist tools; cap agent rounds; keep retrieval separate from the security boundary.

## License
MIT.
