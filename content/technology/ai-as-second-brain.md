---
title: AI as a Second Brain
date: 2026-05-15
categories:
  - Technology
tags:
  - accessibility
  - disability
  - technology
  - workflow
  - ai
  - cognitive-prosthetic
slug: ai-as-second-brain
description: >
  A personal look at how AI tools serve as a cognitive prosthetic for a multiply disabled
  user who relies on a custom stack of Pieces, Supermemory, Hermes Agent, and GitHub
  Copilot to function at baseline.
showTableOfContents: true
---

The productivity advice says: use a second brain. Pick a note-taking app, capture everything, link ideas, review
weekly. Build a system and trust it.

I've tried most of the popular options. Notion collapsed under its own visual complexity. Obsidian's graph view is a
spatial nightmare for someone with topographical agnosia. Roam required too much upfront structure on days when I have
nothing left for structure. Apple Notes doesn't persist across my fragmented hardware setup.

The problem isn't the apps. The problem is that "second brain" advice is written for people whose first brain works
differently than mine. It assumes reliable working memory, the ability to review notes and recognize them as your own,
enough executive function to maintain a capture habit, and the stamina to periodically reorganize a growing knowledge
base.

When you have multiple cognitive and physical disabilities, those assumptions collapse. What I needed wasn't a
note-taking app. I needed a system that could catch what I drop, remember what I forget, act when I can't, and do all
of that without requiring me to maintain it manually on my worst days.

## What I Use

### Pieces MCP Server

Pieces is the backbone of my cross-session memory. Every code snippet I write, every command I run, every note I take
in VS Code gets captured and indexed. When I come back to a project after a multi-day gap (which happens constantly
with chronic illness), I can ask Pieces what I was working on and get a real answer instead of spending twenty minutes
reconstructing my own context. It hooks directly into GitHub Copilot via the MCP server, so the AI assistant I'm
already talking to has access to everything I've done.

### Supermemory

Supermemory handles the web research layer. When I'm reading articles, watching content, or doing deep research on a
topic, Supermemory indexes it and makes it retrievable later. This matters because I can't rely on browser history or
my own recall. If I read something important two weeks ago, I won't remember the article title, the site, or even the
rough content. Supermemory gives me a way to search my own research history semantically, not just by URL or date.

### Hermes Agent

Hermes is my Pi-based personal agent. It handles the administrative layer of my life: calendar events, inbox triage,
GoFundMe monitoring, and health data logging. Because it runs on my Raspberry Pi 5, it's always available and costs
nothing per query. It's not as capable as a cloud-based model, but it doesn't need to be. Its job is to handle the
structured, routine tasks that drain my executive function when I try to do them manually.

### VS Code and GitHub Copilot

This is my primary development environment and the main interface I use for cognitive scaffolding. Copilot isn't just
autocomplete for me. It's the working memory I don't have. I can partially describe a problem, provide context from
Pieces, and have Copilot help me reason through what I'm actually trying to do. It reduces the cognitive re-entry cost
when I return to a task mid-session.

### Hardware Reality

My setup runs on a Raspberry Pi 5 (Hermes server), an old Dell laptop running Windows with WSL (primary dev machine),
and an iPhone SE2. This isn't aspirational hardware. It's what I can afford and what works within my accessibility
requirements. Any solution I build has to function on this stack.

### Supporting Tools

Guava Health handles symptom and medication tracking. Sophtron connects to my financial accounts so I can pull
structured spending and balance data without navigating inaccessible bank interfaces. Both feed into the broader
picture that Hermes can reference when I need to make decisions about pacing, capacity, or resource allocation.

## Why Not Just Use ChatGPT?

The short answer is that ChatGPT doesn't know me. Every session starts from zero. There's no persistent memory of what
I was working on, what my disabilities are, what accommodations I've already explained, or what tools I'm using. For
someone without memory and context continuity challenges, that's a minor inconvenience. For me, it means spending the
first ten to twenty minutes of every session re-establishing baseline context before I can do any actual work.

