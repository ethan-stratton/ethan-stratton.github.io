# Creature Design — GENESYS: Admin & Eve

## Design Philosophy
This is an alien planet with its own ecosystem. Creatures aren't Earth animals with Bible names — they're alien life that *parallels* Genesis thematically. The echoes between this planet and Earth mythology are part of the mystery. Why do the patterns repeat?

Admin names these creatures with EVE's help. The act of naming and understanding is itself a Genesis parallel (Genesis 2:19-20).

## Tier 1: Common Wildlife (world population)

### Crawlers
- **Inspiration:** "Creeping things" (Genesis 1:24)
- **Behavior:** Small ground insects, move in packs, scatter when hit
- **Combat:** Low individual damage, dangerous in groups. Melee AoE effective. Ranged inefficient.
- **Biome:** Everywhere — the basic enemy
- **Prototype:** Insect swarm around trees (already implemented)

### Thornbacks
- **Inspiration:** "Thorns and thistles" (Genesis 3:18, the curse on the ground)
- **Behavior:** Defensive, spiny, don't chase. They block paths and key areas.
- **Combat:** Touch = damage. Must be destroyed to pass or found alternate route. Tanky.
- **Biome:** Overgrown areas, blocking paths between zones

### Wingbeaters
- **Inspiration:** "Fowl of the air" (Genesis 1:20)
- **Behavior:** Flying patrol pattern, dive-bomb when player is directly below
- **Combat:** Fast dive attack with telegraph (shadow/pause). Ranged weapons effective. Melee requires timing.
- **Biome:** Open areas, canopy levels, sky zones

### Burrowers
- **Inspiration:** "The serpent" (Genesis 3:1)
- **Behavior:** Hidden underground. Pop up when player walks over trigger zone. Quick strike then retreat back underground.
- **Combat:** Surprise damage. EVE examine can reveal their hiding spots. Timing-based.
- **Biome:** Desert, dirt, soft ground areas

### Grazers
- **Inspiration:** "Beasts of the field" (Genesis 2:20)
- **Behavior:** Neutral unless attacked. Large, slow, tanky. Docile but devastating if provoked.
- **Combat:** Huge HP pool, powerful charge attack. Best avoided early game. Drops valuable materials.
- **Biome:** Plains near building zones. Coexistence is optimal.

## Tier 2: Territorial / Mini-Boss

### Nephilim Spawn
- **Inspiration:** Nephilim, "mighty men of old" (Genesis 6:4)
- **Behavior:** Large humanoid. Patrols territory with complex attack patterns.
- **Combat:** Souls-like learnable patterns. Telegraphed but punishing.
- **Role:** Zone gatekeepers. Clearing one opens new territory.

### Floodwalker
- **Inspiration:** The Flood (Genesis 7)
- **Behavior:** Amorphous water/fluid creature. Absorbs smaller enemies it contacts. Grows over time.
- **Combat:** Must be fought before it absorbs too many. Gets harder the longer you ignore it.
- **Ties to:** Spawning Grounds mechanic (areas get worse if neglected)

### Babel Hive
- **Inspiration:** Tower of Babel (Genesis 11)
- **Behavior:** Colony organism that builds tower-like structures. Towers spawn more enemies.
- **Combat:** Destroy the tower (the "babel") to stop spawns. Tower gets taller/stronger over time.
- **Ties to:** Building sim — your structures vs their structures. Territory war.

## Tier 3: Mythic / Story (endgame)

### Mecha Dragon
- **Inspiration:** Leviathan / The Serpent
- **Role:** The overarching mystery threat. Never fully understood.
- **Notes:** See GDD Mystery pillar. Keep indiscernible. Study horror pacing.

### The Watcher
- **Inspiration:** "Sons of God" (Genesis 6:2), Watchers from Book of Enoch
- **Behavior:** Observes. Doesn't attack. Appears at edges of vision. Vanishes when approached.
- **Role:** Deeply unsettling presence. What is it watching? Why?
- **Ties to:** Roaming super boss idea? Or something stranger?

### The Voice
- **Inspiration:** God walking in the garden (Genesis 3:8)
- **Role:** Not an enemy. An environmental phenomenon. Sound without source. Ground trembles.
- **Notes:** Could be the planet itself. Could be something in orbit. Don't explain it.

## Narrative Thread
Why does this alien planet's ecosystem mirror Earth's creation mythology? Possibilities (never confirmed):
- Universal laws of creation produce universal patterns
- The planet was seeded by the same source
- Admin's perception is filtering alien reality through human myth
- EVE's translation algorithms impose familiar frameworks
- Something deeper — the mystery IS the game

## Implementation Priority
1. Crawlers (done — insect swarm)
2. Wingbeaters (flying dive-bomber)
3. Thornbacks (stationary blocker)
4. Burrowers (ambush)
5. Grazers (neutral wildlife)
6. Tier 2+ enemies come with level/story progression
