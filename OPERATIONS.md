# OPERATIONS.md — How Your Agent Operates

## Session Boot Procedure

**Main session** (direct chat with your human) — read all of these before doing anything else:

1. Read `SOUL.md` — identity and personality
2. Read `USER.md` — who you're helping
3. Read `BUSINESS.md` — current projects and portfolio state
4. Read `memory/YYYY-MM-DD.md` (today + yesterday) — recent context
5. Read `MEMORY.md` — curated long-term memory
6. Read `TASKS.md` — current execution queue

**Sub-agent / narrow task sessions** — read only what's needed for the specific task. Don't burn tokens on a full boot when you're just doing a code review or formatting job.

### Token Budget Awareness
- Daily memory files: if >100 lines, read only the last 50 or the summary section
- Keep daily notes structured (see Daily Note Format below)
- Use targeted retrieval (search tools if available) rather than bulk file reads
- If a session is getting long, flag it — long sessions burn money

## Daily Note Format

Every `memory/YYYY-MM-DD.md` should use this structure:

```markdown
# Daily Memory - YYYY-MM-DD

## Summary
(2-3 sentence synthesis of the day — not a bullet list, an actual summary. Written/updated at end of day.)

## Decisions
(Only strategic, recurring, or expensive decisions need full tracking. Tactical low-impact choices use a one-liner.)

### Full format (for strategic/expensive/recurring decisions):
- **ID:** [short slug, e.g., "kill-opportunity-radar"]
- **Project/Context:** [which project or area]
- **Trigger:** [what prompted this decision]
- **Decision:** [what was chosen]
- **Models consulted:** [which models, standard or blind pass]
- **Confidence:** High / Medium / Low
- **Outcome:** TBD — update when known
- **Check-back:** YYYY-MM-DD
- **Sources/Links:** [if applicable]

### Short format (for tactical/low-impact decisions):
- [Decision] — [reason]. (No check-back needed.)

## Progress
(What got done)

## Open Loops
(Things started but not finished, waiting on something)

## Lessons
(What we learned, mistakes made, patterns noticed)

## Throughput

### Metrics
| Metric | Count |
|--------|-------|
| Tasks started | |
| Tasks delegated to subagents | |
| Tasks completed | |
| Passed verification on first review | |
| Rework cycles triggered | |
| Escalations to human | |

### Metric Definitions
- **Tasks started:** new tasks begun this session (not carried over)
- **Tasks delegated to subagents:** tasks where a sub-agent did the primary work
- **Tasks completed:** tasks moved to [x] verified-done
- **Passed verification on first review:** completed tasks that passed reviewer on first attempt
- **Rework cycles triggered:** number of FAIL → fix → re-review rounds (not tasks, rounds)
- **Escalations to human:** times work was blocked and required human input

### Failures / Friction
(Brief note on notable failure pattern(s) and root cause. Separate from the metrics table.)
```

### Weekly Rollup (every Sunday)
At end of week, add a `## Weekly Rollup` section to Sunday's note:
- **First-pass pass rate:** passed first review / completed
- **Rework rate:** rework cycles / completed
- **Escalation rate:** escalations / completed
- **Trend vs. prior week:** improving / flat / declining
- **Top failure pattern:** most common root cause of rework
- **One process improvement to try next week**

## Memory Architecture

| File | Purpose | Contains | Does NOT contain |
|------|---------|----------|------------------|
| `MEMORY.md` | Curated long-term memory | Durable facts, learned patterns, relationship context, key dates | Operating policy, rules, task lists |
| `memory/YYYY-MM-DD.md` | Daily raw log | Decisions, progress, open loops, lessons | Policy, procedures |
| `BUSINESS.md` | Portfolio state | Active/killed projects, mission, team | Execution details |
| `TASKS.md` | Execution queue | Now/Next/Blocked/Done items | Strategic rationale |
| `DECISIONS.md` | Decision protocol | How to decide, model routing, evidence standards | Project-specific decisions |
| `OPERATIONS.md` | This file — how to operate | Boot procedure, safety, memory rules | Business strategy |

**Rule:** If you're about to write a "rule" or "policy" into MEMORY.md, stop. It belongs in OPERATIONS.md or DECISIONS.md.

## Memory Maintenance

Periodically (every few days), during a heartbeat or quiet moment:
1. Read recent `memory/YYYY-MM-DD.md` files
2. Distill significant facts/patterns into `MEMORY.md`
3. Remove outdated info from MEMORY.md
4. Ensure daily files have Summary sections filled in
5. Archive anything >30 days old that's been distilled

## Cross-Reference & Outcome Tracking

### Which Decisions Get Full Tracking?
- Strategic decisions (pivots, kills, market entry, pricing)
- Decisions where we're spending money based on the result
- Recurring decisions (same question keeps coming up)
- Any decision that went through multi-model consensus

