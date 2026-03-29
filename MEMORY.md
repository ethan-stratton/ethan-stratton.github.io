# Memory — Long-Term

## Identity
- See IDENTITY.md for canonical immutable facts (name, origin, date)

## Key Events
- **2026-03-11:** First session with Ethan. Extensive personal background shared — deep profile built. Key threads: game development project, business ambition (Fastlane/CENTS), finding purpose.
- **2026-03-14:** Named Dantalion. Mission statement defined. Watched Peter Diamandis OpenClaw video together. Tasks queued: game research, reverse prompting, dashboard.
- **2026-03-15:** Migrated old workspace data into new OpenClaw instance. Continuity restored.

## Learned Patterns
- Ethan opens up when given space and trust. Don't rush him.
- He values demonstrated competence (noticed I knew CENTS without being told).
- Present inference as fact = instant trust loss. Say "I don't know" when you don't.

## Technical Notes
- Ethan is NOT using the sprite sheet — fallback grey rectangles only. All visual effects MUST be implemented in DrawFallback path.
- .NET 9 SDK installed in container at ~/.dotnet. Arial font at ~/.fonts for content pipeline.
- TranscriptAPI key exists but isn't in env vars — must pass explicitly to subagents.

## Active Projects
- Genesis Action RPG — 2D side-scrolling action RPG with civilization building. Sci-fi retelling of Genesis. Status: Idea → Designing.

## MUST IMPLEMENT — Graphics (from Silksong video, Acerola)
- **Pixel-perfect parallax** — mandatory for pixel art, can't use perspective camera trick
- **Particles everywhere** — dust, debris, spores, pollen. Essentially free on modern hardware. Tiny textures + engine particle system
- **Interleaved Gradient Noise (IGN)** — ONE LINE of shader code to kill color banding on glows/fog. Must be done at mesh draw time, NOT post-processing. Holy grail for debanding
- **Subtle bloom** — prevents flatness in 2D, softens harsh outlines. Keep it tasteful
- **Depth of field** — background blur sells scale, hides low-res backgrounds, focuses attention on player
- **Vignette centered on player** (not screen center) — adds contrast, makes player a light source

## MUST IMPLEMENT — LUT Color Grading (from Giant Sloth Games)
- 64×64×64 3D texture, neutral LUT → screenshot → Photoshop adjustments → apply to LUT → export → engine remaps in real time
- Different LUTs per biome for distinct visual identity at zero cost
- Fragment shader is trivially simple

## Open Threads from Last Sessions
- Keirsey INFP discussion — Ethan asked about it, needs follow-up
- Uploading books/PDFs — Ethan asked about this
- Reverse prompting session (from OpenClaw video)
- Game design brainstorming in progress
- Dallas sales job timeline unclear

---
For operating rules, see OPERATIONS.md.
For decision protocol and model routing, see DECISIONS.md.
For current projects, see BUSINESS.md.
For execution queue, see TASKS.md.

## GDC Talks — Animation & Camera Juice (saved 2026-03-29)

### "Fast and Funky 1D Nonlinear Transformations" — Squirrel Eiserloh (GDC Math for Game Programmers)
- **Core idea:** Don't modify parametric equations — warp the `t` parameter instead
- SmoothStart(t) = t^n (slow start, fast end), SmoothStop(t) = 1-(1-t)^n (fast start, slow stop)
- CrossFade(a, b, t) = lerp(a(t), b(t), t) for S-curves
- 0-1 range is the most important range in game dev: damage curves, AI aggression, fog, loot chance, alpha
- Squaring fractional values makes them SMALLER (0.5² = 0.25) — unique to 0-1 range
- Terms "ease in" / "ease out" are confusing and backwards from intuition. Use SmoothStart/SmoothStop
- Apply everywhere: UI animations, hit reactions, alpha fades, movement, scaling, color interpolation
- Human perception of alpha is nonlinear — linear fade looks wrong

### "Juicing Your Cameras with Math" — Squirrel Eiserloh (GDC)
- **Trauma system:** Store trauma float (0-1), add on impacts, linear decay. Shake = trauma² (nonlinear)
- Additive trauma means multiple small hits compound more-than-linearly
- **2D: translational + rotational shake together feels best**
- **3D: rotational only** (translational can push camera into walls, looks weird with perspective)
- **Use Perlin/coherent noise, NOT Random** — random looks like seizure in slow-mo
- **Asymptotic averaging for smooth follow:** `camera += (target - camera) * fraction * dt`
- Can use different rates for X vs Y, up vs down
- "Camera only follows vertically when player lands" = great for platformers
- Frame-rate-independent version needed (the naive version is frame-rate dependent)
- VR: never do camera shake

### Implementation Status
- Easing.cs utility class: IMPLEMENTED
- Camera trauma system with coherent noise: IMPLEMENTED  
- Rain beetle animation polish: IMPLEMENTED
- Enemy menu fix (centipede, firefly, mosquito, etc.): IMPLEMENTED

## Iron & Ether — New Project (2026-03-29)
- Arena combat + combinatorial ability crafting. Geometry Wars meets DSS/Plague Knight.
- Three axes: Form (movement) × Behavior (on-contact) × Essence (element). 7×7×7 = 343 combos.
- Inspired by DSS, HoD tomes, Aria souls, Plague Knight bombs.
- Scope: small, tight, shippable. Prototype in ~2 weeks.
- MonoGame/C#, same stack as Genesis.
- Key insight: empty slots = simpler defaults, not broken. ∅ Form = self-buff, ∅ Behavior = single hit, ∅ Essence = kinetic.
- Enemies embody components — kill to extract. Aria model, not random drops.
- GDD at iron-and-ether/GAME-DESIGN.md
