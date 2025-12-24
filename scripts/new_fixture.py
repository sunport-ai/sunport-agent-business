# orchestrator-core/scripts/new_fixture.py
from __future__ import annotations

import argparse
from pathlib import Path
from datetime import datetime, timezone

TEMPLATE = """\
id: "{fixture_id}"
mode: "{mode}"
input_message: "{input_message}"
meta:
  # Add context dimensions here (business stage, decision_maker, constraints, etc.)
  # Example:
  # stage: "BOOTSTRAPPED"
  # decision_maker: "FOUNDER"
  # business_model: "B2B"
tool_overrides:
  # Override tools deterministically for offline dev
  # Example:
  # search:
  #   results:
  #     - title: "Mock result"
  #       url: "https://example.com"
  #       snippet: "..."
expected_sections:
  # Structure gates (used by tests)
  - "Plan"
  - "Risks"
  - "Next actions"
golden_output: |
  # Optional: paste a "golden" response here for replay/regression.
  # Leave blank initially; your FakeLLM can still return deterministic structured output.
"""

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, help="e.g. BUSINESS, COACH_GUT_HEALTH")
    ap.add_argument("--name", required=True, help="fixture file stem, e.g. pricing_b2b_seed")
    ap.add_argument("--base-dir", default="examples/fixtures", help="base fixtures directory")
    args = ap.parse_args()

    mode = args.mode.strip()
    name = args.name.strip()

    # Normalize folder naming: BUSINESS -> business, COACH_GUT_HEALTH -> coach_gut_health
    folder = mode.lower()
    base_dir = Path(args.base_dir) / folder
    base_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    fixture_id = f"{mode}:{name}:{ts}"
    out_path = base_dir / f"{name}.yaml"

    if out_path.exists():
        raise SystemExit(f"Fixture already exists: {out_path}")

    # Provide a reasonable starter prompt per mode
    default_msg = (
        "Help me price a bootstrapped B2B SaaS product." if mode.upper() == "BUSINESS"
        else "I have bloating after meals. Suggest a safe routine and what to track."
    )

    content = TEMPLATE.format(
        fixture_id=fixture_id,
        mode=mode,
        input_message=default_msg.replace('"', '\\"'),
    )

    out_path.write_text(content, encoding="utf-8")
    print(f"✅ Created fixture: {out_path}")
    print(f"   id: {fixture_id}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())



