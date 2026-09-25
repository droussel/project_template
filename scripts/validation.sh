#!/usr/bin/env bash
# ADAPT THIS FILE during project bootstrap. Do not turn placeholders into no-ops.
# In the adopted project, add python3 scripts/check-adoption.py as a shared phase
# after rewriting project authorities; do not claim its PASS for the kit itself.
# Requires Bash 3.2+, Git, and Python 3.9+ for the portable source-size guard.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ $# -ne 1 || ( "$1" != "check" && "$1" != "verify" ) ]]; then
  printf 'Usage: scripts/check | scripts/verify\n' >&2
  exit 2
fi
MODE="$1"
CURRENT_PHASE='initialization'
trap 'result=$?; printf "FAILED: %s (exit %s). Later phases were not run.\n" "$CURRENT_PHASE" "$result" >&2; exit "$result"' ERR

phase() {
  local label="$1"
  shift
  printf '\n==> %s\n' "$label"
  CURRENT_PHASE="$label"
  # Invoke unconditionally: an `||` here would disable errexit inside shell functions.
  # The inherited ERR trap preserves the actual failure and stops later phases.
  "$@"
  printf 'PASS: %s\n' "$label"
}

unconfigured() {
  printf 'UNCONFIGURED: %s\n' "$1" >&2
  printf 'Wire the real native commands in scripts/validation.sh; see CONTRIBUTING.md.\n' >&2
  exit 2
}

stack_fast() {
  # Replace this function with native check-only formatter, linter/static analysis,
  # types when applicable, and high-value fast behavior tests. Define each native
  # command only once. Commands must fail on errors rather than mask their status.
  unconfigured 'stack fast phases: formatter, static analysis, types, fast tests'
}

stack_full() {
  # Replace with full behavior/integration tests, per-layer coverage enforcement,
  # build/package, dependency-boundary checks, and applicable docs build/link/example
  # checks. Reuse fast-phase results where valid; do not blindly run the same tests
  # twice. List every justified not-applicable phase in the final project script.
  unconfigured 'stack full phases: full tests, coverage, build, architecture, documentation'
}

phase 'Authored source size (300 warning / 500 ceiling)' python3 scripts/check-source-size.py
phase 'Stack fast checks' stack_fast

if [[ "$MODE" == 'check' ]]; then
  # ADAPT this list to the actual full-only phases when wiring the stack.
  printf '\nCHECK ONLY: full-suite, coverage, build/package, architecture, and docs gates were not run.\n'
  printf 'Run scripts/verify before declaring substantial work complete.\n'
else
  phase 'Stack full checks' stack_full
  printf '\nPASS: all configured deterministic verification phases.\n'
fi
