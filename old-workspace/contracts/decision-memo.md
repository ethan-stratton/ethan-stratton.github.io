# Task Contract: Decision Memo

## When to Use
Strategic decisions: pivot, kill, pricing, market entry, new project launch, major spend, architecture choices — anything hard to reverse or with real-money consequences.

## Required Context (Auto-Retrieve)
- DECISIONS.md (full protocol + evidence standards)
- BUSINESS.md (portfolio state, mission)
- Prior decisions in the same domain (search daily notes)
- Project brief if project-specific
- Any prior research briefs on the topic

## Deliverable Structure

```markdown
# Decision: [One-line summary]

## Context
(Why this decision is needed now. What triggered it.)

## Options

### Option A: [Name]
- **Pros:**
- **Cons:**
- **Cost/effort:**
- **Risk:**

### Option B: [Name]
(same structure)

### Option C: [Name] (if applicable)
(same structure)

## Evidence
| Claim | Source | Verified? |
|-------|--------|-----------|

## Assumptions
(What we're taking as true without direct evidence.)

## Unknowns
(What we don't know and can't easily find out.)

## Decision Criteria
(What matters most for this decision: revenue, speed, reversibility, confidence, strategic fit, cash burn, etc.)

## Model Assessments
- **Primary Tier 1 assessment:** (summary)
- **Secondary Tier 1 assessment:** (summary)
- **Agreement:** (where they converge)
- **Disagreement:** (where they diverge and why)

## Recommendation
(Which option and why.)

## Confidence: High / Medium / Low
(Justification.)

## Reversibility
(How hard is it to undo this if we're wrong?)

## If Approved, Immediate Next Step
(What happens first if your human greenlights the recommendation.)
```

## Acceptance Criteria
- [ ] Minimum 2 viable options presented (status quo, defer, or limited experiment count as valid options)
- [ ] Evidence table populated with verified sources
- [ ] Assumptions and unknowns explicitly separated from facts
- [ ] Both models consulted (blind pass for high-stakes per DECISIONS.md)
- [ ] Disagreements highlighted, not smoothed over
- [ ] Reversibility assessed
- [ ] Recommendation follows from evidence, not vibes

## Verification Method
- Always **Critical**: blind-pass multi-model consensus
- your human makes final call — memo is input, not the decision itself

## Model Tier
- Tier 1 only (Opus + GPT 5.4)

## Escalation Conditions
- Models fundamentally disagree → present both cases clearly, don't force consensus
- Evidence is thin (< 3 sources for market claims) → flag explicitly
- Decision is time-sensitive → note deadline and minimum-viable-evidence threshold
