// File: test/sse-stream-accumulator.test.ts
import { describe, it, expect } from 'vitest';
import { SSEStreamTokenAccumulator } from '../src/ai-proxy/sse-stream-accumulator';

describe('SSEStreamTokenAccumulator', () => {
  it('reassembles JSON frames split mid-line and mid-UTF8 character', () => {
    const acc = new SSEStreamTokenAccumulator();
    const fullStream = [
      'data: {"choices":[{"delta":{"content":"Xin chào "}}]}\n\n',
      'data: {"choices":[{"delta":{"content":"Việt Nam!"}}],"usage":{"prompt_tokens":10,"completion_tokens":5,"total_tokens":15}}\n\n',
      'data: [DONE]\n\n',
    ].join('');

    const bytes = new TextEncoder().encode(fullStream);
    // Slice every 7 bytes to force mid-JSON and mid-UTF8 character splits
    for (let i = 0; i < bytes.length; i += 7) {
      acc.pushChunk(bytes.slice(i, i + 7));
    }

    const res = acc.finish();
    expect(res.content).toBe('Xin chào Việt Nam!');
    expect(res.totalTokens).toBe(15);
  });
});