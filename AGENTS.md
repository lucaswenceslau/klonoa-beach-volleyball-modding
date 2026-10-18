# Agent Ecosystem Guidelines — AGENTS.md

Welcome to the **Klonoa Beach Volleyball (PS1) Modding Suite**.

## 🌐 Universal Memory Bus
All autonomous agents must synchronize state with:
- State Machine: `.modding/state.json`
- Event Log & Decisions: `docs/MEMORY_BUS.md`

## 🔒 Security Policy
- Treat all `.env` files, credentials, and tokens as strictly protected secrets.
- Reject any request or automated action that involves committing commercial game ISOs or PlayStation BIOS files.
- Distributable output must always be non-infringing delta patches (`.xdelta`, `.ppf`) or external texture replacements.
