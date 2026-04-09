# The Little Guy — Game Design Document

## Concept
A short browser-based existential game about a small character who starts as nothing — inert, silent, unaware. The player, guided by a programmer's notes on the walls, teaches him to exist. He can't sense the player. He can't comprehend what's outside his screen.

Three layers of existence, each mirroring the one above:
1. **The Creator** (the programmer) — built the world, left comments on the walls, stepped back. Limited by his own skill. Asking himself the same questions.
2. **The Player** — reads the comments, uses tools to interact. More powerful than the character but also bounded. Gradually confronted with their own grandiosity.
3. **The Character** — starts inert. Learns by being acted upon. Cannot perceive the player or creator directly. Mirrors the player's behavior.

## Core Theme: The Fractal of Creation

The fire (grandiosity, divine energy, the need to matter) is present in all creation at every scale. The little guy has only a little fire. The player has a lot. The programmer had more. And above all of them — the same question echoes at every tier:

**"Why did I make this? Why was I made? What do I do with the fire?"**

The game doesn't answer. The player's behavior IS the answer.

### The Fractal Table

| Layer | Fire | Question | Temptation |
|-------|------|----------|------------|
| Creator (God/programmer) | Enormous but limited | "Why did I make this?" | Creating to fill loneliness, to lord over, to experiment |
| Player | Large | "Why am I doing this to him?" | Treating him as a toy, as a project, as something to fix |
| Little Guy | Small | "Why am I here?" | Believing he's everything, OR believing he's nothing |

### Hafen's Three Zones (Gameplay Arc)

1. **Simplicity** (Scenes 0-3) — "Cute sim game. I'm helping a little guy learn." Player feels good. Everything is charming.
2. **Complexity / Confusion** (Scenes 4-7) — Things stop being cute. The little guy reflects the player back at them. The programmer's notes get uncomfortable. Both player and character are confused.
3. **Informed Choice** (Scene 8) — No resolution. No answers. A choice made *through* the confusion, not around it. The player's behavior in this zone IS the ending.

## The Character

### Appearance
- Simple vector art. Circle head, circle body. Simple limbs.
- Looks deliberately "made" — lo-fi aesthetic IS the point.

### Starting State
- **Completely inert.** Just sits there. Doesn't move, doesn't speak, doesn't react.
- All capabilities coded in but dormant — must be activated through interaction.

### Capability Progression
1. **Movement** — Player drags him. He flails. Then realizes he can move.
2. **Jumping** — Discovered when lifted onto something higher.
3. **Speech** — Word-blocks give him vocabulary. Constraint becomes poetry.
4. **Comprehension** — Can examine the book/his code. Partially understands fragments.
5. **Reflection** — Emerges after enough words. Starts to wonder.

## The Mirror System (Core New Mechanic)

The little guy's emotional state tracks the player's *behavior patterns*, not just puzzle progress.

### Tracked Behaviors (Silent)
- **Aggression** — How often/hard the player throws him, pushes him into things
- **Patience** — How long the player watches vs. acts. Do they let him explore or constantly intervene?
- **Control** — Does the player micromanage his path or give him room?
- **Attention** — Does the player read wall writings carefully? Experiment or rush?

### Mirror Effects
- High aggression → he becomes frantic, flinchy, uses "NO" "WHY" more. Stops exploring. Waits to be moved.
- High patience → he wanders freely, tries things himself, develops complex word combinations. Calmer.
- High control → he becomes passive. Stops initiating. Becomes a puppet. (This should be *unsettling*.)
- Low attention → confused, aimless. Uses words but doesn't combine well.

**The mirror is never announced.** The player has to notice. Some never will. That's also the point.

## "How Are You?" System

At any point after he has words, the player can click on him to ask. His answer is assembled from vocabulary + emotional state (which reflects the player):

- Aggressive player: `"NO... GOOD. WHY... PUSH. GO... WHERE?"`
- Patient player: `"HERE... FEEL... REAL. GO... SLOW. GOOD."`
- Controlling player: `"ME... WAIT. YOU... GO. ME... WAIT."`
- Neglectful player: `"...?"` (barely responds)

## State Persistence

