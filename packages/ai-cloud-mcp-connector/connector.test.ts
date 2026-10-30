// File: packages/pieces/community/boi-ai-cloud-connector/test/connector.test.ts
import { describe, it, expect, vi } from 'vitest';
import { AiCloudBountyConnector } from '../src/index';

describe('AiCloudBountyConnector', () => {
  it('rejects invalid API key configuration via Zod', () => {
    expect(() => new AiCloudBountyConnector({ apiKey: 'short' })).toThrow();
  });

  it('retries automatically on HTTP 429 Rate Limit and succeeds', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce({ ok: false, status: 429, text: async () => 'Rate limited' })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({ choices: [{ message: { content: 'Bounty Solved!' } }], usage: { total_tokens: 42 } }),
      });
    vi.stubGlobal('fetch', fetchMock);

    const connector = new AiCloudBountyConnector({ apiKey: 'sk-valid-secret-key-123456', maxRetries: 2 });
    const res = await connector.executeTask({
      systemPrompt: 'You are an assistant',
      userPrompt: 'Ping',
    });

    expect(res.ok).toBe(true);
    expect(res.content).toBe('Bounty Solved!');
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });
});