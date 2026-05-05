#!/usr/bin/env python3
"""Validate the Build Lynx Apps plugin bundle without external dependencies."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REPOSITORY = "https://github.com/ryne2010/build-lynx-apps"
EXPECTED_SKILLS = {
    "lynx-app-builder": "lynx-app-builder",
    "lynx-official-tools": "lynx-official-tools",
    "reactlynx-best-practices": "reactlynx-best-practices",
    "lynx-typescript": "lynx-typescript",
    "lynx-devtool": "lynx-devtool",
    "lynx-trace-record": "lynx-trace-record",
    "lynx-trace-analysis": "lynx-trace-analysis",
    "debug-info-remapping": "debug-info-remapping",
    "lynx-ui-guidance": "lynx-ui-guidance",
    "stripe-best-practices": "stripe-best-practices",
    "supabase-postgres-best-practices": "supabase-postgres-best-practices",
}
REMOVED_DIRS = {"react-best-practices", "shadcn-best-practices", "frontend-app-builder"}
ACTIVE_SUFFIXES = {".md", ".json", ".yaml", ".yml"}
EXCLUDED_TOP_LEVEL = {
    ".git",
    ".omx",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "assets",
    "coverage",
    "dist",
    "node_modules",
    "scripts",
}
STALE_PATTERNS = {
    "Build Web Apps": re.compile(r"Build\s+Web\s+Apps"),
    "build-web-apps": re.compile(r"build-web-apps"),
    "React + Vite": re.compile(r"React\s*\+\s*Vite"),
    "Browser plugin": re.compile(r"Browser\s+plugin"),
    "npx shadcn": re.compile(r"npx\s+shadcn"),
    "react-best-practices": re.compile(r"react-best-practices"),
    "shadcn-best-practices": re.compile(r"shadcn-best-practices"),
}
REQUIRED_PATHS = [
    ".codex-plugin/plugin.json",
    "agents/openai.yaml",
    "README.md",
    "docs/COOKBOOK.md",
    "docs/EVALS.md",
    "scripts/check_evals.py",
    "skills/reactlynx-best-practices/SKILL.md",
    "skills/reactlynx-best-practices/agents/openai.yaml",
    "skills/lynx-typescript/SKILL.md",
    "skills/lynx-typescript/agents/openai.yaml",
    "skills/lynx-devtool/SKILL.md",
    "skills/lynx-devtool/agents/openai.yaml",
    "skills/lynx-trace-record/SKILL.md",
    "skills/lynx-trace-record/agents/openai.yaml",
    "skills/lynx-trace-analysis/SKILL.md",
    "skills/lynx-trace-analysis/agents/openai.yaml",
    "skills/debug-info-remapping/SKILL.md",
    "skills/debug-info-remapping/agents/openai.yaml",
]
OFFICIAL_TOOL_REQUIRED_STRINGS = [
    "lynx-docs://llms.txt",
    "lynx-docs://versions.md",
    "lynx-docs://react/start/quick-start.md",
    "lynx-docs://react/start/integrate-with-existing-apps.md",
    "lynx-docs://ai/lynx-docs-mcp.md",
    "lynx-docs://ai/lynx-devtool-mcp.md",
    "lynx-docs://blog/lynx-3-7.md",
    "lynx-docs://react/reactlynx-testing-library.md",
    "lynx-docs://react/routing/tanstack-router.md",
    "lynx-docs://react/code-splitting.md",
    "lynx-docs://rspeedy/external-bundle.md",
    "lynx-docs://react/state-management/zustand.md",
    "lynx-docs://blog/lynx-3-6.md",
    "reactlynx-use",
    "habitat-usage",
    "CDP commands",
    "App commands",
    "Open URLs",
    "Troubleshooting",
    "lynx-docs://ai/skills/trace-record.md",
    "lynx-docs://ai/skills/trace-analysis.md",
    "lynx-docs://ai/skills/debug-info-remapping.md",
    "local `lynx-typescript`",
    "local `lynx-devtool`",
    "local `lynx-trace-record`",
    "local `lynx-trace-analysis`",
    "local `debug-info-remapping`",
]
REACTLYNX_REQUIRED_STRINGS = [
    "lynx-docs://ai/skills/reactlynx-best-practices.md",
    "lynx-docs://react/best-practices.md",
    "lynx-docs://react/thinking-in-reactlynx.md",
    "lynx-docs://react/main-thread-script.md",
    "lynx-docs://ai/skills/lynx-typescript.md",
    "lynx-docs://react/reactlynx-testing-library.md",
    "background only",
    "bindtap",
    "catchtap",
    "main-thread:",
    "runOnMainThread",
    "runOnBackground",
    "with { runtime: 'shared' }",
    "JSON-serializable",
    "Memory Routing",
    "reactlynx-use",
    "global event hooks",
    "state-management",
]
APP_BUILDER_REQUIRED_STRINGS = [
    "$visual-ralph",
    "$visual-verdict",
    "Visual QA ledger",
    "runOnMainThread",
    "runOnBackground",
    "engineVersion",
    "ReactLynx Testing Library",
    "@dumbooks/lynx-ui",
    "state atlas",
    "asset manifest",
    "icon/SVG",
    "accessibility/i18n",
]

LYNX_TYPESCRIPT_REQUIRED_STRINGS = [
    "lynx-docs://ai/skills/lynx-typescript.md",
    "lynx-docs://rspeedy/typescript.md",
    "@lynx-js/rspeedy/client",
    "isolatedModules",
    "NativeModules",
    "IntrinsicElements",
    "InitData",
    "MainThread",
    "import type",
]
LYNX_DEVTOOL_REQUIRED_STRINGS = [
    "lynx-docs://ai/lynx-devtool-mcp.md",
    "lynx-docs://ai/skills/lynx-devtool.md",
    "connected device/app",
    "console",
    "loaded sources",
    "screenshots",
    "read-only",
    "CDP commands",
    "App commands",
    "Open URLs",
    "Troubleshooting",
    "connector/transport",
]
LYNX_TRACE_RECORD_REQUIRED_STRINGS = [
    "lynx-docs://ai/skills/trace-record.md",
    "lynx-docs://guide/devtool/trace.md",
    "trace artifact path",
    "startup/white screen",
    "scroll jank",
    "JS profiling",
]
LYNX_TRACE_ANALYSIS_REQUIRED_STRINGS = [
    "lynx-docs://ai/skills/trace-analysis.md",
    "lynx-docs://guide/devtool/trace.md",
    "rank",
    "startup/white screen",
    "frame drops",
    "native module",
    "Do not fabricate metric values",
]
DEBUG_INFO_REQUIRED_STRINGS = [
    "lynx-docs://ai/skills/debug-info-remapping.md",
    "lynx-docs://rspeedy/output.md",
    "source maps",
    "main-thread",
    "generated artifact",
    "Do not claim a source location without mapping evidence",
]

LYNX_UI_REQUIRED_FIELDS = [
    "status",
    "stability",
    "ownership.copyInstall",
    "publicExport",
    "exportChannel",
    "engineCompatibility.proof",
    "runtimeCompatibility.proofGate",
    "runtimeCompatibility.targetHosts",
    "runtimeCompatibility.verifiedHosts",
    "sourceProvenance",
    "contentHash",
    "proofArtifacts",
    "proofRequirements",
    "aiUsageHints",
    "licenseOriginalityNotes",
    "officialSubstrateStatus",
    "officialSubstrate",
    "adapterStrategy",
    "dependencyGate",
    "local-workspace",
    "internal-beta",
    "future open source",
    "pnpm lynx-ui list --items --json",
]
SERVICE_REQUIRED_STRINGS = {
    "skills/stripe-best-practices/SKILL.md": [
        "secret keys",
        "webhook",
        "trusted backend",
        "target host surface",
        "Lynx bundle",
    ],
    "skills/supabase-postgres-best-practices/SKILL.md": [
        "service-role",
        "Row-Level Security",
        "anon key",
        "Lynx bundle",
        "host-dependent",
    ],
}


def frontmatter_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        raise ValueError(f"missing frontmatter: {path.relative_to(ROOT)}")
    for line in match.group(1).splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    raise ValueError(f"missing frontmatter name: {path.relative_to(ROOT)}")


def read_readme_roster() -> set[str]:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    return set(re.findall(r"^- `([^`]+)`", text, flags=re.MULTILINE))


def is_git_ignored(rel: Path) -> bool:
    try:
        result = subprocess.run(
            ["git", "check-ignore", "-q", "--", rel.as_posix()],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def active_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in ACTIVE_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        if is_git_ignored(rel):
            continue
        files.append(path)
    return files


def require_strings(errors: list[str], rel_path: str, strings: list[str]) -> None:
    path = ROOT / rel_path
    if not path.exists():
        errors.append(f"missing required file: {rel_path}")
        return
    text = path.read_text(encoding="utf-8")
    for expected in strings:
        if expected not in text:
            errors.append(f"{rel_path}: missing required text {expected!r}")


def validate() -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    try:
        plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report validation context
        errors.append(f"could not read plugin.json: {exc}")
        plugin = {}
    if plugin.get("name") != "build-lynx-apps":
        errors.append("plugin name must be build-lynx-apps")
    if plugin.get("skills") != "./skills/":
        errors.append('plugin skills path must be "./skills/"')
    if plugin.get("repository") != EXPECTED_REPOSITORY:
        errors.append(f"plugin repository must be {EXPECTED_REPOSITORY}")
    if plugin.get("homepage") != EXPECTED_REPOSITORY:
        errors.append(f"plugin homepage must be {EXPECTED_REPOSITORY}")
    website = plugin.get("interface", {}).get("websiteURL")
    if website != EXPECTED_REPOSITORY:
        errors.append(f"plugin interface.websiteURL must be {EXPECTED_REPOSITORY}")

    skills_dir = ROOT / "skills"
    actual_dirs = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    if actual_dirs != set(EXPECTED_SKILLS):
        errors.append(f"skill dirs mismatch: expected {sorted(EXPECTED_SKILLS)}, got {sorted(actual_dirs)}")
    lingering = actual_dirs & REMOVED_DIRS
    if lingering:
        errors.append(f"removed skill dirs still present: {sorted(lingering)}")

    for dirname, expected_name in EXPECTED_SKILLS.items():
        skill_file = skills_dir / dirname / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"missing SKILL.md in {dirname}")
            continue
        try:
            actual_name = frontmatter_name(skill_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if actual_name != expected_name:
            errors.append(f"frontmatter name mismatch for {dirname}: expected {expected_name}, got {actual_name}")
        agent_file = skills_dir / dirname / "agents" / "openai.yaml"
        if not agent_file.exists():
            errors.append(f"missing agents/openai.yaml in {dirname}")

    roster = read_readme_roster()
    if roster != set(EXPECTED_SKILLS):
        errors.append(f"README roster mismatch: expected {sorted(EXPECTED_SKILLS)}, got {sorted(roster)}")

    require_strings(errors, "skills/lynx-app-builder/SKILL.md", APP_BUILDER_REQUIRED_STRINGS)
    require_strings(errors, "skills/lynx-official-tools/SKILL.md", OFFICIAL_TOOL_REQUIRED_STRINGS)
    require_strings(errors, "skills/reactlynx-best-practices/SKILL.md", REACTLYNX_REQUIRED_STRINGS)
    require_strings(errors, "skills/lynx-typescript/SKILL.md", LYNX_TYPESCRIPT_REQUIRED_STRINGS)
    require_strings(errors, "skills/lynx-devtool/SKILL.md", LYNX_DEVTOOL_REQUIRED_STRINGS)
    require_strings(errors, "skills/lynx-trace-record/SKILL.md", LYNX_TRACE_RECORD_REQUIRED_STRINGS)
    require_strings(errors, "skills/lynx-trace-analysis/SKILL.md", LYNX_TRACE_ANALYSIS_REQUIRED_STRINGS)
    require_strings(errors, "skills/debug-info-remapping/SKILL.md", DEBUG_INFO_REQUIRED_STRINGS)
    require_strings(errors, "skills/lynx-ui-guidance/SKILL.md", LYNX_UI_REQUIRED_FIELDS)
    for rel, strings in SERVICE_REQUIRED_STRINGS.items():
        require_strings(errors, rel, strings)

    evals = ROOT / "docs" / "EVALS.md"
    if evals.exists():
        eval_text = evals.read_text(encoding="utf-8")
        fixture_count = len(re.findall(r"^## Fixture\s+\d+", eval_text, flags=re.MULTILINE))
        if fixture_count != 16:
            errors.append(f"docs/EVALS.md must contain exactly 16 fixtures, found {fixture_count}")
        for heading in ["Expected routing", "Required evidence", "Prohibited claims/actions", "Pass criteria"]:
            if heading not in eval_text:
                errors.append(f"docs/EVALS.md missing fixture heading {heading!r}")
        eval_check = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_evals.py")],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if eval_check.returncode != 0:
            detail = (eval_check.stderr or eval_check.stdout).strip()
            errors.append(f"docs/EVALS.md eval contract validation failed: {detail}")

    official_setup_text = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    if "documentation only" not in official_setup_text or "Do not run setup" not in official_setup_text:
        errors.append("README setup commands must remain clearly documentation-only")

    for path in active_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for label, pattern in STALE_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{rel}:{line}: stale active claim {label!r}")

    return errors


def run_self_test() -> int:
    errors = validate()
    if errors:
        print("bundle validation must pass before self-test:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    runtime_file = ROOT / ".omx" / "tmp-bundle-validation-stale.md"
    source_file = ROOT / "bundle-validation-active-source-stale.md"
    try:
        runtime_file.parent.mkdir(parents=True, exist_ok=True)
        runtime_file.write_text("build-web-apps react-best-practices\n", encoding="utf-8")
        runtime_errors = validate()
        if runtime_errors:
            print("ignored runtime stale fixture should not fail validation:", file=sys.stderr)
            print("\n".join(runtime_errors), file=sys.stderr)
            return 1

        source_file.write_text("build-web-apps\n", encoding="utf-8")
        source_errors = validate()
        if not any("bundle-validation-active-source-stale.md" in error for error in source_errors):
            print("active source stale fixture did not fail validation", file=sys.stderr)
            if source_errors:
                print("\n".join(source_errors), file=sys.stderr)
            return 1
    finally:
        runtime_file.unlink(missing_ok=True)
        source_file.unlink(missing_ok=True)

    print("build-lynx-apps bundle validation self-test ok")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return run_self_test()
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("build-lynx-apps bundle validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
