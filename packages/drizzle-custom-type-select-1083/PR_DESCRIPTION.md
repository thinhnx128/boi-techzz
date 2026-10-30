## feat(custom-type): Add `selectFromDb` option for Custom Types (#1083)

### Summary
Adds support for an optional `selectFromDb(column, decoder)` hook on `customType` definitions as proposed in #1083:
- Allows custom types (such as PostGIS `geometry(Point, 4326)`) to wrap selected column identifiers in custom SQL functions (e.g., `st_astext(column)`) while preserving the `fromDriver` decoder automatically across standard and relational queries.
- Includes unit tests verifying PostGIS `POINT(lng lat)` round-trip serialization and `selectFromDb` SQL generation.

### Reference Package
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/drizzle-custom-type-select-1083

/claim #1083
Fixes #1083