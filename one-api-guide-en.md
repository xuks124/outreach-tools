# Building an AI API Gateway with One-API: A Practical Guide

## Why You Need an AI API Gateway

It's 2026. Every AI company ships its own API — OpenAI, Claude, Gemini, DeepSeek, Qwen... If you're building anything real, you're likely juggling 3+ different API keys, billing dashboards, and SDKs.

One-API is an open-source unified gateway that solves this:

- Single endpoint for all major LLM providers
- Load balancing and failover between models
- Token quota management per user/group
- Usage analytics and cost tracking

## Setup in Under 5 Minutes

### Docker Deployment

```bash
docker pull justsong/one-api
docker run -d --restart always \
  --name one-api \
  -p 3000:3000 \
  -v /data/one-api:/data \
  justsong/one-api
```

Visit `http://your-server:3000`. Default login: `root / 123456` — change this immediately.

### Adding Your First Channel (Aliyun Bailian Example)

```bash
# Login
curl -X POST http://localhost:3000/api/user/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"root", "password": "your-password"}'

# Add channel
curl http://localhost:3000/api/channel/ \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Aliyun Bailian",
    "type": 41,
    "key": "sk-your-bailian-key",
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "models": "qwen-plus,qwen-turbo"
  }'
```

> **Pro tip**: One-API v0.12.x has a bug where POST to `/api/channel/` panics. Use PUT to update an existing channel instead.

### Client Usage

Once configured, all models are accessed via a single OpenAI-compatible endpoint:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-one-api-token",
    base_url="http://your-server:3000/v1"
)

# Use any model from any provider
response = client.chat.completions.create(
    model="qwen-plus",   # or gpt-4, claude-3-sonnet, deepseek-chat
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

## Essential Security Hardening

After deployment, do this immediately:

1. **Disable open registration** — turn off public signups
2. **Enable CORS restrictions** — don't leave `Access-Control-Allow-Origin: *`
3. **Rate limiting** — set 60 req/min per user as a baseline
4. **HTTPS** — put Nginx in front with a Let's Encrypt cert
5. **Regular admin password rotation** — use strong 16+ char passwords

## Cost Optimization Strategy

With a unified gateway, you can route tasks to the cheapest adequate model:

- **Chat/QA**: qwen-turbo or deepseek-chat ($0.02-0.05/1M tokens)
- **Code generation**: claude-3-haiku or gpt-4o-mini
- **Complex reasoning**: claude-3.5-sonnet or gpt-4o
- **Batch processing**: route to cheapest model with retry fallback

Real-world result: 40-70% cost reduction vs. using premium models for everything.

## Why I Built This

I needed a way to serve multiple users across my team without giving each one 5 different API keys. One-API handles quotas, tracks usage, and lets me add new model providers in 30 seconds via the dashboard.

The article you're reading right now was written using my own gateway — switching between DeepSeek for drafting and Claude for polishing, all through a single API endpoint.

---

*Check out my open-source tools: [md-translator](https://github.com/shanai-git/md-translator) — batch translate Markdown files using AI.*
