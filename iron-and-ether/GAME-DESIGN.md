# Iron & Ether — Game Design Document

_Arena combat meets combinatorial crafting. Geometry Wars with a spell-builder._
_Scope: small, tight, ship-ready. The system IS the game._

---

## Elevator Pitch

Top-down arena shooter where your weapon is built from three combinable axes: **Form** (how it moves), **Behavior** (what it does on contact), and **Essence** (its elemental nature). Kill enemies to extract components. Slot them to reshape your weapon in real time. 343 possible combinations, each mechanically distinct.

---

## Core Loop

1. **Enemies spawn in waves** (Geometry Wars style)
2. **Kill enemies → extract components** (Aria of Sorrow model: first kill = guaranteed drop)
3. **Slot components into your weapon** (3 axes, swap anytime, even mid-combat)
4. **Harder waves demand better builds** (progression through mastery, not levels)
5. **Repeat, experiment, discover synergies**

---

## The Three Axes

### Axis 1: FORM (How it moves through space)
Controls projectile trajectory and spatial relationship to enemies.

| Component | Movement Pattern | Feel |
|-----------|-----------------|------|
| **Bolt** | Straight line, fast, narrow | Sniper / precision |
| **Arc** | Lobbed, gravity-affected | Mortar / area denial |
| **Burst** | Radiates outward from player | Shotgun / panic button |
| **Wave** | Travels along surfaces | Ground control / area sweep |
| **Orbit** | Circles around player | Defensive / melee-range |
| **Chain** | Jumps between nearby targets | Crowd clear / lazy aim |
| **Seed** | Placed stationary, activates on trigger | Trap / setup play |

**No Form equipped (∅):** Ability becomes a self-buff/aura emanating from the player.

### Axis 2: BEHAVIOR (What happens on contact/over time)
Controls the interaction pattern when the ability connects.

| Component | Effect | Feel |
|-----------|--------|------|
| **Pierce** | Passes through targets, keeps going | Efficient / line-up shots |
| **Shatter** | Splits into fragments on impact | Explosive / chaotic |
| **Linger** | Creates a persistent zone | Area denial / zoning |
| **Bounce** | Reflects off surfaces/enemies | Geometry / trick shots |
| **Siphon** | Returns resource to player (hp/energy) | Sustain / risk-reward |
| **Bloom** | Grows over time, starts small | Patient / scaling power |
| **Bind** | Attaches to target, ticks over time | DoT / lock-down |

**No Behavior equipped (∅):** Single hit, clean impact, no secondary effect. Simple and reliable.

### Axis 3: ESSENCE (Qualitative nature)
Controls the elemental/thematic quality. Affects damage type, status effects, visual identity.

| Component | Theme | Status Effect |
|-----------|-------|---------------|
| **Cinder** | Heat, combustion | Ignite (damage over time) |
| **Brine** | Corrosion, erosion | Corrode (defense reduction) |
| **Bone** | Rigidity, sharpness | Fracture (critical hit vulnerability) |
| **Silk** | Entanglement, softness | Snare (slow) |
| **Pulse** | Rhythm, disruption | Stagger (interrupt / stun) |
| **Hollow** | Void, negation | Silence (disable enemy abilities) |
| **Sap** | Growth, vitality | Leech (heal on hit, weaker than Siphon but stacks) |

**No Essence equipped (∅):** Pure kinetic damage. No status effects. Baseline "unenchanted" weapon.

---

## Incomplete Loadouts

The system supports 0-3 slots filled. Each missing axis has a default:

| Slots Filled | Result | Design Purpose |
|-------------|--------|----------------|
| **0** (∅ + ∅ + ∅) | Basic pea-shooter. Reliable, weak | Starting weapon / safety net |
| **1** (e.g., Form only) | Single-axis ability. Bolt = fast shot, Burst = radial push | Tutorials, early game |
| **2** (e.g., Form + Behavior) | Strong ability, no element | Viable mid-game, rewards positioning |
| **3** (Full combo) | Complete ability with status effects | Full power, late-game |

**Key balance principle:** Empty slots = simpler but weaker. Full slots = complex but powerful. The player is never punished for experimenting — stripping a slot to try something new just means temporarily less power, not death.

---

## Enemies

### Design Principle
Each enemy **embodies** 1-2 components. Their behavior demonstrates the component visually before you acquire it. Kill them → extract what they are.

### Core Enemy Types (Start Small — ~15 for prototype)

**Form Enemies (teach movement patterns):**
| Enemy | Embodied Component | Behavior |
|-------|-------------------|----------|
| Dart | Bolt | Charges straight at you |
| Lobber | Arc | Throws arcing projectiles |
| Nova | Burst | Explodes radially when close |
| Crawler | Wave | Moves along walls/floor |
| Orbiter | Orbit | Circles a point, shields allies |
| Zapper | Chain | Lightning arc to nearest target |
| Mine | Seed | Sits still, detonates on proximity |

**Behavior Enemies (teach interaction patterns):**
| Enemy | Embodied Component | Behavior |
|-------|-------------------|----------|
| Phantom | Pierce | Moves through walls/other enemies |
| Crystal | Shatter | Splits into smaller enemies on death |
| Fog | Linger | Leaves damaging zone where it dies |
| Ricochet | Bounce | Bounces off walls unpredictably |
| Leech | Siphon | Drains your health on contact |
| Spore | Bloom | Starts tiny, grows larger and stronger |
| Parasite | Bind | Attaches to you, drains over time |

