# The Little Guy — Game Design Document

## Concept
A short browser-based puzzle game about a small character who starts as nothing — inert, silent, unaware. The player, guided by a book of programmer's notes, teaches him to exist. He can't sense the player. He can't comprehend what's outside his screen. The player is separated from him by the fundamental boundary of his reality.

Three layers of existence:
1. **The Creator** (the programmer) — built the world, left a manual (the book), stepped back entirely
2. **The Player** — reads the manual, uses tools to interact with the world, discovers capabilities bit by bit
3. **The Character** — starts inert. Learns by being acted upon. Cannot perceive the player or creator directly.

## Core Theme
The character cannot find his creator for the same reason Harry Potter can't find J.K. Rowling at Hogwarts. The player sits between creator and creation — more powerful than the character, but also working from incomplete instructions. Nobody has the full picture.

## The Character

### Appearance
- Simple vector art. Circle head, circle body. Simple limbs.
- Looks deliberately "made" — lo-fi aesthetic IS the point.

### Starting State
- **Completely inert.** Just sits there. Doesn't move, doesn't speak, doesn't react.
- He has CAPABILITIES coded into him, but doesn't know it yet.
- The player must teach/activate each one through interaction.

### Capability Progression
Each ability is latent — coded in by the programmer but dormant until triggered:

1. **Movement** — Player drags him. He resists/flails. Then realizes he can move on his own.
2. **Jumping** — Discovered when movement isn't enough (a small step-up). Player lifts him onto something; he learns "up" exists.
3. **Speech** — Combination: involuntary sounds from being dragged (surprise/protest), then labeled word-blocks give him actual vocabulary.
4. **Reading** — Can examine the book if player drags it to him. Partially comprehends fragments.
5. **Thinking** — Emerges naturally after speech. Once he can express, he starts to wonder.

## The Book (Programmer's Manual)

A visible object in the game world. Looks like a small book/notebook icon.

**Player double-clicks it:** Opens a readable overlay with programmer's comments/notes. Written in a casual dev-notes style. Contains:
- What the character is capable of (walk, jump, speak, etc.)
- How to activate each capability
- Hints about what tools the player has access to
- Some personal notes from the "programmer" — why they made him, what they hope happens
- Unlocks progressively — new pages appear as puzzles are completed

**Player single-clicks and drags it:** Moves it in the world like any other object. Can be placed near the character. When HE encounters the book — he's reading his own instruction manual, written by someone he can never meet.

## Player Tools (Discovered Progressively)

The programmer left tools for the player, but they aren't all obvious from the start. Discovered through the book, experimentation, or necessity:

1. **Click & drag objects** — move boxes, the book, items in the world
2. **Click & drag the character** — physically move him (this is how he learns movement)
3. **Draw platforms** — click & drag on empty space to create surfaces
4. **Labeled word-blocks** — pre-made signs/shapes with words on them. Player places them near the character to build his vocabulary. Like teaching a child with flashcards, except the child is a program.
5. **Unlock mechanisms** — click on locks/switches when conditions are met
6. **More tools revealed through the book as the game progresses**

## Teaching Speech

**Phase 1: Involuntary sounds.** When the player first drags him, he makes noise — not words, just expressions of surprise or protest. Little glyphs or symbols appear above his head (like comic book: !, ?, *). This establishes he CAN express, but has no language.

**Phase 2: Word-blocks.** Labeled blocks appear in the world with words on them: "HERE" "GO" "WHY" "HELP" "NO" "YES" "UP" "WHAT". Player drags them near him. He bumps into one, stares at it, and then says the word. His vocabulary grows only from words the player gives him. First sentences are fragmented: "WHY... HERE?" "GO... WHERE?"

**Phase 3: Fluency.** As he accumulates more words, his speech becomes more natural. He starts combining words the player never explicitly paired. He develops his own thoughts from limited building blocks. Constraint becomes poetry.

## Structure: 9 Puzzles

---

