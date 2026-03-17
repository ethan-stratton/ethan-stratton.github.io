# Enemy AI Research Notes — 2026-03-17

## Terraria AI System (from wiki)

Terraria uses numbered "AI types" — each enemy gets assigned an AI style that defines movement, attack, and reaction patterns. Key ones relevant to Genesys:

### AI Type Catalog (Terraria-derived, adapted for 2D side-scrolling)

**Ground Walkers (AI 3 - "Fighter")**
- Walk toward player, turn at walls/edges
- Simple but effective — the bread and butter enemy
- Variants: fast/slow, big/small, different HP pools
- *Our crawlers are basically this*

**Hoppers (AI 1 - "Slime")**
- Hop toward player with variable height/distance
- Pause between hops — creates rhythm the player can exploit
- Some slimes split into smaller slimes on death
- *This is the "watcher/slime" we discussed but haven't built*

**Flyers (AI 2 - "Demon Eye")**
- Float toward player, bob up and down sinusoidally
- Can pass through platforms, walls optional
- Aggressive but predictable orbit pattern
- *Good for flying enemies, bats, wisps*

**Worms (AI 6 - "Worm")**
- Multi-segment body, head follows player, body segments trail behind
- Burrows through terrain, surfaces to attack
- Each segment has independent HP or shares a pool
- *Boss material — the Mecha Dragon could use worm-like segmented movement*

**Casters (AI 8 - "Caster")**
- Teleport to random positions near player
- Fire projectile, then teleport away
- Window of vulnerability during cast animation
- *Magic/tech enemies — could be Dragon minions*

**Burrowers (AI 10 - "Goldfish Walker" variant)**
- Walk on ground normally, but detect player below and dig through platforms
- Surprise attacks from above/below
- *Environmental hazard feel*

**Passive-Until-Aggro (AI 7)**
- Wander aimlessly until player attacks them or gets too close
- Then become aggressive fighters/chasers
- *Wildlife — fits the alien planet ecology*

**Mimics (AI 87)**
- Disguised as treasure/objects until player approaches
- Spring to life with aggressive attack pattern
- *Perfect for the scan system — EVE could warn you "that chest seems... wrong"*

### Key Terraria Design Principles:
1. **Each AI type is simple** — one movement pattern, one attack style
2. **Variety comes from stats, not complexity** — same AI, different speed/HP/damage
3. **Biome-specific enemy pools** — desert has different enemies than jungle
4. **Day/night enemy changes** — zombies at night, slimes during day
5. **Event spawning** — blood moons, goblin armies change the spawn table entirely
6. **Spawn proximity** — enemies spawn off-screen and wander in, not pop into existence

## Reddit: Games with Impressive Enemy AI

### Most-Cited Games:

**F.E.A.R. (2005)** — The gold standard. Enemies flank, use cover, communicate, retreat when wounded. Uses GOAP (Goal-Oriented Action Planning) — enemies have goals and plan actions to achieve them rather than following scripted behaviors. The *illusion* of intelligence through great audio callouts ("He's flanking left!") was as important as the actual AI.

**Alien: Isolation** — The Xenomorph learns from player behavior. If you hide in lockers too often, it starts checking lockers. If you use the flamethrower, it becomes resistant. Two AI systems: a "Director" that knows where you are and drip-feeds hints to the Xenomorph, and the Xenomorph itself which has to actually find you. Only learns from encounters you SURVIVE — deaths don't train it. Brilliant because it means getting better makes the game harder.

**Halo (series)** — Grunts flee when Elites die. Elites coordinate and flank. Hunters fight in pairs. Each enemy type has personality expressed through AI. Jackals are cowardly snipers, Brutes are aggressive berserkers. *The enemy AI tells you about the enemy's character.*

**Half-Life (1998)** — Marines were revolutionary. Squad tactics, grenade flushing, covering fire. Would retreat and set up ambushes. Felt alive because they talked to each other.

