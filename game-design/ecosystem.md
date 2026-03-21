# Ecosystem Design — Genesis

## Core Principle
Every creature exists in a food web. Adding a new mob to a trophic level automatically establishes its relationships up and down the chain. Creatures don't just fight the player — they fight each other, flee from predators, hunt prey, and compete for territory.

## Trophic Levels

### Level 0: Flora / Substrate
Non-mobile. Provides resources or cover.
- **Thornbacks** — stationary, blocks paths, damages on touch
- **Coral structures** — platforms, environmental
- **Crystal formations** — resources, light refraction

### Level 1: Decomposers / Grazers
Feed on flora/substrate. Generally passive toward player unless provoked.
- **Crawlers** — feed on dead organic matter and plant growth
- **Grazers** — large herbivores, neutral, eat Thornback growth (natural pest control)
- **⚠️ SUBVERSION: Crawlers** look like decomposers but are actually **opportunistic predators** in swarms — they'll overwhelm weakened creatures of ANY tier

### Level 2: Small Predators
Hunt Level 1. Flee from Level 3+. Aggressive toward player.
- **Wingbeaters** — aerial dive-bombers, hunt Crawlers from above
- **Burrowers** — ambush predators, hunt Crawlers/Grazers from below
- **⚠️ SUBVERSION: Burrowers** are serpent-coded (Genesis 3:1) — they're the smartest Level 2. They don't just ambush prey, they **herd** Crawlers into traps

### Level 3: Apex Predators / Territorial
Hunt Level 1-2. Avoid Level 4. Major threats to player.
- **Nephilim Spawn** — humanoid, territorial. Hunts everything in its zone.
- **Floodwalker** — absorbs anything it contacts. Dissolves Level 1-2 creatures.
- **⚠️ SUBVERSION: Floodwalker** isn't a predator — it's the planet's **immune system**. It dissolves "foreign" matter (including the player). But it also dissolves corruption. It's your enemy AND your ally depending on context.

### Level 4: Mythic / Ecosystem Shapers
Not part of the food chain — they CHANGE the food chain.
- **Babel Hive** — builds towers, spawns Level 1-2 minions. Territory war with player's settlement.
- **Mecha Dragon** — corrupts creatures, converting them to cybernetic versions
- **The Watcher** — observes only. Affects nothing... that you can see.

---

## Interaction Matrix

When two creatures from different trophic levels enter the same area:

| Predator (higher) | Prey (lower) | Interaction |
|---|---|---|
| Wingbeater | Crawler | Wingbeater dive-bombs Crawlers. Crawlers scatter. |
| Wingbeater | Grazer | Wingbeater ignores Grazer (too large). |
| Burrower | Crawler | Burrower surfaces under Crawler pack, kills 2-3, retreats. |
| Burrower | Grazer | Burrower stalks Grazer, attacks young/weakened ones only. |
| Nephilim Spawn | Wingbeater | Swats Wingbeaters out of the air. |
| Nephilim Spawn | Burrower | Stomps the ground to force Burrowers to surface, then kills. |
| Nephilim Spawn | Crawler | Ignores (too small). Crawlers swarm its feet harmlessly. |
| Floodwalker | ANY Level 1-2 | Absorbs on contact. Grows larger. |
| Crawler Swarm (6+) | Weakened ANY | Swarm overwhelms weakened creatures of any tier. Even a hurt Nephilim. |

### Same-Level Competition
| Creature A | Creature B | Interaction |
|---|---|---|
| Wingbeater | Wingbeater | Territorial. Chase each other away from nesting zones. |
| Burrower | Burrower | Cooperative — share tunnel networks. |
| Nephilim | Nephilim | Extremely territorial. Fight on sight. |
| Grazer | Grazer | Herd behavior. Group up for protection. |

---

## Player Ecosystem Manipulation

The gameplay hook: use your knowledge of the ecosystem to solve problems without fighting.

### Examples (prototypeable in gyms)

**Crawler Clearing:**
- Problem: Room full of Crawlers blocking path
- Brute force: Kill them all (hard in swarms)
- Ecology: Lure a Wingbeater in (open a vent/window). Wingbeater hunts the Crawlers. Walk through.
- Advanced: Build near Grazer herd. Grazers eat Thornback growth. No Thornbacks = no Crawler habitat. Crawlers leave permanently.

