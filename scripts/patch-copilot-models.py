#!/usr/bin/env python3
"""
Patch pi-ai models.generated.js to fix github-copilot model context windows.
Values sourced from Copilot API /models endpoint (2026-03-24).

Run after `npm i -g openclaw@<version>` to fix built-in model limits.
Source: selyzz's research shared in Discord.
"""
import sys, os, re

# Find the file
paths = [
    os.path.expanduser('~/.local/lib/node_modules/openclaw/node_modules/@mariozechner/pi-ai/dist/models.generated.js'),
    '/usr/local/lib/node_modules/openclaw/node_modules/@mariozechner/pi-ai/dist/models.generated.js',
    '/app/node_modules/.pnpm/@mariozechner+pi-ai@0.58.0_@modelcontextprotocol+sdk@1.27.1_zod@4.3.6__ws@8.19.0_zod@4.3.6/node_modules/@mariozechner/pi-ai/dist/models.generated.js',
]

FILE = None
for p in paths:
    if os.path.exists(p):
        FILE = p
        break

if not FILE:
    print("ERROR: models.generated.js not found", file=sys.stderr)
    sys.exit(1)

print(f"Patching: {FILE}")

with open(FILE) as f:
    content = f.read()

original_len = len(content)

# === PART 1: Fix contextWindow/maxTokens for existing github-copilot models ===
# Format: (old_ctx, new_ctx, old_max, new_max, next_model_anchor)
# If old_max is None, only contextWindow is changed.

FIXES = [
    (128000, 200000, 32000, 64000, 'claude-opus-4.5'),     # claude-haiku-4.5
    (128000, 200000, None, None, 'claude-opus-4.6'),        # claude-opus-4.5
    (1000000,200000, 64000, 32000, 'claude-sonnet-4"'),     # claude-opus-4.6
    (128000, 216000, None, None, 'claude-sonnet-4.5'),      # claude-sonnet-4
    (128000, 200000, None, None, 'claude-sonnet-4.6'),      # claude-sonnet-4.5
    (1000000,200000, None, None, 'gemini-2.5-pro'),         # claude-sonnet-4.6
    (128000, 200000, None, None, 'gemini-3.1-pro-preview'), # gemini-3-pro-preview
    (128000, 200000, None, None, 'gpt-4.1'),                # gemini-3.1-pro-preview
    (64000, 128000, None, None, 'gpt-4o'),                  # gpt-4.1
    (64000, 128000, 16384, 4096, 'gpt-5"'),                 # gpt-4o
    (128000, 264000, None, None, 'gpt-5.1"'),               # gpt-5-mini
    (128000, 264000, None, None, 'gpt-5.1-codex"'),         # gpt-5.1
    (128000, 400000, None, None, 'gpt-5.1-codex-max'),      # gpt-5.1-codex
    (128000, 400000, None, None, 'gpt-5.1-codex-mini'),     # gpt-5.1-codex-max
    (128000, 400000, None, None, 'gpt-5.2"'),               # gpt-5.1-codex-mini
    (264000, 400000, 64000, 128000, 'gpt-5.2-codex'),       # gpt-5.2
]

applied = 0
for old_ctx, new_ctx, old_max, new_max, anchor in FIXES:
    if old_max is not None:
        old = f'contextWindow: {old_ctx},\n            maxTokens: {old_max},\n        }},\n        "{anchor}'
        new = f'contextWindow: {new_ctx},\n            maxTokens: {new_max},\n        }},\n        "{anchor}'
    else:
        pattern = f'contextWindow: {old_ctx},\n            maxTokens: (\\d+),\n        }},\n        "{anchor}'
        match = re.search(pattern, content)
        if match:
            old = match.group(0)
            new = old.replace(f'contextWindow: {old_ctx},', f'contextWindow: {new_ctx},')
        else:
            continue

    if old in content:
        content = content.replace(old, new, 1)
        applied += 1

print(f"Part 1: Applied {applied}/{len(FIXES)} contextWindow/maxTokens fixes")

# === PART 2: Add missing models to github-copilot section ===

NEW_MODELS = {
    'claude-opus-4.6-1m': ('Claude Opus 4.6 (1M context)', 'anthropic-messages',
        'true', '["text", "image"]', None, 1000000, 64000),
    'goldeneye': ('Goldeneye', 'openai-responses',
        'true', '["text", "image"]', None, 400000, 128000),
    'gpt-5.4-pro': ('GPT-5.4 Pro', 'openai-responses',
        'true', '["text", "image"]', None, 400000, 128000),
    'minimax-m2.5': ('MiniMax M2.5', 'openai-completions',
        'true', '["text", "image"]',
        '{ "supportsStore": false, "supportsDeveloperRole": false, '
        '"supportsReasoningEffort": false, '
        '"maxTokensField": "max_completion_tokens" }',
        131000, 40000),
    'accounts/msft/routers/mp3yn0h7': ('Fireworks Router mp3yn0h7',
        'openai-completions', 'false', '["text", "image"]',
        '{ "supportsStore": false, "supportsDeveloperRole": false, '
        '"supportsReasoningEffort": false }',
        196000, 196000),
    'accounts/msft/routers/yaqq2gxh': ('Fireworks Router yaqq2gxh',
        'openai-completions', 'false', '["text", "image"]',
        '{ "supportsStore": false, "supportsDeveloperRole": false, '
        '"supportsReasoningEffort": false }',
        196000, 196000),
}

# Find github-copilot section boundaries
cp_start = content.find('"github-copilot": {')
if cp_start < 0:
    print("ERROR: github-copilot section not found", file=sys.stderr)
    sys.exit(1)

depth = 0
cp_end = cp_start
for i in range(cp_start, len(content)):
    if content[i] == '{': depth += 1
    elif content[i] == '}':
        depth -= 1
        if depth == 0:
            cp_end = i
            break

section = content[cp_start:cp_end]
last_model_end = section.rfind('},')
insert_pos = cp_start + last_model_end + 2

added = 0
entries_text = ''
for model_id, (name, api, reasoning, inp, compat, ctx, maxt) in NEW_MODELS.items():
    if f'"{model_id}":' in section:
        continue

    compat_line = f'\n            compat: {compat},' if compat else ''
    entries_text += f'''
        "{model_id}": {{
            id: "{model_id}",
            name: "{name}",
            api: "{api}",
            provider: "github-copilot",
            baseUrl: "https://api.individual.githubcopilot.com",
            headers: {{ "User-Agent": "GitHubCopilotChat/0.35.0", "Editor-Version": "vscode/1.107.0", "Editor-Plugin-Version": "copilot-chat/0.35.0", "Copilot-Integration-Id": "vscode-chat" }},{compat_line}
            reasoning: {reasoning},
            input: {inp},
            cost: {{
                input: 0,
                output: 0,
                cacheRead: 0,
                cacheWrite: 0,
            }},
            contextWindow: {ctx},
            maxTokens: {maxt},
        }},'''
    added += 1

if entries_text:
    content = content[:insert_pos] + entries_text + content[insert_pos:]

print(f"Part 2: Added {added}/{len(NEW_MODELS)} new models")
print(f"File size: {original_len} -> {len(content)}")

with open(FILE, 'w') as f:
    f.write(content)

print("Patch complete!")
