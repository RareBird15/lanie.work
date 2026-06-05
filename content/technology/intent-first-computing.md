---
title: Intent-First Computing
date: 2026-06-04
categories:
  - Technology
tags:
  - accessibility
  - disability
  - technology
  - ai
  - workflow
  - cognitive-prosthetic
slug: intent-first-computing
description: >
  Text-first and keyboard-first interfaces aren't outdated for many multiply disabled users. They're access. This post
  argues for terminal-like transparency, desktop-like discoverability, and AI that can turn messy intent into action.
showTableOfContents: true
---

A couple weeks ago, my mom said she wished she didn't have to have a phone because of all the spam she gets.

I agreed, but for a different reason.

For me, the phone is often harder to use. Small screens, touch gestures, mobile-first layouts, and apps designed around
visual scanning can all become physically and cognitively exhausting. A lot of the time, I wish I could just use my
computer.

That probably sounds strange in a world where everything keeps moving toward mobile. But for me, desktop-first access
isn't nostalgia. It's function.

## Not old-school vs modern

My access needs aren't simply old-school or modern. They're both.

I benefit enormously from modern technology. I rely on screen readers, accessible desktop apps, browser accessibility
APIs, cloud services, AI chat, touch accommodations, assistive touch, and tools like VS Code and Windows Terminal.

At the same time, a lot of modern design trends make things harder for me: mobile-first interfaces, touch-first
assumptions, video-first learning, visual dashboards, spatial interfaces, audio-first accessibility, and apps that hide
information behind "simple" UI.

What I need isn't old technology.

What I need is technology that is:

- desktop-first
- keyboard-first
- text-first
- screen-reader-friendly
- transparent
- searchable
- reviewable
- forgiving when my brain cannot remember the exact spell

## What still works best for me

Some of what works best for me looks almost old-fashioned:

- full keyboard control
- real windows
- desktop apps
- command lines
- text logs
- lists and menus
- searchable output
- screen-reader review
- interfaces that let me move at my own pace

That's one reason I like MUDs, terminal tools, Betterbird, VS Code, and other keyboard-driven software. They give me
information I can read, review, search, and copy.

But this isn't me asking to go backward.

Without modern technology, I probably wouldn't be very functional at all.

## Text-first isn't terminal-only

I often say I need text-first tools, but that doesn't mean the terminal is always the easiest interface for me.

Terminals are powerful because they expose information. They give me logs, errors, filenames, command output, and state
I can copy, search, and review. When something goes wrong, a terminal often tells me more than a modern app does. That
kind of transparency is a huge accessibility benefit.

But terminals also make me remember exact syntax at exactly the moment I need it. I have to remember command names,
subcommands, flags, argument order, service names, config keys, and little details like whether a systemd service needs
`--user`.

The concept may make sense, but the recall burden is still high.

A well-designed desktop app can sometimes be easier because it gives me structure: menus, keyboard shortcuts, command
palettes, autocomplete, labeled controls, and saved settings. Those all reduce the amount I have to hold in working
memory.

So my ideal interface isn't "everything should be a terminal."

It's this:

> **Terminal-like transparency with desktop-like discoverability.**

I need access to real information, and I need actions to be findable when my brain can't remember the exact spell.

## Low baseline energy changes everything

Because of my conditions, my energy is usually low before I start anything.

There's a constant background level of exhaustion I'm already working around. So when an interface makes me remember
exact syntax, search through settings, switch between apps, recover from errors, or translate a vague need into a clean
technical question, that isn't a small thing.

It can be the difference between doing the task and not doing it at all.

> **Friction is not neutral when my baseline is already low energy.**

## AI as the bridge beside the terminal

Right now, a lot of my terminal work already involves AI.

I often keep an AI chat open beside the terminal so I can ask questions when I get confused, frustrated, or stuck. I
might understand the general goal, then get blocked by one small detail: a flag, argument order, service scope, or error
I can't parse quickly.

Sometimes the question isn't clean. It's just:

> "Ugh, why isn't this working?"

with pasted output and a little context.

That matters. When I'm stuck, I don't always have the energy to turn the problem into a polished technical question, and
even if I have the energy, I often can't find the words. I just need help making sense of the mess.

AI can look at the output, infer what I was probably trying to do, ask for missing details, and help me find the next
step. In those moments, AI becomes an accessibility bridge.

But today it's often a separate layer. I'm still switching between tools, copying output, asking follow-ups, checking
trust, then going back to the terminal.

Helpful, yes. Also extra cognitive work.

## Why AI-integrated terminals matter

This is why AI-integrated terminals interest me.

A terminal like Warp is appealing in theory because it points toward the kind of workflow I want: commands, logs, and
real output in one place, with natural-language help when I get stuck.

But if the terminal itself isn't accessible with a screen reader, the AI layer doesn't solve the problem.

