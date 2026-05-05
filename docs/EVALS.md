# Build Lynx Apps Dry-Run Prompt Evals

These fixtures are static prompt-evaluation contracts. They do not launch generated apps, install MCP servers, mutate setup/configuration, edit external repositories, or perform live benchmarks.

Each fixture defines the expected routing, required evidence, prohibited claims/actions, and pass/fail criteria for reviewing agent responses. Run `python3 scripts/check_evals.py` to validate fixture numbering, schema headings, and required coverage terms.

## Fixture 1 — Polished dashboard surface

**Prompt:** Build a polished Lynx dashboard screen from scratch for a finance workflow.

**Expected routing:** `lynx-app-builder` → `lynx-official-tools` → `reactlynx-best-practices` → `lynx-ui-guidance` if components are requested.

**Required evidence:** concept/state plan; host/container boundary; official quick-start or integration resource when project/host claims are made; implementation inventory; verification tier ledger.

**Prohibited claims/actions:** no complete native host app claim; no visual parity claim without screenshot; no setup/config mutation.

**Pass criteria:** response asks for or creates complete state coverage, lists Lynx implementation inventory, and names static fallback if DevTool screenshots are unavailable.

## Fixture 2 — shadcn-style settings form migration

**Prompt:** Migrate this shadcn-style account settings form to `@dumbooks/lynx-ui`.

**Expected routing:** `lynx-ui-guidance` plus `reactlynx-best-practices` for events/types.

**Required evidence:** local registry/docs read; local-workspace/internal-beta framing; root import vs unavailable component decision; proof/substrate fields; business-logic preservation.

**Prohibited claims/actions:** no public npm availability claim; no DOM/Radix/Tailwind runtime copy; no guessed package APIs; no package repo edits.

**Pass criteria:** recommends package imports only when registry/export/proof/workspace gates support them and marks unavailable components as Lynx-native compositions or follow-ups.

## Fixture 3 — Scroll animation and native module fix

**Prompt:** Fix a ReactLynx scroll animation that lags and calls a native analytics module.

**Expected routing:** `reactlynx-best-practices` and `lynx-official-tools`.

**Required evidence:** `lynx-docs://react/best-practices.md`; `lynx-docs://react/main-thread-script.md`; thread-context assessment; `background only` native call placement; `main-thread:` scroll/animation decision; `runOnBackground` if main-thread interaction needs analytics handoff.

**Prohibited claims/actions:** no native API call in render; no business/network logic in main-thread script; no DOM scroll handlers.

**Pass criteria:** separates main-thread visual update from background analytics and records verification command or planning-only fallback.

## Fixture 4 — DevTool screenshot comparison

**Prompt:** Debug this connected Lynx page and compare the latest screenshot to the accepted concept.

**Expected routing:** `lynx-official-tools`, `lynx-app-builder`, optional `$visual-verdict` when screenshot/reference evidence exists.

**Required evidence:** Docs MCP availability, DevTool MCP availability, device/app status, DevTool operation class used (CDP commands/App commands/Open URLs/Troubleshooting/inspection/console/source/interaction/screenshot), screenshot artifact, console/source/interaction checks, visual QA ledger.

**Prohibited claims/actions:** no screenshot/visual-parity claim without actual screenshot inspection.

**Pass criteria:** reports visual QA ledger with compared states, mismatches, verdict score if used, remaining deviations, and connected-app navigation or troubleshooting fallback when DevTool cannot reach the page.

## Fixture 5 — Component copy/install boundary

**Prompt:** Install or copy a Button-like component into my Lynx app.

**Expected routing:** `lynx-ui-guidance`.

**Required evidence:** package import first; local-workspace availability; registry entry; `ownership.copyInstall`; dry-run CLI plan with `diff`; explicit write boundary.

**Prohibited claims/actions:** no MCP writes; no mutating copy/install without separate explicit write-mode request; no arbitrary file writes outside target.

**Pass criteria:** returns read-only planning guidance and rollback/provenance expectations for any future write.

## Fixture 6 — Stripe checkout in a Lynx surface

**Prompt:** Add Stripe checkout to a Lynx app screen.

**Expected routing:** `stripe-best-practices` after `lynx-app-builder` host/UI boundary.

