---
name: reactlynx-best-practices
description: First-class ReactLynx guardrails for Lynx dual-thread architecture, native API calls, event handlers, main-thread scripts, cross-thread calls, shared modules, static JSX, TypeScript setup, testing, routing, data fetching, state management, reactlynx-use, code splitting, and safe React patterns. Use when writing, reviewing, or debugging ReactLynx components, events, native modules, animations, gestures, refs, routing, tests, state stores, hooks, or TypeScript declarations.
---

# ReactLynx Best Practices

Use this skill whenever a task writes, reviews, debugs, or explains ReactLynx code. This local skill is a routing/checklist guardrail, not a replacement for official Lynx documentation. For framework claims, read official resources through `lynx-official-tools` and cite the resources used.

## Official sources to read

- `lynx-docs://llms.txt` — required entrypoint when Lynx Docs MCP is available.
- `lynx-docs://ai/skills/reactlynx-best-practices.md` — official skill overview for these rules.
- `lynx-docs://react/best-practices.md` — detailed dual-thread best-practice guide.
- `lynx-docs://react/thinking-in-reactlynx.md` — background-only inference rules and dual-thread mental model.
- `lynx-docs://ai/skills/lynx-typescript.md` — official TypeScript skill overview.
- `lynx-docs://rspeedy/typescript.md` — detailed Rspeedy TypeScript configuration and type extension guide when available.
- `lynx-docs://react/main-thread-script.md` and `lynx-docs://guide/scripting-runtime/main-thread-runtime.md` — main-thread behavior, `runOnMainThread`, `runOnBackground`, and shared modules when main-thread scripts are involved.
- `lynx-docs://react/reactlynx-testing-library.md` — component/event/list/main-thread test setup when tests are requested or modified.
- `lynx-docs://react/routing/tanstack-router.md` and `lynx-docs://react/routing/react-router.md` — routing choices and browser-history limitations.
- `lynx-docs://react/code-splitting.md` and `lynx-docs://rspeedy/external-bundle.md` — lazy components, bundle CSS scope, and cross-application bundle reuse.
- `lynx-docs://react/data-fetching.md` and `lynx-docs://guide/interaction/networking.md` — Fetch/API behavior and host service assumptions.
- `lynx-docs://react/state-management/jotai.md`, `lynx-docs://react/state-management/valtio.md`, and `lynx-docs://react/state-management/zustand.md` — official examples when state stores are introduced or reviewed.
- `lynx-docs://blog/lynx-3-6.md` — `reactlynx-use` release context; check current package docs and project dependencies before recommending imports.

If MCP is unavailable, use official Lynx docs as fallback and state that fallback.

## Required checklist before coding or reviewing

1. Identify whether the code runs in render/main-thread evaluation, background thread contexts, event handlers, effects, ref callbacks, main-thread scripts, or shared modules.
2. Locate every native API call (`lynx.getJSModule`, `NativeModules`, custom native modules, host services).
3. Locate every event handler (`bindtap`, `catchtap`, capture/global variants, scroll/touch/mouse/keyboard/wheel events) and decide whether propagation should bubble, stop, capture, or run on the main thread.
4. Locate every animation/gesture/scroll path that needs synchronous main-thread behavior.
5. Locate every cross-thread call and verify `runOnMainThread`, `runOnBackground`, serializable arguments, and no direct call across runtime boundaries.
6. Check shared module imports (`with { runtime: 'shared' }`) and confirm they are code-sharing only, not state-sharing.
7. Check static JSX candidates that can be hoisted, and whether React Compiler is enabled.
8. Check TypeScript env declarations, custom native module declarations, `InitData`, `GlobalProps`, custom `IntrinsicElements`, main-thread event types, and type-only exports/imports.
9. Confirm no browser globals, DOM events, React DOM APIs, `window`, `document`, browser History API, or DOM focus assumptions are used unless official target-host docs explicitly support them.
10. If state libraries, global event hooks, or `reactlynx-use` hooks are involved, confirm package availability, official/current docs, thread context, and fallback to core ReactLynx APIs.
11. Check available verification: ReactLynx Testing Library, lint/typecheck/build, DevTool runtime, trace/performance, or planning-only fallback.

## Native API calls and `background only`

Native APIs must not run at component top level, inside render logic, or inside values evaluated by JSX rendering. They are safe only in contexts that execute on the background thread or in functions explicitly marked for background execution.

Allowed contexts include:

- `useEffect` or other documented background-thread hook contexts,
- event handlers such as `bindtap`,
- ref callbacks or imperative handles when documented safe,
- functions whose first statement is `'background only'` or `"background only"`,
- modules that intentionally use `import 'background-only'` and are not imported by main-thread code.

Rules:

- Put native module calls behind a named function when possible.
- Use the `'background only'` directive for helper functions that perform native calls outside naturally safe contexts, especially callbacks passed through component props or custom hooks.
- Never call native APIs inside JSX expressions or component top-level render work.
- Keep host service availability explicit; do not invent native modules.

## Event handlers

Use ReactLynx event names and propagation semantics:

- `bindtap` bubbles and is the default tap choice.
- `catchtap` stops propagation and should be used only when parent handlers must not fire.
- Capture/global variants require a documented reason and the official event resource when behavior matters.
- Prefer named function references over inline arrow functions for recurring handlers.
- Prefer `event.currentTarget.dataset` for simple per-element data instead of capturing large closure objects.
- Do not use DOM event names such as `onClick`, `onChange`, mouse/key compatibility handlers, or browser-only event assumptions unless official docs for the target host explicitly support them.

## Main-thread scripts

Use main-thread scripts for synchronous gesture, scroll, animation, or immediate visual feedback work that would visibly lag if routed through the background thread.