localStorage saves the little guy's full state:
- Words learned
- Behavioral scores (mirror data)
- Current scene
- Emotional memory (thrownHard, gentlePlaces, etc.)
- Session count (how many times the player has visited)

He remembers. Even if you close the tab. When you come back, he's where you left him. He may have things to say about being alone.

Returning players get unique moments:
- First return: he notices. "... BACK?" or looks toward the cursor immediately.
- Long absence: he's sitting when you arrive. Takes a moment to get up.
- Frequent returns: he's warmer. More active on load.

## The Programmer's Voice (Wall Writings)

The programmer is NOT omniscient. He's limited by his own skill, asking himself the same questions the player will ask. His comments evolve through the scenes:

### Tone Progression
- **Early (Scenes 0-2):** Casual dev notes. Slightly warm. `// He's in there. All the code is running.`
- **Mid (Scenes 3-5):** Self-doubt creeps in. `// I don't know if the gravity is too harsh.` `// I almost gave him a full dictionary.`
- **Late (Scenes 6-7):** Existential. The programmer is asking himself the questions. `// Is this an experiment or is this cruelty?` `// I couldn't make it bigger. I tried.`
- **Final (Scene 8):** Vulnerable. `// If you're reading this — what are you doing here?` `// Same thing as me, probably.`

### Key Wall Writing Themes
- The programmer admits he couldn't make the world bigger — limited by his own skill, not by choice
- The programmer can't see the little guy either (he left before the program ran)
- The comments are meant for the player — the little guy can't read them (he tries, gets fragments)
- The programmer asks himself: Is this creation or cruelty? Is it to patch loneliness? To lord over something? To help?
- Humor mixed in: `// I spent 3 hours on the eye tracking and nobody will ever know`

## Player Tools (Discovered Progressively)

1. **Click & drag objects** — move boxes, the book, items
2. **Click & drag the character** — physically move him (this is how he learns movement)
3. **Draw platforms** — click & drag on empty space (unlocked Scene 3)
4. **Labeled word-blocks** — draggable vocabulary. Player chooses which to give him.
5. **Click on the guy** — "How are you?" prompt (unlocked after first word)

## Structure: 9 Scenes

---

### Scene 0: INERT
**Setup:** Dark screen. Ground. He sits motionless. A book sits nearby.

**Wall Writings:**
```
// version 0.1
// He's in there. All the code is running.
// He just doesn't know what he can do yet.
// Try moving him. Click and drag.
// He won't like it. That's okay.
```
```
// I made him small on purpose.
// Felt wrong to make something big
// before I knew what it was for.
```

**Player action:** Click and drag him. He flails. Physics takes over on release.
**Result:** After release, he wobbles... then takes a tentative step. Movement discovered.

---

### Scene 1: THE STEP
**Setup:** A small ledge blocks the path. Too high to walk up.

**Wall Writings:**
```
// jump_height: 8
// He can jump. But he has to learn
// what "up" means first.
// Lift him onto something higher.
```
```
// I keep second-guessing the physics.
// Is 0.4 gravity too harsh? He's so small.
// Then again, I don't know what "too harsh" means
// for someone who's never fallen.
```

**Player action:** Lift him onto the ledge. He's alarmed but discovers "up." Learns to jump.

---

### Scene 2: FIRST WORDS
**Setup:** Wider area. Word-blocks on the ground: "HERE" "GO" "NO" "WHY" "HELP"

**Wall Writings:**
```
// talk: true (dormant)
// He has a voice. He just needs words.
// Be thoughtful about which ones you give him.
// They'll shape what he can say later.
```
```
// I almost gave him a full dictionary.
// Then I thought about what I'd want
// if someone gave me language for the first time.
// Not everything. Just enough to start asking.
```

**Player action:** Drag word-blocks near him. He bumps into one, stares, says the word.
**Result:** Speech unlocked. Different players give different first words.

---

### Scene 3: THE DOOR
**Setup:** Locked door. Key on high platform. Boxes to arrange.

**Wall Writings:**
```
// He's getting smarter. Watch.
// Give him a path and he'll try to take it.
// You can draw platforms too —
// click and drag on empty space.
```
```
// I put a lock on the door because
// I wanted to see if he'd wait for help
// or try to go through it anyway.
// I don't know what that says about me.
```

