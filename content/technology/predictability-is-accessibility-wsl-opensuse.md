---
title: "Predictability Is Accessibility: Why I'm Moving from Raspberry Pi to openSUSE on WSL"
date: 2026-06-21
categories:
  - Technology
tags:
  - accessibility
  - linux
  - wsl
  - opensuse
  - raspberry-pi
  - cognitive-load
slug: "predictability-is-accessibility-wsl-opensuse"
description: >
  Why I moved my Linux workflow from a Raspberry Pi to openSUSE on WSL, and why reliability, reachability, and lower
  cognitive load matter more than theoretical elegance.
showTableOfContents: true
---

Raspberry Pis are great little Linux machines for a lot of people.

This is not a "Pi bad" post.

It's a post about accessibility tradeoffs.

I wanted the Pi setup to work. On paper, it looked ideal: cheap, low power, always-on, and very "Linux."

In practice, it kept failing one question:

> Can I still use this when I'm sick, tired, blind, overwhelmed, and low on energy?

For me, the answer kept being no.

So I'm moving this part of my Linux workflow to openSUSE on WSL.

## What I Wanted the Pi to Be

I wanted a little Linux box for:

- MiniFlux and feed tooling
- small dev services
- always-on utility tasks
- eventual agent experiments
- coding and static site work: my own little dev box

That's a normal Pi use case.

The issue is that "normal" advice often treats extra steps as tiny. For me, many of those steps are real access costs.

## What Actually Happened

The biggest problem was not one giant failure. It was repeated friction that kept stacking up.

### Headless was fragile for my access needs

I'm blind. "Just glance at the screen" is not part of my troubleshooting toolkit.

When SSH failed, the Pi effectively went silent for me. No SSH, no speech output, no reliable way to confirm state.

Even plugging in a keyboard did not solve that. Blind typing into an unknown login state is guesswork, not access.

Even the Raspberry Pi 500's built-in keyboard didn't solve this. I bought the 500 partly because it was new and partly
because the built-in keyboard sounded like it might make direct access easier. In practice, I didn't realize how tiny
that keyboard would feel. I had to count keys to know where I was, so it never became a usable fallback. If I had to
physically use the Pi, I would want a wireless keyboard, and speech output would still be required.

This is the line I keep coming back to:

> Headless is only accessible when the access path survives failure.

### Network assumptions were not minor

Many recovery suggestions assume Ethernet is easy. In real life, "just plug in Ethernet" can require the right cable,
the right physical setup, and enough energy at the right time.

I also tried mobile tethering ideas, but those can still depend on trust prompts and setup steps that fail exactly when
you need a quick recovery path.

So SSH and network access became a single point of failure.

### ARM increased unpredictability

I kept hitting package issues on ARM: missing packages, older versions, weird differences, and more "why is this
different here?" than I could sustain.

ARM is useful. I'm not anti-ARM.

But for me, it made daily setup and recovery less predictable.

Predictability is an accessibility feature.

### Physical recovery loops were expensive

When things broke badly, recovery could turn into a physical loop:

- remove storage
- connect it to another machine
- mount and edit
- unmount and reinsert
- reboot and hope

That's a lot when you're blind, chronically ill, and fatigued.

Sometimes the Pi needed a power cycle. If I was away, too sick, or in the hospital, work on that device was basically
trapped.

In the worst moments, recovery depended on someone else being home and available.

That's not reliable infrastructure for my life.

There's also the hospitalization problem.

With my health, rehospitalization isn't theoretical. During my last hospital stay, I had my PC with me, but not the Pi.
Just because the Pi was running at home didn't mean it was reachable or useful. If coding work or service setup lives
only on a device across the house or across town, it can get trapped the moment I'm away from it.

It gets worse because the Pi sometimes becomes unresponsive and needs to be physically unplugged and plugged back in.
Asking my mom to power-cycle it can work if she's home, awake, able, and available. But it turns my dev setup into
another chore chain for her: I notice something is broken, ask her to stop what she's doing, wait for her to physically
handle the device, and hope it comes back.

