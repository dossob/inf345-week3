#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python3 - <<'PY'
import sys
import unittest

suite = unittest.defaultTestLoader.discover("tests")
result = unittest.TextTestRunner(verbosity=2).run(suite)
passed = result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)
print(f"TESTS: {passed}/{result.testsRun}", flush=True)
sys.exit(0 if result.wasSuccessful() and result.testsRun >= 3 else 1)
PY