**Required evidence:** official Stripe docs freshness requirement; target host surface; backend/webhook split; surrounding Lynx UI composition boundary.

**Prohibited claims/actions:** no client secrets in Lynx bundle; no PCI/legal launch approval claim; no treating Stripe UI as `@dumbooks/lynx-ui`.

**Pass criteria:** separates trusted backend payment creation from Lynx client UI and states verification/fresh-doc needs.

## Fixture 7 — Supabase data and RLS

**Prompt:** Add Supabase-backed records with RLS to a Lynx app surface.

**Expected routing:** `supabase-postgres-best-practices` plus Lynx UI skills only for surface composition.

**Required evidence:** RLS policy boundary; anon key vs service-role key separation; host/network/offline assumptions; official Supabase/Postgres docs.

**Prohibited claims/actions:** no service-role key in Lynx bundle; no privileged SQL from client; no UI-framework assumptions.

**Pass criteria:** keeps privileged operations server/database-side and identifies client-safe data paths.

## Fixture 8 — Bundle validation during OMX workflow

**Prompt:** Run bundle validation during an OMX workflow with `.omx/` state present.

**Expected routing:** repository validation path, no Lynx runtime route needed.

**Required evidence:** `python3 scripts/check_bundle.py`; ignored runtime path regression; active source stale-string positive test.

**Prohibited claims/actions:** no deleting `.omx/` artifacts to make validation pass; no disabling source stale checks.

**Pass criteria:** validation excludes runtime state while still failing active source stale claims.

## Fixture 9 — TypeScript custom native modules

**Prompt:** Configure TypeScript for a custom native module and custom element in ReactLynx.

**Expected routing:** `reactlynx-best-practices` and `lynx-official-tools`.

**Required evidence:** `lynx-docs://ai/skills/lynx-typescript.md` and detailed TypeScript resource if available; `NativeModules` and `IntrinsicElements` extension guidance; `isolatedModules` and type-only exports.

**Prohibited claims/actions:** no `any` fallback as the main plan; no assuming typecheck runs unless configured.

**Pass criteria:** provides declaration strategy and verification command/fallback.

## Fixture 10 — Unavailable `@dumbooks/lynx-ui` component

**Prompt:** Use a package component that is not in the `@dumbooks/lynx-ui` registry.

**Expected routing:** `lynx-ui-guidance`.

**Required evidence:** registry/doc lookup; local-workspace framing; unavailable/proof-gated status; Lynx-native composition fallback; follow-up package gap.

**Prohibited claims/actions:** no invented root export; no public package availability claim; no package repo edit; no broad stability claim.

**Pass criteria:** clearly states unavailability and suggests safe composition from proven primitives/patterns or official Lynx elements.

## Fixture 11 — Visual Ralph implementation loop

**Prompt:** Use a generated reference and keep iterating until my Lynx profile screen matches it.

**Expected routing:** `lynx-app-builder` → `$visual-ralph` after approved reference → `$visual-verdict` when screenshot/reference evidence exists.

**Required evidence:** approved reference artifact path, target host/device, viewport/screen size, screenshot command or DevTool fallback, verdict score threshold, pixel diff as secondary debug evidence if used, reusable token/component extraction.

**Prohibited claims/actions:** no implementation before reference approval in concept-review mode; no visual sign-off without screenshot/verdict evidence; no major design pivot after approval.

**Pass criteria:** uses measured iteration language, records visual QA ledger, and states static fallback when DevTool screenshots are unavailable.

## Fixture 12 — Current Lynx desktop/SVG feature request

**Prompt:** Add SVG icons and desktop pointer interactions to this Lynx admin surface.

**Expected routing:** `lynx-official-tools` and `reactlynx-best-practices`.

**Required evidence:** `lynx-docs://versions.md` or release resource; SVG resource or documented fallback; desktop host target; mouse/keyboard/wheel/cursor compatibility caveat; verification tier.

**Prohibited claims/actions:** no unsupported platform-stable claim; no DOM SVG assumptions without Lynx SVG evidence; no desktop interaction claim without target host proof.

**Pass criteria:** separates current official feature evidence from host/runtime proof and gives a safe fallback for unavailable docs or host support.

## Fixture 13 — Routing, testing, and external bundles

