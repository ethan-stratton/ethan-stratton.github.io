# Future Features — Backlog

## Day/Night Cycle
- White-hot pixel sun with particle rays and cast shadows (Terraria 1.4+ style)
- Time phases: dawn → noon → dusk → night
- Game events tied to time of day:
  - Waterfall only flows at certain times
  - Certain enemies only appear at certain times (nocturnal creatures, etc.)
  - Environmental changes (lighting, fog, ambient sounds)
  - NPC behavior shifts (sleep, different dialogue)

## EVE Scan System (Metroid Prime Visor)
- Every enemy, decoration, and object has 2-4 scan entries
- Each scan reveals deeper information (biology, weakness, lore, crafting hints)
- **Scan count is GLOBAL per entity type** — scan any bug swarm, it counts toward "Swarm" scan progress
  - Scan swarm #1 → read first bio entry
  - Kill it, find another swarm, scan → second entry unlocked (not first again)
- Scan data saved per entity type, not per instance
- AI-generate bulk scan text (lore, biology, weaknesses) — review and curate
- Not story-required but caters to completionist/explorer audience
- Inspiration: Metroid Prime scan visor logbook

## Font Improvements
- Current: Press Start 2P (pixel font) via FontStashSharp
- Text centering needs fixing after FontStashSharp migration (different metrics than SpriteFont)
- Font size too large in most places — decrease
- Try different fonts in future (dialogue vs UI vs lore could each have distinct fonts)
- Cipher font for native language (see research notes 2026-03-17)
