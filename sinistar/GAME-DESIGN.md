# Sinistar Remake — Design Document
## Reverse-Engineered from Original 6809 Assembly Source

### Core Loop
Mine crystals → Build sinibombs → Destroy Sinistar before it eats you.

---

## Entities (from source)

### Player Ship
- Free-roaming 2D space, 360° rotation + thrust (inertia-based, no friction)
- **Fire button**: shoots bullets (forward-facing)
- **Sinibomb button**: launches sinibomb at Sinistar (limited ammo, built from crystals)
- Collision types: planetoids, warriors, workers, sinibombs, Sinistar, crystals

### Planetoids (5 types in original: Plan1-Plan5)
- Mineable asteroids scattered in the play field
- Player shoots them → they release **crystals**
- Planetoid 5 is special (spawns later, difficulty-gated)
- Each has vibration/offscreen behavior
- Workers also mine them for Sinistar pieces

### Workers
- Enemy drones that mine planetoids for crystals
- **5 mission states** (from WORKER.SRC):
  1. **Drift** — float in space awaiting orders
  2. **Tail target** — follow a planetoid
  3. **Intercept target** — fly toward planetoid to mine
  4. **Deliver crystal** — carry crystal back to Sinistar to build it
  5. **Evade** — flee from current course (when threatened)
- Workers WITH crystals move faster (allowed farther offscreen delivery)
- Workers are not aggressive — they're builders

### Warriors
- Enemy fighter ships that hunt the player
- **Mission-based AI** (from WARRIOR.SRC):
  - Squadron behavior: fly in formation with a leader
  - `OSFLANG` = squadron flight angle (leader updates, others copy)
  - `OSSQSIZ` = squadron size
  - Can be called away from squadron on special missions
  - Mission types dispatched via table (even-indexed)
- Warrior aggression increases with difficulty (`WAgg` parameter)
- Population scales: starts at 14, increases over time

### Sinistar (THE BOSS)
- **Assembly states** (from ADDPIEC.SRC): Built piece by piece from worker-delivered crystals
- `Finish` variable: compared to `Alive` — not alive until fully assembled
- **AI when alive** (from SINI.SRC):
  - Chases player relentlessly
  - Orbital approach: starts with large orbit, shrinks to direct pursuit
  - `PSiniInhibit`: shooting inhibitor that counts down
  - Inner orbit (< MaxSinOrbit*3/4): only reduces when ON SCREEN
  - Outer orbit: reduces at any time
  - Can be **stunned** (`InStun` timer — sinibomb hit)
  - Stops when dying (`SinGrave`) or in attract mode demo
  - Velocity: separate long-distance and short-distance pursuit vectors
  - Uses `ReTarget` to aim at player, `newvel` for velocity calculation
- **Animation**: "chomp chomp chomp" (`anisinistar`)
- **Voice lines**: "RUN, COWARD!", "BEWARE, I LIVE!", "I HUNGER!", "RUN RUN RUN!"

### Sinibombs
- Player-built weapons (crystals → sinibombs)
- Only weapon that damages Sinistar
- Has `DeathFlag` collision indicator
- Limited quantity — resource management is key

### Crystals
- Released when planetoids are shot
- Player collects by flying over them
- Workers also collect them (competitive resource)
- Converted to sinibombs in player inventory

---

## Difficulty System (from DIFFICUL.SRC)
- **DTime**: master difficulty timer
- Parameters that scale:
  - `Pop+1`: Worker population (starts ~6)
  - `Pop+4`: Warrior population (starts ~14) 
  - `Pop+13`: Planetoid 5 population (starts ~3)
  - `WAgg`: Warrior aggression (starts 0, increases)

## Collision System (from COLLISIO.SRC)
- Bitmask-based: each entity has a collision mask and collision type
- Collision pairs checked via mask AND
- Entity types: PLAYER, PLANET, SBOMB, WORKER, WARRIOR, SINISTAR, CRYSTAL

## Scanner (SCANNER.SRC)
- Minimap/radar showing relative positions of all entities
- Each entity has a scanner workspace with position, velocity, mission state

---

## Remake Plan

### Tech Stack
- **MonoGame C# (.NET 9)** — same as Genesis, reuse infrastructure
- OR **Godot** — faster for a jam-style ship-it project
- Target: **itch.io release**, 1-2 week dev cycle

### What to Keep (Subtractive Design)
- ✅ Free-roaming 2D space with inertia
- ✅ Mine asteroids for crystals → build sinibombs
- ✅ Workers building Sinistar piece by piece (TENSION)
- ✅ Warriors hunting in squadrons
- ✅ Sinistar's orbital approach → direct chase
- ✅ The VOICE ("RUN, COWARD!")
- ✅ Scanner/radar
- ✅ Limited sinibombs (resource scarcity)

### What to Add (Modern Polish)
- Particle effects (explosions, crystal trails, thruster exhaust)
- Screen shake on Sinistar approach
- Bloom on sinibomb explosions
- Camera zoom on Sinistar awakening
- Juicy asteroid destruction (fragments, debris)
- Progressive music intensity
- Subtle vignette darkening when Sinistar is near

### What to Subtract
- No lives system (one round, survive or die, chase high score)
- No complex menus (press start, play)
- No complicated controls (twin-stick or mouse-aim + WASD)

### Scope
- 1 play field, 1 boss, ~10 minutes per run
- 5-10 asteroid types (visual variety only)
- 3-5 warrior types (speed/aggression variants)
- Score → leaderboard
- Ship in 1-2 weeks, polish in week 3
