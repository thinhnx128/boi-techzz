## feat: Use PGlite in-memory instance so Postgres isn't required during `db:generate` (#2)

### Summary
Solves #2 so running `bun run db:generate` does not require a background PostgreSQL server:
- Automatically falls back to an ephemeral in-memory `@electric-sql/pglite` instance when generating types offline.
- Applies schema DDL migrations in memory and exposes the standard `information_schema` query interface for type generation.
- Includes unit tests verifying schema migration and introspection without a Postgres daemon.

### Reference Package
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/pgstrap-pglite-typegen-2

/claim #2
Fixes #2