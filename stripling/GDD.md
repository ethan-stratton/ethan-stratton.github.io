# Title of Liberty — Game Design Document

**Genre:** Real-Time Tactical Strategy (with pause)
**Perspective:** Top-down
**Platform:** PC (web prototype feasible)
**Scope:** Small — campaign of 8-12 missions following the Alma war chapters
**Tone:** Reverent but not preachy. Military history told straight. Let the text speak.

---

## Vision

You are a field commander in the Nephite armies during the war chapters of Alma (roughly chapters 43–63). You receive orders from Captain Moroni, coordinate with Helaman, Teancum, Lehi, and others. You command small units — dozens, not thousands — across a bare, rugged landscape of wilderness, rivers, and fortified cities.

The gameplay loop: **receive orders → scout the terrain → position your forces → execute the plan → adapt when it falls apart.**

The Book of Mormon war chapters read like a tactical manual. The game just makes them playable.

---

## Core Pillars

### 1. Follow the Captain
You are not the general. You receive instructions — sometimes clear, sometimes vague. Your job is to interpret and execute. Moroni says "fortify the city of Manti" — *how* you do it is up to you. This creates a command-chain feel: you have autonomy within constraints.

### 2. Stratagems Over Strength
The Alma chapters are full of cunning: decoy retreats, surrounding armies with hidden forces, night raids, cutting off supply lines. Combat should reward clever positioning over raw power. A well-executed flanking maneuver should feel devastating. A head-on charge into a fortified position should feel suicidal.

### 3. The Righteousness Factor
This is the mechanic that makes it a Book of Mormon game, not just a generic tactics game.

