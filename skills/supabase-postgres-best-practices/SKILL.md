---
name: supabase-postgres-best-practices
description: Optional service-domain guidance for Postgres and Supabase data layers used by Lynx.js apps. Use when writing, reviewing, or optimizing queries, schema designs, indexes, RLS policies, connection behavior, or database configuration; do not use as UI implementation guidance.
license: MIT
metadata:
  author: supabase
  version: "1.1.0"
  organization: Supabase
  date: January 2026
  abstract: Comprehensive Postgres performance optimization guide for developers using Supabase and Postgres. Contains performance rules across 8 categories, prioritized by impact from critical query performance and connection management to advanced features.
---

# Supabase Postgres Best Practices

Use this skill for database and backend/service-layer decisions in Lynx apps. Keep UI composition in `lynx-app-builder` and `lynx-ui-guidance`.


## Lynx host/client safety

When Supabase or Postgres powers a Lynx app surface, keep database and auth boundaries explicit:

- Never put Supabase service-role keys, database passwords, JWT signing secrets, or privileged admin credentials in a Lynx bundle.
- If a Lynx client uses a Supabase anon key, require Row-Level Security policies and verify that the anon role can access only intended rows/actions.
- Keep schema changes, migrations, privileged writes, cron jobs, and server-side aggregation on trusted backend or database surfaces.
- Treat network/offline behavior as host-dependent; record the target host service/network assumptions before promising sync, caching, or background behavior.
- Place generated clients and environment loading according to the consuming app's conventions, and avoid leaking private environment variables into bundled code.
- Route UI composition back to `lynx-app-builder`, `reactlynx-best-practices`, and `lynx-ui-guidance`; this skill owns data, policy, query, and performance guidance only.
- Cite current Supabase/Postgres docs for security, auth, and RLS claims.

## When to Apply

Reference these guidelines when:
- Writing SQL queries or designing schemas
- Implementing indexes or query optimization
- Reviewing database performance issues
- Configuring connection pooling or scaling
- Optimizing for Postgres-specific features
- Working with Row-Level Security (RLS)

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Query Performance | CRITICAL | `query-` |
| 2 | Connection Management | CRITICAL | `conn-` |
| 3 | Security & RLS | CRITICAL | `security-` |
| 4 | Schema Design | HIGH | `schema-` |
| 5 | Concurrency & Locking | MEDIUM-HIGH | `lock-` |
| 6 | Data Access Patterns | MEDIUM | `data-` |
| 7 | Monitoring & Diagnostics | LOW-MEDIUM | `monitor-` |
| 8 | Advanced Features | LOW | `advanced-` |

## How to Use

Read individual rule files for detailed explanations and SQL examples:

```
references/query-missing-indexes.md
references/schema-partial-indexes.md
references/_sections.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect SQL example with explanation
- Correct SQL example with explanation
- Optional EXPLAIN output or metrics
- Additional context and references
- Supabase-specific notes when applicable

## References

- https://www.postgresql.org/docs/current/
- https://supabase.com/docs
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
- https://supabase.com/docs/guides/auth/row-level-security
