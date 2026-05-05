---
name: lynx-typescript
description: First-class TypeScript guardrails for Lynx and ReactLynx projects. Use when configuring, reviewing, or fixing TypeScript for Rspeedy, JSX, CSS Modules, native modules, InitData, GlobalProps, custom elements, main-thread events/refs, or package-import boundaries.
license: MIT
---

# Lynx TypeScript

Use this skill when a Lynx task touches TypeScript setup, types, declarations, native modules, custom elements, InitData, GlobalProps, CSS Modules, main-thread event/ref types, or package API boundaries.

This skill is a routing/checklist companion to the official Lynx TypeScript skill. It is not a fork of the docs. For framework claims, use `lynx-official-tools` and read current official resources first.

## Official sources to read

- `lynx-docs://llms.txt` — required entrypoint when Lynx Docs MCP is available.
- `lynx-docs://ai/skills/lynx-typescript.md` — official skill overview.
- `lynx-docs://rspeedy/typescript.md` — Rspeedy TypeScript setup and CSS Module declarations.
- `lynx-docs://react/thinking-in-reactlynx.md` — background/main-thread inference rules.
- `lynx-docs://react/main-thread-script.md` — main-thread event/ref typing.
- `lynx-docs://guide/use-native-modules.md` — native module type boundaries.
- `lynx-docs://guide/custom-native-component.md` — custom element type boundaries.

If MCP is unavailable, use the official Lynx docs URLs as fallback and state the fallback.

## TypeScript checklist

1. Read the consuming app's `package.json`, lockfile when relevant, `tsconfig.json`, `lynx.config.*`, and `src/rspeedy-env.d.ts` or equivalent before changing or recommending types.
2. Confirm `compilerOptions.jsx` and `compilerOptions.jsxImportSource` are compatible with ReactLynx conventions when JSX is touched.
3. Ensure CSS Module typing is available through `/// <reference types="@lynx-js/rspeedy/client" />` or the app's existing generated declaration strategy.
4. Preserve `isolatedModules` or equivalent SWC/Rspeedy compatibility. Use `import type` and `export type` for type-only boundaries.
5. Extend official Lynx types instead of hiding gaps with `any`:
   - `@lynx-js/types` for `GlobalProps`, `NativeModules`, custom `IntrinsicElements`, `MainThread` event/ref types, `NodesRef`, and related Lynx APIs.
   - `@lynx-js/react` for `InitData` and ReactLynx-specific hooks/types.
6. Type event handlers with the correct Lynx event model: `bindtap`, `catchtap`, capture/global variants, and `main-thread:` variants when used.
7. For main-thread scripts, verify the function has the `'main thread'` directive, captures JSON-serializable data only, and uses `useMainThreadRef()`/`MainThreadRef` where needed.
8. For native modules, keep calls in background-thread contexts and type host availability explicitly. Do not invent native modules or mark optional host services as guaranteed.
9. For custom elements, type attributes, commands, and events against the app's declared host contract and official custom-element docs.
10. For `@dumbooks/lynx-ui`, prefer package-exported types from `@dumbooks/lynx-ui` when registry/proof gates support the root import. Do not reach into private source paths unless the consuming workspace already owns that source-alias contract.
11. Use the project's configured typecheck command when present. Do not assume Rspeedy build runs full type checking unless the project proves it.

## Output requirements

When answering a Lynx TypeScript task, include:

- official resources read or fallback used,
- files/configs inspected,
- declaration strategy and exact extension point,
- thread/event/native-module typing decision,
- `@dumbooks/lynx-ui` package/source boundary if relevant,
- verification command run or planning-only reason.
