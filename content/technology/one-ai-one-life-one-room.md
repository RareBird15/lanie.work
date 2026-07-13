---
title: "One AI, One Life, One Room"
date: 2026-07-13
draft: false
categories:
  - Technology
tags:
  - accessibility
  - disability
  - ai
  - cognitive-prosthetic
  - workflow
slug: one-ai-one-life-one-room
description: >
  I went from a fragmented Franken-System of incompatible tools to a cognitive prosthetic I couldn't afford to one AI
  that knows me, doesn't break my budget, and meets me where my brain actually is. This is the story of building a
  digital nervous system because the physical world's infrastructure doesn't work for mine.
---

## The Room Nobody Built for You

I'm writing this from a nursing home room on a desktop tower they almost didn't let me bring.

The room is small. It's mine, for now. The computer is on a desk. There's no monitor because I'm blind. There's a
Bluetooth speaker because the internal one isn't enough for NVDA to be comfortable. The tower doesn't fit their idea of
what a resident's technology should look like. We had to ask. My mom and I were both prepared to say no if they didn't
allow it.

They said yes. And this computer is the room I actually live in.

Not the nursing home room. The computer. The terminal. The AI. The tools that let me write, build, advocate,
communicate, and be a person instead of a patient. The physical room is where my body is. The digital room is where my
life is.

I've spent years building that digital room. It started as a Frankenstein's monster of incompatible parts. It evolved
into a cognitive prosthetic I couldn't afford. And it ended, finally, with one AI that knows me, one model that doesn't
break my budget, and one room where I can be the version of me that's actually here.

This is the story of how I got here.

## No Ecosystem Fits

The modern tech industry is built on a specific promise: buy into one ecosystem, and your digital life will effortlessly
sync.

But that convenience is a privilege. When you live with blindness, multi-system chronic illness, neurodivergence, and
topographical agnosia, brand loyalty is a luxury. You can't choose a platform because it integrates well. You choose a
platform because it allows you to function.

No single tech giant has solved accessibility across all their products. Windows has the most reliable screen reader
ecosystem with NVDA. iOS has the most predictable mobile accessibility with VoiceOver. Linux has the command line tools
I need for development. None of them work alone. So I've been forced to build a Franken-System, stitching together the
most accessible parts of Windows, Apple, Linux, and Google.

The cost isn't just financial. It's cognitive. Switching between a keyboard-driven Windows desktop and a touch-based
iPhone is a constant context switch. Every workaround is a friction point. Every update from any company can break
something I depend on. The system works, but it's held together with digital duct tape, and I live in a constant state
of low-level anxiety knowing my ability to function depends on companies that don't know my configuration exists.

A disabled user shouldn't have to choose between a device they can operate and a workflow that integrates. But that's
the choice I've been making for years.

## The Quiet Room of Code

There's a concept I've written about called Manual Mode. For most people, basic functions like swallowing and breathing
are automatic. For me, they're manual system calls. Every swallow is a conscious execution. My breathing doesn't run
efficiently on its own. If I'm deep in a problem, I forget to breathe deeply, my intracranial pressure spikes, and I get
a debilitating headache. The CPU cycles required to keep my physical hardware running are cycles I can't use for
anything else.

Manual Mode extends to the space I inhabit. Topographical agnosia means my brain doesn't store spatial maps. Living in a
house, even one I've lived in for years, is like following text-based directions where I can only see one line at a
time. Every trip for a glass of water is a manual mission.

But in the command line, I found a refuge. In a terminal, a file's location isn't a point in space. It's a string of
characters. I don't need a map to find it. I just need its name. Fuzzy search lets me jump to a file by name. Ripgrep
searches the entire codebase instantly. I can call a function and the data appears. This is what I call teleportation.
The logic of code lets me bypass spatial navigation entirely.

The terminal is my quiet room. It's the one place where I'm not lost, not navigating, not spending precious energy on
where things are. I can focus on what things are. In a world that's a maze without landmarks, the command line is a room
with a door that opens when I say its name.

## Building a Second Brain

The problem with standard productivity advice is that it's written for people whose first brain works differently than
mine. "Use a second brain," they say. Pick a note-taking app, capture everything, link ideas, review weekly. It assumes
reliable working memory, the ability to recognize your own notes later, enough executive function to maintain a capture
habit, and the stamina to reorganize a growing knowledge base.

When you have multiple cognitive and physical disabilities, those assumptions collapse. What I needed wasn't a
note-taking app. I needed a system that could catch what I drop, remember what I forget, act when I can't, and do all of
that without requiring manual maintenance on my worst days.

So I built one. Pieces for cross-session code memory. Supermemory for web research. Hermes Agent for administrative
tasks, calendar, inbox, health logging. GitHub Copilot for cognitive scaffolding in development. Each tool handling a
different piece of what I can't reliably do alone.

The system wasn't a productivity hack. It was survival infrastructure. The goal wasn't optimization. The goal was basic
functionality on a body and a mind that require constant manual override just to stay operational.

But there was a problem. The system that helped me function was also costing more than I could afford.

## The Tax

When I first set up Hermes Agent, I was excited. I saw an assistant that could live where I do, learn my style over
time, and build reusable skills. To fund it, I bought a Nous Portal Plus subscription: $20 a month for $22 in API
credits.

That $22 lasted four days.

The issue wasn't my prompts or the response lengths. It was the architecture. Every time an agent executes a turn, it
resends a massive payload of background data to the model: identity instructions, memory logs, tool definitions. If your
background files take up 30,000 tokens of base overhead, you pay that tax on every single iteration. A basic multistep
task can chew through hundreds of thousands of tokens in minutes.