That's not independence. It's another dependency.

My coding environment needs to follow me. At minimum, the important work has to live somewhere I can reach from the
computer I actually have with me.

## Why WSL Works Better for Me

WSL is not "pure Linux," and I'm fine with that.

That tradeoff matters less to me than having a Linux environment I can actually reach and recover.

It lives where I already work:

- same keyboard
- same NVDA/screen reader workflow
- same desktop, browser, and AI tools
- same files and copy/paste
- same recovery path

If WSL gets weird, I can usually recover from the same environment with a shutdown/restart workflow and keep moving.

No separate device. No separate network path. No separate physical intervention for basic access.

That matters because Windows and NVDA are not separate from the setup. They are part of what makes the setup usable.

## Why openSUSE on WSL Surprised Me

I didn't assume "Linux is Linux."

I'd already learned that distro choice, package manager choice, and maintenance culture matter.

I tried Ubuntu, Debian, and Raspberry Pi OS. They were stable in the usual sense, but older packages became a recurring
problem for accessibility-adjacent tools, dev tools, and newer workflows. I can use `apt`, but it has never felt very
intuitive.

Then I tried Arch. At first, I liked it. It was current and flexible, and it felt empowering.

But on a Raspberry Pi, that empowerment started feeling fragile. Arch Linux ARM gave me rolling-release sharpness plus
extra ARM and Pi friction: boot quirks, SSH dependence, SD cards, and headless recovery loops. When it worked, it felt
elegant. When it failed, it became a silent box I could not reliably reach or recover.

That's what made me try openSUSE.

On paper, Tumbleweed looked like the balance I wanted: current packages with more structure and guardrails than Arch. I
wanted a distro that still respected power users but gave me more cognitive help.

I first tried openSUSE on the Pi, and that attempt didn't make it past first boot in a usable way. On a headless Pi with
no speech output, a first-boot failure isn't minor. It's the same trap again: no reliable SSH, no accessible feedback,
no clear state, and no low-energy recovery path.

Then I tried openSUSE in WSL.

That was the version that finally clicked.

The same distro that felt painful on a silent, separate Pi became usable and even pleasant inside my existing Windows
workflow. I had NVDA, my keyboard, my browser, my notes, ChatGPT, VS Code, copy/paste, and my usual recovery path.

I was no longer rescuing a silent box across the network. I was working in a system I could actually reach.

What helped inside openSUSE itself:

- `zypper` output is easier to follow with a screen reader
- `zypper` short forms like `zypper in` and `zypper se` are easy to remember
- package recommendations reduce follow-up setup work
- command-not-found suggestions help on low-cognitive-energy days
- package behavior feels less punishing when things are already current

> Friendly defaults are not hand-holding. They are reduced cognitive load.

## Quick Checklist: Pi vs WSL for Access Needs

If you're deciding between a separate Linux box and WSL, ask:

- If remote access fails, do I still have an accessible fallback?
- Can I recover this setup without visual checks?
- Does this setup depend on physical intervention I may not be able to do?
- Are package and tooling differences predictable enough for my energy level?
- Can I troubleshoot from the same device where I already use my accessibility tools?
- On my worst health day, is this still usable?

If most answers are no, the setup may be technically impressive but practically inaccessible.

## The Accessibility Lesson

For disabled users, reliability is not boring.

Predictability is not optional.

A tool that technically works but repeatedly needs physical access, obscure recovery steps, or network luck can still be
inaccessible in practice.

The best tool is not the one that looks most elegant to the average Linux hobbyist.

It's the one I can still use when I'm sick, tired, blind, overwhelmed, and alone in bed.

## Final Stance

Raspberry Pi is still a great platform.

It's just not the right accessibility tradeoff for me right now.

For now, openSUSE on WSL is the Linux setup that fits my body, my brain, and my access needs.

For me, simpler doesn't mean fewer machines in theory. It means fewer failure paths in practice.

One accessible workstation. One keyboard. One screen reader. One familiar path back when things break.
