# Research Notes — 2026-03-17

## 1. Fonts in MonoGame

**Current state:** We use MonoGame's built-in SpriteFont (bitmap-based, baked at compile time). Looks blurry at non-native sizes, no runtime scaling, limited character sets.

**Better option: FontStashSharp**
- NuGet: `FontStashSharp.MonoGame`
- Load .ttf files at runtime, render at any size on demand
- Text effects: stroked text, blurry text, underline, strikethrough
- Rich text engine built in (bold/italic/color inline)
- HarfBuzz text shaping support (important if we ever display Hebrew/Arabic script)
- Drop-in replacement for SpriteBatch.DrawString — minimal refactor
- **Action item:** Switch to FontStashSharp. Lets us use any TTF font, scale cleanly for UI/dialogue, and opens the door for stylized text (damage numbers, boss names, lore fragments with different typefaces).

**Font choices for GENESYS:**
- Dialogue: Something readable, slightly archaic (IM Fell types, Cormorant Garamond)
- UI/HUD: Clean pixel font or monospace (Press Start 2P, Silkscreen)
- Lore fragments: Hand-drawn or uncial style (Uncial Antiqua, MedievalSharp)
- Native language: Could use a constructed/cipher font — EVE "translates" by swapping font rendering

## 2. Visual Art Options for Solo Dev

**Viable approaches for a single developer:**
1. **Pixel art** — Most proven for solo 2D. Celeste, Hyper Light Drifter, Dead Cells. Time-intensive but learnable. Tools: Aseprite, LibreSprite, Pyxel Edit.
2. **Vector/Flash-style** — Hollow Knight, Dust: An Elysian Tail. Cleaner, scales perfectly, but requires drawing skill. Tools: Inkscape, Affinity Designer.
3. **Silhouette/minimalist** — Limbo, Inside, Badland. Very achievable solo. Strong atmosphere from lighting/particles alone.
4. **Rotoscope/mixed media** — Flashback, Another World. Unique but labor-intensive.
5. **AI-assisted + hand-painted** — New frontier. Generate base assets, hand-refine. Risky for consistency but fast for prototyping.
6. **Stylized simple** — Downwell (2 colors), Thomas Was Alone (rectangles with personality). Constraint as style.

**Recommendation for GENESYS:**
Given the Genesis/alien planet aesthetic, **pixel art with selective HD elements** could work beautifully:
- Characters and enemies: 32x48 to 64x64 pixel art (manageable sprite counts)
- Backgrounds: Parallax layers, could be painterly or AI-assisted
- Effects: Particle systems, screen shake, color bursts (these are code, not art)
- UI: Clean vector/FontStashSharp rendered text

The **silhouette approach** also fits the Mystery pillar perfectly — the Mecha Dragon as a massive dark shape with glowing seams, never fully detailed.

## 3. 2D Sidescroller Movement — What Makes It Great

**Games cited as having the best 2D movement:**

### Celeste
- **Coyote time** (grace frames after leaving platform edge)
- **Input buffering** (jump registered slightly before landing)
- **Variable jump height** (hold = higher, tap = short hop)
- **Dash feels explosive** — screen shake, freeze frame, speed lines
- **Sound and visual feedback** are 50% of why it feels good
- **Key insight:** The base movement (run + jump) must feel perfect BEFORE adding abilities

### Hollow Knight
- **Weight** — the character has mass. Landing has impact.
- **Pogo mechanic** (downward slash bouncing) creates emergent movement
- **Dash is earned** and transforms how you navigate old areas
- **Nail arts** require commitment — hold and release, risk/reward

### Ori and the Blind Forest / Will of the Wisps
- **Bash** — redirect off enemy projectiles for movement. Turns combat into traversal.
- **Launch** — ground pound that propels you upward. Satisfying loop of down→up.
- **Flow state** — stringing abilities together creates continuous momentum
- **Key insight:** The best movement systems let you CHAIN abilities into something the designer didn't explicitly plan

