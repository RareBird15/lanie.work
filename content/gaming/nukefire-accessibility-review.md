---
title: "NukeFire: A Post-Apocalyptic MUD That Built Accessibility Into the Wasteland"
date: 2026-08-13
draft: false
categories:
  - Gaming
tags:
  - accessibility
  - nukefire
  - mud
  - nvda
  - screen-reader
  - crafting
slug: nukefire-accessibility-review
description: >
  NukeFire is a post-apocalyptic MUD with screen reader profiles, GPS
  navigation, and a crafting system that stores your materials between
  sessions. It's the most accessible MUD I've played since Erion, and
  it does several things Erion doesn't.
---

I wrote earlier this month about Erion, the MUD that finally got
accessibility right. I said it was the first MUD where I wasn't
fighting the interface to access the game. That's still true. But
Erion isn't the only MUD doing this work. NukeFire is another one,
and it does several things Erion doesn't.

NukeFire is a post-apocalyptic wasteland MUD. You're not an elf
in a forest. You're a freejack in the ruins of Tek Angeles,
killing junker robots in a scrapyard and crafting gear from their
parts. The welcome message warns you: "This MUD does not have a
traditional fantasy theme. There may be things here which offend
you." It's gritty, weird, and full of players who've been here
for years.

I've been playing for about a day. My character is a Slinger — the
mage class — named Liora. She's level 40, alignment Evil, and she's
killed more sparkroaches and data grubs than I can count. Here's
what NukeFire gets right.

## Screen Reader Profiles, Not Just a Toggle

Erion has a screen reader mode. NukeFire has three. The `sr setup`
command lets you choose between descriptive, balanced, and minimal
profiles:

- **Descriptive** keeps full room descriptions with clean combat
  and output summaries.
- **Balanced** uses brief rooms with the same clean output tools.
- **Minimal** uses balanced output and also quiets optional public
  communications like gossip and auction.

You can switch between them anytime. If I'm exploring a new area,
I use descriptive. If I'm grinding the scrapyard for the fiftieth
time, I switch to balanced. The game doesn't assume one setting
works for every situation.

Two commands help when things get fast. `sr status` reads your
active profile, prompt mode, summaries, line gags, and presets —
everything about how the game is currently presenting information
to you. `sr recap` reads a stable snapshot of the current room,
exits, resources, opponent, group condition, and immediate danger.
This is specifically for when combat or group output moves faster
than a screen reader can follow. You don't have to scroll back
through spam to find out what's happening. You type two words and
the game tells you.

## Gags That Work for Screen Readers

Most MUDs have some form of output filtering. NukeFire's gag
system was built with screen reader users in mind. The standard
`gag` command shows a colored, organized guide for sighted players.
`sr gag` shows the same controls in short, plain lines designed
for screen readers.

There are friendly presets that do what you'd actually want:

- `gag comms` quiets gossip, auction, congratulations, and newbie
  information.
- `gag loot` enables loot, item-proc, and concealed-weapon
  summaries.
- `gag combat` enables compact combat and the full Output
  Intelligence profile.
- `gag skynet` hides ordinary lines containing the word SKYNET.

You can also build your own rules: `gag exact`, `gag starts`, `gag
contains`. Matching ignores capitalization and display color codes.
Type `gag list` to review saved rules, `gag test` to test a sample,
or `gag status` to see both custom rules and friendly presets.

The Output Intelligence profile — enabled with `toggle dedupe max`
— folds repeated lines, summarizes combat rounds, and compresses
group movement. It changes presentation only. Damage, healing,
drops, timing, and combat rules are unchanged. The game is the
same. The noise is gone.

## GPS Navigation That Works

NukeFire has a GPS system built into the game. `gps find` searches
linked destinations by partial name. `gps set` locks in your
destination. `gps route` shows the full path. `gps nearest` finds
the closest reachable destination. `gps anchor` speedwalks you to
your saved anchor point. `pindrop` drops a personal waypoint.

The GPS list is organized by difficulty tier: newbie, fresh remort,
early remort, low remort, seasoned, veteran, high, elite, advanced,
extreme, endgame. Each destination shows its remort requirement
and whether it has crafting. You don't have to guess whether an
area will kill you. The game tells you.

You can also save personal speedwalk routes with `path save` and
replay them with `path run`. And `bigmap` toggles a local minimap
that follows your GPS route — useful if you have some vision, but
the GPS text output works fine without it.

This matters for the same reason Erion's `runto` matters. With
topographical agnosia, I can't build a mental map of rooms I've
been through. GPS navigation means I don't have to.

## Equipment Management That Doesn't Require Memorization

NukeFire's equipment system is the most screen-reader-friendly
I've seen in a MUD. The key commands:

- **GearCheck** gives a broad gear review.
- **Compare** checks an item against your current gear.
- **Upgrade** suggests better equipment, implant, or tattoo options
  for a specific slot.
- **Upgrade All** checks every slot at once.
- **Autocompare** shows quick upgrade hints in your inventory
  output. Items are marked better, toss-up, worse, or cannot wear.
- **Highlight** shows where a stat like damroll or spellpower comes
  from — which piece of gear is giving you that number.
- **SetWeights** lets you customize how the upgrade system
  evaluates equipment for your class. If armor no longer matters
  because you're past the cap, set it to zero. If spellpower
  matters more, raise its weight. The recommendations reflect the
  build you're actually playing.
- **SocketCheck** searches equipped items by socket shape. `socketcheck
  round` returns only items with round sockets, showing the full
  socket layout for each match.
