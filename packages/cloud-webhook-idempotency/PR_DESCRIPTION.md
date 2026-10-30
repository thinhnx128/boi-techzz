## Fix: Prevent Duplicate Webhook Execution Under High Concurrency
Resolves the check-then-act race condition when multiple identical webhook deliveries arrive within the same event-loop tick.

### Root Cause
Previously, the webhook handler performed an asynchronous state lookup before acquiring an execution lock, allowing concurrent deliveries with the same `Idempotency-Key` to trigger duplicate deployments.

### Solution
- Implemented `AtomicIdempotentExecutor` which synchronously registers an `in_flight` lock prior to yielding to the event loop.
- Concurrent arrivals coalesce onto the same in-flight promise and automatically release the lock if the underlying task throws an error.
- Added a 50-way concurrency unit test proving the handler executes strictly once.

/claim #issue_number
Fixes #issue_number