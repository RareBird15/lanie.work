---
title: "Everrealm: A Game I Built Because Nobody Else Would"
date: 2026-07-14
lastmod: 2026-07-14
categories:
  - Gaming
tags:
  - accessibility
  - game-dev
  - blindness
  - neurodivergent
  - screen-reader
  - everrealm
slug: everrealm-alpha-playtest
description: >
  I built a screen-reader-first kingdom builder because I can't play the games
  the audiogame community keeps making. The alpha is live, the feedback is
  coming in, and it works.
---

I can't play most games made for blind people.

That sentence used to feel like a confession. Now it's just a fact. I have
topographical agnosia, which means I can't build mental maps of spatial
environments. I have auditory processing issues that make spatial audio feel
like noise instead of information. I get overstimulated by too many sounds at
once. Most audiogames rely on at least one of those things, usually all of
them. I've bought games that were recommended specifically for blind players,
only to discover that the grid gets too complex for me to track, or the audio
cues pile up faster than I can process them.

I spent a while being frustrated about this. Then I decided to build something
instead.

## What Everrealm Is

[Everrealm](https://everrealm.lanie.work) is a browser-based kingdom-building
game. You start with tents and build your way toward citadels. You establish
settlements, develop them by merging pairs into higher-level buildings, unlock
discoveries that enable special structures, and guide your realm through six
Ages.

There's no combat, no timers, no fail states. Every action is initiated by
you. The game waits patiently while you think.

The design choices aren't accidents. They're responses to specific access
barriers I've hit over and over:

- **No spatial grid.** Every building is a list entry, not a position on a
  map. You don't need to know where anything is. You just need to know what
  it is.
- **No required audio.** The game communicates through semantic HTML and ARIA
  live regions. Your screen reader tells you what happened. No spatial audio to
  interpret, no sound cues to miss.
- **Keyboard shortcuts for everything.** E to establish, A to advance, T
  through I to develop settlements, and so on. No dragging, no mouse
  coordinates, no canvas elements that screen readers can't see.
- **Saves locally.** No account, no login, no server. Your realm lives in
  your browser.

I built it with AI assistance because I don't have a game dev background. I
built it because I wanted to prove that accessible games can be genuinely fun,
not just "accessible enough." The code is [open source on
GitHub](https://github.com/RareBird15/everrealm).

## The Alpha Is Live

I posted the playtest on [AudioGames.net](https://audiogames.net), which is
the largest community of blind gamers and audiogame developers. The response
has been encouraging in ways I didn't expect.

### Three Platforms, Three Confirmations

The game has been tested on three different screen reader and browser
combinations so far:

| Player | Screen Reader | Browser | OS |
| -------- | -------------- | --------- | ----- |
| Me | NVDA | Chrome | Windows |
| JaceK | Orca | Firefox | Linux |
| fluffy | VoiceOver | Safari | iOS |

JaceK is a high-reputation community member (nearly 600 karma on the forum),
so his confirmation that it works on Firefox and Orca on Linux carries weight.
fluffy confirmed it works on iOS with VoiceOver, which was a relief because I'd
only tested with NVDA in Chrome myself.

### Mechanics Feedback

JaceK was confused about how settlements, capacity, and prosperity connect.
That's useful feedback because it means the UI isn't making the relationship
clear enough yet. I explained the loop for him in the thread:

> Earn Prosperity, establish settlements, develop them by merging (which frees
> capacity and earns more Prosperity), buy improvements to boost your rate,
> fill your capacity, build toward 2 Citadels, advance to the next Age.

The fact that he needed the explanation means I need to make that connection
more discoverable in the game itself. That's exactly the kind of feedback I was
looking for.

### Sound

fluffy asked for sounds to be added. I want to be upfront about this, the same
way I was on the forum: sound might come in the future, but Everrealm will
never be a full audiogame. I have a combination of disabilities that means I
can't interpret spatial audio, and I get overstimulated by too many sounds at
once. That's part of why there's no spatial grid at all. If I add sound, it
will be optional, minimal, and never required to play.

## What I'm Looking For

The alpha is open. If you use a screen reader, I want to know:

- Does it work with your setup? Any announcement issues?
- Is the game flow clear? Can you tell what's happening and what your options
  are?
- Is it fun? What feels satisfying? What feels tedious?
- Balance feedback. How long does it take to reach your first Citadel? Does
  the economy feel right?
- Any bugs or confusing error messages.

I'd especially love feedback from JAWS users, since I haven't been able to
test with JAWS yet.

## Play

[Play Everrealm](https://everrealm.lanie.work) in your browser. Just open the
link and name your realm. The game walks you through the rest.

If you want to look under the hood or contribute, the code is on
[GitHub](https://github.com/RareBird15/everrealm). There's also a
[downloadable v0.1 release](https://github.com/RareBird15/everrealm/releases)
if you want to play locally.

## Why This Matters

I built Everrealm because I wanted a strategy game that actually works with my
access needs from the ground up. Not a game that was made accessible after the
fact. Not a game that technically works with screen readers but overwhelms my
nervous system. A game designed for players like me first, and everyone else
second.

The forum feedback tells me the approach works. Three screen readers, three
browsers, three operating systems, and it works. That's not nothing. That's the
thing I was trying to prove.

Come play it. Tell me what breaks. Tell me what's fun. Tell me what's
confusing. I built this for us, and I want it to be good.
