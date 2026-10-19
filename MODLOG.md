# Diário de Bordo & Engenharia Reversa (Klonoa Beach Volleyball)

## Metadados do Jogo
- **Título:** Klonoa Beach Volley: Saikyou Team Kettei-sen!
- **Plataforma:** Sony PlayStation (PSX / PS1)
- **Desenvolvedora / Publicadora:** Namco
- **Região & Serial Ativo:** Japão (NTSC-J) — **`SLPS-03433`**
- **Executável Principal:** `SLPS_034.33` (boot via `SYSTEM.CNF`)
- **Mídia:** CD-ROM (Mode 2 Form 1 - 2048 bytes/setor para arquivos de dados)
- **Local da Imagem de Disco:** `extracted/disc/original_dump/` (661.575.264 bytes)
- **BIOS em Uso:** `scph5500.bin` (Sony NTSC-J oficial) em `~/.local/share/duckstation/bios/`

---

## Log de Sessões & Conquistas

### Sessão 1: Fundação do Ambiente, Tooling e Primeiro Boot (Concluída)
1. **Ambiente & Ferramentas:**
   - Criado o repositório `/home/rodrigues/modding` e publicado no GitHub: `lucaswenceslau/klonoa-beach-volleyball-modding`.
   - Instalado Blender 5.2 via Flatpak (`org.blender.Blender`).
   - Identificado GIMP 3.2 via Flatpak (`org.gimp.GIMP`).
   - Baixado e configurado DuckStation AppImage em `tools/duckstation/DuckStation-x64.AppImage`.
   - Criado script de execução rápida `tools/scripts/run_game.sh` e atalho na Área de Trabalho.
2. **Arquitetura Multi-Agentes & Universal Memory Bus:**
   - Configurados 7 subagentes especializados (`@mod-architect`, `@mod-security-auditor`, `@mod-qa-tester`, `@ps1-reverse-engineer`, `@game-asset-coder`, `@ps1-texture-artist`, `@ps1-3d-modeler`).
   - Criado barramento universal agnóstico de IAs (`.modding/state.json`, `docs/MEMORY_BUS.md`, `GEMINI.md`, `CLAUDE.md`, `AGENTS.md`, `.cursorrules`).
3. **Engenharia Reversa & Dumps de Textura:**
   - ROM japonesa alinhada e corrigido o arquivo `.cue` para apontar corretamente para o arquivo `.bin`.
   - Primeiro boot bem-sucedido no DuckStation com renderizador Vulkan e BIOS `scph5500.bin`.
   - Teste de dumping de VRAM: extraídas 137 texturas brutas (`vram-write-*`) e gerada galeria visual `gallery.html`.
   - Diagnóstico técnico do CLUT: compreendido que `vram-write` gera dados brutos pré-paleta (estática colorida).
   - Configuração refinada para a próxima sessão: `DumpVRAMWrites = false`, `DumpTexturePages = true`, `DumpFullTexturePages = true` para capturar as texturas limpas (`texpage-*`) com cores e CLUTs reais aplicados.

---

## Próximos Passos Imediatos para a Próxima Sessão:
1. Executar `./tools/scripts/run_game.sh` para iniciar o jogo com as novas configurações de dump.
2. Jogar 10 segundos para gerar as texturas com prefixo `texpage-*` (com as cores e rostos reais).
3. Abrir a galeria `assets/raw_dump/textures/gallery.html` e selecionar a textura da skin do Klonoa.
4. Pintar a nova skin no GIMP e salvar em `replacements/textures/SLPS-03433/replacements/`.
5. Ver o mod funcionando em tempo real na quadra de areia!
