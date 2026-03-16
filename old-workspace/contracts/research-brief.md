# Task Contract: Research Brief

## When to Use
Competitive analysis, market research, technology assessment, vendor evaluation, or any task where the deliverable is structured findings that inform a decision.

## Required Context (Auto-Retrieve)
- Project brief (if project-specific)
- Prior research on the same topic (search daily notes + memory)
- DECISIONS.md evidence standards
- Any constraints from your human (budget, timeline, scope)

## Deliverable Structure

```markdown
# [Topic] — Research Brief

## Question
(What are we trying to answer?)

## Key Findings
(Numbered list, most important first. Each finding must cite a source.)

## Evidence Table
| Claim | Source | Confidence | Notes |
|-------|--------|------------|-------|

## Contradictions & Unknowns
(Where sources disagree. What we couldn't verify.)

## Risks
(What could go wrong if we act on these findings?)

## Recommendation
(What to do, based on the evidence.)

## Confidence: High / Medium / Low
(Brief justification for the rating.)

## Sources
| # | Source | Type (primary/secondary/anecdotal) | Date Accessed |
|---|--------|------------------------------------|---------------|

## Scope Boundaries
(What this brief does NOT answer.)
```

## Acceptance Criteria
- [ ] Minimum 3 independent sources for market claims
- [ ] Competitor pricing verified from primary source (their website)
- [ ] No inference presented as fact
- [ ] Contradictions explicitly flagged, not hidden
- [ ] Confidence level justified, not just stated
- [ ] Recommendation follows logically from evidence
- [ ] Sources include type (primary/secondary/anecdotal) and access date
- [ ] Stale sources (>12 months for fast-moving markets/tech) are flagged
- [ ] "Insufficient evidence — recommend next data collection step" is an acceptable recommendation

## Verification Method
- **Standard:** Tier 2 reviewer checks evidence quality and logical consistency
- **Strategic (informs a pivot/kill/major spend):** Blind-pass multi-model consensus per DECISIONS.md

## Model Tier
- Tier 1 for strategic research
- Tier 2 for routine research

## Escalation Conditions
- Fewer than 3 credible sources found → flag to your human before recommending
- Sources materially contradict each other → present both sides, don't pick a winner
- Research scope expands beyond original question → check in before continuing
