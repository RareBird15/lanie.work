---
title: "The MUD That Got It Right: How Erion Makes Text Gaming Accessible"
date: 2026-08-02
draft: false
categories:
  - Gaming
tags:
  - accessibility
  - erion
  - mud
  - nvda
  - screen-reader
  - usability
slug: erion-accessibility-review
description: >
  Most MUDs are technically accessible because they're text-based, but
  Erion is the only one I can actually play. Here's what it does that
  every other MUD gets wrong.
---

I wrote last year about gaming as a blind, neurodivergent, chronically ill
woman. I said MUDs should work for me because they're text-based, but they
usually don't. The problem is topographical agnosia. Room-based navigation
without explicit directions means I spend more energy trying not to get
lost than I do playing the game.

I've been playing Erion for two days now. It's the first MUD I've played
where I'm not fighting the interface to access the game.

This isn't a WCAG audit. It's a report from someone who is blind, autistic,
has rheumatoid arthritis, chronic fatigue, and topographical agnosia, and
who has tried more MUDs than I can count. Most of them lost me within an
hour. Erion didn't. Here's what it does differently.

## Screen Reader Mode That Actually Changes Things

Erion has a `screenreader` toggle built into the game. You can turn it on
during account creation or with a command after you're in. It's not a
token gesture. It changes how the game sends information to you.

When screen reader mode is on, the game:

- Silences room names and descriptions while you're running to a
  destination. You don't hear every room you pass through. When you
  arrive, the game automatically shows you the room.
- Strips symbols from room names so they read cleanly.
- Turns off mob flags like (E) for Evil that add visual noise without
  adding information.
- Condenses combat messages into short single lines instead of
  multi-line spam blocks.
- Turns off the side map, which is visual and useless to me.
- Replaces important punctuation with words. Help file references show
  as "Help 3 dot class" instead of "help 3.class" so screen readers that
  ignore punctuation still read the instruction correctly.
- Moves door states before exit directions: "Locked East" instead of
  "East (locked)," so the information comes first instead of after the
  direction.
- Replaces ASCII art with text. The level-up graphic becomes a text
  message. The hangman game replaces its ASCII gallows with text.
- Turns off login notifications so you're not interrupted by "X has
  logged in" messages.
- Enables tell buffering so messages wait for you instead of vanishing
  before you can read them. Type `replay` to see them.

That's not one feature. That's a dozen features, all designed to reduce
spam and present information in the order a screen reader user needs it.

There's also a `tts` command that toggles speech on and off. When I type
`tts`, NVDA says "speech off" and the game stops speaking through
MUSHclient. I can still type commands and manually review the output
buffer, but I'm not hearing every line of game text in real time. This
is useful when I want to listen to music or talk to someone without
leaving the game.

## The Soundpack

Erion ships with a MUSHclient soundpack that you download from their
blind support page. It's not an add-on someone in the community built
three years ago and stopped maintaining. It's part of the game, and it
has an installer that sets up both Git and MUSHclient for you. You
download, unzip, double-click `installer.bat`, and you're ready to play.

The soundpack gives you:

- **F11 and F12** to turn volume up and down.
- **F10** to switch between volume categories: sound effects, ambiance,
  and music.
- `sound off` and `sound on` to disable or enable everything.
- `sound ambiance`, `sound music`, `sound combat`, `sound weather` to
  toggle individual categories.
- `sound toggle <keyword>` to disable a specific sound you don't want to
  hear.
- `sound print` to identify what sound is currently playing, so you
  know what to toggle off.

That last one matters. If a sound is annoying me, I can find out what
it is and turn it off without turning off everything else. That level of
granular control is more than most mainstream games offer.

The soundpack also supports custom sounds. Drop a file in the custom
sounds folder and it plays when your custom channel receives a
message. You can add sounds for community-created channels without
modifying the core soundpack.

Under the hood, the soundpack uses MSP, the MUD Sound Protocol. Erion
detects when your client supports it and enables it automatically. The
protocol triggers sounds based on game events, so the audio feedback is
tied to what's actually happening, not just ambient noise.

## Hotkeys That Respect TTS

The soundpack includes hotkeys that report game state:

