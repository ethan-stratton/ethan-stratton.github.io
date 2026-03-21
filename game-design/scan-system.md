# EVE Scan System — Design Document

## Core Identity
EVE's scan is the universal "analyze/interact with knowledge" button. It is NOT a combat tool — it's a scientific instrument, a translator, a puzzle solver, and your window into the planet's secrets.

**Button: L** (left hand, combat side — accessible without moving fingers off WASD)

---

## Foundational Rules

### 1. No Scanning Live Hostile Enemies
If an enemy is aggro'd on you, L does nothing on them. You scan:
- **Corpses** after kills
- **Sleeping/passive creatures** in the wild
- **Caged/trapped creatures** (in labs, behind barriers)
- **Creatures you've tranquilized/frozen/put to sleep**
- **Creatures you've lured into traps**

This creates gameplay loops:
- **Trapping** — build or find traps to immobilize enemies for scanning
- **Camouflage** — use native materials to mask your scent/presence
- **Sleep tools** — later-game abilities/items that put creatures to sleep
- **Observation** — watch from hiding before engaging

### 2. Everything Is Scannable (~10 entries each)
Not 3 scans per enemy. TEN per everything. Each scan reveals a deeper layer.

**Creatures (10 scans):**
1. Species identification + basic description
2. Diet and habitat
3. Sensory capabilities (sight, hearing, smell ranges)
4. Social behavior (solitary, pack, herd, territorial)
5. Reproductive cycle / lifecycle stage
6. Trophic relationships (what it eats, what eats it)
7. Stress responses (what makes it flee, fight, freeze)
8. Anatomical weak points (combat relevance)
9. Material composition (what you can harvest from corpse)
10. Ecological role + EVE speculation ("I think this species was engineered...")

**Flora/Substrate (10 scans):**
1. Basic identification
2. Growth conditions (light, water, soil)
3. Chemical properties (toxic? medicinal? flammable?)
4. Structural integrity (can you build with it?)
5. Interactions with fauna (who eats it, who avoids it)
6. Root system / underground connections
7. Response to corruption (resistant? accelerant? immune?)
8. Seasonal/temporal behavior (grows at night? blooms in heat?)
9. Crafting potential (EVE suggests recipes)
10. Planetary function ("This is part of the planet's respiratory system")

**Ancient Tech/Ruins (10 scans):**
1. Material identification
2. Age estimate
3. Functional state (broken, dormant, active)
4. Power source
5. Original purpose (partial — EVE guesses)
6. Connection to other scanned tech (network map builds)
7. Interaction method (how to activate/deactivate)
8. Hazard assessment
9. Cultural context (who built this and why)
10. Hidden function ("There's a second layer to this mechanism...")

**Items/Weapons (10 scans):**
1. Material composition
2. Current durability / condition
3. Optimal usage (slash vs crush vs throw)
4. Maintenance requirements
5. Enhancement potential (what can be added/modified)
6. Origin (crafted? found? alien?)
7. Comparison to current loadout
8. Elemental properties / resistances
9. Best enemy matchup ("Effective against chitinous armor")
10. Lore ("This blade was forged by the same alloy as the ruins in Sector 4")

**Environment (10 scans):**
1. Geological composition
2. Stability assessment (safe to stand on? about to collapse?)
3. Water/resource presence
4. Hidden passages or breakable surfaces
5. Corruption level
6. Historical context (what was this before?)
7. Wildlife activity (tracks, nests, markings)
8. Atmospheric data (oxygen, temperature, pressure)
9. Strategic value for settlement
10. Anomalies ("The magnetic field here is... wrong")

**Natives/NPCs (special — see Communication section):**

