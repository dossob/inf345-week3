#!/bin/sh
set -euo pipefail

output=$(python3 -m unittest discover -s tests -q 2>&1) || {
    echo "$output"
    exit 1
}

echo "$output"

count=$(python3 -m unittest discover -s tests -q 2>&1 | grep -oE '[0-9]+ test' | head -1 | awk '{print $1}')

echo "TESTS: $count/$count"
