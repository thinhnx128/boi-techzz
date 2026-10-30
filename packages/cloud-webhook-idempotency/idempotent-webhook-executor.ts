// File: src/cloud/idempotent-webhook-executor.ts
export interface IdempotencyRecord<T> {
  status: 'in_flight' | 'completed';
  result?: T;
  promise?: Promise<T>;
  expiresAt: number;
}

/**
 * Eliminates Check-Then-Act race conditions when concurrent cloud webhooks
 * arrive within the same millisecond.
 */
export class AtomicIdempotentExecutor<T = unknown> {
  private readonly store = new Map<string, IdempotencyRecord<T>>();
  private readonly ttlMs: number;

  constructor(ttlMs = 15 * 60 * 1000) {
    this.ttlMs = ttlMs;
  }

  async executeOnce(idempotencyKey: string, handler: () => Promise<T>): Promise<{ deduplicated: boolean; data: T }> {
    const now = Date.now();
    const existing = this.store.get(idempotencyKey);

    if (existing && existing.expiresAt > now) {
      if (existing.status === 'completed') {
        return { deduplicated: true, data: existing.result as T };
      }
      if (existing.status === 'in_flight' && existing.promise) {
        const sharedData = await existing.promise;
        return { deduplicated: true, data: sharedData };
      }
    }

    // Atomic registration before yielding to the event loop
    let resolvePromise!: (val: T) => void;
    let rejectPromise!: (err: unknown) => void;
    const inFlightPromise = new Promise<T>((res, rej) => {
      resolvePromise = res;
      rejectPromise = rej;
    });

    this.store.set(idempotencyKey, {
      status: 'in_flight',
      promise: inFlightPromise,
      expiresAt: now + this.ttlMs,
    });

    try {
      const data = await handler();
      this.store.set(idempotencyKey, {
        status: 'completed',
        result: data,
        expiresAt: Date.now() + this.ttlMs,
      });
      resolvePromise(data);
      return { deduplicated: false, data };
    } catch (error) {
      // Remove failed execution lock so legitimate retries can proceed
      this.store.delete(idempotencyKey);
      rejectPromise(error);
      throw error;
    }
  }
}