### 3. Scan Depth ≠ Repeat Button Presses
You don't scan the same corpse 10 times. Scan depth increases through:
- **Different contexts**: Scan a Crawler corpse = entries 1-3. Scan a Crawler nest = entries 4-5. Scan a Crawler during feeding = entry 6. Scan a Crawler fleeing a predator = entry 7.
- **Different states**: Sleeping vs dead vs trapped vs corrupted versions each reveal different entries
- **Progression**: Some entries require EVE upgrades. Early game she can identify species. Mid-game she reads chemical composition. Late game she detects planetary-level functions.
- **Combinations**: Scan a Crawler next to a Thornback = reveals their symbiotic relationship (entry not available scanning either alone)
- **Time**: Some scans require observing behavior over 10+ seconds. EVE tracks what she sees.

### 4. Combat Knowledge Comes From Combat
Scanning gives STRATEGIC knowledge (ecology, materials, lore).
Combat gives TACTICAL knowledge (attack patterns, telegraphs, timing).

| Source | What You Learn | Example |
|---|---|---|
| Kill 3 Crawlers | Attack pattern visibility | Telegraph appears before lunge |
| Kill 5 Crawlers | Weak point highlight | Dorsal segment glows on HUD |
| Kill 10 Crawlers | Damage bonus | +15% damage to type |
| Scan Crawler corpse | Biology, diet | "Feeds on dead organic matter" |
| Scan Crawler nest | Social behavior | "Swarms when colony > 6" |
| Scan Crawler near Bird | Trophic relationship | "Primary prey of Wingbeaters" |
| Scan corrupted Crawler | Corruption data | "Mutation increases aggression 300%" |

### 5. EVE Grows With You
EVE's scanning capability improves over the game:
- **Early**: Basic identification. Short voice lines. Limited depth.
- **Mid**: Chemical analysis, behavioral prediction, partial translations.
- **Late**: Planetary-scale understanding, full native communication, corruption analysis.
- **Endgame**: EVE understands the planet better than anyone. She sees connections you don't.

EVE upgrade sources: scanning milestones, ancient tech interfacing, native knowledge gifts.

---

## Native Communication

### You NEVER Learn Their Language
Admin never speaks the native tongue. EVE translates, but imperfectly at first.

**Communication progression:**
1. **Gestures only** — Point, wave, show items. Natives respond with body language.
2. **Pictograms** — Draw simple images (menu UI). Natives understand basic concepts.
3. **EVE partial translation** — EVE catches fragments. "Something about... water? And danger?"
4. **EVE full translation** — EVE relays full meaning but in her own words. You miss nuance.
5. **EVE + gesture hybrid** — You gesture, EVE supplements. Natives appreciate the effort. Better quest rewards.

### Fetch Quest Subversion
Natives don't give you quest markers. They:
- Point in a direction
- Show you an item/drawing of what they need
- Perform a gesture you have to interpret
- Sometimes they're wrong about what they need (they think they need X, but the real solution is Y that you discover through scanning)

You have to FIGURE OUT what they want. Bring the wrong item? They react — disappointment, confusion, sometimes amusement. Bring the right one? Genuine gratitude that builds relationship.

Scan the native (with permission / from observation) to learn:
- What they're looking at (gaze direction)
- Emotional state (body language)
- Health status
- Cultural role in their group
- What they're carrying
- Relationship to other natives you've met

---

## EVE Alert System (Combat Integration)

EVE doesn't scan in combat — but she WARNS you.

### Passive Combat Alerts
Based on accumulated scan knowledge, EVE provides real-time warnings:
- **"Above you!"** — Wingbeater dive-bomb incoming (requires Wingbeater scan level 3+)
- **"It's burrowing!"** — Burrower about to surface (requires Burrower scan level 5+)
- **"The swarm is forming!"** — Crawlers grouping to critical mass (requires Crawler scan level 4+)
- **"That one's different."** — Corrupted variant mixed into normal group

Alert quality scales with scan depth:
- Low scan: vague warnings ("Something's coming")
- High scan: specific warnings with timing ("Dive in 2 seconds, dodge left")

### Surprise Attack Prevention
Enemies that jumpscare or ambush you:
- **No scans**: Full surprise. No warning. Maximum damage.
- **Some scans**: EVE says "I have a bad feeling" when entering their territory
- **Full scans**: EVE marks ambush points on your HUD. You see the trap before it triggers.

