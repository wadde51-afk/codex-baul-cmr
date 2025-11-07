#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

REPO="$HOME/codex-baul-cmr"
cd "$REPO"

# 1) Regenerar el reporte
python3 listar_contenido_cmr.py

# 2) Preparar commit solo si hay cambios
git add -A
if git diff --cached --quiet; then
  echo "$(date -Iseconds) • Sin cambios, no se hace push."
  exit 0
fi

# 3) Sincronizar con remoto y subir
git pull --rebase || true
git commit -m "Auto: inventario CMR actualizado $(date -Iseconds)"
git push origin main

echo "$(date -Iseconds) • Cambios enviados a GitHub."
