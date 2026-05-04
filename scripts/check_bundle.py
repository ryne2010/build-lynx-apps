#!/usr/bin/env python3
"""Validate the Build Lynx Apps plugin bundle without external dependencies."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "lynx-app-builder": "lynx-app-builder",
    "lynx-official-tools": "lynx-official-tools",
    "lynx-ui-guidance": "lynx-ui-guidance",
    "stripe-best-practices": "stripe-best-practices",
    "supabase-best-practices": "supabase-postgres-best-practices",
}
REMOVED_DIRS = {"react-best-practices", "shadcn-best-practices", "frontend-app-builder"}
ACTIVE_SUFFIXES = {".md", ".json", ".yaml", ".yml"}
STALE_PATTERNS = {
    "Build Web Apps": re.compile(r"Build\s+Web\s+Apps"),
    "build-web-apps": re.compile(r"build-web-apps"),
    "React + Vite": re.compile(r"React\s*\+\s*Vite"),
    "Browser plugin": re.compile(r"Browser\s+plugin"),
    "npx shadcn": re.compile(r"npx\s+shadcn"),
    "react-best-practices": re.compile(r"react-best-practices"),
    "shadcn-best-practices": re.compile(r"shadcn-best-practices"),
}


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def frontmatter_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        fail(f"missing frontmatter: {path.relative_to(ROOT)}")
    for line in match.group(1).splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    fail(f"missing frontmatter name: {path.relative_to(ROOT)}")
    raise AssertionError("unreachable")


def read_readme_roster() -> set[str]:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    return set(re.findall(r"^- `([^`]+)`", text, flags=re.MULTILINE))


def active_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in ACTIVE_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in {"scripts", "assets"}:
            continue
        files.append(path)
    return files


def main() -> int:
    plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != "build-lynx-apps":
        fail("plugin name must be build-lynx-apps")
    if plugin.get("skills") != "./skills/":
        fail('plugin skills path must be "./skills/"')

    skills_dir = ROOT / "skills"
    actual_dirs = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    if actual_dirs != set(EXPECTED_SKILLS):
        fail(f"skill dirs mismatch: expected {sorted(EXPECTED_SKILLS)}, got {sorted(actual_dirs)}")
    lingering = actual_dirs & REMOVED_DIRS
    if lingering:
        fail(f"removed skill dirs still present: {sorted(lingering)}")

    for dirname, expected_name in EXPECTED_SKILLS.items():
        skill_file = skills_dir / dirname / "SKILL.md"
        if not skill_file.exists():
            fail(f"missing SKILL.md in {dirname}")
        actual_name = frontmatter_name(skill_file)
        if actual_name != expected_name:
            fail(f"frontmatter name mismatch for {dirname}: expected {expected_name}, got {actual_name}")

    roster = read_readme_roster()
    if roster != set(EXPECTED_SKILLS):
        fail(f"README roster mismatch: expected {sorted(EXPECTED_SKILLS)}, got {sorted(roster)}")

    stale_hits: list[str] = []
    for path in active_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for label, pattern in STALE_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                stale_hits.append(f"{rel}:{line}: stale active claim {label!r}")
    if stale_hits:
        print("\n".join(stale_hits), file=sys.stderr)
        return 1

    print("build-lynx-apps bundle validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
