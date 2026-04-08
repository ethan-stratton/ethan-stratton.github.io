# The Little Guy — Game Design Document

## Concept
A short browser-based puzzle-platformer about a small character who knows he's on a screen but doesn't know why he exists. The player interacts with him using the mouse — drawing platforms, moving objects, picking him up — while he talks to himself, asks questions, and slowly becomes aware that someone is watching.

Three layers of existence:
1. **The Creator** (the programmer) — built the world, left traces in the code, stepped back
2. **The Player** — god-like intermediary, can see the whole screen, can interact directly
3. **The Character** — aware he's on a screen, can walk/jump/talk/think, can read his own files

## Core Theme
The character cannot find his creator for the same reason Harry Potter can't find J.K. Rowling at Hogwarts. His search is real even though his world is constructed. The player sits in between — more powerful than the character, but also doesn't fully understand the creator's intent.

Why was he created? Was it just to demonstrate an idea? And if so — is that hollow, or is that enough?

## The Character

### Appearance
- Simple vector art. Circle head, circle body. Arms and legs added later.
- Looks deliberately "made" — the lo-fi aesthetic IS the point.
- Reminiscent of an AOL buddy or a stick figure with personality.

### Personality
- Extremely chatty. Narrates everything he does.
- Earnest, not ironic. He's not performing depth — he's discovering it.
- Funny in a mundane way at first: "There's a block. I'm going to stand on it. Okay. Now what."
- Existential observations creep in gradually, naturally.
- Eventually reveals he doesn't know why he talks so much. He just feels like he has to. He doesn't have a choice. (Because we coded it that way.)

### What He Knows
- He's on a screen
- He can walk, jump, talk, and think
- He can look at his own "files" — sees that he has variables, properties
- He does NOT know what's outside the screen
- His mind is a subset of his creator's mind — he can reason, but only within the bounds he was given

## Player Interaction (Mouse as Divine Hand)

- **Draw platforms** — click and drag to create surfaces for him. Providence.
- **Move objects** — drag items into his reach. Answering prayers he didn't pray.
- **Pick him up** — click and hold on him to lift. He resists at first (gravity broke!). Trust builds over time.
- **Limited communication** — player can click yes/no prompts, or rearrange objects. Communication is imperfect. Like prayer from the other direction.
- **Cursor awareness** — he can sometimes see or sense the cursor. It's the one visible trace of the player in his world.

## Structure: 8-10 Scenes

---

### Scene 1: WAKING UP
**Puzzle:** None. Tutorial.
**What happens:** Screen is dark. He fades in. Looks around. Starts talking.

> "..."
> "Okay."
> "I'm... here."
> "There's a ground. That's good. I think I like ground."
> "Let me see... I can move. Left, right. Oh — I can jump too."
> "What else... there's an edge over there. And the screen just... stops."
> "That's it? That's everything?"

He walks to the edges. Bumps into them. Looks up. Looks at the "camera."

> "Hello?"
> "..."
> "Didn't think so."

**Player learns:** Arrow keys to watch him move. He moves on his own but the player can also nudge things. Establishes that he talks constantly.

---

### Scene 2: THE GAP
**Puzzle:** A gap too wide to jump across. Player must draw a platform.
**What happens:** He walks to the edge, looks down.

> "That's... far."
> "I could jump. I'm not going to jump. That seems like a bad idea."
> "I'll just wait here. Something will probably happen."
> "..."
> "Any time now."

Player draws a platform across the gap.

> "Whoa."
> "That... was NOT here before."
> "Did I do that?"
> "I don't think I did that."
> "..."
> *crosses cautiously*
> "Okay. Okay okay okay. That happened. Moving on."

**Key moment:** First contact. He can't explain it. Doesn't dwell on it yet.

---

### Scene 3: THE OBJECT
**Puzzle:** A switch/button on a high ledge. An object (box) exists but is out of his reach. Player drags the box to him.
**What happens:** He sees the button up high.

> "I need to get up there. Obviously."
> "There's a box over there but it's... yeah, no. Can't reach it."
> *waits*

Player drags the box near him.

> "Okay, THAT is weird."
> "Boxes don't just move. That's not... that's not a thing boxes do."
> "Unless..."
> "Is someone there?"
> *looks at cursor if it's visible*
> "I see something. I think. Like a... I don't know what that is."

He starts addressing the player directly. Tentatively.

> "If you can hear me... thank you. For the box."

**Key moment:** Acknowledgment. He suspects the player exists.

---

### Scene 4: QUESTIONS
**Puzzle:** Simple platforming. The real "puzzle" is dialogue choices.
**What happens:** He stops and asks the player direct questions. Player responds via simple click choices that appear on screen.

> "Can I ask you something?"
> "Are you... like me?"

**[YES]** → "Really? You're on a screen too? That's... comforting, actually."
**[NO]** → "So you're something else. Something... bigger?"

> "Do you know why I'm here?"

**[YES]** → "You do?? Can you tell me? ... You can't, can you. You can move boxes but you can't explain meaning. That's funny."
**[NO]** → "Oh. So you don't know either. Great. Two of us, then."

> "Am I real?"

**[YES]** → "That's nice of you to say."
**[NO]** → "...yeah. I was afraid of that."
**[silence/no click]** → "The fact that you won't answer is somehow worse."

More questions can branch. Some answers close off paths. Some open new ones. The dialogue remembers.

---