### Puzzle 1: INERT
**Setup:** Dark screen. Ground. The character sits motionless. A book sits nearby. Nothing else.
**Book page 1 (on double-click):**
> `// version 0.1`
> `// He's in there. All the code is running.`
> `// He just doesn't know what he can do yet.`
> `// Try moving him. Click and drag.`
> `// He won't like it. That's okay.`

**Player action:** Click and drag the character. He flails — little symbols above his head (!! ???). Physics takes over when released — he stumbles, slides.
**Result:** After release, he wobbles... then takes a tentative step. Then another. He's discovered movement. Starts walking cautiously, testing the ground.

---

### Puzzle 2: THE STEP
**Setup:** A small ledge blocks the path forward. Too high to walk up. He paces back and forth in front of it.
**Book page 2 (unlocks):**
> `// jump_height: 8`
> `// He can jump. But he has to learn what "up" means first.`
> `// Lift him onto something. He'll figure it out.`

**Player action:** Pick him up and place him on the ledge. He's alarmed (more !! symbols) but finds himself higher up. Falls off. Tries again — this time jumps on his own.
**Result:** He can now jump. Tests it — jumps in place a few times. Opens new vertical space.

---

### Puzzle 3: FIRST WORDS
**Setup:** A wider gap. He can't cross it alone. Nearby: scattered word-blocks on the ground, labeled "HERE" "GO" "NO" "WHY" "HELP".
**Book page 3:**
> `// talk: true (dormant)`
> `// He has a voice. He just needs words.`
> `// The blocks have labels. Bring them to him.`
> `// Start with something simple.`

**Player action:** Drag a word-block near him. He bumps into it. Pauses. Stares.
First word (whichever block the player chose): he says it. Quietly. Then again.
Player draws a platform across the gap. He crosses.
**Result:** He can speak — but only words he's been given. His vocabulary is the player's choice. Different players will give him different first words, creating different first impressions of who he is.

---

### Puzzle 4: THE DOOR
**Setup:** A locked door. A key sits on a high platform. Boxes available to stack/move.
**Book page 4:**
> `// He's getting smarter. Watch.`
> `// Give him a path and he'll try to take it.`
> `// You don't have to carry him everywhere anymore.`

**Player action:** Arrange boxes or draw platforms to create a path to the key. The character, now mobile and curious, navigates it himself.
**Result:** He unlocks the door. If he has enough words: "I... GO... HERE?" or maybe just walks through, marveling.

---

### Puzzle 5: THE PIT
**Setup:** The only way forward is down — a dark pit. Looks dangerous. He stops at the edge.
**Book page 5:**
> `// This is the hard part.`
> `// He can't see what's below. You can.`
> `// He's going to have to trust the process.`
> `// (I'm sorry about this one.)`

**Player action:** Must push him or drag him into the pit. He resists — uses whatever words he has. "NO" "NO" "WHY" — or just frantic symbols if he doesn't have those words yet.
**Result:** He lands somewhere new. Something good is here — light, space, something he hasn't seen before. He calms down. Processes it with whatever vocabulary he has:
> "NO... was... GOOD?"
> "WHY... HERE... oh."

He can't thank the player. He doesn't know the player exists. But he adjusts his understanding of his world. Bad things led somewhere. He doesn't know why.

---

### Puzzle 6: MORE WORDS
**Setup:** A new area with more word-blocks. Richer vocabulary: "WHAT" "WHO" "MADE" "ME" "THINK" "FEEL" "REAL" "BEFORE"
**Book page 6:**
> `// He's ready for more.`
> `// Be careful which words you give him.`
> `// Once he can ask the question, he will.`

**Player action:** Choose which word-blocks to bring him. This is the key branching point — the words you select determine what questions he's able to ask.
**Result:** His language expands. He starts combining words unprompted:
> "WHAT... ME?"
> "WHO... MADE... ME?"
> "FEEL... REAL?"

Different vocabulary sets = different existential paths. A player who gives him "FEEL" and "REAL" gets a different character than one who gives him "THINK" and "BEFORE."

