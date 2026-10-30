// File: packages/pieces/community/boi-ai-cloud-connector/src/index.ts
import { z } from 'zod';

export const AiCloudConnectorConfigSchema = z.object({
  apiKey: z.string().min(16, 'API Key is required'),
  baseUrl: z.string().url().default('https://api.openai.com/v1'),
  timeoutMs: z.number().int().min(1000).max(120000).default(30000),
  maxRetries: z.number().int().min(0).max(5).default(3),
});

export type AiCloudConnectorConfig = z.infer<typeof AiCloudConnectorConfigSchema>;

export const ExecuteAgentTaskInputSchema = z.object({
  model: z.string().default('gpt-4o-mini'),
  systemPrompt: z.string().min(1),
  userPrompt: z.string().min(1),
  temperature: z.number().min(0).max(2).default(0.2),
  IdempotencyKey: z.string().uuid().optional(),
});

export type ExecuteAgentTaskInput = z.infer<typeof ExecuteAgentTaskInputSchema>;

export class AiCloudBountyConnector {
  private readonly config: AiCloudConnectorConfig;

  constructor(rawConfig: unknown) {
    this.config = AiCloudConnectorConfigSchema.parse(rawConfig);
  }

  async executeTask(rawInput: unknown): Promise<{ ok: boolean; content: string; usage?: Record<string, number> }> {
    const input = ExecuteAgentTaskInputSchema.parse(rawInput);
    let lastError: Error | null = null;

    for (let attempt = 0; attempt <= this.config.maxRetries; attempt++) {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), this.config.timeoutMs);

      try {
        const res = await fetch(`${this.config.baseUrl.replace(/\/$/, '')}/chat/completions`, {
          method: 'POST',
          signal: controller.signal,
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.config.apiKey}`,
            ...(input.IdempotencyKey ? { 'Idempotency-Key': input.IdempotencyKey } : {}),
          },
          body: JSON.stringify({
            model: input.model,
            temperature: input.temperature,
            messages: [
              { role: 'system', content: input.systemPrompt },
              { role: 'user', content: input.userPrompt },
            ],
          }),
        });

        clearTimeout(timer);

        // Retry automatically on 429 Rate Limit or 5xx Server Error
        if (res.status === 429 || res.status >= 500) {
          const backoffMs = Math.min(1000 * Math.pow(2, attempt), 8000);
          await new Promise((r) => setTimeout(r, backoffMs));
          continue;
        }

        if (!res.ok) {
          const errText = await res.text();
          throw new Error(`Upstream API Error (${res.status}): ${errText}`);
        }

        const data = await res.json();
        return {
          ok: true,
          content: data.choices?.[0]?.message?.content ?? '',
          usage: data.usage,
        };
      } catch (err) {
        clearTimeout(timer);
        lastError = err instanceof Error ? err : new Error(String(err));
        if (attempt === this.config.maxRetries) break;
      }
    }

    throw lastError ?? new Error('Failed to execute AI Cloud Connector action');
  }
}