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
