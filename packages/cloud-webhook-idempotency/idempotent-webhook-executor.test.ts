// File: test/idempotent-webhook-executor.test.ts
import { describe, it, expect, vi } from 'vitest';
import { AtomicIdempotentExecutor } from '../src/cloud/idempotent-webhook-executor';

describe('AtomicIdempotentExecutor Concurrency Guarantee', () => {
  it('executes handler exactly ONCE when 50 identical webhooks arrive simultaneously', async () => {
    const executor = new AtomicIdempotentExecutor<{ jobId: string }>();
    let executionCount = 0;

    const slowCloudDeployment = vi.fn(async () => {
      executionCount++;
      await new Promise((r) => setTimeout(r, 50));
      return { jobId: 'deploy-999' };
    });

    // Fire 50 concurrent requests at the exact same tick
    const results = await Promise.all(
      Array.from({ length: 50 }, () => executor.executeOnce('webhook-evt-12345', slowCloudDeployment))
    );

    expect(executionCount).toBe(1);
    expect(results.filter((r) => !r.deduplicated)).toHaveLength(1);
    expect(results.filter((r) => r.deduplicated)).toHaveLength(49);
    expect(results.every((r) => r.data.jobId === 'deploy-999')).toBe(true);
  });
});