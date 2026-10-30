## feat(js-sdk): Add native QdrantClient vector database support for EdgeChains JS SDK

### Summary
Implements native Qdrant Vector Database support in the EdgeChains JavaScript/TypeScript SDK as requested in #273.
- **Zero external Qdrant packages**: Uses direct HTTP REST calls wrapped in the `QdrantClient` EdgeChains class (`JS/edgechains/lib/src/lib/clients/QdrantClient.ts`).
- **Full lifecycle methods**: `ensureCollection()`, `upsertPoints()`, `search()` (compatible with `HydeSearchService.ts`), and `deleteCollection()`.
- **Unit tests**: Added full Vitest test suite covering collection creation, api-key authentication, point upsert, and similarity search.

### Reference Implementation
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/edgechains-qdrant-sdk-273

/claim #273
Fixes #273