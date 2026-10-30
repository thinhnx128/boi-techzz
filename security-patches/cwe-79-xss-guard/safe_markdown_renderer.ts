/**
 * Remediates CWE-79 Stored XSS in AI Chat Markdown/HTML Renderers.
 * Strips script tags, inline event handlers (on*), and javascript:/data: URIs.
 */
export function sanitizeAiMarkdownHtml(rawHtml: string): string {
  return rawHtml
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
    .replace(/\son[a-z]+\s*=\s*(['"]).*?\1/gi, '')
    .replace(/\b(href|src)\s*=\s*(['"])\s*(javascript|data|vbscript):.*?\2/gi, '$1="#"');
}