Beyond memory, there's the control problem. I can't build custom integrations into ChatGPT. I can't give it direct
access to my local files, my Hermes logs, or my Pieces snippets. The tool is powerful in isolation but sealed off from
the rest of the stack I depend on.

## How the Architecture Actually Works

**Capture layer**: Pieces logs my coding context and notes. Supermemory indexes my research. Hermes logs structured
health and administrative events.

**Memory layer**: Pieces LTM holds cross-session code and workflow history. Supermemory holds the web research graph.
Hermes holds structured logs of routine tasks and health data.

**Reasoning layer**: GitHub Copilot pulls from Pieces via MCP and handles the technical and cognitive scaffolding.
Gemini, accessible through Hermes, handles the administrative reasoning layer. Local models handle lightweight tasks
where latency or cost matters.

**Execution layer**: Hermes executes scheduled tasks and administrative actions on the Pi. VS Code tasks and custom
scripts handle the development execution layer.

**Why this matters**: The system reduces cognitive re-entry cost. When I come back to any task, the context is already
there. I don't have to reconstruct it from memory I don't reliably have.

## How They Help with Specific Struggles

**Memory loss**: Pieces gives me a searchable log of everything I've worked on. I don't need to remember; I need to
search. Supermemory does the same for research. Hermes logs what it did and when so I can audit my own history.

**Executive dysfunction**: Hermes handles the task-initiation problem for routine administrative work. I don't need to
decide to check my inbox, triage calendar conflicts, or log symptoms. The system does it on schedule.

**Health tracking**: Guava captures symptoms and medications. Hermes reads those logs and can surface patterns or flag
anomalies when I ask. I don't need to maintain a manual health journal on days when I have nothing left.

**Financial complexity**: Sophtron pulls structured account data. This removes the need to log into inaccessible
financial interfaces on high-cognitive-load days.

**Accessibility barriers**: The whole stack is keyboard and screen-reader accessible. I built it around NVDA on
Windows and VoiceOver on iOS. Nothing in the workflow requires me to navigate a visual interface I can't use.

**Phone anxiety**: Hermes handles communication tasks that would otherwise require phone calls. Copilot handles the
drafting of emails and messages when word-finding is failing.

**Physical limitations**: Because most of the system runs on a server or in the background, I don't need to be actively
operating it to benefit from it. Hermes runs while I rest.

## Concrete Examples

**Coding session after a multi-day gap**: I open VS Code, ask Copilot what I was working on, and Pieces surfaces the
relevant snippets and context. Instead of spending twenty minutes reconstructing my own state, I'm back in the work
within two or three minutes.

**Low-energy logging on a bad day**: I speak a rough health update into my phone. Hermes transcribes it, structures it,
and logs it. I didn't have to type, navigate, or maintain a format. The data is captured without friction.

**Research without tab management**: I read three articles on a topic. Supermemory indexes them. Two weeks later, I
need to reference one of them. I search semantically and find it without needing to remember the title, the site, or
that I even read it.

**Phone-free communication**: I need to respond to something that would normally require a phone call. I draft the
response in Copilot, adjust it, and send it as a message or email. No call required.

## What This System Doesn't Look Like

The AI gets things wrong. Copilot misunderstands context. Hermes occasionally fails to parse a task correctly.
Supermemory misses things I'd consider important. These are real limitations, not edge cases.

The infrastructure requires maintenance. Scripts break. The Pi needs reboots. MCP connections time out. On my worst
days, I don't have the capacity to debug the system I depend on. This is a real vulnerability in the architecture.

The system doesn't replace human connection or human support. It handles the administrative and cognitive overhead that
would otherwise block me from accessing human connection. That's a meaningful distinction.

## The Closer

This isn't a productivity system. It's a survival infrastructure. The goal isn't optimization or efficiency or becoming
a better developer. The goal is baseline functionality on a body and a mind that require constant manual override just
to stay operational.

If you're multiply disabled and the standard second brain advice has never worked for you, this might be why. The advice
is built for a different kind of nervous system. What works for me is a system that catches what I drop, remembers what
I forget, and acts when I can't, without requiring me to maintain it perfectly on the days when I have nothing left to
give.
