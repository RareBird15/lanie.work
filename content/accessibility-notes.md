---
title: Accessibility Notes
slug: accessibility-notes
date: 2026-03-31
description: >
  My consistent interaction model: Why text-first, keyboard-centric, and query-based systems work for my neurodivergent
  profile.
showDate: false
showTableOfContents: true
---

This page documents my **consistent interaction model**. My access needs aren't just preferences; they are the framework
that makes programming, gaming, and digital life possible for me as a blind, neurodivergent, and chronically ill user.

## What Works: The Persistent Text Model

I thrive in systems that are **text-first** and **keyboard-centric**. Information must be persistent so I can process it
at my own pace.

- **Keyboard-First Interaction:** I rely on standard screen reader navigation (NVDA) and command-line interfaces.
- **Explicit State:** I need coordinates and structure (e.g., "You are at 10, 20") rather than relative directions.
- **Query over Memory:** I prefer systems where I can _find_ information (Command Palettes, `fzf`, `tldr`, AI) rather
  than having to memorize a thousand unique shortcuts.
- **Guided Interactivity:** I learn by doing with immediate feedback. "Go build something" without structure doesn't
  work; I need knowledge checks and guided practice.
- **Step-by-Step Workflows:** Breaking complex tasks into small, concrete steps respects my limited cognitive energy.

## Physical & Ergonomic Constraints

My choice of hardware is driven by a need for stability, precision, and low physical fatigue.

- **PC over Everything:** The desktop PC is my primary tool. The tactile feedback of a physical keyboard and the
  precision of keyboard-driven navigation are irreplaceable.
- **The Mobile Barrier:** I use my iPhone only when necessary. Mobile interfaces are inherently **spatial** and
  **ephemeral**. Holding a device is physically fatiguing, and my coordination makes small touch targets difficult to
  hit.
- **The "Large Screen" Fallacy:** Devices like tablets or the **Echo Show 15** are completely unusable for me. A larger
  screen often just creates more empty spatial "noise" and requires more expansive, fatiguing gestures without adding
  the tactile precision I need.
- **Wearables:** Small screens on smartwatches are a hard barrier. The tiny touch targets and requirements for
  multi-finger gestures are incompatible with my coordination and sensory needs.

## What Doesn't Work: The Ephemeral Barrier

I struggle with systems that are "ephemeral" (information that appears once and vanishes) or that require spatial
processing.

- **Audio-Heavy Systems:** Audio is ephemeral. If I miss a sound or a voice cue, it's gone. I can't "reread" a sound.
  Text works better because I can re-process it as many times as needed.
- **Spatial Navigation:** Because of **topographical agnosia**, I can't build mental maps of 2D or 3D spaces.
- **Real-Time Reactions:** My nervous system requires "slower, thoughtful problem-solving." I can't use systems that
  penalize me for taking time to think.
- **Passive Learning:** Watching videos or listening to lectures without hands-on interaction leads to zero retention
  for me.

---

## Real-World Examples

### Programming & Tooling

This is why I prefer **VS Code and the CLI** over mobile or web apps. The CLI is a persistent text stream that I can
query and manipulate. It's also why I focus on **Python and Backend Tooling** rather than frontend - it's about logic
and systems, not visual layouts.

### Gaming & Interactive Media

- **Audiogames:** Most "blind-accessible" games rely on directional audio and spatial awareness. For me, this is sensory
  overload and provides no persistent information.
- **MUDs (Text Games):** I love text-based worlds, but only if they offer coordinates or pathing (like _EmpireMUD_). If
  a game requires me to "Map the forest" in my head, it's a hard barrier.
- **Automation:** I enjoy games like _Trimps_ and _Evolve_ because they are menu-driven and allow me to query the state
  of my systems at any time.

---

## For Developers & Testers

If you're building a tool and want to know if it fits this model, ask yourself:

1. Can a user find every command without a manual?
2. Is the state of the app queryable via text at any time?
3. Does the user have as much time as they need to make a decision?
4. **Is it fully functional via a standard keyboard?** (Crucial for avoiding the fatigue of touch/spatial interfaces.)