### Dead Cells
- **No animation startup on direction change** — instant response
- **Roll has i-frames** and maintains momentum
- **Verticality** — the combination of wall jump, slam, and roll creates 3D-feeling movement in 2D

### Mega Man X (SNES)
- **Wall jump** changed everything — added a whole vertical axis
- **Dash** shortens horizontal gaps, makes the game feel faster
- **Key insight:** Each new ability should make you want to replay OLD levels

### What they all share:
1. **Instant response** — no input lag, no animation wind-up for basic moves
2. **Generous edge cases** — coyote time, input buffering, corner correction
3. **Visual/audio feedback** — every action has satisfying juice
4. **Chaining** — abilities combine in ways that feel creative and emergent
5. **Progressive mastery** — easy to do, hard to optimize

**For GENESYS:** We already have many of these (slide, cartwheel, dash, wall climb, vault kick, blade dash). What we need:
- Coyote time and input buffering (if not already implemented)
- Better visual feedback per move (screen shake, particles, freeze frames)
- Ability chaining that feels emergent (e.g., slide → vault kick → wall jump → blade dash)
- Sound design per action (even placeholder sounds help feel)

## 4. Hebrew Etymology — Adam, Eve, Eden

### Adam (אדם)
**Not a name — a category.** Hebrew has no capital letters. "Adam" is indistinguishable from the common noun for "man/humanity." To a Hebrew reader, the story of Adam is the story of **all humanity**, not one person.

