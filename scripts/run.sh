#!/usr/bin/env bash

set -euo pipefail

export PORT="${PORT:-8080}"

cd "$(dirname "$0")/.."
exec python3 app.py
