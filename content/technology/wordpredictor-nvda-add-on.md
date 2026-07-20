---
title: "I Built a Word Predictor for NVDA Because the Existing One Didn't Work for Me"
date: 2026-07-20
categories:
  - Technology
tags:
  - accessibility
  - disability
  - nvda
  - screen-reader
  - assistive-tech
  - autism
  - chronic-illness
slug: wordpredictor-nvda-add-on
description: >
  The existing word prediction tools don't work with NVDA. So I built my own add-on
  that predicts words using n-gram analysis, announces them through NVDA's speech
  engine, and works inside the screen reader instead of against it.
showTableOfContents: true
---

I use NVDA as my screen reader. I type a lot — articles, advocacy, code, messages. Word prediction would save me keystrokes and reduce the finger-brain disconnect that comes with my fine motor issues. The problem is that the existing word prediction tools don't work with NVDA.

Lightkey Pro AT is the main option. Its gestures conflict with NVDA commands. Its system-wide mode requires clicking with a mouse. Words get mangled when it pastes alongside the screen reader. It works against NVDA instead of with it.

So I built my own.

WordPredictor is an NVDA add-on that watches what you type and predicts the next word using n-gram analysis. Predictions are announced through NVDA's own speech engine. No external TTS. No clipboard pasting. No mouse required. It works inside NVDA instead of against it.

## Why I Need Word Prediction

I'm autistic and have multiple cognitive disabilities. Sometimes the word I need is right there in my head but the path from brain to fingers gets lost somewhere in between. Word prediction gives me options I can hear and pick from instead of having to pull every word out from scratch. It reduces the cognitive load of composing text when my brain is already working harder to process everything around me.

I also have rheumatoid arthritis. Hand pain makes typing expensive — every keystroke costs me something. When the add-on predicts the word I was reaching for and I can accept it with one keystroke instead of typing eight or ten characters, that's real pain saved over the course of a day.

And then there's the finger-brain disconnect — my fingers don't always do what my brain tells them to. I'll mean to type one word and my fingers will produce something else entirely. Word prediction lets me hear the options and choose deliberately rather than relying on my fingers to carry the full load.

These three things together — autism, cognitive disabilities, RA hand pain, and motor disconnect — are why I went looking for word prediction. The fact that what I found didn't work with my screen reader is why I built my own.

## How It Got Better Through Feedback

I developed versions 0.1.0 through 0.3.0 in one night. The next day, I posted about it on Mastodon and got feedback that made the add-on significantly better.

Nikola Jović pointed out that the bare number keys I was using for prediction selection broke heading navigation in browse mode. He was blunt about it, and he was right. I changed the selection keys to NVDA+Control+1 through NVDA+Control+0.

Justin Ekis suggested terminal auto-detection so the add-on doesn't interfere with command-line work. Good idea. I added detection for 30+ terminal applications, using both NVDA's own terminal classification and a list of known terminal names. It's toggleable in settings.

There was also a tricky bug where accepting a prediction with NVDA+Control+number would trigger application shortcuts because Control was still physically held down when the predicted word was typed. Chrome's history panel kept opening. Save dialogs appeared. It took several iterations to get right, but the final version polls for the Control key to be physically released before typing anything. No key injection, no stuck keys.

## What It Does

- Announces up to 10 predicted next words after you complete a word
- Partial-word prediction: type part of a word and get completions
- Learns from your writing in real time and saves across restarts
- Ships with pre-trained n-gram data
- Automatically disables in terminals
- Settings panel for configuration
- All keys remappable in NVDA Input Gestures

## How I Built It

I design and review. AI implements. This is how I build software now — I couldn't do it without AI assistance, but every design decision, every feature, every bug fix came from my experience as a screen reader user. When the Control key bug was firing Chrome's history panel, I was the one testing it, reporting it, and verifying the fix.

WordPredictor v0.5.0 is available now. It requires NVDA 2026.1 or later.

**Download:** [github.com/RareBird15/wordpredictor](https://github.com/RareBird15/wordpredictor/releases/tag/v0.5.0)

This is my first NVDA add-on. I'd love feedback from the community.
