#!/usr/bin/env python3
"""
Gera uma galeria visual HTML responsiva de todas as texturas extraídas pelo DuckStation.
Permite inspecionar facilmente as texturas do Klonoa com renderização pixelada nítida.
"""

import struct
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEXTURES_DIR = BASE_DIR / "assets" / "raw_dump" / "textures"
OUTPUT_HTML = TEXTURES_DIR / "gallery.html"


def get_png_dimensions(path: Path):
    try:
        data = path.read_bytes()
        if len(data) >= 24 and data[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", data[16:24])
            return w, h
    except Exception:
        pass
    return None, None


def generate_gallery():
    png_files = sorted(TEXTURES_DIR.glob("*.png"))
    if not png_files:
        print(f"[-] Nenhuma textura encontrada em {TEXTURES_DIR}")
        return

    cards_html = []
    for p in png_files:
        w, h = get_png_dimensions(p)
        size_str = f"{w}x{h}" if w else "Desconhecido"
        kb_size = f"{p.stat().st_size / 1024:.1f} KB"

        card = f"""
        <div class="card" onclick="copyName('{p.name}')">
            <div class="img-wrapper">
                <img src="{p.name}" alt="{p.name}">
            </div>
            <div class="info">
                <div class="dim">{size_str} <span class="size">({kb_size})</span></div>
                <div class="filename" title="{p.name}">{p.name}</div>
            </div>
        </div>
        """
        cards_html.append(card)

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galeria de Texturas — Klonoa Beach Volleyball (SLPS-03433)</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: #12141a;
            color: #e6edf3;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            padding: 24px;
        }}
        header {{
            max-width: 1400px;
            margin: 0 auto 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid #30363d;
        }}
        h1 {{ font-size: 24px; color: #58a6ff; margin-bottom: 8px; }}
        p {{ color: #8b949e; font-size: 14px; line-height: 1.5; }}
        .instructions {{
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 12px 16px;
            margin-top: 12px;
            font-size: 13px;
            color: #c9d1d9;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 16px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .card {{
            background: #1c2128;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            transition: transform 0.15s ease, border-color 0.15s ease, background 0.15s ease;
        }}
        .card:hover {{
            transform: translateY(-2px);
            border-color: #58a6ff;
            background: #22272e;
        }}
        .img-wrapper {{
            width: 100%;
            height: 140px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #0d1117;
            border-radius: 6px;
            background-image:
              linear-gradient(45deg, #161b22 25%, transparent 25%),
              linear-gradient(-45deg, #161b22 25%, transparent 25%),
              linear-gradient(45deg, transparent 75%, #161b22 75%),
              linear-gradient(-45deg, transparent 75%, #161b22 75%);
            background-size: 16px 16px;
            background-position: 0 0, 0 8px, 8px -8px, -8px 0px;
            overflow: hidden;
        }}
        .img-wrapper img {{
            max-width: 90%;
            max-height: 90%;
            image-rendering: pixelated;
            image-rendering: crisp-edges;
            object-fit: contain;
        }}
        .info {{
            width: 100%;
            margin-top: 10px;
            text-align: center;
        }}
        .dim {{
            font-size: 12px;
            font-weight: 600;
            color: #7ee787;
        }}
        .size {{
            color: #8b949e;
            font-weight: normal;
        }}
        .filename {{
            font-size: 10px;
            color: #8b949e;
            margin-top: 4px;
            word-break: break-all;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            font-family: ui-monospace, monospace;
        }}
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #238636;
            color: white;
            padding: 10px 18px;
            border-radius: 6px;
            font-size: 13px;
            display: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }}
    </style>
</head>
<body>
    <header>
        <h1>🎮 Galeria de Texturas — Klonoa Beach Volleyball</h1>
        <p>Total de texturas extraídas da VRAM: <strong>{len(png_files)} texturas</strong></p>
        <div class="instructions">
            💡 <strong>Como editar:</strong> Clique em qualquer textura para copiar o nome do arquivo. Abra-a no GIMP, pinte sua modificação e salve em <code>replacements/textures/SLPS-03433/replacements/</code> com exatamente o mesmo nome. O DuckStation atualizará o jogo na hora!
        </div>
    </header>

    <div class="grid">
        {"".join(cards_html)}
    </div>

    <div id="toast">Nome copiado para a área de transferência!</div>

    <script>
        function copyName(name) {{
            navigator.clipboard.writeText(name);
            const toast = document.getElementById('toast');
            toast.innerText = "Copiado: " + name;
            toast.style.display = "block";
            setTimeout(() => {{ toast.style.display = "none"; }}, 2000);
        }}
    </script>
</body>
</html>
    """

    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    print(f"[+] Galeria visual gerada com sucesso em: {OUTPUT_HTML}")


if __name__ == "__main__":
    generate_gallery()
