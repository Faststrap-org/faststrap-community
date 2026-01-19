---
description: Faststrap Community Development Workflow
---

# /community-test
Run all community integration and component tests.
// turbo
1. Run pytest: `$env:PYTHONPATH="src"; pytest tests -v`

# /community-showcase
Run the community showcase application to verify visual styles.
1. Run showcase: `$env:PYTHONPATH="src"; python examples/showcase.py`

# /community-cleanup
Cleanup temporary log files and test artifacts.
// turbo
1. Cleanup: `rm test_results*.log, coverage.xml, .pytest_cache -r -ErrorAction SilentlyContinue`
