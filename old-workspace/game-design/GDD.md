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

---

## The EVE System (AI Companion)
- EVE assists with all four pillars based on player need
- Combat: enemy analysis, weakness hints
- Building: layout suggestions, resource optimization
- Relationships: NPC mood/need indicators, dialogue hints
- Exploration: map reveals, hidden area hints
- Player can choose how much help to accept (difficulty/immersion slider)

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
- No motion inputs for abilities — button combinations or equipment-based
- Inspired by: Castlevania movement + modern indie responsiveness

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
