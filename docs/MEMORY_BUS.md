# Universal AI Memory Bus — Klonoa Beach Volleyball Modding

Este documento é a **Fonte Única de Verdade (Single Source of Truth - SSOT)** e o barramento de memória compartilhado para **qualquer inteligência artificial ou desenvolvedor** que interaja com este repositório (Gemini CLI, Antigravity, Claude Code, Cursor, ChatGPT, etc.).

---

## 📌 Regra Fundamental para IAs que entrarem neste repositório:
1. **Sempre leia `.modding/state.json` e este arquivo (`docs/MEMORY_BUS.md`)** antes de propor alterações ou executar comandos.
2. **Atualize o `.modding/state.json`** ao concluir tarefas, descobrir novos offsets de memória ou identificar hashes de textura.
3. **Respeite a divisão de responsabilidades** dos subagentes definidos em `.gemini/agents/`.
4. **NUNCA comite ou escreva dados sensíveis** (chaves de API, arquivos `.env`, tokens) e **NUNCA adicione arquivos de ROMs proprietárias** (`.iso`, `.bin`, `.cue`) ao Git.

---

## 🏛️ Registro de Decisões de Arquitetura (ADRs)

### [ADR-001] Estratégia em Fases: Do Visual Imediato à Geometria 3D
- **Contexto:** Modificar binários do PS1 e recompilar código MIPS é complexo e propenso a frustrações iniciais.
- **Decisão:** O projeto adotará 3 fases progressivas:
  - **Fase 1 (Nível 1):** Substituição de texturas/skins via DuckStation (Texture Replacement). Retorno visual imediato, teste de game feel e extração de hashes.
  - **Fase 2 (Nível 2):** Engenharia reversa dos pacotes Namco na ISO e manipulação nativa de arquivos `.TIM` via Python.
  - **Fase 3 (Nível 3):** Substituição de malhas 3D no Blender com injeção de vértices de 16 bits.
- **Status:** Aprovado e em execução.

### [ADR-002] Governança de Agentes e Segurança
- **Contexto:** Múltiplos agentes e usuários executando tarefas de engenharia reversa podem vazar dados ou quebrar a integridade do disco.
- **Decisão:** Adicionados os agentes `@mod-architect` (orquestrador de contratos), `@mod-security-auditor` (bloqueio de segredos e checagem de legalidade de ROMs) e `@mod-qa-tester` (validação de paridade de bytes e alinhamento de 2048 bytes por setor).
- **Status:** Implementado.

---

## 📡 Log de Eventos e Comunicação Inter-Agentes

| Timestamp (UTC) | Agente / Autor | Evento / Descoberta | Impacto no Projeto |
| :--- | :--- | :--- | :--- |
| 2026-10-18 17:15 | `mod-architect` | Inicialização do repositório e time de 7 subagentes | Ambiente base configurado no Linux e pronto para Windows. |
| 2026-10-18 17:25 | `mod-security-auditor` | Blindagem de `.gitignore` e criação de `.env.example` | Segredos, arquivos `.env` e ROMs blindados contra commit acidental. |
| 2026-10-18 17:30 | `mod-architect` | Criação do Universal Memory Bus (`state.json` + `MEMORY_BUS.md`) | Interoperabilidade garantida entre Gemini, Claude, Antigravity e Cursor. |
| 2026-10-18 17:45 | `ps1-reverse-engineer` | Validação da ROM em `extracted/disc/` e correção do `.cue` | Identificado Game ID `SLPS-03433` (NTSC-J), executável `SLPS_034.33`. Pronto para dump no DuckStation. |
| 2026-10-18 18:00 | `ps1-texture-artist` | Extração de 137 texturas da VRAM e geração da galeria visual | Texturas salvas em `assets/raw_dump/textures/` e `gallery.html` gerada para inspeção visual. |
