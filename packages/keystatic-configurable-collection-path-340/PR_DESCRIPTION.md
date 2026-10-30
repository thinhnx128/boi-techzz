## feat(core): Support dynamic function & field interpolation in collection `path` (#340)

### Summary
Implements configurable dynamic collection paths as proposed in #340:
- Allows `collection({ path })` to accept either a static wildcard string (`'src/content/blog/*'`) or a typed callback function (`({ locale, publishDate }) => \`src/content/blog/\${locale}/\${publishDate}.*\``).
- Validates wildcard presence (`*`) and normalizes path boundaries.
- Includes unit tests covering locale subdirectories, publish date prefixes, and wildcard validation.

### Reference Package
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/keystatic-configurable-collection-path-340

/claim #340
Fixes #340