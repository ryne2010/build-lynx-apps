# Build Lynx Apps Cookbook

Use these workflows as implementation guidance. Commands that install MCP servers, add community skills, or mutate user configuration are intentionally not run by this plugin unless the user starts a separate setup/configuration task.

## 1. Create or inspect a Lynx project/bundle

1. Use `lynx-official-tools` and read `lynx-docs://llms.txt` first when Lynx Docs MCP is available.
2. Read `lynx-docs://react/start/quick-start.md` for project creation and development flow.
3. Read `lynx-docs://rspeedy/output.md` when claiming build artifacts or bundle names.
4. Record package manager, Rspeedy config, `engineVersion` when present, output bundle targets, and available scripts.
5. Verify with the consuming project’s build/type/lint/test scripts when present.
6. Do not imply this creates a complete native/mobile/desktop/web host app; it creates or works with Lynx project/bundle surfaces.

## 2. Integrate a Lynx bundle into an existing host

1. Read `lynx-docs://react/start/integrate-with-existing-apps.md` or the platform-specific integration resource.
2. Identify target host: iOS, Android, HarmonyOS, Web, Windows, macOS, Lynx Explorer, or an existing product container.
3. Separate host initialization/resource loading from Lynx bundle UI work.
4. Record host services needed for image, log, HTTP, native modules, storage, font loading, or resource fetchers.
5. Treat native host code as outside the Lynx UI surface unless the user explicitly scopes host integration work.
6. For desktop, SVG, or platform-specific events, check current official resources such as `lynx-docs://versions.md` and release resources before making support claims.

## 3. Build a polished Lynx screen

1. Use `lynx-app-builder` for concept-first workflow.
2. Generate or request enough visual concept detail for all required states.
3. Build an implementation inventory: elements, CSS Modules, tokens, data, events, native modules, routing, test plan, bundle target, host services, and verification tier.
4. Use `reactlynx-best-practices` for events, native API calls, main-thread scripts, cross-thread calls, shared modules, static JSX, TypeScript, routing, and tests.
5. Use `lynx-ui-guidance` for package components and proof-gated component selection.
6. Verify with DevTool screenshot evidence when available; otherwise report static/build evidence and state that visual parity is not proven.

## 4. Run measured visual iteration with OMX

1. Use `$visual-ralph` when a generated reference, static reference, or URL-derived baseline should drive implementation.
2. Save the approved reference in the workspace, for example `.omx/artifacts/visual-ralph/<slug>/reference.png`.
3. Record target host/device, route/state, viewport/screen size, seed/login assumptions, and visible interaction parity notes.
4. Capture a current Lynx screenshot through Lynx DevTool MCP when a device/app is connected.
5. Run `$visual-verdict` before the next visual edit when both reference and screenshot exist; target score is 90 or higher.
6. Use pixel diff or overlay only as secondary debug evidence. Do not claim visual sign-off without screenshot/verdict evidence.

## 5. Compose UI with local-workspace `@dumbooks/lynx-ui`

1. Read local registry/docs before recommending a component.
2. Frame the package as local-workspace/internal-beta for now. It is poised for future open source, but do not imply public npm availability, public release approval, or external stable support.
3. Prefer root imports from `@dumbooks/lynx-ui` when `exportChannel` and proof gates support package usage and the target workspace can resolve the local package.
4. Check proof fields, runtime target/verified hosts, official substrate fields, dependency gate, source provenance, and AI usage hints.
5. Check visual style/base-color and platform-item metadata through `pnpm lynx-ui theme --json`, `pnpm lynx-ui list --items --json`, registry `items`, docs, or MCP resources when available.
6. Keep `@dumbooks/lynx-ui/experimental` as an opt-in compatibility alias, not the default.
7. Do not edit `/Users/ryneschroder/Developer/git/dumbooks/packages/lynx-ui` from this plugin without a separate package-edit task.

## 6. Debug with Lynx DevTool MCP

1. Use `lynx-official-tools` to record Docs MCP and DevTool MCP availability.
2. If a device/app is connected, use only the DevTool capabilities supported by the installed MCP surface and record which category was used: CDP commands, element/style inspection, App commands, Open URLs, console/stack traces, loaded sources, interactions, screenshots, or troubleshooting.
3. Use App commands and Open URLs only for preview/navigation of the connected Lynx app; do not treat them as setup/config mutation.
4. Use connector/transport troubleshooting when the MCP exists but no device/app/page is visible, and preserve the exact diagnostic/error output.
5. If no device/app is connected, fall back to static/build/type/lint/test evidence and state that runtime/visual evidence is unavailable.
6. For trace/performance issues, use official trace resources and do not fabricate metrics.
7. For minified or generated stack traces, route through the debug-info remapping guidance when available.

