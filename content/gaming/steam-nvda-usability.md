---
title: "Using Steam with NVDA: What Works, What Doesn't, and What Valve Should Fix"
date: 2026-07-19
lastmod: 2026-07-19
categories:
  - Gaming
tags:
  - accessibility
  - steam
  - nvda
  - screen-reader
  - usability
slug: steam-nvda-usability
description: >
  Steam added accessibility features in 2025, but the desktop experience with
  NVDA still has real barriers. Here's what works, what doesn't, and what
  Valve should fix next.
---

I use Steam with NVDA every day. It works, mostly. But "mostly" is doing a
lot of heavy lifting in that sentence.

In 2025, Valve added accessibility settings to the Steam desktop client and
introduced a built-in screen reader for SteamOS and Big Picture Mode. That's
real progress, and I want to acknowledge it. But the desktop experience that
most Windows users rely on still has significant barriers for screen reader
users. This post is not a WCAG audit. It's a report from daily use.

## What Works

Let me start with the positive, because it's important to acknowledge what
Valve got right.

Steam's main interface is navigable with NVDA. I can arrow through the library,
launch games, and manage my account. Clicking on elements generally works. I
can usually accomplish what I'm trying to do, sometimes with a bit of work.
The fact that Steam is functional at all with a screen reader is more than
can be said for many game launchers.

One important note: I navigate with arrow keys, not Tab. Tab only moves to
buttons, edit fields, links, and similar form elements. Since most of Steam's
interface is clickables, Tab skips over large portions of the UI. Arrow
navigation is the only way to move through everything linearly. This works,
but it means I'm reading every element in order rather than jumping to
interactive controls.

## What Doesn't Work

Here's where the daily experience breaks down.

### No Heading Structure

Steam has almost no heading structure. For an NVDA user, headings are the
primary way to navigate a complex interface. Pressing H to jump by heading,
or inserting a heading list with NVDA+F7, is how we orient ourselves in a
page or app. The library page has one heading for library filters. That's it.
Everywhere else, navigation is linear. You arrow through everything or use
object navigation to move around. In a content-rich app like Steam, the
absence of headings turns navigation into a slow, linear crawl.

### Clickables Instead of Links or Buttons

Most interactive elements in Steam are generic clickables rather than proper
links or buttons. NVDA announces them as "clickable," which tells me I can
activate them but gives me no semantic information about what they are. A
link should be announced as a link. A button should be announced as a button.
When everything is "clickable," I lose the ability to use quick navigation
keys (B for buttons, K for links) to move efficiently through the interface.

### Popups on Launch

When Steam launches, popups appear for the friends list and special offers.
These popups capture focus and interrupt navigation before I've even oriented
myself in the main window. For a screen reader user, unexpected focus shifts
are disorienting. I have to find and dismiss these popups before I can start
doing what I opened Steam to do. A setting to suppress launch popups, or at
least to delay them until the main window is focused, would make a meaningful
difference.

### Unlabeled Window Controls

The minimize, maximize, and close buttons are unlabeled. NVDA announces them
as "clickable" with no indication of what they do. There's no text, no
accessible name, nothing. In an interface where these are the first elements
encountered when managing the window, having to guess which clickable closes
the app and which one minimizes it is an unnecessary barrier.

### Unlabeled Buttons in the Library

The library page has unlabeled buttons alongside its combo boxes and filter
controls. NVDA announces them as "button" with no text describing what they
do. In a library where buttons control filtering, sorting, and view options,
an unlabeled button is a guess. I can click it and see what happens, but I
shouldn't have to. Every button should have a text label or an aria-label
that tells NVDA what it does.

### Two Confusing Tables on the Library Page

The library page contains two tables, both showing my games but in different
layouts. One is a table with 1 row and 38 columns. The other is 7 rows and 6
columns. NVDA announces both as tables, but neither is clearly labeled to
explain what layout it represents or why there are two of them. For a screen
reader user, encountering two unlabeled tables with the same content in
different shapes is confusing. Which one should I use? What's the difference?
Without labels or headings to distinguish them, I have to explore both to
figure it out.

### Menus Don't Respond to Alt Commands

