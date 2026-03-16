# Verification Checklists

> **Policy context:** For verification tier intent, routing, and overarching protocol, see `DECISIONS.md` → "Trust, But Verify."
> **Execution rules:** For approval requirements and execution discipline, see `OPERATIONS.md` → "Execution Discipline."

Executable checklists for each verification tier. When a task is tagged to a tier, the reviewer runs the corresponding checklist. These are not suggestions — they are required steps.

---

## Reviewer Inputs (All Tiers)

Before starting any review, the reviewer must receive:
1. **Intent statement** — what was this supposed to produce?
2. **Acceptance criteria** — what does "done" look like?
3. **The implementation** — the actual output/artifact
4. **Execution evidence** — test results, logs, screenshots, read-backs (whatever applies)
5. **Applicable task contract** — if one exists in `contracts/`

The reviewer does **NOT** receive the implementer's self-assessment or quality opinion.

---

## Critical Checklist

**Triggers:** Architecture decisions, security code, production deploys, strategic pivots, billing/auth changes, external-facing communications, anything where being wrong costs real money or trust.

**Reviewer:** Independent Tier 1 model, different from implementer. Required.

### Pre-Implementation
- [ ] Intent defined with explicit acceptance criteria
- [ ] Security/quality constraints documented
- [ ] TASKS.md entry exists

### Review Steps
- [ ] **Requirements match:** Does the output fulfill every stated acceptance criterion? (List each criterion, check each one.)
- [ ] **Evidence verified:** All factual claims cite a source. Reviewer spot-checks at least 2 sources for accuracy.
- [ ] **Uncertainty listed:** Assumptions, unknowns, and risks are explicitly separated from facts.
- [ ] **Security check:** No credentials exposed, no auth bypasses, no data leaks, no injection vectors.
- [ ] **Edge cases:** At least 3 failure scenarios considered and addressed.
- [ ] **Consistency check:** No contradictions with existing workspace files.
- [ ] **Reversibility assessed:** If this goes wrong, how do we undo it?
- [ ] **Task-type verification** (run the applicable sub-checklist below)

### Post-Review
- [ ] Reviewer provides: PASS or FAIL + specific issues + suggested fixes
- [ ] If FAIL: fix issues → re-run full checklist
- [ ] If PASS: human approval required before external action (deploy, send, publish)
- [ ] Log verification method and result in TASKS.md Done entry

---

## Standard Checklist

**Triggers:** Normal code, config changes, file restructures, infrastructure setup, operational doc updates, non-strategic research.

**Reviewer:** Separate agent instance (Tier 1 or Tier 2). Required.

### Pre-Implementation
- [ ] Intent defined (1-2 sentences of what "done" looks like)
- [ ] TASKS.md entry exists

### Review Steps
- [ ] **Requirements match:** Does the output fulfill the stated intent?
- [ ] **Targeted checks:** Reviewer spot-checks non-obvious claims or logic
- [ ] **Format and structure:** Follows applicable task contract template (if one exists)
- [ ] **No regressions:** Doesn't break or contradict existing work
- [ ] **Completeness:** Nothing obviously missing that the intent implies
- [ ] **Task-type verification** (run the applicable sub-checklist below)

### Post-Review
- [ ] Reviewer provides: PASS or FAIL + specific issues
- [ ] If FAIL: fix issues → reviewer re-checks failed items only (full re-run only if architecture changed)
- [ ] If PASS: mark [x] in TASKS.md with verification method
- [ ] No human approval needed unless it touches an approval-required action (see OPERATIONS.md)

---

## Light Checklist

**Triggers:** Formatting, mechanical tasks, memory updates, daily notes, status messages. Only for work where no one will act on the output beyond internal reference.

**Reviewer:** Self-review only.

### Self-Review Steps
- [ ] **Re-read:** Read the output fresh — does it match the intent?
- [ ] **Format check:** Correct structure, no broken markdown, no orphaned references
- [ ] **Accuracy spot-check:** Any facts/dates/names correct?
- [ ] **No unintended changes:** If editing an existing file, verify nothing was accidentally deleted or altered
- [ ] **Task-type verification** (run the applicable sub-checklist below, self-review version)

### Post-Review
- [ ] If issues found: fix and re-read
- [ ] Mark [x] in TASKS.md with "self-reviewed"

---

## Task-Type Sub-Checklists

Run the applicable sub-checklist as part of the tier checklist above.

### Code
- [ ] Build passes (no compilation/syntax errors)
- [ ] Lint and type checks pass (if configured)
- [ ] Tests pass (if they exist); if no tests exist, flag this as a gap
- [ ] Security-sensitive code (auth, billing, crypto, data handling) → must be Critical tier regardless of other factors
- [ ] No hardcoded secrets, credentials, or API keys

### Docs / Operational Files
- [ ] Re-read the modified file in full after editing
- [ ] No accidental content deletion (compare section count before/after if major edit)
- [ ] Cross-references to other files are still valid
- [ ] No contradictions introduced with other workspace files

### Research / Decision Memos
- [ ] Follows applicable task contract in `contracts/`
- [ ] Evidence table populated; sources verified from primary source where required
- [ ] Contradictions between sources explicitly flagged
- [ ] Confidence level stated and justified

### System / Config Changes
- [ ] Verify actual state matches expected state (read-back, test behavior, confirm registration)
- [ ] Rollback plan documented or obvious
- [ ] No unintended side effects on other services/configs

---

## Tier Assignment Rules

1. **External, public, security-sensitive, or money-involved → Critical**
2. **Internal but someone will act on the output (code, decisions, research) → Standard**
3. **Pure recordkeeping/formatting where no one acts on it → Light**
4. **If still unsure → Standard** (err toward more review)
5. **Tier escalation always allowed; tier downgrade requires explicit justification**

Examples:
- Landing page copy → Critical (external-facing)
- OPERATIONS.md restructure → Standard (agents act on it daily)
- Daily memory note → Light (internal record)
- Auth code → Critical (security)
- Task contract draft → Standard (guides future work)
- Fixing a typo in MEMORY.md → Light