This makes scanning a SURVIVAL tool without it happening during combat.

---

## The Knowledge Tree

All scan data feeds into a central Knowledge Tree (the in-game name for the progression system).

### Branches
- **Ecology** — creature scans, trophic relationships, ecosystem manipulation
- **Geology** — environment scans, resource locations, structural analysis
- **Archaeology** — ruins, ancient tech, pre-native civilization
- **Linguistics** — native communication, translations, cultural understanding
- **Biology** — flora, medicine, crafting materials, corruption analysis
- **Engineering** — items, weapons, settlement optimization, hybrid tech

### Gates
Knowledge gates check branch totals:
- "ECOLOGY 15/20" — scan 15 ecology entries to open this path
- "ARCHAEOLOGY 8/10" — understand enough ancient tech to activate this door
- Gates are NEVER binary. There's always another way (combat, movement, or a different knowledge branch). Knowledge gates are shortcuts and bonus paths.

### The Tree of Knowledge (Thematic)
The Knowledge Tree is literally themed as the Tree of Knowledge of Good and Evil. The more you understand, the more complex the moral landscape becomes. Early game: creatures are threats. Late game: you understand they're part of a system you're disrupting. The knowledge IS the Fall — you can't un-know what you've learned.

---

## Scan Visual/Audio Design

### Visuals
- L pressed near scannable object: green reticle appears on target
- Hold L for 1 second: scan beam connects, progress ring fills
- Scan complete: brief green flash, target pulses once
- New entry: small "+" icon floats up from target
- Already-scanned (no new data): brief yellow flash, no beam (instant feedback "nothing new here")

### EVE Voice Lines
Every scan gets a 1-2 sentence EVE response. She has personality:
- Curious: "Fascinating. The cellular structure is completely unlike anything in our database."
- Practical: "Edible. Barely. Don't make it a habit."
- Emotional: "...Admin. I think this was someone's home."
- Humorous: "It's a rock. I'm not sure what you expected."
- Disturbed: "The corruption here is... I need a moment to process this."
- Awed: "This is older than the Federation. By a LOT."

### Audio
- Scan start: soft electronic chirp
- Scanning: quiet hum that builds
- Scan complete (new data): satisfying ping + EVE line
- Scan complete (no new data): flat tone (non-punishing but clear)
- Major discovery: special chime + longer EVE line + screen-edge glow

---

## Implementation Priority

### Phase 1 (NOW — prototype in debug room)
- [ ] Move scan to L key
- [ ] Scan only works on non-aggro'd targets (corpses, passive, caged)
- [ ] Basic scan depth: 3 tiers for creatures (ID, vitals, weakness)
- [ ] EVE text bubble (1 sentence) on scan complete
- [ ] Scan gym with caged creatures for testing

### Phase 2 (When building first real level)
- [ ] Environment scanning (rocks, water, plants)
- [ ] Item scanning (weapons, materials)
- [ ] Knowledge Tree HUD (branch totals)
- [ ] First knowledge gate

### Phase 3 (When natives are implemented)
- [ ] Gesture communication UI
- [ ] EVE translation progression
- [ ] Native scan entries
- [ ] Fetch quest system

### Phase 4 (Polish)
- [ ] EVE voice lines (text-to-speech or recorded)
- [ ] Scan depth through context (different states/locations)
- [ ] EVE combat alerts
- [ ] Full 10-entry scan depth for all categories

---

## Open Questions
- [ ] Should scan data persist across deaths? (Probably yes — knowledge is permanent)
- [ ] Can you scan your own settlement objects for optimization tips?
- [ ] Should there be "missable" scans (one-time events)?
- [ ] How does corruption affect scan accuracy? (EVE gets confused near heavy corruption?)
- [ ] Can enemies evolve/adapt if you scan them too much? (They learn you're studying them?)