**Essence enemies:** Reskinned versions of the above with elemental properties. A "Cinder Dart" is a Bolt+Cinder enemy — charges at you and leaves fire trail. Encountering them teaches what essences DO.

**Bosses:** Multi-component enemies that use full 3-axis combinations. They're a preview of what the player can become.

---

## Arena Design

### Phase 1 (Prototype)
- Single rectangular arena
- Wave-based spawning with escalating difficulty
- Component drops appear where enemies die, auto-collect on proximity
- HUD at top shows: [FORM] + [BEHAVIOR] + [ESSENCE] = current weapon
- Pause menu shows full grid of discovered/undiscovered combinations

### Phase 2 (If core is fun)
- Multiple arena shapes (obstacles, walls for Bounce/Wave interactions)
- Hazards that interact with essences (oil pools + Cinder, water + Pulse)
- Endless mode with leaderboards
- Challenge rooms: "Clear this wave using only Seed-type builds"

---

## UI / HUD

```
┌─────────────────────────────────────────────┐
│  [FORM: Bolt ▼]  [BEHAVIOR: Pierce ▼]  [ESSENCE: Cinder ▼]  │
│  ═══════════════════════════════════════════ │
│  Current: Fire Arrow (piercing flame bolt)  │
└─────────────────────────────────────────────┘

                    ARENA

┌──────────┐                        ┌──────────┐
│ HP ████░░ │                        │ Wave: 12 │
│ EN ██████ │                        │ Kills: 87│
└──────────┘                        └──────────┘
```

- **Hotswap:** Number keys or shoulder buttons to quick-switch individual axes mid-combat
- **Discovery grid:** Accessible from pause. 7×7×7 cube visualization? Or three 7×7 grids (Form×Behavior for each Essence)?
- **New component flash:** When you acquire a new component, brief slow-mo + name + icon. Celebration moment.

---

## Art Direction

- **Minimal.** Player is a geometric shape or simple sprite
- **Effects-driven.** The weapon combinations should be visually distinct — particles, colors, trails
- **Component identity through color/shape language:**
  - Forms = distinct projectile shapes/trails
  - Behaviors = distinct impact/interaction animations
  - Essences = color palette (Cinder=orange/red, Brine=green/teal, Bone=white/gray, Silk=purple/pink, Pulse=yellow/electric, Hollow=dark/void, Sap=bright green/amber)
- **Arena:** Dark background, neon elements. Geometry Wars proved this works

---

## Tech

- **Engine:** MonoGame (C#) — we know it, same stack as Genesis
- **Resolution:** 1920×1080, pixel-art-optional (effects can be smooth)
- **Target:** Windows first, then Steam

---

## Development Phases

### Phase 0: Foundation (Week 1-2)
- [ ] Player movement + basic shooting in arena
- [ ] Single Form (Bolt), single Behavior (Pierce), single Essence (Cinder)
- [ ] One enemy type (Dart) that spawns in waves
- [ ] Component drop + collection
- [ ] HUD showing active loadout
- **Milestone: You can shoot a fire arrow at a charging enemy and it feels good**

### Phase 1: The Grid (Week 3-4)
- [ ] All 7 Forms implemented
- [ ] All 7 Behaviors implemented
- [ ] All 7 Essences implemented
- [ ] Incomplete loadout defaults working
- [ ] Component swap UI (pause or hotkey)
- [ ] 3-5 enemy types
- **Milestone: You can swap components mid-fight and every combo feels different**

### Phase 2: The Bestiary (Week 5-6)
- [ ] All 15+ enemy types, each dropping their component
- [ ] Wave director (escalating difficulty, introduces new enemy types over time)
- [ ] Discovery grid UI (shows found/unfound combinations)
- [ ] At least 1 boss fight
- **Milestone: A full session loop — start with nothing, build up your arsenal, fight a boss**

### Phase 3: Polish & Ship (Week 7-8)
- [ ] Screen shake, particles, juice (we know how to do this now)
- [ ] Sound design (SoundThread for alien ability sounds)
- [ ] Arena variations or hazards
- [ ] Balancing pass — are all axes viable? Any dead combos?
- [ ] Leaderboards / score system
- [ ] Upload to itch.io or Steam demo
- **Milestone: Someone who isn't you plays it and wants to keep playing**

---

## Open Questions

- [ ] Is this real-time or does swapping components pause the game?
- [ ] Can you store multiple loadouts and swap between presets?
- [ ] Should there be a resource cost to firing (energy meter) that varies by combo complexity?
- [ ] Multiplayer potential? (Co-op arena, competitive?)
- [ ] Name: "Iron & Ether" is a working title — refine later

---

## Inspirations

- **Geometry Wars** — arena feel, spawn patterns, screen-filling chaos
- **Castlevania: Circle of the Moon** — DSS card grid, discovery joy
- **Castlevania: Harmony of Dissonance** — tome × subweapon visual feedback
- **Castlevania: Aria of Sorrow** — kill → acquire, tight curation
- **Shovel Knight: Plague of Shadows** — 3-axis bomb crafting, feel-changing combos
- **Noita / Magicka** — spell combination (what to learn from AND what to avoid)
- **Vampire Survivors** — proof that "small scope + deep systems" sells

---

_The system is the game. If the system is fun, everything else is decoration._
