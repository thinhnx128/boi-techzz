// File: src/ai-proxy/sse-stream-accumulator.ts
export interface TokenUsageSummary {
  promptTokens: number;
  completionTokens: number;
  totalTokens: number;
  content: string;
}

/**
 * Safely parses fragmented Server-Sent Events (SSE) chunks across arbitrary
 * TCP byte boundaries and accumulates LLM content + token usage metrics.
 */
export class SSEStreamTokenAccumulator {
  private readonly decoder = new TextDecoder('utf-8');
  private carryOver = '';
  private contentParts: string[] = [];
  private promptTokens = 0;
  private completionTokens = 0;
  private totalTokens = 0;

  pushChunk(chunk: Uint8Array): void {
    // stream: true preserves incomplete multi-byte UTF-8 sequences across chunks
    this.carryOver += this.decoder.decode(chunk, { stream: true });
    this.processCompleteLines(false);
  }

  finish(): TokenUsageSummary {
    this.carryOver += this.decoder.decode();
    this.processCompleteLines(true);
    return {
      promptTokens: this.promptTokens,
      completionTokens: this.completionTokens,
      totalTokens: this.totalTokens || this.promptTokens + this.completionTokens,
      content: this.contentParts.join(''),
    };
  }

  private processCompleteLines(flushRemainder: boolean): void {
    const lines = this.carryOver.split(/\r?\n/);
    this.carryOver = flushRemainder ? '' : (lines.pop() ?? '');

    for (const rawLine of lines) {
      const line = rawLine.trim();
      if (!line.startsWith('data:')) continue;
      const payload = line.slice(5).trim();
      if (!payload || payload === '[DONE]') continue;

      try {
        const parsed = JSON.parse(payload);
        const delta = parsed.choices?.[0]?.delta?.content;
        if (typeof delta === 'string') {
          this.contentParts.push(delta);
        }
        if (parsed.usage) {
          this.promptTokens = parsed.usage.prompt_tokens ?? this.promptTokens;
          this.completionTokens = parsed.usage.completion_tokens ?? this.completionTokens;
          this.totalTokens = parsed.usage.total_tokens ?? this.totalTokens;
        }
      } catch {
        // Ignore non-JSON heartbeat frames
      }
    }
  }
}