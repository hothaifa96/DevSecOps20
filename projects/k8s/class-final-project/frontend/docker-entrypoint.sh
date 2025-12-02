#!/usr/bin/env sh
set -euo pipefail

CONFIG_PATH="/usr/share/nginx/html/app-config.js"
API_URL="${VITE_API_URL:-http://127.0.0.1:5000}"

if [ -f "$CONFIG_PATH" ]; then
  # Replace placeholder with runtime value; fallback is already baked in code.
  sed -i "s#__API_URL__#${API_URL}#g" "$CONFIG_PATH"
fi

exec "$@"

