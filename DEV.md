# Local Dev Harness Workflow (Offline)

## Setup
```bash
make setup
```

## Run with a fixture
```bash
make harness-run MODE=BUSINESS FIXTURE=examples/fixtures/business/pricing_bootstrapped_b2c.yaml
```

## Run with a raw message
```bash
make harness-run-msg MODE=BUSINESS MSG="Help me write a GTM plan"
```

## Create a new fixture
```bash
make new-fixture MODE=BUSINESS NAME=pricing_b2b_seed
```

## Run tests
```bash
make test
```

Traces are saved to `.sunport/traces/` by default.

