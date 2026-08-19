#!/usr/bin/env bash
# PostToolUse wrapper. Silent no-op when python3 is unavailable.
command -v python3 >/dev/null 2>&1 || exit 0
exec python3 "${CLAUDE_PLUGIN_ROOT:-$(dirname "$0")/..}/scripts/slop-check.py"
