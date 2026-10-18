# Diretrizes do Projeto — Gemini CLI

Este é o arquivo de governança do Gemini CLI para o projeto **Klonoa Beach Volleyball (PS1) Modding Suite**.

## 🧠 Fonte Única de Verdade (Single Source of Truth)
- Antes de iniciar qualquer tarefa, leia `.modding/state.json` e `docs/MEMORY_BUS.md`.
- Mantenha o arquivo `.modding/state.json` atualizado ao concluir tarefas ou registrar novos dados de engenharia reversa.

## 🛡️ Mandatos de Segurança e Integridade
- **Zero Secrets:** NUNCA escreva, imprima ou comite chaves de API, credenciais ou dados do `.env`.
- **Zero Piracy:** NUNCA adicione arquivos `.iso`, `.bin`, `.cue` ou BIOS do PS1 ao repositório Git. Use exclusivamente patches delta ou texture packs.
- **Auditoria Obrigatória:** Todas as alterações estruturais devem ser validadas contra as regras do `@mod-security-auditor` e `@mod-qa-tester`.

## 🤖 Subagentes Especializados Disponíveis
- `@mod-architect`: Governança de arquitetura e contratos entre agentes.
- `@mod-security-auditor`: Verificação de segurança, dados sensíveis e compliance.
- `@mod-qa-tester`: Testes de paridade round-trip, alinhamento de setores e validação de hashes.
- `@ps1-reverse-engineer`: Desmontagem MIPS R3000A e análise de ISO/setores.
- `@game-asset-coder`: Scripts Python para extração de `.TIM` e empacotamento.
- `@ps1-texture-artist`: Texturas, paletas CLUT e DuckStation Texture Replacement.
- `@ps1-3d-modeler`: Geometria low-poly e Blender para PS1.
