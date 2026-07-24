---
title: "Knowing Where Your Window Is: A Small NVDA Add-on That Fills a JAWS Gap"
date: 2026-07-23
draft: false
categories:
  - Technology
tags:
  - accessibility
  - disability
  - nvda
  - screen-reader
  - assistive-tech
  - windows
slug: windowstate-nvda-add-on
description: >
  NVDA doesn't tell you whether a window is maximized when you query the title.
  JAWS does. I built a small add-on that adds this feature, with a dedicated
  command and an optional NVDA+T enhancement that matches the JAWS behavior.
showTableOfContents: true
---

I press Windows+Up Arrow to maximize a window. Sometimes it maximizes. Sometimes the Windows 11 snap layout chooser pops up instead. Either way, NVDA doesn't tell me which one happened unless I press Windows+Arrow keys again and listen to what NVDA says changed. There's no way to just ask, "Is this window maximized?"

JAWS has this. When you press JAWS+T for the title, it tells you if the window is maximized. NVDA doesn't. I checked the NVDA source code, the existing add-ons, and the open feature requests. Nobody had built this yet.

So I did.

## The Problem

Sighted users glance at a window and know its state. Is it maximized? Is it taking up half the screen? Is it sitting there in a small windowed box? One look answers all of it.

Blind users don't get that glance. NVDA announces window state changes when you press Windows+Arrow keys to resize. But there's no command to query the current state without trying to resize and seeing what happens. If you press Windows+Up Arrow and get the snap chooser instead of a maximize, you're left guessing.

This matters more than it sounds. Non-maximized windows can cause all kinds of issues. Controls get cut off. Content shifts. Layout breaks. Things that sighted users fix with a quick visual check become a guessing game.

## What I Built

WindowState is a small NVDA add-on with two features.

**NVDA+Shift+T** reports the state of the current foreground window. It will say one of:

- maximized
- restored
- minimized
- docked left, docked right, docked top, docked bottom (half-screen snaps)
- top left quarter, top right quarter, bottom left quarter, bottom right quarter

**Optional NVDA+T enhancement.** In NVDA Settings under Window State, there's a checkbox to append the window state to NVDA+T. When enabled, NVDA+T says "Firefox, maximized" or "Firefox, restored" on first press. This matches the JAWS behavior. The second press (spell title) and third press (copy to clipboard) still work exactly as before. The setting is off by default so it doesn't change NVDA+T until you opt in.

All commands are remappable from NVDA's Input Gestures dialog.

## How It Works

The add-on uses three Win32 API calls. `GetWindowPlacement` checks whether the window is maximized, minimized, or normal. `GetWindowRect` gets the window's actual position and size. `MonitorFromWindow` and `GetMonitorInfoW` get the monitor's work area, which excludes the taskbar.

For snap detection, it compares the window's rectangle against the work area. If the window fills the full width and full height, that's maximized, not snapped. If it fills half the width and the full height, it's docked left or right. If it fills half the width and half the height, it's a quarter. There's a pixel tolerance to account for window borders.

The maximized, restored, and minimized detection is reliable. It uses the same Win32 calls JAWS uses. The snap detection needed real Windows testing to get right, and it works on my machine. I'd love feedback from anyone using multi-monitor setups or unusual resolutions.

## How I Built It

Same as WordPredictor. I design and review. AI implements. Every feature decision came from my experience as a screen reader user. I tested it, reported the bug I found (ctypes.wintypes doesn't have WINDOWPLACEMENT, which crashed NVDA on startup), and verified the fix.

WindowState v1.0.0 is available now. It requires NVDA 2026.1 or later.

**Download:** [github.com/RareBird15/windowState](https://github.com/RareBird15/windowState/releases/tag/v1.0.0)

This is my second NVDA add-on. Feedback welcome.