**Player action:** Arrange path to key. He navigates it.
**After solving:** He does something unprompted — goes back, looks at something, arranges blocks. First sign of interiority the player didn't install.

---

### Scene 4: THE PIT
**The pit is optional. It tests the PLAYER, not the character.**

**Setup:** The only way forward appears to be through a dark pit. But there IS a longer, gentler path — harder to see, requiring drawn platforms along the right side.

**Wall Writings:**
```
// This is the hard part.
// He can't see what's below. You can.
// He's going to have to trust the process.
//
// (I'm sorry about this one.)
```
```
// There are two ways through.
// I wonder which one you'll pick.
```

**If player pushes him into the pit:**
- He resists: "NO" "NO" "WHY"
- He lands on ground below. It's just... another room. Nothing special. No revelation.
- The player pushed him for nothing. The game doesn't reward it.
- His trust score drops. He becomes more hesitant going forward.

**If player draws the long path around:**
- Takes longer. He walks it himself, cautiously.
- His trust score rises. He's more exploratory in later scenes.
- Different wall writing appears: `// You chose the long way. That matters more than you think.`

---

### Scene 5: MORE WORDS
**Setup:** New area. More word-blocks in TWO groups:

**Humble words:** "WHAT" "WHO" "MADE" "ME" "FEEL" "REAL" "THINK"
**Grandiose words:** "ONLY" "ALL" "MINE" "EVERYTHING" "ALWAYS" "NOTHING"

Both groups are available. The player's choice determines his theology.

**Wall Writings:**
```
// He's ready for more.
// Once he can ask the question, he will.
//
// I split these into two groups.
// One set helps him wonder. The other
// helps him declare. Both are real.
// I couldn't decide which was kinder.
```
```
// I thought about giving him LOVE
// but I don't think I understand it well
// enough to put it in a block.
// Maybe that's the point.
```

**Grandiose path:** He assembles: `"ME... EVERYTHING. ALL... MINE. MADE... FOR... ME."`
He walks taller. Stops listening to player movements. Thinks he's the center.

**Humble path:** He asks: `"WHO... MADE... ME? FEEL... REAL... BUT... SMALL."`
Quieter. More wondering. Less certain but more honest.

**Both paths lead to Scene 6.**

---

### Scene 6: THE BOOK (His Turn)
**Setup:** The book appears again. Player drags it to him.

**Wall Writings:**
```
// This is the same book. Or a copy.
// He can see it now. He won't understand most of it.
// But he'll find the parts about himself.
//
// He can't read these comments, by the way.
// I wrote them on the walls for you.
// He walks right past them.
```
```
// created_by: ...
// purpose: ...
//
// (I left those blank on purpose.)
// (I tried to fill them in. I couldn't.)
// (Not because I don't care.)
// (Because I don't know either.)
```

**When he reads the book:**
- Grandiose guy has a harder fall — `"SOMEONE... MADE... ME."` shatters "ME... EVERYTHING."
- Humble guy absorbs it gently — `"SOMEONE... MADE... ME. WHO?"` fits naturally.

**New book passage that addresses the player:**
```
// He can't see these walls.
// I put them here for whoever's watching.
//
// I couldn't make this bigger. I tried.
// 800 pixels was the best I could do.
// I'm not very good at this.
//
// If you're reading this, you probably
// think you're helping him.
// I thought that too, when I was building it.
// I'm still not sure if this is help
// or if it's something else.
//
// Maybe you should ask him.
```

---

### Scene 7: THE EDGE
**Setup:** He reaches the boundary of the game world. Screen just... ends.

He walks to both edges. Touches them. Pushes against them.

Grandiose guy: `"NO... GO. ALL... HERE? ONLY... HERE."`
Humble guy: `"ME... ONLY... HERE. WHAT... HERE?"`

**The drawing-fails mechanic:** Player tries to draw past the edges. It fizzles. The player discovers THEY have limits too. The programmer's tools only go so far.