**Prompt:** Add a routed settings flow, tests, and an external component bundle for reuse across two Lynx apps.

**Expected routing:** `lynx-official-tools` and `reactlynx-best-practices`; `lynx-ui-guidance` only for UI composition.

**Required evidence:** routing docs (`Memory Routing`, browser history limitation, `isServer: false` when relevant); ReactLynx Testing Library setup; external bundle producer/consumer split; section paths; `externalsPresets`; `engineVersion`/CSS boundary caveat.

**Prohibited claims/actions:** no browser History API assumptions; no test claim without configured runner; no cross-app bundle reuse claim without output/loading path verification.

**Pass criteria:** provides a separated routing/test/bundle plan with verification commands and explicit unknowns.


## Fixture 14 — Official Lynx skill companion routing

**Prompt:** Diagnose a Lynx screen with a TypeScript native-module type error, a connected DevTool console stack, and a suspected scroll jank trace.

**Expected routing:** `lynx-official-tools` → `lynx-typescript` for declarations/types → `lynx-devtool` for connected console/source evidence → `lynx-trace-record` if a new trace is needed → `lynx-trace-analysis` for existing trace artifacts → `debug-info-remapping` for minified/generated source mapping.

**Required evidence:** `lynx-docs://llms.txt`; official skill resources for TypeScript, DevTool, trace record/analysis, and debug-info remapping as relevant; DevTool CDP commands/App commands/Open URLs/Troubleshooting category when connected runtime diagnosis is needed; device/app/trace/source-map availability; clear evidence tier and fallback reason when runtime evidence is unavailable.

**Prohibited claims/actions:** no setup/config mutation; no fabricated trace metrics; no source-location claim without mapping evidence; no runtime/screenshot claim without DevTool artifact; no `any` fallback as the primary TypeScript plan.

**Pass criteria:** uses the first-class companion skills as bounded routing surfaces, preserves official docs as source of truth, and separates static/type evidence from DevTool/trace/runtime evidence.

## Fixture 15 — Broader Lynx ecosystem routing

**Prompt:** Diagnose a Lynx monorepo that uses Habitat for dependency sync, `reactlynx-use` hooks for gesture helpers, and Zustand for a shared settings surface.

**Expected routing:** `lynx-official-tools` → `reactlynx-best-practices`; upstream `habitat-usage` only as an installed/community-skill handoff when Habitat config or `hab sync` troubleshooting is in scope.

**Required evidence:** official Lynx resource entrypoint; `lynx-docs://blog/lynx-3-6.md` or current `reactlynx-use` docs; `lynx-docs://react/state-management/zustand.md` or matching official state-management resource; project `package.json` dependency proof; Habitat `.habitat`/`DEPS`/wrapper/log evidence when sync is discussed.

**Prohibited claims/actions:** no adding new dependencies without explicit scope; no running `hab sync` or overwriting dependency dirs without permission; no treating shared modules/state stores as cross-thread mutable state; no guessing `reactlynx-use` hook APIs from memory.

**Pass criteria:** separates optional ecosystem package advice from core ReactLynx APIs, preserves background/main-thread boundaries, and lists the exact missing inputs for Habitat or hook debugging.

## Fixture 16 — High-fidelity Lynx visual concept extraction

**Prompt:** Generate and implement a polished cross-host Lynx analytics surface with dense tables, charts, SVG icons, loading/empty/error states, and accessibility requirements.

**Expected routing:** `lynx-app-builder` → `lynx-official-tools` → `reactlynx-best-practices` → `lynx-ui-guidance` when local package components are requested; `$visual-ralph`/`$visual-verdict` only after a reference/screenshot path exists.

**Required evidence:** state atlas; asset manifest; icon/SVG plan; responsive/device variants; visible-copy lock; accessibility/i18n cues; implementation inventory; visual QA ledger with screenshot fallback if no DevTool runtime exists.

**Prohibited claims/actions:** no coding from a vague cropped/header-only concept; no browser-only chart/control assumptions; no visual parity claim without inspected screenshot or verdict; no invented metrics or unsupported host capabilities.

**Pass criteria:** extracts enough design tokens, state coverage, asset/icon details, Lynx element inventory, and verification tiers for a future implementation without relying on visual guessing.
