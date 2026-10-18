# Klonoa Beach Volleyball (PS1) — Modding & Reverse Engineering Suite

Projeto de engenharia reversa, substituição de texturas/skins e pesquisa de geometria 3D para o jogo **Klonoa Beach Volleyball** (PlayStation 1).

Compatível com **Linux** (Ubuntu/Zorin) e **Windows**.

---

## 🎯 Fases do Projeto

1. **Nível 1 (Visual Imediato):** Substituição de skins em tempo real via **DuckStation Texture Replacement** (`replacements/textures/`).
2. **Nível 2 (ROM Hacking & Assets Nativos):** Extração e conversão de arquivos de imagem `.TIM` nativos do disco e descompactação de arquivos da Namco via scripts Python (`tools/`).
3. **Nível 3 (Modelagem 3D Retro):** Análise da malha poligonal no Blender com restrições do PS1 (low-poly, coordenadas fixed-point de 16-bit, Gouraud shading).

---

## 🤖 Time de Subagentes Especializados

No Gemini CLI, você pode acionar os subagentes dedicados a qualquer momento:

| Subagente | Comando / Arquivo | Foco Principal |
| :--- | :--- | :--- |
| **Engenharia Reversa** | `@ps1-reverse-engineer` | Análise de ISO (LBA 2048/2352), disassembly MIPS R3000A no Ghidra, depuração no PCSX-Redux. |
| **Pipeline de Código** | `@game-asset-coder` | Scripts Python (`struct`, `Pillow`, `numpy`), parser de cabeçalhos `.TIM`, manipulação de paletas CLUT. |
| **Artista de Texturas** | `@ps1-texture-artist` | Edição 2D no GIMP/Photoshop, resolução, canais alfa/STP, dumps e texture packs do DuckStation. |
| **Modelagem 3D PS1** | `@ps1-3d-modeler` | Low-poly no Blender, UV mapping compacto, sem z-buffer, exportação OBJ e dados de vértices. |

---

## 📁 Estrutura do Repositório

```text
modding/
├── .gemini/agents/               # Definições dos subagentes locais
├── docs/                         # Especificações de formatos e mapas de memória
│   ├── formats/
│   └── memory-map/
├── tools/                        # Scripts Python e utilitários de extração
│   ├── scripts/
│   └── requirements.txt
├── replacements/                 # Texture Packs para DuckStation
│   └── textures/
│       └── SLES-03899/           # ID do jogo (Klonoa Beach Volleyball PAL)
│           └── replacements/     # Coloque aqui as skins modificadas (.png)
├── extracted/                    # (Ignorado pelo Git) Arquivos brutos extraídos da ISO
├── workspace/                    # (Ignorado pelo Git) Arquivos .blend, .xcf, .psd
├── build/                        # (Ignorado pelo Git) Patches .xdelta gerados
├── MODLOG.md                     # Diário de bordo com offsets e descobertas
├── README.md
└── .gitignore                    # Proteção estrita contra commit de ISOs comerciais
```

---

## 🚀 Setup Rápido

### Linux
```bash
# 1. Configurar o ambiente Python
cd tools
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Executar DuckStation
# Baixe a AppImage oficial do DuckStation e torne-a executável:
# chmod +x DuckStation-x86_64.AppImage && ./DuckStation-x86_64.AppImage
```

### Windows
```powershell
# 1. Configurar o ambiente Python
cd tools
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2. Executar DuckStation
# Baixe o pacote portátil .zip do DuckStation e execute duckstation-qt-x64-ReleaseLTCG.exe
```

---

## 🎮 Como Usar o Texture Replacement do DuckStation (Nível 1)

1. Abra o DuckStation e vá em **Settings (Configurações) -> Graphics (Gráficos) -> Texture Replacement (Substituição de Textura)**.
2. Marque as opções:
   - **Dump Textures (Despejar Texturas):** Salva as texturas originais do jogo em formato `.png` na pasta de dump do emulador.
   - **Load Custom Textures (Carregar Texturas Personalizadas):** Substitui as texturas originais pelas modificadas.
3. Inicie o *Klonoa Beach Volleyball*, jogue uma partida para que o emulador descarregue a textura do Klonoa.
4. Pegue o arquivo `.png` correspondente ao Klonoa na pasta de dump, edite no GIMP/Photoshop.
5. Salve o arquivo editado com o **mesmo nome e hash** na pasta `replacements/textures/SLES-03899/replacements/`.
6. No DuckStation, desative o *Dump Textures* e aproveite a skin no jogo!