Your army has a **Faith** meter (0–100). It rises when you:
- Follow your captain's orders faithfully
- Protect civilians during retreats
- Show mercy to surrendering enemies
- Keep your soldiers fed and rested (don't force-march them to death)
- Pray before battle (an actual gameplay action — costs time but boosts Faith)

It drops when you:
- Pursue fleeing enemies beyond what's needed (bloodlust)
- Sacrifice units carelessly
- Disobey or ignore orders
- Neglect wounded
- Attack during a truce or negotiation

**What Faith does:**
- High Faith: soldiers hold formation under pressure, morale breaks less, scouts report more accurately, your units fight above their weight class
- Low Faith: soldiers rout easily, friendly fire incidents, scouts give bad intel, units refuse risky orders
- This mirrors the text exactly: "Inasmuch as ye keep my commandments, ye shall prosper in the land"

Faith isn't a magic shield. You can still lose with high Faith if your tactics are garbage. But it's the wind at your back or the weight on your shoulders.

---

## Gameplay Systems

### Unit Types
Keep it simple. 4-5 unit types max:

| Unit | Role | Notes |
|------|------|-------|
| **Swordsmen** | Frontline melee | Solid, hold ground. Inspired by Moroni's breastplates and arm-shields (Alma 43:19) |
| **Archers** | Ranged support | Fragile but deadly from high ground or behind fortifications |
| **Scouts** | Recon & flanking | Fast, fragile, reveal fog of war. Can set ambushes. Inspired by Moroni's spies (Alma 43:28) |
| **Stripling Warriors** | Elite melee | Appear in Helaman missions only. High Faith baseline — they *never* rout. "They did not fear death" (Alma 56:47) |
| **Engineers** | Fortification | Build walls, dig trenches, set up wooden palisades. Slow but critical for defense missions. Inspired by Moroni's fortification program (Alma 49-50) |

### Movement & Formation
- Units move as **groups** (squads of ~20 men represented as a single token with a health bar)
- Drag to move, right-click to set facing direction
- Formation matters: a unit attacked from the rear takes massive morale damage
- Terrain affects speed: roads fast, jungle slow, rivers require fording points
- **Real-time with pause** — press Space to freeze time, issue orders, unpause

### Combat
- When two units engage, it's automatic — they fight based on stats, terrain, flanking, morale
- Your role is positioning, not micromanaging attacks
- **Flanking bonus:** Attacking from the side = +30% damage. From the rear = +50% damage + morale shock
- **Pincer attack:** If an enemy unit is engaged from 2+ sides simultaneously, they take a massive morale penalty and may rout
- **High ground:** Archers on hills get range and damage bonus
- **Fortifications:** Units behind walls get huge defense bonus. Attackers must breach or go around

### Fog of War
- You can only see what your scouts and units can see
- Scouts reveal a wide radius and can be sent ahead
- **Intel quality tied to Faith:** High Faith = scouts give accurate enemy counts. Low Faith = "we think there's... a lot of them?"
- Enemy movements are hidden until spotted — ambushes are possible (for both sides)

### The Map
- Bare landscape: brown earth, sparse trees, rivers, hills
- Named cities from the text: Zarahemla, Manti, Nephihah, Gid, Mulek, etc.
- Cities can be fortified (walls, trenches, towers)
- Wilderness areas between cities where ambushes happen
- Not a large open world — each mission is a focused map

---

## Campaign Structure

The campaign follows the chronological war chapters. Each mission is a chapter or cluster of chapters turned into a tactical scenario.

### Mission 1: "Prepare for War" (Alma 43)
**Briefing:** The Lamanites are coming. Captain Moroni has armed the Nephites with breastplates and shields — a first. Scout the approaching Lamanite army. Moroni asks Alma to inquire of the Lord where the Lamanites will attack.
**Objective:** Scout enemy position. Position forces at the hill Riplah near the river Sidon.
**Key mechanic intro:** Scouting, basic movement, terrain advantage.
**Climax:** Execute Moroni's pincer — Lehi attacks from behind while you hold the front at the river crossing.

### Mission 2: "The Covenant" (Alma 43-44)
**Briefing:** The Lamanites are surrounded but fighting desperately. Moroni calls for their surrender.
**Objective:** Force the Lamanite surrender without massacring them. Contain their army.
**Key mechanic intro:** Mercy mechanic — killing fleeing/surrendering enemies tanks Faith. Zerahemnah refuses the covenant, fights on, eventually relents.
**Decision:** How far do you push? The game lets you slaughter them, but Faith consequences are severe.

### Mission 3: "Title of Liberty" (Alma 46)
**Briefing:** Internal dissent. Amalickiah is pulling soldiers away. Moroni raises the Title of Liberty.
**Objective:** Rally scattered Nephite units before Amalickiah's forces can consolidate. A race against time.
**Key mechanic intro:** Morale/rally system. The Title of Liberty is a gameplay item — raise it near wavering units to restore morale.

### Mission 4: "The Fortification" (Alma 49-50)
**Briefing:** Peacetime. Moroni orders massive fortification of all cities.
**Objective:** Tower defense-style mission. Build walls, trenches, and towers across multiple cities before the next Lamanite assault.
**Key mechanic intro:** Engineer units, fortification building, resource management (wood, earth, time).
**Twist:** Lamanites attack the city you *least* fortified. Teach the player that they can't protect everything.

### Mission 5: "Helaman's March" (Alma 56-57)
**Briefing:** You now command the 2,000 stripling warriors under Helaman. Your force is small but fearless.
**Objective:** Lure the Lamanite garrison out of Antiparah by feigned retreat. Lead them into Antipus's ambush.
**Key mechanic intro:** Feigned retreat (give a "retreat" order that's actually a lure). Timing the ambush with Antipus.
**Emotional beat:** Antipus falls. You must decide: keep retreating or turn and fight? The stripling warriors beg to fight.
**Faith moment:** "They had been taught by their mothers" — high Faith because of the mothers' faith. None die, but many are wounded.

### Mission 6: "City of Mulek" (Alma 52)
**Briefing:** The city of Mulek is occupied. Moroni coordinates a complex stratagem: Teancum lures the garrison out along the seashore, Lehi cuts off retreat, Moroni storms the weakened city.
**Objective:** Execute a three-pronged coordinated attack. You control one prong and must trust the AI-controlled allies to do their parts.
**Key mechanic:** Multi-force coordination. If you move too early or too late, the plan falls apart.

### Mission 7: "Teancum's Raid" (Alma 62)
**Briefing:** Night mission. Teancum infiltrates the Lamanite camp to assassinate the king.
**Objective:** Stealth mission with a single scout unit. Avoid patrols, reach the king's tent.
**Tone shift:** Quiet, tense. No armies — just one man in the dark.
**Tragedy:** Teancum succeeds but is discovered and killed. The mission "succeeds" but the cost is personal.

### Mission 8: "Peace" (Alma 62-63)
**Briefing:** Final combined assault to retake all lost cities. Moroni, Helaman, Lehi, Teancum's remaining forces.
**Objective:** Full campaign climax. Everything you've learned — flanking, fortification, scouting, faith, coordination.
**Ending:** The war ends. Brief epilogue. Moroni retires. The question lingers: was it worth it?

---

## Art Style

- **Minimalist top-down** — units are simple colored tokens/sprites on a muted earth-tone landscape
- Think: parchment map come to life
- Subtle scripture verse overlays between missions (actual text from Alma)
- UI inspired by military campaign maps — clean, functional, a little weathered

---

## Audio

- Sparse. Wind, distant drums, footsteps.
- Battle: clash of metal, shouts, arrows
- Between missions: a simple hymn-like melody (not cheesy — think Gregorian chant energy but with a Book of Mormon feel)
- High Faith: ambient music is warmer, more harmonic
- Low Faith: dissonant, unsettled, drums feel heavier

---

## The Righteousness Mechanic — Design Philosophy

This isn't a morality system where you choose "good" or "evil." It's a *covenant* system. The text is explicit: obedience to God's commandments = strength in battle. The game takes that at face value.

The player isn't being judged. The player is experiencing what the text describes. If you play ruthlessly, your army becomes demoralized and unreliable — not because the game is punishing you, but because that's what the text says happens.

The brilliance of the war chapters is that Moroni wins through *preparation and strategy*, not divine intervention. God doesn't send angels to fight for them. He gives them clarity of mind, courage, and the wisdom to fortify and outmaneuver. The Faith mechanic reflects this: it doesn't make your swords sharper. It makes your soldiers braver and your intel more reliable.

---

## Scope Notes

- **Prototype scope:** Mission 1 (the Riplah pincer) as a standalone playable scenario
- **Tech:** Could be web-based (Canvas/WebGL) or a lightweight engine like Godot
- **Minimum viable:** Top-down map, drag-to-move units, fog of war, basic combat resolution, one complete mission
- **Stretch:** Full 8-mission campaign, Faith system, fortification building, narrative cutscenes with Alma text

---

## Why This Works

The Book of Mormon war chapters are the most detailed military narrative in scripture. They describe specific terrain, named commanders, precise stratagems, supply line problems, political intrigue, and the spiritual dimension of warfare. They're *already* a strategy game design document.

Nobody has made this game. The LDS gaming market is mostly word games and trivia. This is the game that treats the material with the seriousness and craft it deserves — not as a teaching tool, but as a *real game* that happens to be set in a world that millions of people care deeply about.

Captain Moroni is one of the most compelling military figures in any scripture. Let the player walk in his shadow.

---

*"If all men had been, and were, and ever would be, like unto Moroni, behold, the very powers of hell would have been shaken forever." — Alma 48:17*
