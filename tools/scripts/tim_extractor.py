#!/usr/bin/env python3
"""
PS1 TIM Texture Extractor & Scanner
Compatível com Linux e Windows.
Usado pelo subagente @game-asset-coder para escanear binários e extrair texturas .TIM do PS1.
"""

import sys
import struct
from pathlib import Path
from typing import Optional, Tuple

TIM_MAGIC = b"\x10\x00\x00\x00"

# BPP (Bits Per Pixel) modes do PlayStation 1
BPP_MODES = {
    0: "4-bit CLUT (16 cores)",
    1: "8-bit CLUT (256 cores)",
    2: "16-bit Direct Color (BGR555)",
    3: "24-bit Direct Color (RGB888)",
}


def scan_file_for_tim(file_path: Path) -> int:
    """Escaneia um arquivo binário em busca do magic byte do formato TIM."""
    if not file_path.exists():
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
        return 0

    data = file_path.read_bytes()
    offset = 0
    found_count = 0

    print(f"[*] Escaneando '{file_path.name}' ({len(data)} bytes)...")

    while True:
        idx = data.find(TIM_MAGIC, offset)
        if idx == -1 or idx + 8 > len(data):
            break

        # Ler flag do TIM
        flag = struct.unpack_from("<I", data, idx + 4)[0]
        bpp_mode = flag & 0x07
        has_clut = bool((flag >> 3) & 0x01)

        if bpp_mode in BPP_MODES:
            print(
                f"  [+] TIM encontrado no offset 0x{idx:08X} | "
                f"Modo: {BPP_MODES[bpp_mode]} | Tem CLUT: {has_clut}"
            )
            found_count += 1

        offset = idx + 4

    print(f"[*] Busca finalizada. Total de texturas TIM detectadas: {found_count}")
    return found_count


def main():
    if len(sys.argv) < 2:
        print("Uso: python tim_extractor.py <caminho_do_arquivo_binario>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    scan_file_for_tim(target_path)


if __name__ == "__main__":
    main()
