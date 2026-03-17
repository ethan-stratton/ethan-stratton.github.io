# Game Design Document — [Working Title TBD]

## Overview
2D side-scrolling action RPG with civilization building. Fight through levels, settle the land, build a world from nothing.

**Core Loop:** Clear hostile territory (action) → Settle and build (strategy) → Unlock new areas and abilities → Repeat

**Platform:** PC first
**Perspective:** 2D side-scrolling (combat/exploration), top-down or menu-based (building/management)
**Engine:** TBD — MonoGame/FNA (Terraria's lineage), Godot, or other

---

## Gameplay Pillars

### 1. Combat (Tactical)
- Side-scrolling action. Movement must feel GREAT.
- Weapons with distinct movesets — not just damage numbers, different *feel*
- Bosses with learnable patterns (Souls-like)
- New movement options unlock over time (metroidvania progression)
- Combinatorial systems: weapon + modifier combinations (DSS card / Harmony of Dissonance style)

### 2. Building (Logistical)
- Between combat levels, you settle and build on cleared land
- Place structures, assign NPCs to roles, manage resources
- ActRaiser-inspired: your civilization grows based on your decisions
- Building upgrades unlock new weapons, abilities, and story content

### 3. Relationships (Diplomatic)
- NPCs with real stories — not just quest dispensers
- Genesis archetypes: Cain/Abel dynamics, dragon worshippers, prophets
- Choices in how you handle conflicts (Cain kills Abel — what do you do?)
- EVE relationship deepens over time — she's your primary relationship

### 4. Exploration (Strategic)
- World map showing cleared vs hostile territory
- Choose which direction to expand
- Some replayability in levels — different routes, hidden areas
- Discovery is rewarded: lore items, crafting components, movement upgrades

### 5. Mystery (Atmospheric)
- **Preserve a sense of mystery at all times.** The player should never feel like they fully understand the world.
- Lore is discovered, not explained. Environmental storytelling over exposition dumps.
- The planet itself should feel unknowable — strange phenomena, unexplained ruins, things that don't add up.
- NPCs have incomplete knowledge. Nobody has the full picture — including the player.
- Resist the urge to over-explain. Questions are more compelling than answers.
- Inspirations: Dark Souls lore delivery, Shadow of the Colossus atmosphere, the Voynich manuscript ethos — forbidden knowledge that can't be fully decoded.
- **"What we fear is what we cannot see clearly."** The mecha dragon should be mysterious and somewhat indiscernible — never fully revealed, never fully understood.
- Focus on mystery-horror elements. Study what makes a great horror level: pacing, dread, the unseen. Reference: [GMTK — What Makes a Good Horror Level](https://www.youtube.com/watch?v=GJlhjhr_VN4)

---

## The EVE System (AI Companion)
- EVE assists with all four pillars based on player need
- Combat: enemy analysis, weakness hints
- Building: layout suggestions, resource optimization
- Relationships: NPC mood/need indicators, dialogue hints
- Exploration: map reveals, hidden area hints
- Player can choose how much help to accept (difficulty/immersion slider)

---

## Weapons & Equipment

### Starting Weapons
- **Sling & Stones** — First ranged weapon. Fast projectile speed with arc falloff; damage decreases at range. Found/crafted early.
- **Stick** — Found on the ground at game start. Basic melee. Breakable.

### Weapon System
- Carry up to 3 weapons at a time. Swap between them freely.
- Store excess weapons (in shelter/camp inventory once built).
- Melee weapons found along the way have **durability** — they break at certain stages of wear.
- Progression path: Stick → Axe (crafted) → random melee drops → late-game crafted weapons
- Ranged progression: Sling & Stones → Bow & Arrows → Gun & Bullets

### Crafting Progression (Early Game)
1. **Shelter** — Craft using tree leaves. EVE analyzes which leaves have structural integrity (first quest/tutorial for EVE's examine ability).
2. **Axe** — Crafted for melee combat AND tree chopping (dual-purpose tools).
3. **Bow & Arrows** — Mid-game ranged upgrade.
4. **Gun & Bullets** — Late-game ranged. Requires more advanced materials.
5. **Body Armor** — Crafted from animal corpses and materials. Multiple tiers. EVE examines animal remains to determine what's usable.

---

## EVE as Knowledge Engine

EVE isn't just a companion — she's your scientific instrument.

### Examine System
- Point EVE at anything in the world: trees, rocks, animals, corpses, ruins, NPCs
- She analyzes and tells you what it can be used for (or can't)
- Not required — examining is always optional but rewarded
- Sometimes examining reveals nothing useful. That's fine. Not every tree is special.

### Language & Translation
- Natives speak their own language. Early game: you can't understand them fully.
- With enough interaction and exposure, EVE learns to **translate the native language**.
- Progression: broken fragments → partial understanding → full translation
- EVE can eventually **talk to natives on your behalf** and relay summaries of their questlines and what they wanted to discuss.

### EVE as Delegate (Player Agency)
- **Story-driven players:** Talk to every NPC yourself, examine everything, soak in the world.
- **Action-driven players:** Send EVE to handle NPC conversations, get quest summaries, skip to the action.
- Both approaches are valid. Neither is punished.
- EVE's summaries are accurate but lose flavor — you miss the Native's poetry, the emotional beats. Incentive to do it yourself without forcing it.

---

## Core Design Principle: No Forced Pauses

**The player chooses when to engage.** Gameplay should never stop and force interaction.

- Find a cool tree? Examine it with EVE or walk past it. Your call.
- NPC wants to talk? Listen yourself, send EVE, or ignore them entirely.
- Examining/interacting is rewarded but never strictly necessary for progression.
- Sometimes examining something yields nothing. The world isn't a theme park where everything is meaningful — that unpredictability makes the discoveries feel real.
- Cutscenes and forced stops should be extremely rare and earned (major story beats only).

---

## Crafting / Combination System
- Inspired by: DSS cards (Circle of the Moon), spell books (Harmony of Dissonance), Plague Knight potions (Shovel Knight)
- Two-axis combination: Base item + Modifier = unique result
- Discovery-driven — finding new combinations is part of the fun
- Thematically tied to creation: Adam is learning to create, mirroring the divine act
- No motion inputs. Clean, accessible menus.

---

## Movement & Controls
- Movement must feel good FIRST. Responsive, satisfying, precise.
- Unlockable movement abilities (dash, wall jump, grapple, etc.)
- **Control layout:** WASD = pure directional stick, JKL; = action buttons (attack, jump, special, super)
- **Motion inputs** for advanced moves — fighting game DNA:
  - ↑↓↙→ + Attack = Dash attack
  - ↓↑ + Jump = Super jump (damages, goes slightly forward)
  - Jump × 2 fast = Backflip
  - Slide kick × 2 = Jumping slide kick
  - Attack (hold) + direction = Spinning weapon attack
  - Supers on dedicated button(s) — TBD
- Inspired by: Castlevania (Richter's uppercut, slide), Megaman, fighting game inputs
- Primarily melee-focused combat

---

## Progression
1. Start with nothing — improvised weapons, basic movement
2. Clear first area → settle → build basic structures
3. Structures unlock: better weapons, crafting options, NPC roles
4. New movement abilities open new level paths
5. Civilization growth unlocks story beats
6. Late game: full civilization, powerful loadout, Dragon confrontation

---

## Player Types (balanced, not heavy-handed)

| Type | Primary Draw | EVE Support |
|------|-------------|-------------|
| Tactical | Combat mastery, boss patterns | Enemy analysis, weakness hints |
| Logistical | Building optimization, resource management | Layout suggestions, efficiency tips |
| Diplomatic | NPC stories, moral choices | Relationship tracking, dialogue context |
| Strategic | World map planning, expansion choices | Scouting, risk assessment |

Each type can complete the game. EVE provides scaffolding for weak areas so no one hits a wall.

---

## Art Direction
- 2D pixel art or high-res 2D (TBD)
- Influences: Castlevania SotN, Terraria, Hyper Light Drifter
- Alien planet aesthetic — not Earth. Strange flora, unfamiliar sky.
- Civilization areas should feel warm and human vs hostile wilderness
- The Dragon and its forces: mechanical, cold, cybernetic

### Style Pillars (ref: "Modern Games NEED Style")
1. **Kinetic Beauty** — Every movement ability should look like art. The combo system is the visual signature. Design for GIF-ability: screen shake, hit-freeze frames, color bursts on DSS activations, speed lines during blade dashes.
2. **Tonal Whiplash (Controlled)** — The shift between frenetic action and contemplative civilization-building IS the style. Embrace the contrast.
3. **Strategic Abstraction** — Pixel art that suggests more than it shows. Horror through implication. Lore through fragments. The Mecha Dragon is scarier when you can't fully see it. Keep sprites expressive but abstracted — let the player's imagination do the work (Crow Country principle).
4. **Personal Mythology** — The Genesis retelling filtered through Ethan's specific worldview. Sincere, weird, and unforgettable. The Suda 51 approach: inject yourself, don't sand down the weird edges. The genre mashup (ActRaiser + Castlevania + Dark Souls + fighting game combos) IS the style.
5. **Systemic Depth as Style** — The DSS card system, the civ-building consequences, the Metroidvania progression — mechanical depth IS a stylistic statement that says "this game respects you."

### Style as Marketing
- The genre collision is the hook: "Did you see that game where you do stylish combo parkour and then build a civilization between levels?"
- Something niche is way better than something forgotten. Target the overlap: Dark Souls community + Metroidvania fans + ActRaiser nostalgia.
- There is no safety in playing too safe. The most dangerous thing is being forgettable.
- Don't simplify the combo system to be "more accessible" — the depth IS the appeal.
- Don't soften the mystery/horror — the Dark Souls approach to lore works because it respects the player's intelligence.

---

## Scope Control
**Prototype (Weeks 1-2):** Movement + one combat level + one building phase. Gray boxes. Is it fun?
**Vertical slice (Month 1):** One complete loop — fight level, build, unlock, fight next level. Basic art.
**Alpha (Month 2):** 3-4 levels, building system, core NPCs, EVE system functional.

---

## Open Decisions
- [ ] Engine choice (MonoGame/FNA vs Godot vs other)
- [ ] Art style (pixel art vs high-res 2D)
- [ ] Working title
- [ ] Save system design
- [ ] Music direction
- [ ] How many levels total
- [ ] Multiple endings?
