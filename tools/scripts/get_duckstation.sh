#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
EMU_DIR="$PROJECT_ROOT/tools/duckstation"

mkdir -p "$EMU_DIR"
cd "$EMU_DIR"

APPIMAGE_URL="https://github.com/stenzek/duckstation/releases/download/latest/DuckStation-x64.AppImage"
TARGET_FILE="DuckStation-x64.AppImage"

echo "[*] Baixando DuckStation para Linux ($TARGET_FILE)..."
curl -L -o "$TARGET_FILE" "$APPIMAGE_URL"
chmod +x "$TARGET_FILE"

echo "[+] DuckStation baixado com sucesso em: $EMU_DIR/$TARGET_FILE"
echo "[+] Para iniciar o DuckStation: $EMU_DIR/$TARGET_FILE"