**Etymology layers:**
- **אדם ('adam)** = man, humanity, "corporeal one," "dustling"
- **אדמה ('adama)** = arable soil, earth, acre (feminine form of adam)
- **אדם ('adom)** = red, ruddy
- **דם (dam)** = blood (seat of life)
- Root **דמם (dmm)** = stillness, silence, beginning — "the simplicity from whence complexity arises"

**Key insight:** Adam means something like "Living Creature" or "Corporeal One" — the physical body BEFORE receiving breath. Adam was literally a corpse until God breathed into him (Genesis 2:7). The relationship between adam (humanity) and adama (earth/soil) implies that **humanity arose from the land** — the agricultural revolution, when humans began changing the land as much as the land changed them.

**"The first Adam became a living being; the last Adam became a life-giving spirit."** (1 Cor 15:45)

### Eve (חוה / Chawwa)
**Not "Life" — "Symbiosis."** While traditionally derived from חיה (haya, to live), Abarim argues the name is spelled/pronounced identical to חוה (hawwa), meaning **tent village** — the most rudimentary collective that operates as a living symbiotic whole.

**Etymology:**
- **חוה (hawa)** = to lay out in order to live collectively, to invest personal sovereignty into a living collective
- **חוה (hawwa)** = tent village, primary form of human settlement
- Eve as "mother of all life" (אם כל־חי) — "mother" (אם) is the same root as "nation/tribe"
- The "mother of all life" is the **biosphere** — not just humans

**Key insight:** Eve represents the **transition from primitive tribe to sophisticated culture** — from natural caves to constructed shelters (twigs, leaves, later wool). She embodies the drive to group up, to cluster for viability. If life is culture, and ultimately language, then Eve IS the mother of all life.

**The character Eve "did not happen just once" — she embodies the transition from single-cell to multicellular, from atom to molecule, from tribe to civilization.**

### Eden (עדן)
- **Meaning:** Delight, Finery, Luxury
- Root **עדן ('eden)** = "free exchange of broadly diverse information, services and goods — which is where wealth comes from"
- The garden was "east of Eden" or "just prior to Eden" — Eden is what comes AFTER the garden, not the garden itself
- Four rivers = possibly four centers of early civilization (Indus Valley, Nubia, Anatolia, Sumer)
- Eden as a concept: **the state of abundance that emerges from free exchange and cooperation**

### Hebrew (עבר)
- Means "One Who Transits" or "Passer Over" — from עבר ('abar), to pass over
- The Hebrews invented the alphabet — "the greatest invention mankind has ever made"
- The alphabet was the fire around which civilization gathered
- **Key insight:** Language itself is what makes humanity human. The invention of writing = the breath of God entering the clay.

## 5. Synthesis — How This Shapes GENESYS

### The Title: GENESYS
The name works on multiple levels:
- Genesis (beginning, creation)
- System (the game's mechanical depth)
- Sys (computer/AI — EVE as artificial intelligence)

### Adam as Player Character
The player isn't playing "a man named Adam." They're playing **humanity itself**. The Corporeal One. A body without direction until EVE (the drive to organize, to build, to create culture) gives them purpose.

- **Start as a corpse-like thing** — no abilities, no language, no tools. A dustling.
- **The breath** = EVE's activation. She IS the breath of life — the organizing intelligence.
- **Redness/blood motif** — Adam's color palette should incorporate reds and earth tones. His health IS his blood (the seat of life). When he's hurt, it's not just HP — the life is literally leaving.

### EVE as Civilization Itself
Eve isn't just a companion. She's the **tent village**. She's the drive to cluster, to cooperate, to build.

- **EVE's growth = civilization's growth.** As you build structures, EVE gets smarter. She IS the collective intelligence of your settlement.
- **EVE as language.** She starts speaking broken fragments, just like the Hebrew etymology — early humans clustering, developing shared language. Her fluency GROWS with the civilization.
- **EVE translating native languages** maps perfectly to the historical reality: the alphabet was the fire that let different peoples communicate. EVE is that fire.
- **"Tent village" as literal gameplay** — the first thing you build is a shelter from leaves (already in the GDD). This IS Eve manifesting. The shelter is the first tent village.

### Eden as Endgame
Eden isn't the garden you START in. Eden is what comes AFTER. It's the state of **delight that emerges from free exchange** — a thriving civilization. The whole game is building toward Eden.

- **The garden is "just prior to Eden"** — the wilderness IS the pre-Eden state
- **Eden = your completed civilization** — the "luxury" that comes from free exchange of goods, services, and information
- **Four rivers = four major biomes/zones?** Each one a different challenge, a different "center of civilization" to establish

### The Mecha Dragon as Anti-Language
If EVE is language/cooperation/civilization, the Dragon is the anti-thesis:
- **Isolation** — it separates, it divides
- **Silence** — root דמם (dmm), the stillness BEFORE language, before complexity
- **The Dragon wants to return everything to dust** — to the pre-Adam state, the corpse without breath
- **Its forces are mechanical, cold** — not alive, not symbiotic, not clustered. Individual units following programming, not cooperating organically.

### Movement as Breath
The movement system IS the breath metaphor:
- **Start still** (דמם, damam — to be still). Basic walk, basic jump. A corpse learning to move.
- **Each new ability = another breath.** Dash, wall jump, grapple — each one is the body becoming more alive.
- **Chaining abilities = fluency.** Just as language becomes fluent through practice, movement becomes fluent through mastery. The combo system IS speaking.
- **"The first Adam became a living being; the last Adam became a life-giving spirit."** Endgame Adam doesn't just HAVE movement — he IS movement. He's become the life-giving spirit.

### Native Language Cipher Font
Using FontStashSharp, we could literally render native dialogue in a **constructed cipher font** — same letters but visually alien. As EVE learns the language, the font gradually morphs from cipher → readable. The player literally watches language being decoded in real-time.

### Blood as System
Adam = Blood Man. Blood = the seat of life, but also "isolated from the world at large" (blood circulates INSIDE, separated from the outside). When blood is shed, the isolation is broken — life escapes.

- **Health isn't abstract.** It's Adam's blood. Visual: as HP drops, Adam's red color fades. He's becoming dust again.
- **Healing = re-sealing.** Bandages, food, rest at shelter — restoring the boundary between inside and outside.
- **"When a river turns to blood, it becomes isolated from the greater hydrological cycle."** Water levels or river mechanics could play on this — contaminated water = death, clean water = life.
