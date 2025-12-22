# orchestrator-core/Makefile

.PHONY: help setup test harness-run harness-run-msg new-fixture fmt

PY ?= python
VENV ?= .venv
PIP := $(VENV)/bin/pip
PYBIN := $(VENV)/bin/python

# Defaults (override at runtime)
MODE ?= BUSINESS
FIXTURE ?=
MSG ?= "Hello"
SEED ?= 42
TRACE_DIR ?= .sunport/traces
FILE_MEMORY ?= 1

help:
	@echo ""
	@echo "Targets:"
	@echo "  make setup                         Create venv + install deps"
	@echo "  make test                          Run pytest"
	@echo "  make harness-run MODE=... FIXTURE=...   Run harness using a fixture"
	@echo "  make harness-run-msg MODE=... MSG='...' Run harness with a raw message"
	@echo "  make new-fixture MODE=... NAME=...      Scaffold a new fixture YAML"
	@echo ""
	@echo "Examples:"
	@echo "  make harness-run MODE=BUSINESS FIXTURE=examples/fixtures/business/pricing_bootstrapped_b2c.yaml"
	@echo "  make harness-run-msg MODE=BUSINESS MSG='Help me price a B2B API'"
	@echo ""

setup:
	$(PY) -m venv $(VENV)
	$(PIP) install -U pip
	$(PIP) install -e ".[dev]"

test:
	$(PYBIN) -m pytest -q

harness-run:
	@if [ -z "$(FIXTURE)" ]; then \
		echo "ERROR: FIXTURE is required. Example:"; \
		echo "  make harness-run MODE=BUSINESS FIXTURE=examples/fixtures/business/pricing_bootstrapped_b2c.yaml"; \
		exit 1; \
	fi
	@mkdir -p "$(TRACE_DIR)"
	$(PYBIN) -m orchestrator_core.harness.cli \
		--mode "$(MODE)" \
		--fixture "$(FIXTURE)" \
		--seed "$(SEED)" \
		$(if $(filter 1,$(FILE_MEMORY)),--file-memory,) \
		--trace-dir "$(TRACE_DIR)"

harness-run-msg:
	@mkdir -p "$(TRACE_DIR)"
	$(PYBIN) -m orchestrator_core.harness.cli \
		--mode "$(MODE)" \
		--message $(MSG) \
		--seed "$(SEED)" \
		$(if $(filter 1,$(FILE_MEMORY)),--file-memory,) \
		--trace-dir "$(TRACE_DIR)"

new-fixture:
	@if [ -z "$(MODE)" ] || [ -z "$(NAME)" ]; then \
		echo "ERROR: MODE and NAME are required. Example:"; \
		echo "  make new-fixture MODE=BUSINESS NAME=pricing_b2b_seed"; \
		exit 1; \
	fi
	$(PYBIN) scripts/new_fixture.py --mode "$(MODE)" --name "$(NAME)"

