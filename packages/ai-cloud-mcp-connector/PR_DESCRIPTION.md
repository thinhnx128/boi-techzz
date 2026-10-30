## Summary
Implements the requested **AI Cloud Action & MCP Connector Piece** with full Zod schema validation, automatic exponential backoff for `HTTP 429 / 5xx` responses, request timeout cancellation via `AbortController`, and idempotency key support.

### Changes Included
- Added strict input & auth configuration validation using `zod`.
- Implemented resilient retry logic with exponential backoff for transient cloud errors.
- Added comprehensive unit test suite covering schema validation and `HTTP 429` retry recovery.

/claim #issue_number
Closes #issue_number