## 7. ReactLynx advanced implementation paths

1. For main-thread visual responsiveness, read `lynx-docs://react/main-thread-script.md` and record `main-thread:` handlers, `useMainThreadRef`, `runOnMainThread`, `runOnBackground`, and JSON-serializable captures.
2. For shared modules, state that `with { runtime: 'shared' }` shares code, not state.
3. For routing, read `lynx-docs://react/routing/tanstack-router.md` or `lynx-docs://react/routing/react-router.md`; record Memory Routing/browser history limitations and any required polyfills.
4. For tests, read `lynx-docs://react/reactlynx-testing-library.md`; use the project’s Rstest/Vitest setup and account for list/main-thread behavior.
5. For code splitting or external bundles, read `lynx-docs://react/code-splitting.md` or `lynx-docs://rspeedy/external-bundle.md`; record bundle CSS boundaries, producer/consumer config, section paths, and `engineVersion` caveats.
6. For data fetching, read `lynx-docs://react/data-fetching.md` and `lynx-docs://guide/interaction/networking.md`; record host-provided Fetch/network/storage assumptions.
7. For state management, read official examples such as `lynx-docs://react/state-management/jotai.md`, `lynx-docs://react/state-management/valtio.md`, or `lynx-docs://react/state-management/zustand.md`; keep store updates on the correct background/main-thread boundary.
8. For hook utilities, treat `reactlynx-use` as an optional ecosystem library introduced in the Lynx 3.6 release notes; check the target app dependency and official/current docs before recommending an import.
9. For global/event hooks or runtime event listeners, retrieve the current official API docs/resource before prescribing the exact hook or event name.

## 8. Migrate web or shadcn-style patterns safely

1. Preserve business logic, navigation, data selectors, and user-visible workflow.
2. Replace DOM elements/events with Lynx elements/events.
3. Replace Radix/browser/Tailwind runtime assumptions with Lynx-native behavior, CSS Modules, tokens, and package APIs.
4. Query `@dumbooks/lynx-ui` registry/docs for equivalent local-workspace components; if unavailable, propose a Lynx-native composition and mark the package gap as follow-up.
5. Verify with static/build checks and runtime/visual proof when available.

## 9. Use first-class official Lynx skill companions

1. Start with `lynx-official-tools` and `lynx-docs://llms.txt` for framework truth.
2. Route ReactLynx code through `reactlynx-best-practices`.
3. Route TypeScript setup, declarations, native module typings, custom elements, and main-thread event/ref types through `lynx-typescript`.
4. Route connected runtime inspection, console/source checks, interaction checks, and screenshots through `lynx-devtool`.
5. Route trace capture through `lynx-trace-record`, then analyze existing trace artifacts with `lynx-trace-analysis`.
6. Route minified/generated/main-thread runtime stack mapping through `debug-info-remapping`.
7. These bundled companions are local routing/checklists over official Lynx docs and MCPs. They do not install community skills or replace current official documentation.

## 10. Route broader Lynx ecosystem workflows

1. For Habitat or multi-repo dependency-sync questions, route to the upstream `habitat-usage` skill when installed or the `lynx-community/skills` release tree as a current reference.
2. Treat Habitat setup/sync as separate from Lynx UI implementation. Collect `.habitat`, `DEPS`, wrapper/version, command output, OS/architecture, and auth/network context; do not overwrite dependency directories without explicit user scope.
3. For `reactlynx-use`, state-management libraries, and global event helpers, check the consuming app dependency graph before recommending imports.
4. Keep ecosystem packages optional unless the project already depends on them or the user explicitly asks to add them; no new dependencies are introduced by this plugin itself.
5. Record whether advice came from official Lynx MCP resources, release notes, upstream community skills, or project-local evidence.

## 11. Add Stripe or Supabase service guidance

1. Keep payment/data services separate from Lynx UI composition.
2. Never place Stripe secrets, Supabase service-role keys, database passwords, webhook secrets, or privileged backend logic in a Lynx bundle.
3. Use backend/webhook/RLS boundaries for privileged operations.
4. Record host/client surface and cite current official provider docs before writing implementation guidance.
5. Compose only the surrounding Lynx UI with `lynx-app-builder` and `lynx-ui-guidance`.