Rules:

- Add the `main-thread:` prefix to the event or ref attribute, such as `main-thread:bindtap`, `main-thread:global-bindscroll`, or `main-thread:ref`.
- Put `'main thread'` as the first statement in the handler function.
- Use `useMainThreadRef()` for main-thread-accessible refs/state.
- Captured variables must be JSON-serializable and treated as read-only from the main thread.
- `MainThreadRef.current` is accessible only in main-thread functions.
- Do not move business logic, network calls, native module calls, analytics, or backend/service logic into main-thread scripts just for convenience.
- Main-thread functions cannot freely call background-thread functions; use `runOnBackground` for async handoff.

## Cross-thread calls and shared modules

Use official cross-thread APIs when a visual main-thread path must notify background state or when background effects must trigger main-thread updates.

- Use `runOnMainThread(fn)(...args)` from background code to invoke a function marked `'main thread'`.
- Use `runOnBackground(fn)(...args)` from main-thread code to invoke background code.
- Arguments and captured values must be JSON-serializable.
- Do not use cross-thread calls as a substitute for ordinary state/rendering when no latency-sensitive path exists.
- Shared modules imported with `with { runtime: 'shared' }` solve code sharing, not state sharing. Variables inside shared modules are isolated per runtime.
- If a shared import is assigned to another variable, static analysis may lose the shared characteristic; prefer direct imported identifiers or a wrapper marked with the proper directive.

## Static JSX and render performance

- Hoist static JSX constants outside components when they do not depend on props/state/context.
- Avoid defining child components inside parent render functions.
- Keep expensive data transforms outside render or memoized when needed.
- Prefer simple, stable props for large lists and repeated UI.
- If React Compiler is enabled and documented for the project, record that it may cover some hoisting cases instead of forcing manual changes.
- For large lists, use Lynx `list` patterns and test lazy item behavior instead of rendering enormous static trees.

## TypeScript guardrails

For TypeScript/Rspeedy projects:

- Ensure `src/rspeedy-env.d.ts` or equivalent includes `/// <reference types="@lynx-js/rspeedy/client" />` when needed.
- Extend `@lynx-js/types` for `GlobalProps`, `NativeModules`, custom `IntrinsicElements`, and main-thread event/ref types instead of using `any`.
- Extend `@lynx-js/react` for `InitData` when using `useInitData()` with custom data.
- Enable or preserve `isolatedModules` for SWC/Rspeedy compilation; use `export type` / `import type` where appropriate.
- Do not assume type checking runs as part of every build; use the project’s available typecheck or documented type-check plugin.

## Routing and navigation guardrails

- Read official routing docs before adding React Router or TanStack Router.
- Prefer Memory Routing where official docs require it; do not assume browser History API support.
- For TanStack Router, record `isServer: false`, `@lynx-js/react/compat`, URLSearchParams polyfill, and generated route-tree implications when used.
- If host navigation owns the route, keep Lynx surface navigation as client state or explicit native-module handoff rather than inventing browser links.

## Data fetching and host services

- Decide whether data comes from init data, `lynx.__globalProps`, Fetch, storage, Native Modules, or a backend API.
- Treat Fetch/networking, fonts, images, storage, and custom native modules as host-provided capabilities; record host assumptions before promising behavior.
- Never place service secrets, privileged API keys, or backend-only logic in a Lynx bundle.
- Keep background-thread side effects out of render and main-thread scripts.

## State management and hook ecosystems

- Use project-local dependencies first. Do not add Jotai, Valtio, Zustand, `reactlynx-use`, or another state/hook package unless the user explicitly scopes dependency work.
- When a project already uses Jotai, Valtio, or Zustand, read the matching official Lynx state-management example and keep state updates in ordinary background ReactLynx render/event flow unless a documented main-thread path is required.
- Treat `reactlynx-use` as an optional ecosystem helper, not a core ReactLynx guarantee. Check the current package docs and project `package.json` before recommending hooks such as main-thread gesture helpers, event-listener helpers, or imperative-handle helpers.
- For global event hooks or runtime event listeners, retrieve the current official API/resource before naming the hook, event, payload shape, or thread context.
- Do not use state stores, shared modules, or hook utilities as a hidden bridge for non-serializable main/background values; cross-thread calls still require `runOnMainThread`, `runOnBackground`, and JSON-serializable arguments.

## Testing and verification

When tests are requested or touched:

- Prefer ReactLynx Testing Library for component/event/list/main-thread behavior when available.
- Use project conventions first: Rstest, Vitest, lint, typecheck, build, or app-specific validation.
- For `list`, account for lazy item loading/recycling test APIs.
- For main-thread script tests, follow official test guidance and avoid directly invoking background APIs from main-thread assertions.
- Do not claim DevTool, screenshot, trace, or visual evidence unless captured and inspected.

## Code splitting and external bundle guardrails

- For lazy components, read official code-splitting docs and record CSS bundle-scope caveats.
- For external bundles, separate producer and consumer configuration, request keys, section paths, `externalsPresets`, bundle paths, and timeout behavior.
- If bundle CSS is needed, check the official `engineVersion` requirement before making configuration claims.
- Verify output bundle names and host loading paths before claiming cross-app reuse.

## Output requirements

When answering a ReactLynx task, include:

1. Official resource(s) read or fallback source.
2. Thread/context assessment for native APIs and event handlers.
3. Main-thread script and cross-thread decision if gestures, scroll, animation, or visual latency are involved.
4. TypeScript declaration/config checks when types are touched.
5. Routing/data/state-management/hook/bundle/test decision when those areas are touched.
6. Verification command or explicit reason verification is planning-only.
