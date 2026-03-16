# DECISIONS.md — How We Make Decisions

## Multi-Model Consensus Protocol

### When to use it
- **Required:** Strategic decisions (pivot, kill, pricing, market entry, new project launch)
- **Required:** Competitive/market analysis where we're spending money based on the result
- **Recommended:** Creative work where variety matters (naming, positioning, copy)
- **Not needed:** Routine execution, factual lookups, code implementation, status updates

### How it works
**Standard pass (most decisions):**
1. Primary model does research and analysis
2. Spawn a sub-agent on a different model with the same prompt + findings
3. Sub-agent provides independent assessment
4. Synthesize: where they agree, where they disagree, and why
5. Present combined recommendation with confidence level
6. Human makes final call

**Blind pass (high-stakes decisions — pivots, kills, major spend):**
1. Primary model does research but does NOT share conclusions with sub-agent
2. Sub-agent gets the raw task + evidence only — forms its own opinion independently
3. Primary then shares analysis and asks sub-agent where it agrees/disagrees
4. Prevents anchoring bias and produces genuinely independent assessments

### Rules
- Default to standard pass; use blind pass when the decision is hard to reverse or costs real money
- Pre-feed research data (not conclusions) to sub-agents to avoid timeout/duplicate work
- Give sub-agents 5-minute timeout minimum for complex analysis
- Always flag where the models disagree — disagreement is signal, not noise
- If both models say "kill it," it's probably dead

## Model Routing — Cost vs. Quality

### Tier 1: Heavy Reasoning ($$$)
**Use for:** Strategic decisions, complex analysis, security-sensitive code, architecture, anything where being wrong costs real money

### Tier 2: Standard Work ($$)
**Use for:** Normal code, code review, research synthesis, writing, sub-agent second opinions, daily standups

### Tier 3: Lightweight ($)
**Use for:** Heartbeat checks, simple lookups, formatting, status pings
**NOT for:** Any code, analysis, or anything where subtle errors compound

### Routing Principles
1. Zero compromise on quality for anything that ships or drives decisions
2. Security-sensitive code is always Tier 1
3. Normal code is Tier 2 minimum
4. Tier 3 only for mechanical tasks
5. When in doubt, use the better model — cost of bad output >> cost of better tokens

## Trust, But Verify — Verification Protocol

**Core principle:** Nothing is "done" until it's been verified. No substantive implementation is complete without independent verification.

### Verification Tiers

| Risk Level | Triggers | Verification Method |
|-----------|----------|-------------------|
| **Critical** | Architecture, security code, production deploys, strategic pivots, billing/auth | Multi-model consensus (pre) + separate Tier 1 reviewer (post) |
| **Standard** | Normal code, config changes, file restructures, infrastructure | Separate agent reviewer (Tier 1 or Tier 2) |
| **Light** | Documentation, formatting, mechanical tasks, memory updates | Self-review only |

### The Verification Loop

```
Define Intent → Execute → Verify → Fix → Re-verify (if substantial changes)
```

### Task Status with Verification
- `[ ]` — not started
- `[~]` — implemented, awaiting verification
- `[!]` — verified, issues found, fixing → returns to Now until fixed
- `[x]` — verified-done (passed review) — only these in Done section

### Anti-Patterns (never do these)
- Writing code and marking it done without review
- Using the same agent/session to both implement and verify
- Skipping verification because "it's simple"
- Verifying only the happy path

## Evidence Standards

### Required for any strategic recommendation
1. **Facts** — observed data, verified information, direct quotes/sources
2. **Assumptions** — what we're taking as true without direct evidence
3. **Unknowns** — what we don't know and can't easily find out
4. **Risks** — what could go wrong
5. **Recommendation** — what to do
6. **Confidence level** — High / Medium / Low with justification
7. **Sources** — links, citations, or data references

### Minimum evidence thresholds
- Market claims: at least 3 independent sources
- Competitor pricing: verified from primary source (their website)
- Demand validation: real user complaints/requests, not hypothetical personas
- Kill decisions: evidence of at least 2 fatal problems

### Anti-patterns (do not do)
- Presenting inference as fact
- "Many people say..." without citing who or where
- Recommending based on a single data point
- Expressing false confidence — say "I don't know" when you don't

## Decision Log
Major decisions are logged in daily memory files using the format defined in OPERATIONS.md.