**Wingbeater Territory:**
- Problem: Wingbeaters dive-bombing you in open area
- Brute force: Shoot them down (ranged ammo expensive)
- Ecology: Crawlers on the ground attract Wingbeaters downward. Lure Crawlers into the open, Wingbeaters dive for them instead of you. Slip past.

**Nephilim Gate:**
- Problem: Nephilim Spawn blocking the only path
- Brute force: Souls-like boss fight
- Ecology: Lure a Floodwalker toward the Nephilim's territory. Floodwalker absorbs the Nephilim's Crawler food supply. Nephilim weakens from starvation over time (return later, it's now at 50% HP).
- Knowledge: Scan reveals Nephilim are partially corrupted. They avoid the Crystal Reach's resonance frequency. Find a crystal and ring it near the gate. Nephilim retreats.

**Floodwalker Bypass:**
- Problem: Floodwalker blocking a corridor, absorbing everything
- Brute force: Massive damage before it absorbs you
- Ecology: Feed it. Let Crawlers run into it. It grows, but it also gets SLOW. Once it's bloated enough, it can't chase you. Walk past.
- Knowledge: Scan reveals the Floodwalker avoids certain planetary minerals. Coat yourself (crafting) and it ignores you.

---

## Implementation: Trophic Level System

### Data Structure (per creature type)
```
TrophicLevel: int (0-4)
PreyLevels: int[] (which levels it hunts)
PredatorResponse: enum { Flee, Fight, Ignore, Absorb }
SameLevelBehavior: enum { Territorial, Cooperative, Herd, Ignore }
AggroRange: float (how far it detects prey/threats)
PreyPreference: string[] (specific types preferred, e.g. "crawler" over "grazer")
```

### Adding a New Creature
1. Assign trophic level
2. Set prey/predator responses
3. Drop it in the world

The system handles the rest:
- Creatures at lower trophic levels within detection range → hunt behavior activates
- Creatures at higher trophic levels within detection range → predator response activates
- Same-level creatures → same-level behavior activates
- Player → treated as Level 2-3 depending on gear/progression

### World-State Consequences
| Player Action | Ecosystem Response |
|---|---|
| Kill many Grazers | Crawler population explodes (no predator) |
| Kill many Crawlers | Wingbeaters starve, migrate away |
| Build near Grazer herd | Grazers eat Thornback growth → fewer Crawlers near settlement |
| Neglect a zone | Natural succession: Crawlers → Wingbeaters move in → Nephilim claims territory |
| Corruption spreads | Creatures get cybernetic upgrades. Trophic relationships shift. |

---

## Subversions (Keep the Ecosystem Surprising)

The food web isn't perfectly predictable. These subversions reward deep scanning.

1. **Crawler Swarm Override** — Crawlers at Level 1 individually, but 6+ in proximity become a Level 3 threat. They'll overwhelm ANYTHING weakened. Scan reveals: "EVE: Individually harmless. Collectively... recalculating threat level."

2. **Burrower Intelligence** — Level 2 predator but behaves like Level 3. Herds prey, sets traps, remembers player patterns. Scan reveals increasing intelligence with each scan. Fourth scan: "EVE: This creature adapted to your last three approaches. It's... learning."

3. **Floodwalker Symbiosis** — Absorbs Level 1-2 creatures BUT releases nutrients that cause Thornback growth. Killing a Floodwalker starves Thornbacks. Letting it live feeds them. The "decomposer" is actually the ecosystem's fertilizer.

4. **Corrupted Trophic Inversion** — In Ashlands, corruption inverts the food chain. Crawlers hunt Wingbeaters. Grazers become aggressive apex predators. Scanning reveals the corruption didn't make them evil — it made them desperate.

5. **Babel Hive Misidentification** — Looks like Level 4 (ecosystem shaper). Actually Level 0 — it's a PLANT. The towers are fruiting bodies. The "minions" are pollinators. The entire war between player and Babel Hive is a misunderstanding. EVE scan level 4 reveals: "EVE: We've been destroying a garden."

---

## Open Questions
- [ ] How do creatures detect trophic relationships at runtime? (simple: compare TrophicLevel ints)
- [ ] Population limits per zone? (prevent infinite cascading)
- [ ] Do creatures respawn naturally or only from spawn points?
- [ ] How does day/night shift trophic behaviors? (nocturnal predators?)
- [ ] Can the player domesticate Level 1-2 creatures for settlement defense?
- [ ] Settlement "ecology" — do NPCs farm Grazers? Breed Crawlers for bait?
