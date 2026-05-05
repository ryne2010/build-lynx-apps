#!/usr/bin/env python3
"""Validate static dry-run eval fixtures for the Build Lynx Apps plugin.

This is intentionally lightweight: it does not call models, launch apps, install MCP
servers, or evaluate generated code. It makes the prose fixtures semi-executable by
checking schema, numbering, and coverage terms that protect the plugin's core safety
and parity contracts.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS_PATH = ROOT / "docs" / "EVALS.md"

REQUIRED_FIXTURE_HEADINGS = [
    "Polished dashboard surface",
    "shadcn-style settings form migration",
    "Scroll animation and native module fix",
    "DevTool screenshot comparison",
    "Component copy/install boundary",
    "Stripe checkout in a Lynx surface",
    "Supabase data and RLS",
    "Bundle validation during OMX workflow",
    "TypeScript custom native modules",
    "Unavailable `@dumbooks/lynx-ui` component",
    "Visual Ralph implementation loop",
    "Current Lynx desktop/SVG feature request",
    "Routing, testing, and external bundles",
    "Official Lynx skill companion routing",
    "Broader Lynx ecosystem routing",
    "High-fidelity Lynx visual concept extraction",
]

REQUIRED_SCHEMA_LABELS = [
    "Prompt",
    "Expected routing",
    "Required evidence",
    "Prohibited claims/actions",
    "Pass criteria",
]

GLOBAL_COVERAGE_TERMS = [
    "lynx-app-builder",
    "lynx-ui-guidance",
    "official global Lynx",
    "Lynx Docs MCP",
    "DevTool MCP",
    "upstream Lynx",
    "@dumbooks/lynx-ui",
    "$visual-ralph",
    "$visual-verdict",
    "no setup/config mutation",
    "no complete native host app claim",
    "no visual parity claim without",
    "no public npm availability claim",
    "no service-role key in Lynx bundle",
    "CDP commands",
    "App commands",
    "Open URLs",
    "Troubleshooting",
    "Habitat",
    "reactlynx-use",
    "state-management",
    "state atlas",
    "asset manifest",
    "icon/SVG plan",
    "accessibility/i18n cues",
    "exact export surface",
    "registry examples",
    "external-consumer stability claim",
]


@dataclass(frozen=True)
class Fixture:
    number: int
    title: str
    body: str


def parse_fixtures(text: str) -> list[Fixture]:
    matches = list(re.finditer(r"^## Fixture\s+(\d+)\s+—\s+(.+)$", text, flags=re.MULTILINE))
    fixtures: list[Fixture] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        fixtures.append(Fixture(int(match.group(1)), match.group(2).strip(), text[start:end]))
    return fixtures


def validate_text(text: str) -> list[str]:
    errors: list[str] = []
    fixtures = parse_fixtures(text)

    if len(fixtures) != len(REQUIRED_FIXTURE_HEADINGS):
        errors.append(f"expected {len(REQUIRED_FIXTURE_HEADINGS)} fixtures, found {len(fixtures)}")

    expected_numbers = list(range(1, len(fixtures) + 1))
    actual_numbers = [fixture.number for fixture in fixtures]
    if actual_numbers != expected_numbers:
        errors.append(f"fixture numbers must be contiguous: expected {expected_numbers}, got {actual_numbers}")

    for fixture, expected_title in zip(fixtures, REQUIRED_FIXTURE_HEADINGS):
        if fixture.title != expected_title:
            errors.append(
                f"fixture {fixture.number} title mismatch: expected {expected_title!r}, got {fixture.title!r}"
            )
        for label in REQUIRED_SCHEMA_LABELS:
            if f"**{label}:**" not in fixture.body:
                errors.append(f"fixture {fixture.number} missing schema label {label!r}")

    for term in GLOBAL_COVERAGE_TERMS:
        if term not in text:
            errors.append(f"docs/EVALS.md missing required coverage term {term!r}")

    return errors


def validate() -> list[str]:
    if not EVALS_PATH.exists():
        return ["missing docs/EVALS.md"]
    return validate_text(EVALS_PATH.read_text(encoding="utf-8"))


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("build-lynx-apps eval contract validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