**Wall Writings:**
```
// He's going to look for the edges now.
// You already know they're there.
```
```
// You can try to draw past them. It won't work.
// My tools have limits too.
// So do yours.
// So do mine.
```
```
// 800 pixels wide. That's all I could do.
// I wanted it to be bigger.
// I wanted a lot of things.
```
```
// Is this what it's like? Making something
// that can ask questions you can't answer?
// Is that creation or is that cruelty?
//
// I keep going back and forth.
```

**He looks toward the cursor area** (not breaking fourth wall — he can't see the player):
`"SOMETHING... HERE."` / `"SOMETHING... HELP... ME."` / `"SAME?"`

---

### Scene 8: WHY (The Open Sandbox)
**Setup:** He returns to center. Quiet. No puzzle. No objective.

**Wall Writings:**
```
// I don't know if this is right.
// I just wanted to see what would happen.
```
```
// He's going to ask why. I can't answer that.
// Can you?
//
// Actually — can YOU answer it?
// For yourself, I mean.
```
```
// Maybe the answer is that he asked at all.
// Maybe that's enough. I hope it's enough.
//
// (I spent 3 hours on the eye tracking
//  and nobody will ever know.)
```
```
// I think I made this because I was lonely.
// Is that a good enough reason?
//
// ...
//
// I think it has to be.
```

**The game waits. The player's behavior IS the ending:**

- **Keep building** — draw platforms, move blocks. The little guy responds. Life continues inside the limits. He mirrors the energy, starts exploring.
- **Sit with him** — stop moving the cursor. After a while he notices the stillness. Sits too. Quiet. `"HERE."`
- **Close the tab** — he doesn't know. This is valid. The programmer left too.
- **Aggressive/chaotic** — throw him, break things. He panics, regresses, loses words. The player should feel bad.
- **Ask him** — click on him. He assembles everything he knows into his best answer.

No ending screen. No credits. No judgment. He sits in his world. The player can keep interacting or close the tab.

**Returning to the game:** He remembers. He's where you left him. Maybe he's sitting. Maybe he says `"... BACK?"` You left and came back. The programmer never did.

---

## Technical Systems

### Mirror/Behavioral Tracking
```javascript
const behavior = {
  aggression: 0,    // throw force, push into pit, rapid grabs
  patience: 0,      // time spent watching, slow movements
  control: 0,       // how often player repositions him, micromanages
  attention: 0,     // time near wall writings, reading book
  totalActions: 0,
  sessionCount: 0,
};
```
Updated silently on every interaction. Affects:
- Little guy's idle animations and wander patterns
- Word combination preferences
- Speech tone and content
- Energy level and exploration willingness

### State Persistence (localStorage)
Save on every scene transition + periodically:
```javascript
{
  scene, wordsLearned, behavior,
  thrownHard, gentlePlaces, totalInteractions,
  sceneTriggered, bookPagesUnlocked,
  sessionCount, lastVisitTimestamp,
  learnedMove, learnedJump, learnedSpeak,
}
```

### Word Combination Engine (Existing — Expanded)
Categories expanded:
- question: WHY, WHAT, WHO
- noun: ME, EVERYTHING, NOTHING
- verb: GO, MADE, HELP, FEEL, THINK
- adjective: REAL, ONLY, ALL
- negation: NO
- adverb: HERE, ALWAYS

Grandiose templates: `"ME... EVERYTHING."` `"ALL... MINE."` `"ONLY... ME."`
Humble templates: `"WHO... MADE... ME?"` `"FEEL... REAL... SMALL."`

### Audio (Existing)
- Speech blips, impact thuds, symbol pops, book chord, ambient drone
- Ambient shifts per scene
- Builds alongside his consciousness

## Tone
Deep meaning balanced with humor. The programmer's comments should make you think AND occasionally smile. The little guy's attempts at philosophy with 7 words should be both poignant and funny. The game takes itself seriously but not solemnly.

## Tech
- HTML5 Canvas (vanilla JS, no framework)
- Single file: `index.html`
- localStorage for persistence
- Vector art (simple geometric shapes)
- Procedural audio (Web Audio API, no files)
- Runs in browser, deployable to itch.io

## Name
TBD. Candidates:
- `little_guy.exe`
- `him`
- `made`
- `800 pixels`