- **F1** reports HP as a percentage.
- **Shift+F1** reports hitpoints in full.
- **F2** reports mana as a percentage.
- **Shift+F2** reports mana in full.
- **F3** reports experience needed to level.
- **F7** recalls you to safety.

Here's the part that shows someone was thinking. F1, F2, Shift+F1, and
Shift+F2 all work even when you've toggled speech off with the `tts`
command. So I can mute TTS to listen to music or a conversation, and
still check my health and mana with a single keypress.

The accelerator keys go further. The soundpack keeps a history of
events like channel messages, and you can replay them:

- **Alt+Left/Right** moves between category buffers.
- **Alt+1 through Alt+0** reads the 1st through 10th latest message in
  the current buffer.
- **Alt+Up/Down** moves through messages in the current buffer.
- **Alt+PageUp/PageDown** jumps 10 messages at a time.
- **Alt+Home/End** jumps 2000 messages at a time.
- **Alt+Space** repeats the currently selected message.
- **Alt+Shift+Space** copies the selected message to the clipboard.
- **Alt+Enter** opens URLs in the current message.
- Pressing a message key twice within half a second copies the message
  to the clipboard. Three times pastes it into the command window.

This means I can go back and read something I missed without scrolling
through the output buffer. The game keeps the history for me, organized
by category, and I can navigate it with keystrokes that don't conflict
with NVDA.

## Navigation That Doesn't Require a Mental Map

This is the feature that made me stay.

`runto <area name>` automatically walks me to any area from any room.
I don't need to know the path. I don't need to build a mental map of
rooms and exits. I type `runto holy grove` and my character runs there.

The `dirs <area name>` command prints out a list of directions to any
area from my current position. So if I want to learn the path, I can.
But I don't have to.

`stop` halts the run if I need to interrupt it. `toggle open` makes the
runner automatically open or unlock doors along the way.

In my earlier gaming post, I said that without a `dirs` command, I
spend more energy trying not to get lost than I do playing the game.
Erion has both `dirs` and `runto`. Problem solved.

Waypoints let me save locations for fast travel. `waypoint save` in a
waypoint room. `waypoint <number>` to travel there. `waypoint recall`
to set my recall point. I can build a travel network without ever
needing to visualize the world map.

## Text That's Structured for Screen Readers

Room descriptions, items, mobs, and exits all follow a consistent
format that NVDA can parse linearly:

- Room name on its own line.
- Room description as a paragraph.
- Items on the floor with counts in parentheses.
- Mobs with level labels: `(x1)(Level 13) A doe is here, munching on
  grass.`
- Exits in brackets: `[Exits: north east south west up]`

Nothing is hidden in visual formatting. Nothing requires me to
interpret a graphic or parse a table. Everything reads in order.

## Commands Designed for Keyboard Efficiency

Erion has small features that reduce typing and cognitive load, and
several of them seem designed with disabled players in mind.

Spells have numbers. `showspell magic slash` shows me that Magic Slash
is spell number 832. I can cast it by typing `cast 832` instead of
`cast 'magic slash'`. Shorter, faster, and easier to remember once you
learn the numbers.

The `autoskill` feature automatically executes a skill or spell in
combat without repeated typing. The help file says: "Inspired by
players concerned about carpal tunnel." That's the first time I've
seen a game acknowledge carpal tunnel in a help file. With RA, not
having to type the same spell name every combat round is the difference
between playing for an hour and playing for twenty minutes.

The errand system tests game knowledge through multiple choice
questions typed as `errand solve c`. No interactive menu. No visual
selection. No timed response. Just a question, four letter options,
and a typed answer. I can pull up the relevant help file, read it,
and answer at my own pace.

Help files are numbered. `help death` shows a list of related help
topics. `help 1.death` opens the first one. In screen reader mode, the
game writes it as "Help 1 dot death" so my screen reader reads the
number correctly instead of skipping the punctuation. I don't have to
guess exact keywords or type long filenames. The number system means I
can navigate help files with single digits.

The `db` command lets me search for equipment without memorizing where
anything is. I set preferences and run a search:

`db prefs minlevel 40`
`db prefs maxlevel 50`
`db prefs slot shield`
`db search`