> **An AI terminal only helps me if both halves are accessible: the terminal and the AI layer.**

This is also why Microsoft's Intelligent Terminal caught my attention.

I don't assume Microsoft gets accessibility right automatically. But compared with a lot of companies making shiny AI
dev tools, Microsoft has a better track record in tools I actually use: Windows, Office, VS Code, and Windows Terminal.
Those aren't perfect, but they're broadly usable with screen readers and keyboard workflows in a way many newer apps are
not.

In early testing, Intelligent Terminal seems promising for me. I don't know yet whether it will fit my workflow
long-term, but the early accessibility signs matter. The key word is still if.

## Natural language is not the same as voice

I also want to be explicit about this:

> **Natural language does not have to mean voice.**

Many people want an AI computer they can talk to out loud. I understand that.

For me, speech is complicated. I pause. I lose words. I trail off. I may know the shape of what I mean before I can say
it cleanly.

Typing gives me more control. I can be messy and still edit. I can write half a thought, backspace, paste an error, add
context, and keep going.

Maybe one day voice AI will handle pauses, word-finding issues, restarts, and unfinished thoughts well enough that I
trust it more.

For now, the dream is not only a computer I can speak to.

It's a computer I can type messy human intent into, and have it help me turn that intent into action.

## What I mean by intent-first computing

I'm drawn to the idea of an AI operating system, but not in the "assistant sprinkled on top" sense.

I mean a computer where I can type what I need in ordinary language, even when the thought is half-formed, and the
system can help me turn that into concrete steps.

Sometimes I don't have the energy to remember the exact command, find the right setting, navigate the right app, or
explain the problem neatly. I may only have something like:

- Ugh, why is this broken
- I need this service running again
- Find the form I was working on and help me finish it
- Clean up these downloads, but ask before deleting anything important

For me, that kind of interface wouldn't be laziness.

> **It would be access.**

The ideal system would work from intent instead of syntax. It would gather context, suggest next steps, run safe
actions, and ask before risky ones.

It would also be accessible by design, not as a patch later.

I'd need:

- keyboard control
- screen-reader and Braille support
- typed natural language input
- optional voice input that can handle pauses and word-finding issues
- text output
- reviewable logs
- clear confirmations
- predictable focus
- settings for AI autonomy levels

I need to know what changed, what failed, and what the system plans to try next.

The dream is not a black box that takes over my computer.

The dream is a computer that can meet me where my brain actually is, translate messy intent into concrete steps, and
still let me inspect, correct, and trust what's happening.

## Gaming shows the same pattern

I've written before about
[what gaming is like for me as a blind, neurodivergent, chronically ill woman](/gaming/blind-neurodivergent-gamer/).
Games are one of the places where this access pattern becomes especially obvious.

A lot of blind-accessible gaming focuses on audio cues, soundpacks, spatial audio, or mods for visual games. Those help
many blind gamers, and I'm glad they exist.

But they often aren't good access for me.

I'm blind, autistic, chronically ill, often exhausted, and have topographical agnosia plus probable auditory processing
issues. So adding more audio or spatial processing can make a game less accessible for me, not more.

What works better is text-first, low-spatial, low-audio, low-timing, low-social play.

But even “text-first” isn't enough by itself.

A MUD can be technically readable and still be exhausting if I have to memorize routes, interpret maps, ask other
players where to go, or manage hidden information in my head. What works well isn't just text. It's structured,
queryable, action-ready text.

That's one reason a MUD like Erion works well for me. Commands like `dirs`, `where`, mission info, quest systems, and
searchable equipment tools reduce the hidden map-and-memory burden. They help me turn “I need to find this target” into
a concrete next action.

That's the same thing I want from my tools more broadly.

The best interfaces for me aren't just technically accessible. They're sustainable. They help me recover when I'm lost,
review what happened, find the next step, and continue when my energy is low.

## What accessible should mean

For me, accessible doesn't only mean "a blind person can technically use this."

It means:

- I can use it when I'm tired
- I can recover when I get lost
- I can review information at my own pace
- I don't have to rely on visual maps or spatial audio
- I don't have to memorize every command
- I don't have to constantly ask other people to rescue me
- I can understand what changed
- I can find the next action
- I can stop and come back later

Access isn't only about whether something works once under ideal conditions.

It's about whether the interface still works when my real brain and body show up.

## Closing

I'm not behind technology.

My needs just reveal something modern design often forgets.

Text-first, keyboard-first, desktop-first interfaces aren't outdated. They can be some of the most liberating interfaces
for multiply disabled people, especially when combined with modern accessibility APIs, cloud tools, and AI.

But the future I want isn't voice-first AI, mobile-first AI, or black-box automation.

> **The future I want is intent-first computing.**

I want tools that expose information clearly, make actions discoverable, accept messy human language, and help me move
from need to action without forcing me to memorize every spell.

That isn't laziness. It's access.