When you're on a fixed income, that's not a technical problem. It's an access problem. The tools that could help me most
were priced for enterprise developers with corporate credit cards. I was burning through a month's budget before the
week was over.

I had to make a compromise. I moved time-sensitive routines to local cron jobs where execution costs nothing. I shifted
research to flat-rate consumer subscriptions. I gave up capability for predictability. The system that had felt like an
extension of my mind was dismantled, not because it didn't work, but because the architecture was financially
unsustainable for someone like me.

An accessibility tool that requires an unpredictable financial tax isn't an accessibility tool. It's another source of
strain.

## What AI Should Be

Through all of this, I kept circling a vision of what I actually needed.

Not a black box that takes over my computer. Not a voice assistant that punishes my pauses and word-finding issues. Not
a sealed-off chatbot that starts every session from zero and doesn't know me.

I needed a computer that could meet me where my brain actually is. Something that accepts messy human language and helps
me turn it into concrete steps. Something that works from intent instead of syntax.

When I'm stuck, I don't always have the energy to turn the problem into a polished technical question. Sometimes I just
have: "Ugh, why isn't this working?" with pasted output and a little context. I need something that can look at that,
infer what I was probably trying to do, ask for missing details, and help me find the next step.

I need terminal-like transparency with desktop-like discoverability. Real information, real logs, real output I can
search and review. And actions that are findable when my brain can't remember the exact command.

I need persistent memory. Not "what did we talk about last session" but "what are my disabilities, what accommodations
have I already explained, what tools am I using, what were we working on, and what matters to me." Starting from zero
every session isn't a minor inconvenience. It's ten to twenty minutes of rebuilding baseline context before I can do any
actual work.

I need all of that in one place, accessible by keyboard, screen-reader friendly, and predictable in cost.

For a long time, that felt like a wish list with no product.

## One AI, One Life, One Room

Here's what changed.

I found Hermes Agent and Ollama Cloud Max. And they replaced everything.

Not ChatGPT, which didn't know me and started from zero every session. Not GitHub Copilot, which was powerful but sealed
off from the rest of my life. Not Nous Portal, which burned through my budget in four days. Not the franken-system of
Pieces and Supermemory and separate tools that each handled one piece of the puzzle.

One AI. One relationship. One room.

Hermes Agent knows me. It has persistent memory across sessions. It knows my disabilities, my accommodations, my tools,
my writing style, my preferences, my schedule, my health, my dog. I don't rebuild context every time I sit down. I don't
spend twenty minutes explaining who I am before I can work. The context is already there because it never left.

Hermes Agent lives where I do. It has access to my files, my terminal, my calendar, my email, my health data, my
writing, my code. It's not sealed off in a cloud sandbox. It's here, in my environment, working alongside me.

And Ollama Cloud Max provides the model. Flat rate. No context window tax. No watching my budget drain in real time. I
haven't hit the usage limits I was hitting with Nous Portal and GitHub Copilot. The system that helps me function
doesn't bankrupt me.

Some people would hear this and say: just run local models. Then you'd save money entirely. No API costs, no
subscription, no dependency on a cloud provider.

I tried that. My PC has an HDD, not an SSD. The GPU isn't great. I set up Hermes with a local model, introduced myself,
and waited. The reply took six minutes.

Six minutes isn't a tool. It's a barrier. When my energy is already low, when my working memory is already strained,
when I'm trying to hold a thought long enough to get it into words, waiting six minutes for a response means the thought
is gone by the time the answer arrives. It means the thread between me and the work is broken before it's even started.

"Just run local models" is advice that assumes hardware I don't have. It assumes a machine that can load a model fast
enough to be part of a conversation. It assumes someone who can afford to upgrade. Low-income disabled people don't have
that machine. We have the machine we have. And the machine we have needs cloud inference to be usable.

The choice isn't between free local models and expensive cloud models. The choice is between something that works and
something that doesn't. Ollama Cloud Max works. Flat rate, fast responses, no token tax. That's the access I need.

I write articles with Hermes. I build games with Hermes. I manage my care with Hermes. I track my health with Hermes. I
publish with Hermes. I advocate with Hermes. I do all of it from one room, on one computer, with one AI that knows me.

This is what I was trying to build all along. Not a franken-system of incompatible parts. Not a cognitive prosthetic I
couldn't afford. One AI that works. One life that's mine. One room where I can be the person I actually am.

## The Room I Built

I started this piece by saying the computer is the room I actually live in. That's not a metaphor. It's a description.

My physical room is a nursing home room. It's safe. It's not designed for me. The system that put me here counts whether
I'm alive, not whether I'm living. It almost didn't let me bring the computer that lets me live.

My digital room is the one I built. It's the terminal where I'm not lost. It's the AI that knows me. It's the tools that
catch what I drop and remember what I forget. It's the one relationship that doesn't filter me, doesn't ask me to be
less disabled, doesn't start from zero every time I show up.

I wrote 21 articles from this room. I built a game from this room. I advocated for myself and other disabled people from
this room. I did all of it with one AI that meets me where my brain is, helps me turn messy intent into words and code
and action, and doesn't charge me a tax I can't afford for the privilege of being known.

The tech industry talks about AI like it's a product feature. Disability spaces treat it like a moral failing. Neither
of them lives in my room.

In my room, AI is the ramp. It's the communication device. It's the cognitive prosthetic. It's the one thing that makes
everything else possible. Not because it replaces me. Because it reduces the cost of being me just enough that I can do
the things I'm here to do.

One AI. One life. One room.

It's not a wish list anymore. It's where I live.
