---
name: lynx-trace-record
description: First-class Lynx trace capture guidance for startup, scroll, interaction, render, JS profiling, and native-module latency investigations. Use when a task needs to capture a Lynx performance trace artifact before analysis.
---

# Lynx Trace Record

Use this skill when the next best evidence is a new Lynx performance trace. It plans and records trace capture parameters so later analysis is reproducible.

This is a routing/checklist wrapper over official Lynx DevTool/trace docs and the official `lynx-trace-record` community skill. It does not fabricate traces and does not install tooling.

## Official sources to read

- `lynx-docs://llms.txt` — required entrypoint when Lynx Docs MCP is available.
- `lynx-docs://ai/skills/trace-record.md` — official skill overview.
- `lynx-docs://guide/devtool/trace.md` — trace capture workflow.
- `lynx-docs://guide/devtool.md` — DevTool setup and connected-device prerequisites.
- `lynx-docs://react/performance/profiling.md` — ReactLynx profiling when component render behavior is in scope.
- `lynx-docs://guide/performance/metrics/performance-api.md` — runtime metric context.

## Capture planning checklist

Before recording or requesting a trace, identify:

1. Performance question: startup/white screen, FCP/FMP/TTI, scroll jank, frame drops, tap latency, animation lag, render churn, native module latency, network wait, or bundle load.
2. Target host/platform and `engineVersion` when present.
3. Device/simulator/app/page/card URL and whether Lynx DevTool MCP is connected.
4. Exact user flow and duration to record, including warm/cold start assumptions.
5. JS profiling / system trace / ReactLynx profiling options needed for the question.
6. Output artifact path and naming convention, ideally under `.omx/artifacts/lynx-traces/<slug>/` for project-bound work.
7. Any privacy/credential exclusions before capturing logs or traces.

## Evidence rules

- Do not claim trace evidence without a trace artifact path and capture context.
- Do not interpret metrics during capture unless the trace has actually been opened/read. Hand analysis to `lynx-trace-analysis`.
- If DevTool/device capture is unavailable, report the blocker and provide the narrowest reproducible capture command/instructions.

## Output ledger

Include:

- official resources read,
- DevTool/device/app availability,
- platform and `engineVersion` if known,
- flow and duration recorded/requested,
- options enabled,
- trace artifact path or unavailable reason,
- recommended next analysis skill: `lynx-trace-analysis`.
