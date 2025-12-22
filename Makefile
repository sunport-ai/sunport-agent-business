.PHONY: install test run run-msg new-business

PY ?= python
VENV ?= .venv
PIP := $(VENV)/bin/pip
PYBIN := $(VENV)/bin/python

MODE ?= BUSINESS
FIXTURE ?=
MSG ?= "Hello"
SEED ?= 42
TRACE_DIR ?= .sunport/traces
FILE_MEMORY ?= 1

install:
	$(PY) -m venv $(VENV)
	$(PIP) install -U pip
	$(PIP) install -e ".[dev]"

test:
	$(PYBIN) -m pytest -q

run:
	@if [ -z "$(FIXTURE)" ]; then \
		echo "ERROR: FIXTURE required. Example:"; \
		echo "  make run FIXTURE=examples/fixtures/business/pricing_bootstrapped_b2c.yaml"; \
		exit 1; \
	fi
	@mkdir -p "$(TRACE_DIR)"
	$(PYBIN) -m orchestrator_core.harness.cli \
		--mode "$(MODE)" \
		--agent "agent.agent:BusinessAgent" \
		--fixture "$(FIXTURE)" \
		--seed "$(SEED)" \
		$(if $(filter 1,$(FILE_MEMORY)),--file-memory,) \
		--trace-dir "$(TRACE_DIR)"

run-msg:
	@mkdir -p "$(TRACE_DIR)"
	$(PYBIN) -m orchestrator_core.harness.cli \
		--mode "$(MODE)" \
		--agent "agent.agent:BusinessAgent" \
		--seed "$(SEED)" \
		$(if $(filter 1,$(FILE_MEMORY)),--file-memory,) \
		--trace-dir "$(TRACE_DIR)" \
		$(MSG)

new-business:
	@if [ -z "$(name)" ]; then \
		echo "ERROR: name required. Example:"; \
		echo "  make new-business name=pricing_strategy_saas"; \
		exit 1; \
	fi
	@$(PYBIN) scripts/new_fixture.py business $(name)

