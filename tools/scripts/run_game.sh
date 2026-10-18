#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

EMU="$PROJECT_ROOT/tools/duckstation/DuckStation-x64.AppImage"
CUE_FILE="$PROJECT_ROOT/extracted/disc/original_dump/Klonoa Beach Volley - Saikyou Team Ketteisen! (Japan).cue"

if [ ! -f "$EMU" ]; then
    echo "[-] DuckStation não encontrado em: $EMU"
    echo "[*] Baixando DuckStation..."
    "$SCRIPT_DIR/get_duckstation.sh"
fi

if [ ! -f "$CUE_FILE" ]; then
    echo "[-] Arquivo .cue do jogo não encontrado em: $CUE_FILE"
    exit 1
fi

echo "[+] Iniciando Klonoa Beach Volleyball (SLPS-03433) no DuckStation..."
"$EMU" "$CUE_FILE"
