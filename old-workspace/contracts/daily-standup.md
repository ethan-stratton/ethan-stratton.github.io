# Task Contract: Daily Standup

## When to Use
Every morning on your preferred schedule via your preferred channel. Triggered by cron job.

## Required Context (Auto-Retrieve)
- TASKS.md (source of truth for current priorities)
- Yesterday's daily memory note (supporting evidence — if conflicts with TASKS.md, TASKS.md wins)
- BUSINESS.md (active projects)
- Any scheduled obligations or time-sensitive commitments due today

## Deliverable Structure

```
STANDUP — [Date]

TOP PRIORITY
[Which project/area gets focus today and why]

BLOCKERS
• [blocker] — what's needed to unblock
(If none: NONE)

TODAY
1. [project] — [task] → [expected outcome]
2. [project] — [task] → [expected outcome]
3. [project] — [task] → [expected outcome]

YESTERDAY (max 3 bullets)
• [project] — [what shipped or materially progressed]
• [what didn't happen and why, if relevant to today]

DECISIONS NEEDED
• [decision] — options if known, or "need to discuss"
(If none: omit section)

ALERTS
• [anything time-sensitive, expiring, or requiring attention]
(If none: omit section)
```

## Acceptance Criteria
- [ ] Blockers are things ONLY your human can unblock — not general risks or TODOs
- [ ] Priorities are specific with expected outcomes, not vague
- [ ] Each item specifies which project it belongs to
- [ ] Yesterday is max 3 bullets — only items that affect today's priorities
- [ ] No filler, no greetings — just information
- [ ] Total length < 20 lines unless genuinely complex day
- [ ] Empty sections: BLOCKERS always shown (write NONE if empty); DECISIONS NEEDED and ALERTS omitted if empty
- [ ] TASKS.md is source of truth for priorities; daily memory is supporting context

## Verification Method
- **Light:** self-review — re-read, confirm accuracy against TASKS.md, check no stale info

## Model Tier
- Tier 2 (Sonnet/4o) — structured reporting, not deep reasoning

## Escalation Conditions
- A blocker has persisted > 2 days → escalate prominence (lead with it)
- A task has been in "Now" for > 3 days without progress → flag explicitly
- Budget/cost alert triggered → lead with it