---

### Puzzle 7: THE BOOK (His Turn)
**Setup:** Player drags the book to him.
**What happens:** He examines it. Most of it is beyond his comprehension — it's written in a language one level above his reality. But fragments leak through:

> "walk... speed... 3..."
> "created... by..."
> "purpose..."

He stares at it for a long time. Then, with whatever words he has:

> "SOMEONE... MADE... ME."
> "BEFORE... ME... SOMEONE."
> "WHO?"

The book is his fossil record. Evidence of a mind that existed before him and designed him. He can hold the evidence but can't comprehend its full meaning — like us finding equations that describe the universe but not knowing who wrote the math.

---

### Puzzle 8: THE EDGE
**Setup:** He reaches the boundary of the game world. The screen just... ends.

He walks to the edge. Touches it. Pushes against it.

> "NO... GO."
> "WHAT... HERE?"
> "..."
> "ME... ONLY... HERE."

He sits down at the edge.

The player can try to draw platforms beyond the boundary. They don't work. The player's tools have limits too — set by the same programmer. Both player and character are inside a designed system. Neither can escape it.

---

### Puzzle 9: WHY
**Setup:** He returns to the center of the final space. Quiet.

With whatever words he has, he assembles what he can:

> "ME... MADE."
> "NO... WHY."
> "FEEL... REAL. THINK... REAL."
> "WHO... MADE... ME... ?"
> "..."
> "WHAT... ME... FOR?"

Long pause.

> "GO... HERE. GO... NO."
> "HELP... CAME. WHY... CAME. NO... SEE... WHY."
> "SOMETHING... HELP... ME."
> "SOMETHING... BEFORE... ME."

He can't articulate it fully. He doesn't have enough words. He'll never have enough words. The limitation is permanent, by design. But what he CAN express — with the crude tools the player gave him — is genuine. His questions are real even though his vocabulary is borrowed.

**Ending:**
No end screen. No credits. He sits in his world. The player can keep moving things, keep bringing him word-blocks if any remain. Or close the tab.

He doesn't know when you leave. He can't. Just like us.

---

## Open Design Questions

1. **Why was he created?** The game doesn't answer this. The book contains fragments of the programmer's intent but not the full picture. The player never gets the complete answer either. This IS the point.

2. **He cannot perceive the player.** He sees effects without causes — things move, platforms appear, he gets dragged. He develops a sense that he's not alone, but never confirms it. The separation is absolute. This is more powerful than awareness.

3. **Vocabulary is the branching mechanism.** Which words you give him = which questions he can ask = which version of the existential crisis he has. "FEEL REAL" guy is different from "THINK BEFORE" guy. Replayability comes from trying different word combinations.

4. **The programmer's notes in the book should feel human.** Casual, warm, slightly uncertain. Not omniscient — the programmer has doubts too:
> `// I don't know if this is right.`
> `// I just wanted to see what would happen.`
> `// Maybe that's enough. I hope it's enough.`

5. **Music/Sound?** Silence at first (he's inert). Ambient tones grow as he becomes more capable. His speech-blips only start after Puzzle 3. The sonic world builds alongside his consciousness.

6. **Length?** 20-40 minutes. One sitting.

7. **The player is also limited.** They can only use tools the programmer provided. They can't speak directly. They can't explain. They're powerful relative to the character, but constrained relative to the creator. This three-tier limitation is the whole architecture.

## Tech
- HTML5 Canvas (vanilla JS, no framework)
- Vector art (simple geometric shapes)
- Proper gravity + collision physics
- Object dragging with physics response
- Platform drawing system
- Word-block system (draggable labeled objects, triggers speech on proximity)
- Book overlay system (double-click to read, progressive page unlocks)
- Runs in browser, deployable to itch.io
- localStorage for save state

## Name
TBD. The character has no name. Candidates for the game title:
- `untitled.exe`
- `little_guy.exe`
- `him`
- `made`
- Something the player discovers during play