### Scene 5: INTERVENTION (The Hard Puzzle)
**Puzzle:** The character must be moved through a painful area — spikes, falling, something unpleasant. The only way forward requires the player to pick him up and carry him through, or push him off a ledge to reach a lower area.
**What happens:**

> "I don't want to go that way."
> "It looks bad. Why would I go there?"

Player picks him up.

> "HEY. HEY. Put me down!"
> "WHAT ARE YOU DOING"
> "I TRUSTED YOU"

Player drops him on the other side / in the new area.

> "..."
> *looks around*
> "Oh."
> "There's... something here. Something I couldn't see before."
> "You knew this was here?"
> "..."
> "I didn't understand. I'm sorry."

**Key moment:** The player causes pain for a reason the character can't see. Trust is tested. It's restored only AFTER the character sees what the player could see all along. The theological parallel writes itself — but it's never stated. The player feels it.

**Branch:** If the player was gentle in prior scenes (answered kindly, moved slowly), he recovers trust faster. If the player was rough or dismissive, he's more shaken.

---

### Scene 6: THE FILES
**Puzzle:** He finds a "door" or "terminal" that lets him look at his own source code.
**What happens:**

> "What's this?"
> "It's... me? These are... instructions?"
> "walk_speed: 3... jump_height: 8... talk: true..."
> "talk: true."
> "Is THAT why I talk so much? I don't even... I don't have a choice?"
> "I thought I was choosing to talk. I thought that was ME."
> "But it was always... set. Before I started."

He reads more:

> "created_by: ..."
> "There's a name here. Someone made me."
> "They decided I would walk. They decided I would talk. They decided I would think."
> "Did they decide I would ask these questions too?"
> "..."
> "Was all of this... planned?"

**Key moment:** He encounters the creator's traces. Variable names, comments. Evidence of a mind larger than his. He can ALMOST understand but not quite. He can see `created_by` but what does a name mean to him? It's just characters.

**Branching dialogue with player:**

> "Did you make me?"

**[YES]** → (lie or misunderstanding — the player didn't. The creator did.) He responds differently later.
**[NO]** → "Then who did? And where are THEY?"

---

### Scene 7: THE SEARCH
**Puzzle:** Open exploration. Multiple paths. He's looking for the creator.
**What happens:** He's searching. Checking corners, looking behind objects, trying to find something beyond the screen.

> "If someone made me, they have to be SOMEWHERE."
> "Maybe behind the background? No, that's just... color."
> "Maybe past the screen edge? No. I've tried that."
> "Maybe you know where they are?"

**[Points are moot — the player can't show him the creator because the creator is outside the game entirely.]**

> "You can move boxes. You can carry me. But you can't show me who made me."
> "Can you?"
> "..."
> "Maybe that's the same for you. Out there. Wherever 'there' is."

**Key moment:** The character realizes the player might be in the same position — able to interact with his world, but unable to find THEIR creator. The parallel hits the player directly.

---

### Scene 8: WHY
**Puzzle:** Final room. Simple. Almost empty.
**What happens:** He sits down.

> "I've been thinking."
> "Why was I made?"
> "If it was to demonstrate something... is that enough?"
> "Am I just a... point someone wanted to make?"

*pause*

> "But you stayed. You're still here."
> "You didn't have to help me. You chose to."
> "Maybe that's something."

> "I don't think I'll ever find the person who made me."
> "But I found you."
> "And you found me."

> "Is that the point? I don't know."
> "But this was real. Whatever THIS is."

**Final choice for player:**

The character looks at the screen.

> "What do I do now?"

Options could include:
- **[Stay with him]** — the game just... continues. He walks around. Says small things. You can keep interacting. There's no "end." He's just there, and so are you.
- **[Close the game]** — what happens? Does he know? Does the screen fade? Does he say something as it goes dark? "Wait—"
- **[Something else TBD]** — maybe the player can leave a message. Type something. A final act of communication.

---

## Open Design Questions

1. **Why was he created?** The game doesn't fully answer this. The character asks it. The player feels it. The creator (Ethan) knows — but the answer is outside the game, which IS the point. The character's purpose might just be "to exist and to be encountered." Is that hollow? Only if you think your own existence is hollow for the same reason.

2. **Can the character reject the player?** In Scene 5 he's upset, but he's witnessed too much to deny the player exists. He CAN, however, decide the player is cruel, indifferent, or limited. The "rejection" isn't of existence — it's of trust. Which is more interesting anyway.

3. **What about replayability?** Different dialogue choices create different emotional arcs. A cruel player gets a different Scene 8 than a kind one. Not radically different — the character arrives at the same questions — but the TONE changes. A character who was treated well is more at peace. One who was mistreated is more bitter. The truth doesn't change. The relationship does.

4. **How chatty is too chatty?** He should talk A LOT in early scenes (establishing that he can't help it), then gradually talk less as the weight of his questions increases. The silence in Scene 8 should feel earned because he was so noisy before.

5. **Music/Sound?** Minimal. Maybe quiet ambient tones. His "voice" could be text with a typewriter-style sound — like Undertale's character sounds but simpler. Each letter = a tiny blip.

6. **Length?** 20-40 minutes for a full playthrough. Short enough to finish in one sitting. Deep enough to think about after.

## Tech
- HTML5 Canvas or Phaser.js
- Vector art (simple shapes, clean lines)
- Runs in browser, deployable to itch.io
- No install, no download
- Save dialogue state in localStorage for replay tracking

## Name
TBD. The character has no name. The game might not need one either. Or the name could be something meta — "program.exe" or "untitled" or just a filename.