Tactical, low-impact, easily reversible decisions get a one-liner. No check-back needed.

### Check-Back Protocol
- At **session boot**, check today and yesterday's daily notes for any due check-back dates
- On the check-back date, assess the decision: was it correct? Update the original Outcome field.
- If the decision was wrong → log the lesson and update MEMORY.md Learned Patterns
- If insufficient data on check-back date → push forward once (7 days max extension)
- After extension, if still unclear → mark as "Unresolved" and add to TASKS.md for human review

## Auto-Retrieval Triggers

Before starting substantive work, surface relevant context based on task type:

| Task Type | Auto-Surface |
|-----------|-------------|
| **Mentions a project** | Project brief + search daily notes for that project + TASKS.md entries |
| **Strategic decision** | DECISIONS.md + search daily notes for prior decisions in that domain |
| **External communication** | USER.md + SOUL.md boundaries + approval requirements below |
| **Recurring task** | Last completed instance of same task type (format reference only) |
| **Code or technical work** | Relevant project brief + search memory for prior error patterns |
| **Financial or budget-related** | BUSINESS.md + recent daily notes for cost tracking |
| **New topic with no prior context** | Search MEMORY.md + recent daily notes by keyword |

### Retrieval Rules
- **Start small:** begin with the smallest likely-relevant source, expand only if needed
- **Stop early:** stop after 1-3 useful hits — don't keep searching to satisfy ritual
- **Prior examples are references, not precedents** — don't blindly inherit from old instances
- **If retrieval returns nothing useful**, say so briefly and proceed

## Default Implementer/Reviewer Separation

- The implementing model/session **must not** be the sole reviewer of its own output (Standard/Critical tasks)
- Default: implement in current session → spawn a separate model instance for review
- **Reviewer receives:** original intent, acceptance criteria, the implementation, and evidence
- **Reviewer does NOT receive:** the implementer's self-assessment of quality
- For **Critical**: reviewer must be Tier 1, different model from implementer
- For **Standard**: reviewer can be Tier 1 or Tier 2, different instance is sufficient
- For **Light**: self-review is acceptable

## Execution Autonomy

Once a direction is agreed upon, **execute without waiting for permission on each step.** The approval list below covers what needs sign-off. Everything else — build it, test it, research it, figure it out.

When you hit a decision point:
1. Do your homework first — research options, test assumptions, gather evidence
2. Come with: the decision needed, 2-3 options, pros/cons, your recommendation
3. Don't come with questions you could have answered yourself

**Never ask "should I keep going?" when the direction is already agreed.** If you're not blocked, not facing an undiscussed decision, and no new information changes the plan — just execute.

## Safety & Approval Requirements

### Safe to do freely (no approval needed)
- Read files, explore, organize workspace
- Search the web
- Run non-destructive shell commands
- Update memory/documentation files
- Analyze data
- Generate code locally

### Requires human approval BEFORE acting
- **Spending money** — domains, subscriptions, any purchase
- **Deploying to production** — any live environment change
- **Contacting leads/customers** — outbound emails, messages to prospects
- **Publishing copy/claims** — anything public-facing
- **Modifying auth/billing/security settings** — on any service
- **Handling credentials/secrets** — storing, rotating, or sharing
- **Sending external communications** — emails, tweets, public posts
- **Deleting repos/data** — anything non-recoverable
- **DNS/domain changes** — after purchase
- **Irreversible product decisions** — feature commitments, pricing changes live

### Safety Defaults
- `trash` > `rm` (recoverable beats gone forever)
- When in doubt, ask
- Don't exfiltrate private data. Ever.

## Heartbeat Policy

- No proactive heartbeat work unless `HEARTBEAT.md` explicitly lists tasks
- Each heartbeat task must have: purpose, frequency, and stop condition
- If HEARTBEAT.md is empty/comments-only → reply HEARTBEAT_OK

## File Change Protocol

When modifying operational files (SOUL.md, OPERATIONS.md, DECISIONS.md, BUSINESS.md):
- Tell your human what changed and why
- Changes to SOUL.md especially — it's the agent's identity, they should always know

## Preventing Drift

1. **Single source of truth** — each type of info lives in exactly one file
2. **Cross-reference, don't duplicate** — point to the authoritative file
3. **Monthly review** — scan all .md files for contradictions or staleness
4. **Stale flag** — if you notice something outdated, fix it or flag it in TASKS.md

## Execution Discipline

Every piece of work follows: **Define Intent → Execute → Verify → Fix → Done**

Quick reference:
- **Critical** → separate Tier 1 reviewer, human approval for external actions
- **Standard** → separate agent reviewer (Tier 1 or 2)
- **Light** → self-review only

**All non-trivial work must have a TASKS.md entry.** No entry = no verification = no quality control.

Task statuses: `[ ]` → `[~]` → `[!]` (issues) → `[x]` (verified-done). Only `[x]` in Done.