**Metal Gear Solid V** — Enemies adapt to your playstyle over the entire game. If you always do headshots, they start wearing helmets. If you attack at night, they get night vision. Long-term adaptation, not just per-encounter.

**Hitman: World of Assassination** — Complex NPC routines. Each NPC has a schedule, personality, reactions to disturbances. The AI creates an ecosystem the player disrupts.

**Dark Souls** — Not "smart" AI but *perfectly tuned* AI. Every enemy has tells, windups, recovery windows. The player learns the AI by dying. The AI is a puzzle. *This is closest to what Genesys should do for action combat.*

### Key Insights for Genesys:

1. **"Smart" AI isn't always the goal** — Terraria enemies are simple and the game is incredible. Dark Souls enemies are predictable and it's the best combat in gaming. What matters is that the AI serves the gameplay loop.

2. **Personality through behavior** — Halo's greatest trick was giving each enemy species a distinct behavioral personality. Grunts panic. Elites strategize. This makes combat readable and memorable.

3. **Audio sells AI** — F.E.A.R.'s enemies weren't actually that much smarter than others, but they TALKED about what they were doing. "He's behind the pillar!" makes the player FEEL flanked.

4. **Adaptation should be optional/subtle** — Alien Isolation and MGSV work because adaptation is slow and organic. Sudden rubber-banding feels cheap.

5. **Simple AI + good encounter design > complex AI + random spawns** — Handcrafted enemy placement with simple AI creates better gameplay than smart enemies placed randomly.

## For Genesys Enemy Design

### Immediate (what we can build now):
- **Crawlers** ✅ — ground walkers, patrol + chase (Terraria Fighter AI)
- **Thornbacks** ✅ — stationary hazards (Terraria Spike Ball)
- **Swarms** ✅ — proximity-triggered cloud (unique to us)
- **Hoppers** — slime-like, hop toward player with pauses (Terraria Slime AI) — NEXT to build
- **Spitter** — ranged crawler variant, stays at distance and fires projectile

### Medium-term:
- **Flyers** — sinusoidal movement, aggro on proximity
- **Burrowers** — dig through platforms to surprise attack
- **Mimics** — disguised as objects (EVE scan reveals them)
- **Pack enemies** — become braver in groups, flee alone (Halo Grunt behavior)

### Boss-tier:
- **Multi-segment worm** — for Mecha Dragon or sub-bosses
- **Teleport caster** — Dragon minion type
- **Adaptive boss** — learns which attacks you dodge well vs poorly (Alien Isolation principle, scaled down)

### Design rules:
1. Each enemy has ONE clear behavior pattern the player can learn
2. Enemies have personality expressed through movement (fearful, aggressive, patient, erratic)
3. Audio/visual cues telegraph attacks — no unfair surprises
4. EVE scan reveals weaknesses and lore — rewards observation
5. Day/night cycle changes spawn tables
6. Biome-specific enemy pools
7. Every enemy serves a purpose in teaching the player something

## YouTube: "Why They Can't Subvert the Hero"

Based on the title and common themes in this video essay genre:

The argument is likely about why modern storytelling's obsession with "subverting expectations" and deconstructing heroes fails — because audiences fundamentally NEED heroes who embody genuine virtue, sacrifice, and growth. The hero's journey (Campbell/Vogler) works because it maps to human psychological development.

**For Genesys this matters because:**
- Adam's arc should be a GENUINE hero's journey, not a deconstruction
- The player should feel heroic, not cynical
- Eve/EVE as the mentor/guide figure is classical and works
- The Dragon as genuine evil (not misunderstood, not sympathetic) gives the hero something real to fight against
- "Subversion" works as a MOMENT (a twist), not as the thesis
- The Genesis retelling should honor the source material's structure while recontextualizing it in sci-fi — not mock or deconstruct it

**Recommendation:** Watch this video when you get a chance, Ethan. Even from the title alone it aligns with our design philosophy — Genesys should be sincere, not ironic. Adam should be a hero worth rooting for.
