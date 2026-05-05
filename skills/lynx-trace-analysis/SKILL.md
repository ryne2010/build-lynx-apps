---
name: lynx-trace-analysis
description: First-class Lynx trace analysis guidance for startup, white screen, FCP/FMP/TTI, scroll jank, frame drops, interaction latency, render pipeline, ReactLynx render churn, and native-module bottlenecks. Use when reading an existing Lynx trace or performance artifact.
license: MIT
---

# Lynx Trace Analysis

Use this skill when a Lynx performance trace, profiling output, runtime metric log, or DevTool trace artifact needs interpretation.

This skill is read-first: inspect trace evidence, rank likely bottlenecks, and separate direct evidence from inference before proposing changes.

## Official sources to read

- `lynx-docs://llms.txt` — required entrypoint when Lynx Docs MCP is available.
- `lynx-docs://ai/skills/trace-analysis.md` — official skill overview.
- `lynx-docs://guide/devtool/trace.md` — trace semantics.
- `lynx-docs://react/performance/profiling.md` — ReactLynx profiling interpretation.
- `lynx-docs://guide/performance/metrics/performance-api.md` — runtime metric definitions.
- `lynx-docs://react/main-thread-script.md` — latency-sensitive interaction interpretation.
- `lynx-docs://react/best-practices.md` — remediation guardrails.

## Analysis workflow

1. Confirm trace artifact path, capture device/platform, app/page, flow, duration, and build mode.
2. Classify the issue:
   - startup/white screen/FCP/FMP/TTI,
   - smoothness/scroll jank/frame drops,
   - interaction/tap/gesture latency,
   - ReactLynx render/diff churn,
   - main-thread script misuse,
   - native module/service latency,
   - network/resource/bundle loading.
3. Read the trace/profiling evidence before proposing code changes.
4. Rank bottlenecks by support level and impact.
5. Map each recommendation to the correct skill:
   - `reactlynx-best-practices` for dual-thread/render/event fixes,
   - `lynx-typescript` for type/declaration correctness,
   - `lynx-devtool` for more runtime inspection,
   - `debug-info-remapping` for minified source mapping.
6. State what remains unknown if the trace lacks necessary channels.

## Evidence rules

- Do not fabricate metric values, frame counts, or bottleneck locations.
- Do not attribute a regression to code without trace/source corroboration.
- Do not move business/network/native-module work to the main thread to fix latency.
- Prefer specific, measured next probes over broad performance advice when evidence is incomplete.

## Output contract

Include:

- trace artifact(s) analyzed,
- capture context,
- ranked bottlenecks with evidence vs inference,
- recommended next probes or changes,
- verification plan for a follow-up trace.
