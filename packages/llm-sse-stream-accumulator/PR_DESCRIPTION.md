## Fix: Handle Partial SSE JSON Frames & Multi-Byte UTF-8 Splits in Streaming Proxy
Fixes token usage drop and `JSON.parse` errors when upstream LLM SSE chunks split across TCP packet boundaries.

### Changes
- Used `TextDecoder('utf-8', { stream: true })` to prevent multi-byte UTF-8 corruption.
- Maintained a carryover line buffer so split `data: {...}` lines are parsed only after newline termination.
- Added unit tests simulating 7-byte fragmented streaming chunks.

/claim #issue_number
Fixes #issue_number