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

---

## Map Philosophy: History First, Geography Second

Don't draw the map and then justify it. Know what happened, then let geography reflect it.

### Questions That Generate the Map
- **Where did the ship crash?** That's your starting zone (Eden Reach). The crash itself scarred the land — a crater, scattered debris, the ship's leaking energy creating an oasis of familiarity in alien territory.
- **Where were the natives before Adam?** Their settlements cluster around water/resources that the planet naturally provides. Their ruins tell you where they USED to live vs where they live now. What pushed them?
- **Where does the corruption come from?** If it radiates from a source (the Dragon's domain?), the map should show concentric rings of degradation. Eden Reach is far from the source — that's why it's still livable. The Ashlands are close. The Void Rift is ground zero.
- **What was here before the corruption?** The ruins. The pre-native civilization. Their infrastructure shapes the terrain — ancient roads are now canyons, their towers are now mountains, their cities are now cave systems. Level 6 worldbuilding of an extinct civilization that literally became the geography.
- **Where does the Dragon live?** Not a single lair. An AXIS that the whole map orients around. Everything flows toward or away from it. The natives' settlements are all positioned to be as far from it as possible. Trade routes detour around it. The map itself tells you what everyone fears.

---

## Rule of Cool Inside Constraints

Cool ideas earn their place when tied to the core constraint and history. One sentence of justification turns Level 2 (rule of cool) into Level 4-5 (functional power + deep culture).

### Examples
- **"City carved into the bones of a god"** → A native settlement built inside the petrified remains of a massive creature. Why? Because the creature's body *resists the corruption*. The bone-material is the only thing that doesn't degrade. That's why they live there.
- **Babel Hive enemy** → It builds towers. Why? Because it's the planet's immune response to the Dragon's corruption — trying to build barriers. But it's mindless, so it attacks everything indiscriminately. The creature that should be your ally is your enemy because you can't communicate with it. *Until EVE learns to.*
- **The Floodwalker absorbing enemies** → It's the planet's waste disposal. It dissolves corruption. But Adam registers as foreign too. The planet can't tell the difference between Adam and the Dragon's influence. The world's immune system is attacking you because you don't belong. *Yet.*
- **The Watcher** → It's observing because something about Adam is unprecedented. The planet has never seen a being that LEARNS to work with it instead of against it. The Watcher is waiting to see what Adam becomes.
- **Every cool idea gets one question:** "Why does this exist given the planet resists technology?" If you can answer it, it stays and gets deeper. If you can't, either find the answer or cut it.

---

## Biome Design: Surface Identity From Gameplay

Each biome should make you PLAY differently. The visual identity follows the mechanical identity. A region isn't just a color palette — it's a different verb emphasis.

| Biome | Gameplay Feel | Why It Looks That Way | Mechanical Identity |
|---|---|---|---|
| **Eden Reach** | Tutorial comfort zone. Open, horizontal. | Crash site energy creates Earth-like growth. Familiar. | Basic platforming, all tiles work normally |
| **Petrified Forest** | Vertical, cramped, ambush-heavy. | Something flash-froze the ecosystem. Burrowers hide in cracked stone. | Breakable floors, hidden enemies, tight corridors |
| **Ashlands** | Hot, punishing, sprint-based. | Near the corruption source. Ground damages you over time. | Damage tiles everywhere, speed tiles for safe paths, time pressure |
| **Coral Heights** | Aerial, bouncy, momentum-based. | Organic structures grew upward to escape ground-level corruption. | Float tiles, rope/wall climbing, Wingbeater territory |
| **The Depths** | Slow, horror, resource-scarce. | Underground ruins of the pre-native civilization. | Low visibility, limited ammo, Floodwalker territory |
| **Void Rift** | Everything breaks the rules. | Ground zero. The constraint itself is failing here. | Tech works better here (guns don't degrade), but enemies are vastly stronger. Double-edged. |

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

---

## The Core Constraint: "The Planet Resists Technology"

This is the ONE rule that cascades into everything — combat, society, architecture, narrative.

The planet's atmosphere, magnetic field, or some unknowable property corrodes complex machinery. Advanced technology degrades. EVE herself is degrading. The ship is destroyed. This single constraint produces:

### Combat Balance
Guns work but are unreliable and expensive to maintain. Primitive weapons — stick, axe, sword, bow — are the most dependable. This is why the game is melee-focused. Ranged weapons are powerful but costly. Each tier of technology represents Adam and EVE figuring out how to work WITH the planet's resistance, not against it.

- Sling works because it's rocks.
- Bow works because it's organic.
- Gun works but it *costs* you — durability, materials, maintenance.
- Late-game weapons are hybrids of Federation knowledge and planetary materials.

### Crafting Motivation
You can't replicate Federation tech. You have to build WITH the planet — using its materials, its biology, its rules. Crafting isn't just "combine items." It's Adam learning the planet's language of materials. EVE's examine system is literally how you learn what the planet allows.

### Why the Dragon is Terrifying
The Dragon is cybernetic. Mechanical. It shouldn't be able to exist here — but it does. That breaks the one rule. How? That's another mystery.

### Ties to the Theme
The Fall stripped Adam of technology. The planet's resistance ensures he CAN'T go back to what he was. He has to become something new. The constraint IS the salvation.

### Narrative Stakes
Why you can't just radio for help. Why the Federation quarantined the planet. Why rebuilding is hard. One rule, infinite consequences.

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