The menus at the top of the Steam window (Steam, View, Games, Friends, and
others) are clickables, not standard menu bar items. They don't respond to
Alt or Alt+letter, which are the standard Windows keyboard shortcuts for
opening menus. The only way to open them with a screen reader is to navigate
to them and press Space or Enter. The good news is that once a menu opens,
NVDA can announce the items inside it as menu items. But getting there
requires navigating through clickables to find the menu rather than pressing
a single keyboard shortcut.

### Store and Community Are Not In the App

When I click Store or Community in the Steam app, I don't get an in-app
store or community interface. Instead, I get a URL. Clicking the URL or the
clickable right under it copies it to my clipboard. There's no text
explaining what to do with this URL, no instruction to open it in a browser.
Just a URL sitting there. I'm guessing this means Valve intends for me to
visit the store and community sections in my web browser, but nothing in the
interface says that. For a screen reader user, encountering an unexplained
URL where you expected a page is disorienting. If the store and community are
web-only, the app should say so.

### Right-Click Context Menus Don't Work from Keyboard

Certain actions, such as uninstalling a game from the library, require
right-clicking an item to open a context menu. The standard keyboard
shortcut for right-click is Shift+F10. In Steam, Shift+F10 does nothing. To
access the context menu, I have to route the mouse cursor to the focused
element using NVDA's mouse routing command and then simulate a right-click.
This is a workaround that requires technical knowledge of NVDA and adds
unnecessary steps to a basic action.

## A Pleasant Surprise: Big Picture Mode

After writing most of this post, I decided to try Big Picture Mode. I wish
I'd done this sooner. It's significantly more accessible than the desktop
client.

Big Picture Mode has headings. It has lists. It has buttons that are
announced as buttons, not clickables. It has keyboard shortcuts that work.
It even has a couple of sound effects that provide useful feedback. The
overall structure is more navigable, more predictable, and more screen reader
friendly.

I may switch to Big Picture Mode as my default. The fact that Valve's more
accessible interface is the one most Windows users never open is worth
noting. If Big Picture Mode is this much better with NVDA, the desktop client
should be learning from it, not ignoring it.

## What Valve Should Fix

Based on my daily experience, here are the changes that would have the biggest
impact for NVDA users on the desktop client, in order of priority:

1. **Add heading structure.** This is the single most impactful change Valve
   could make. Headings in the library, settings, and account sections would
   transform navigation from linear scanning to efficient jumping.

2. **Use proper semantic elements.** Links should be links. Buttons should be
   buttons. Menus should be menus, not clickables. "Clickable" is not a
   semantic role.

3. **Label all controls.** Window controls, library buttons, icon-only
   buttons, and any element that relies on visual context needs a text label
   that screen readers can announce.

4. **Support standard Windows keyboard shortcuts.** Alt for menus, Shift+F10
   for context menus. These are Windows conventions. Steam should follow them.

5. **Suppress or delay launch popups.** Let screen reader users orient in the
   main window before presenting secondary content.

6. **Label the library tables.** If there are two tables showing games in
   different layouts, label them so screen reader users know which is which
   and what the difference is.

7. **Explain the store and community URLs.** If these sections are web-only,
   say so. Don't just drop a URL with no context.

8. **Bring Big Picture Mode's accessibility to the desktop client.** Big
   Picture Mode proves Valve can build an accessible Steam interface. The
   desktop client should inherit those patterns.

## Why This Matters

Steam is the primary PC gaming platform for millions of players. Valve has
made real accessibility progress in 2025, and Big Picture Mode shows they can
do better. But the desktop client, which is what most Windows users rely on,
still has fundamental barriers that make daily use harder than it needs to be.

I'm not writing this to complain. I'm writing it because I use Steam every
day, and I want it to be better. I want to browse my library without arrowing
through unlabeled tables. I want to uninstall a game without routing my
mouse. I want to open a menu with Alt like every other Windows app. And I
want the desktop client to be as accessible as Big Picture Mode already is.

Valve is clearly thinking about accessibility. The 2025 updates and Big
Picture Mode prove that. This post is feedback, not criticism. Here's what's
still broken from where I sit.