- **WearBest** removes your current gear and wears the best
  available items from your inventory for every slot.

This is the difference between being self-sufficient and being
dependent on other players' knowledge. I don't have to memorize
which area drops a better ring. I don't have to ask the gossip
channel whether this implant is an upgrade. The game tells me.

## Crafting That Stores Your Materials

NukeFire's crafting system uses stored materials. When you kill
a monster, it drops parts — servo couplers, nerve leads, ink
ampoules, data wafers. You type `addmat` and the game sweeps
valid materials from your inventory into saved storage. The
materials live on your character, survive logout, and can be
checked with `materials`.

When you're ready to craft, you go to a crafter NPC and type
`craft`. If you have enough materials, it makes you something.
If you don't, it tells you exactly what's missing. You can also
use `gather` to pull materials back into your inventory if you
need to move them.

The scrapyard — the newbie crafting zone — has three crafters
scattered throughout the area: Ratch for equipment, Suture-9
for implants, and a tattoo crafter for tattoos. Each one uses
a different material family, and the Intake Sorting Yard has
bins labeled for armor stock, ink stock, and implant stock so
you know what goes where.

I crafted a rookie spinal damper implant at Suture-9's chair,
took it to Vlad the Implanter in Tek Angeles, and had it
surgically installed in my back. It gave me +2 damage. That's
a crafting loop that works entirely through text commands and
screen reader output, with no visual interface and no guesswork.

## A Community That Answers Questions

NukeFire's community is active and helpful. When I asked on
gossip what areas were good for my level, multiple players
responded within seconds. When I asked how crafting worked,
someone explained it. When I mentioned I'd cleared most of the
scrapyard and crafted my first implant, a veteran player said
"first steps :)" — the kind of small encouragement that makes
a new player feel welcome.

The welcome message says: "Do not hesitate to ask questions.
Everyone was new once. The wastes are easier with guidance."
That's not just flavor text. The community actually behaves
that way.

There's also active development. The news file shows updates
from August 5 through August 10, 2026 — WHO modernization,
SetWeights cleanup, SocketCheck improvements, new zones, TinTin
compatibility work, memory leak fixes. This is a game that's
being actively maintained, and the developers are thinking
about accessibility. One player — The Eldritch One — is building
a NukeFire client with screen reader functionality built in.

## What NukeFire Does That Erion Doesn't

I love Erion. It's still my primary MUD. But NukeFire does
several things Erion doesn't:

- **Multiple screen reader profiles** instead of a single toggle.
  You can adjust output verbosity based on what you're doing.
- **sr recap** for recovering context when combat moves too fast.
  Erion has nothing like this.
- **Stored crafting materials** that survive logout. Erion has
  separate craft and alchemy inventories, but NukeFire's `addmat`
  and `gather` system is more streamlined — one command sweeps
  everything into storage, and materials persist across sessions
  without needing to manage multiple inventories.
- **Equipment comparison and upgrade suggestions** built into the
  game. Erion has a database search, but NukeFire's autocompare
  and upgrade system is more immediate.
- **GPS with difficulty tiers.** Erion's `runto` is great, but
  NukeFire's GPS tells you whether an area will kill you before
  you go there.
- **A post-apocalyptic setting.** If you're tired of elves and
  dragons, NukeFire is robots, radiation, and Thunderdome.

## What Erion Does That NukeFire Doesn't

Fair is fair. Erion has things NukeFire doesn't:

- **A soundpack with an installer.** NukeFire has no soundpack
  that I'm aware of.
- **Hotkeys for health, mana, and experience** that work even
  when TTS is off.
- **Message history buffers** you can navigate with keystrokes.
- **Spell numbers** so you can type `cast 832` instead of
  `cast 'magic slash'`.
- **Autoskill** for repetitive combat actions, designed with
  carpal tunnel in mind.
- **A fantasy setting.** If you want elves and dragons, Erion
  has them.

The two games complement each other. Erion is my medieval fantasy
MUD with alchemy and faiths. NukeFire is my post-apocalyptic
wasteland MUD with robots and crafting. I play both, and I don't
have to choose.

## What Other MUDs Could Learn

Most MUDs are technically accessible because they're text-based.
A screen reader can read the output. But "technically accessible"
and "actually playable" are different things, and the distance
between them is where multiply disabled players fall through.

NukeFire closes that distance with features that aren't
complicated:

- Screen reader profiles that adjust output verbosity.
- A recap command for recovering lost context.
- GPS navigation with difficulty tiers.
- Equipment comparison and upgrade suggestions.
- Stored crafting materials that survive logout.
- Gag presets designed for screen reader users.
- A community that answers questions without making you feel
  stupid for asking.

None of these features are hard to implement. Most MUDs already
have the text infrastructure. What NukeFire has that others don't
is the awareness that blind and disabled players exist, and the
willingness to build for us instead of waiting for us to figure
it out.

I've been playing for about a day. My character is a Slinger
named Liora, level 40, alignment Evil. She's killed over three
hundred junker robots, crafted an implant from their parts, and
explored a wasteland she can actually navigate.

For the second time in a MUD, I'm playing the game instead of
fighting it.

## How to Connect

NukeFire is free to play. Connect with any MUD client (Mudlet,
MUSHclient, TinTin++) at:

- **Host:** tdome.nukefire.org
- **Port:** 4000

Good first help files: `help newbie`, `help class`, `help prestige`,
`help qol`, `help gps`, `help screenreader`, `help gag`.