The game returns matching items from across the world. I don't have to
remember which area drops a shield I need. I don't have to ask other
players where to find gear. I search, I see results, I go get it. For a
blind player who can't build a mental map of the world, this is the
difference between being self-sufficient and being dependent on
sighted players' knowledge.

## A Community That Knows We're Here

Erion has a `client` channel specifically for soundpack and MUSHclient
questions. The blind support page on their website has the soundpack
download, an installer, update instructions, reset instructions, and
troubleshooting. When someone asked on the global channel whether the
soundpack was only available for MUSHclient, another player responded
with help.

The screen reader help file ends with: "If you use a screen reader and
have suggestions for how we can improve the game for you, please let us
know by writing an idea note." They're not just tolerating blind
players. They're asking for our feedback.

I've been in MUDs where accessibility is an afterthought someone
mentioned on a forum once. Erion treats it as part of the game.

## Why This Matters: A Brief Contrast

Alter Aeon is the other MUD that comes up when you search for blind-accessible
text games. It's popular in the blind community, and it has a custom MUSHclient
soundpack called Mush-Z. On paper, it should work for me. It doesn't.

Alter Aeon has no `runto` or `dirs` command. Navigation is manual. You walk
room by room, or you use a movement pad that maps Alt+I to north, Alt+K to
south, and so on. But knowing which direction to go is the whole problem.
With topographical agnosia, I can't build a mental map of rooms I've been
through. A movement pad gives me a faster way to type directions I don't
know.

The Mush-Z soundpack turns Alter Aeon into something closer to an audiogame.
Health is communicated through heartbeat sounds that speed up as you take
damage. Mana, movement, and experience have audio prompts that replace text.
Battle music changes based on your health or your enemy's health. There are
death quote voiceovers and condition alert sounds. For some blind players,
this works. For me, it's sensory overload. I can't process that much audio
information at once, and I can't read the text when the soundpack is
filtering it out.

There's no equipment database search. If I want to find a piece of gear, I
either remember where I last saw it, or I ask other players. In a game with
thousands of items spread across hundreds of areas, that's not a minor
inconvenience. It's a wall.

Mapping in Mush-Z works by recording your directions in a notepad window as
you walk. You can copy those directions later to create speedwalk aliases.
That's a manual workaround for a problem Erion solves with `runto`. It
assumes I can explore without getting lost first.

I'm not saying Alter Aeon is bad. It has a dedicated blind community, and
Mush-Z is a serious piece of work. But it was built for blind players who
navigate by audio and can build spatial memory from repeated exploration. I
can't do either of those things. Erion was built for someone like me: blind,
yes, but also disabled in ways that make audio navigation and spatial memory
unreliable. The difference is that Erion didn't assume one kind of blindness.

## What Other MUDs Could Learn

Most MUDs are technically accessible because they're text-based. A
screen reader can read the output. But "technically accessible" and
"actually playable" are different things, and the distance between them
is where multiply disabled players fall through.

Erion closes that distance with features that aren't complicated:

- A screen reader mode that changes how the game sends information.
- Pathfinding that doesn't require spatial reasoning.
- Equipment search so you don't have to memorize the world.
- A soundpack with granular volume control and an installer.
- Hotkeys that work when TTS is off, plus message history you can
  replay.
- Commands that reduce typing for players with joint issues.
- Help files and answers that don't require timing or visual
  navigation.
- Punctuation replaced with words so screen readers don't miss
  instructions.

None of these features are hard to implement. Most MUDs already have
the text infrastructure. What Erion has that others don't is the
awareness that blind and disabled players exist, and the willingness to
build for us instead of waiting for us to figure it out.

I've been playing for two days. My character is a Spark Mage/Witch
following Aura, the goddess of change, magic, and alchemy. I'm mining
ore in the Holy Grove, running errands for the Quest Mistress, and
exploring a world I can actually navigate.

For the first time in a MUD, I'm playing the game instead of fighting
it.

## How to Connect

Erion is free to play. Connect with any MUD client (MUSHclient, VIPMud, TinTin++) at:

- **Host:** erionmud.com
- **Port:** 1234

The blind support page with the soundpack and setup instructions is at
[erionmud.com](https://erionmud.com).
