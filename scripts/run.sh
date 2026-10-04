#!/bin/sh
set -euo pipefail

PORT="${PORT:-8080}"

cd "$(dirname "$0")/.."
python3 app.py
