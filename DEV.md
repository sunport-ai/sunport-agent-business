# Developer Guide — Business Agent (Offline)

You are building isolated agent logic. **You do not need access** to databases, AWS, or live LLMs.

This repo provides:
- A **local harness** (FakeLLM + Fake tools + Fake memory)
- **Fixture-driven tests** ("golden prompts")
- A **trace file** written per run for debugging

---

## ⚡ Quick Start

### 1) Install dependencies
```bash
make install
```

### 2) Run all tests
```bash
make test
```

### 3) Run the harness with a fixture
```bash
make run FIXTURE=examples/fixtures/business/pricing_bootstrapped_b2c.yaml
```

### 4) Run the harness with an ad-hoc message
```bash
make run-msg MSG="Help me price a bootstrapped SaaS"
```

Traces are written to `.sunport/traces/` by default.

---

## ✅ Adding new test coverage (Fixtures)

### Create a new BUSINESS fixture
```bash
make new-business name=pricing_strategy_saas
```

Then edit the generated YAML under:
- `examples/fixtures/business/`

### Fixture schema (YAML)
Fixtures support:
- `id`: unique fixture id (defaults to file stem)
- `mode`: `BUSINESS`
- `input_message`: what the user asked
- `meta`: mocked context (stage/persona/budget/etc.)
- `tool_overrides`: deterministic tool outputs (e.g., fake search results)
- `expected_sections`: structure gates
- `golden_output`: optional replay output for deterministic regression

---

## 🧪 Testing Standards

- **Every logic change must add or update at least one fixture**.
- Use **FakeLLM** in tests (no API keys, no costs, deterministic).
- Keep outputs structured (no generic paragraphs).
- Prefer **section-based assertions** over full string equality.

---

## 🔒 Security rules

- Do not add API keys.
- Do not add calls to production services.
- Do not add real database clients to harness execution paths.

