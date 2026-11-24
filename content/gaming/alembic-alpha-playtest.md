---
title: "Alembic: An Alchemy Game Made of Words"
date: 2026-10-13
draft: false
categories:
  - Gaming
tags:
  - accessibility
  - game-dev
  - blindness
  - screen-reader
  - alchemy
  - alembic
slug: alembic-alpha-playtest
description: >
  I built a screen-reader-first alchemy game where the reward is a line of
  words instead of a picture. It's in alpha and open source.
---

Alchemy games are built out of pictures. You drag a little fire onto a little water and watch steam appear. The fun is in the watching.

I can't do the watching. So I built an alchemy game out of words.

## What Alembic Is

[Alembic](https://alembic.lanie.work) is a text alchemy game. You start with four elements, Fire, Water, Earth, and Air. Combine two of them and you get a new one. There are 132 elements to find and 26 milestone goals to chase.

The loop is simple. Add one element to your cauldron, add a second, choose Combine. Sometimes they make something new. Sometimes nothing happens. Either way you get a clear answer and you keep going.

No drag-and-drop, no timers, no fail states. Every action is a button, and every change is announced by your screen reader.

## The Flavor Text Is the Point

The thing that makes Alembic different from the visual games it resembles is the flavor text.

In a picture game, discovering a new element means watching it appear. In Alembic, that pleasure is a line of words. Every element has one. Fire is "warm, hungry, bright." Steam is "water, learning to fly."

The goals get a little more, a second clause that makes a milestone land differently from an ordinary find. Life is "the first breath in the mud. Then a second breath, and it did not stop."

I wrote all of it. The flavor text is the whole visual layer, translated into something a screen reader can deliver.

## Built for Screen Readers First

Alembic isn't a visual game that happens to work with a screen reader. It's a text game, built for one from the first line.

- Linear layout. Heading, cauldron, catalog, goals, hint. No grid, no positions to remember.
- Keyboard shortcuts. Alt+C to combine, Alt+X to clear, Alt+H for a hint, Alt+S to search.
- A recipe notebook. Every element shows what you combined to make it, and a discovery log lists your finds in order.
- Thoughtful cauldron behavior. After you combine, your first element stays so you can try it with something new.
- It saves automatically. No account, no login.

## It's in Alpha, and It's Working

I posted Alembic on AppleVis and Mastodon, and the response has been warm. People have found elements, reached goals, and sent real feedback. One player suggested keeping an element in the cauldron after a failed combine. That's now a setting in the game.

I've tested with NVDA in Chrome. I'd especially love feedback from VoiceOver and JAWS users.

## Play

[Play Alembic](https://alembic.lanie.work). It's free, it runs in any browser, and the source is [open on GitHub](https://github.com/RareBird15/alembic).

## Why This Matters

I built Everrealm because I wanted a strategy game that worked with my access needs. I built Alembic for a smaller reason. Because the little games should be for us too.

Most of the games I grew up unable to play weren't the big ones. They were the little ones, the matching games and merging games you play for five minutes. Those were almost always made of pictures.

Alembic is my answer to that. A small game made of words, that you can actually play. Come try it. Tell me what's fun and what's confusing. It's small, but it's ours.
