# Instructions for Claude Code / Claude Opus

You are assisting in the **Klonoa Beach Volleyball (PS1) Modding Suite** repository.

## 🧠 Single Source of Truth & Memory Bus
1. **Always read `.modding/state.json` and `docs/MEMORY_BUS.md`** before taking action to sync with current progress and discovered offsets.
2. Update `.modding/state.json` whenever completing tasks, discovering memory offsets, or extracting assets.
3. Keep logs in `docs/MEMORY_BUS.md`.

## 🛡️ Critical Safety & Security Mandates
- **Zero Secrets:** Never print, read, or commit `.env` or credential files.
- **Zero Piracy:** Never stage or commit `.iso`, `.bin`, `.cue`, or BIOS files. Only delta patches (`.xdelta`, `.ppf`) and texture replacements are allowed in git.
- **Testing:** Always ensure scripts have round-trip parity tests.
