---
Title: "How I Use AI for Cognitive Help and as a Second Brain"
Date: 2026-05-15
Category: Technology
Tags:
  - Accessibility
  - Disability
  - Technology
  - Workflow
  - AI
  - Cognitive Prosthetic
Slug: ai-as-second-brain
Summary:
  A personal look at how AI tools serve as a cognitive prosthetic for a multiply disabled
  user who relies on a custom stack of Pieces, Supermemory, Hermes Agent, and GitHub
  Copilot to function at baseline.
---

## Table of Contents

[TOC]

Most "second brain" content assumes a neurotypical user who can see a board, remember to open it, and has the executive function to maintain a system. The advice is always the same: capture everything, review weekly, trust the process.

That doesn't work when memory is the broken thing.

I can't trust the process because I won't remember to review. I can't capture everything because on bad days, the energy required to decide what matters and where to put it exceeds what I have. And I can't see a physical board at all.

Most productivity tools solve the problem from their point of view: how do I help organized people stay organized? They don't solve it from mine: how do I help someone who can't reliably start, maintain, or review a system?

This isn't a post about how AI makes me more productive. It's about how AI lets me function at baseline. The tools I describe remove the friction between having a thought and capturing it. Between needing to know something and finding it. The gap is smaller when you don't have to manually bridge every step yourself.

For most people, a "second brain" is a nice-to-have. For me, it's infrastructure. Without it, I lose track of my work, my health data, and the details that keep my freelance accessibility testing business running. With it, I can work from bed, keyboard-only, screen reader first.

The rest of this post covers what I use, how I use it, and why the combination matters when most tasks are a struggle to initiate and complete.

## What I use

I don't rely on one tool. The stack works because each layer covers what the others can't. Here's what I actually run:

### Pieces MCP Server

Pieces is my global brain. It captures everything in the background: clipboard text, screenshots with OCR, audio transcriptions, browser history. I don't have to remember to save context. It's already there. When I need to recall a debugging session from three weeks ago or find a code snippet I copied, Pieces finds it. It's less like a tool and more like a recording I can query.

### Supermemory

Supermemory is the curated memory layer. Pieces captures raw activity; Supermemory stores what I tell it matters. It's integrated into both Hermes Agent and GitHub Copilot, so they both know who I am and what I'm working on. I prune it regularly: delete stale task artifacts, keep durable facts like my writing preferences, project conventions, and environment setup. Atomic entries, one fact per entry, so search actually works.

### Hermes Agent

Hermes is the executor. It runs on a Raspberry Pi 500, always on, headless. My interface is text-only: no GUIs, no dashboards, just type what I need and get results back in Markdown. It handles browser automation, email triage, research, task breakdown. It reads from both Pieces and Supermemory, so it doesn't start every conversation blank.

### VS Code + GitHub Copilot

This is where I code. Copilot has access to Pieces and Supermemory through global instructions, so it knows my conventions: no em dashes, screen-reader-first structure, clean Markdown. When I open a project, I don't spend energy explaining context. The setup phase is already handled.

### The hardware reality

I'm totally blind and mostly bed-bound. My setup is a headless Pi 500 on my network, a keyboard-only workflow with a Keychron K10 Max, and a screen reader. Everything is terminal or web. This isn't a compromise. It's the most reliable way for me to work without physical strain or visual navigation.

### Guava Health

Browser-based health tracker for symptom and medication logging. They have an API for healthcare providers but nothing patient-facing for self-logging. I've asked them to add an API or MCP. For now, I use two workarounds: Hermes drives a headless browser to fill and submit forms, or I open Guava myself and tell its built-in assistant what to log. The browser automation breaks often enough that I need the second path as a backup.

### Sophtron

Money management for fixed income. I'm on a fixed income except for small amounts I earn from usability testing, but subscriptions and routine costs pile up. Most budgeting apps don't work for me: they have accessibility issues, no PC or web version, or they're built around variable income and don't make sense when you're tracking every dollar against a ceiling. Sophtron would give me a system designed around that reality. Tracking what goes out. Flagging when I'm close to limits. Doing the math without opening a spreadsheet. Still setting this up, but that's what I'm aiming for.

## Why not just use ChatGPT?

The obvious question: why build all this instead of just paying for ChatGPT?

ChatGPT does have a memory feature now, but it's limited. It doesn't save things reliably unless I explicitly ask it to, and what it does remember is surface-level. It can't connect to my files, my health tracker, my code editor, or my browser. It can't run in the background capturing what I do without me telling it to start. It's a general-purpose chat interface that generates text.

My stack remembers things automatically. It reads my context without me pasting it back in. It integrates with specific apps I use. It captures activity passively. It's not one product. It's a system I put together because I need specific capabilities: reliable permanent memory, background capture, local execution, and deep customization. ChatGPT doesn't offer any of that.

ChatGPT works fine for quick questions. But it doesn't solve the actual problem, which is that I need tools that work with my life rather than asking me to bring everything into the tool myself.

If you read my earlier piece about building a Franken-System across hardware ecosystems, this is the same pattern. No single AI product fits my needs. So I stitched together Pieces, Supermemory, Hermes, and Copilot, just like I stitched together Windows, iOS, and Linux, because nothing on its own was built for how I actually need to work.

## How the architecture actually works

The tools don't work in isolation. They form layers, each handling a different part of the problem. Thinking about them as layers is what makes the system reliable.

### Capture layer: Pieces

Pieces runs in the background and records what I do without me remembering to log it. Clipboard text, screenshots, audio, browser history. It doesn't need me to initiate anything. On days when my memory is gone or I'm in too much pain to plan, Pieces has already captured the raw material.

### Memory layer: Supermemory

Pieces captures everything, but most of it isn't worth keeping. Supermemory is where I store what actually matters: durable facts, project conventions, environment setup details, writing preferences. I manage it like a garden. Delete the dead stuff. Keep what lasts. This is the layer both Hermes and Copilot read from so they don't forget who I am between sessions.

### Reasoning layer: Hermes Agent and GitHub Copilot

These consume the other two layers. They know my context. When I start a coding session, Copilot already knows my conventions. When I ask Hermes to triage email, it knows what matters and can reference past work stored in Pieces. I don't spend energy explaining myself every time.

### Execution layer: text interface

Everything comes back as text. Markdown, clean structure, screen reader compatible. I give a command, the agent figures out the steps, handles the inaccessible GUIs, returns results I can actually read. The physical act of working doesn't require leaving bed or navigating a mouse-based interface.

### Why this matters

No single tool solves the whole problem. Pieces captures but doesn't curate. Supermemory curates but doesn't execute. Hermes executes but needs context to do it well. The stack works because the layers cover each other's gaps.

## How they help with specific struggles

Each tool in the stack solves a different kind of friction. Here's where they actually matter.

### Memory loss

I don't have to remember what I worked on. Pieces captured it. Supermemory indexed it. Either one retrieves it when I search. I used to spend energy trying to reconstruct a debugging session from last week, scrolling through chat logs and guessing at terminal history. Now I just ask, "what was I working on with the Flask routes yesterday?" and Pieces surfaces it. Search replaces recall. That saves energy I don't have on bad days.

### Executive dysfunction

I don't have to plan the order of steps. If a task is complex, AI breaks it into numbered actions with exact commands. I don't need to figure out what to do first, second, third. I just follow. "Set up ABLE account tracking" becomes a list of concrete actions. The cognitive load of deciding where to start is what usually stops me. Removing that decision is what gets things done.

### Health tracking without the initiation cost

RA flare tracking, medication logging, symptom patterns. The real problem isn't that I can't see the form. It's that on bad pain days, the executive function required to decide to log, remember what matters, and manually fill out fields just doesn't exist. Telling Hermes "log: ibuprofen at 2" removes all the intermediate steps. Hermes drives a headless browser and submits the entry to Guava. The data gets captured without me having to plan or initiate anything myself. When the browser automation breaks, I open Guava and tell its assistant instead. Both paths compress six decision points into one sentence.

### Financial complexity

Disability finance is complicated. I'm on a fixed income with small usability testing earnings, but subscriptions and routine costs pile up. Budgeting apps either don't work on PC, have accessibility barriers, or assume you have variable income to juggle. Sophtron would track thresholds, flag when I'm close to limits, and do the math without me opening a spreadsheet. The cognitive load of managing disability finance alone is massive. One wrong move can trigger a benefit review.

### Accessibility barriers

Screen readers work with text. AI generates clean Markdown, navigates GUIs I can't use, and handles visual CAPTCHAs through browser vision tools. Most web forms are inaccessible. They rely on visual cues, drag-and-drop, or date pickers that don't work well with assistive technology. AI bridges that gap by handling the interface and giving me text back.

### Phone anxiety

Calls are a major barrier for me. Word-finding issues and social anxiety make it hard to know what to say. AI drafts scripts, composes async messages, and handles communication that would otherwise require a phone call. GoFundMe updates, benefit paperwork, business emails: all of it goes through text. I don't have to perform on command.

### Physical limitations

I'm totally blind and mostly bed-bound. A headless Pi means no desk setup at all. Everything is keyboard and screen reader. This isn't a compromise. It's the setup that works for my body. I don't need to reach for a mouse, position a monitor, or navigate anything visual. The terminal is always available through my braille display and screen reader, and I can work from wherever I'm physically comfortable.

## Concrete examples

Telling you the stack works is one thing. Showing you how it works in practice is another. Here's what a typical day looks like.

### The coding session

I open VS Code on a new repo. Before I type a single line, Copilot's already reading my context. It knows from Supermemory that I write Markdown with specific structure, avoid em dashes, and prioritize screen reader compatibility. Pieces finds the last time I touched similar code, so it sees patterns I've already solved.

We start working. I don't spend twenty minutes explaining the project, my setup, and what I'm trying to do. The setup phase is already handled. I type a function, Copilot reviews it, I iterate. It catches an edge case I missed because I'm tired. If I get stuck, I ask Hermes to find a reference, and it searches the web, reads the docs, and returns a clean summary with links.

This isn't about writing code faster. It's about removing the twenty-minute ramp-up that usually stops me before I start.

### Low-energy logging on a bad day

Pain level is high today. I take ibuprofen and need to log it. The old way required: open Guava, navigate to today's date, pick the symptom category, select severity from a dropdown, add the medication, save. Six decision points. On a good day, annoying. On a bad day, impossible.

Now I send one sentence to Hermes: "ibuprofen at 2pm, pain level 6." Hermes opens a headless browser to Guava, navigates to the right form, fills the fields I can't easily access, and submits it. When the browser automation breaks, which it does sometimes, I open Guava directly and tell its assistant instead. Either way, the log happens with one input instead of six decisions.

### Research without tab management

I need to check how a new accessibility feature works in a specific browser before I give feedback on it for a usability testing gig. The alternative: open a browser, search for the feature, click through multiple results, read each page, cross-reference it with what I actually experience in my own setup, and take mental notes. That's exhausting.

Instead, I tell Hermes to summarize how the latest screen reader handles a particular feature and pull recent user reports. It browses, reads the pages, extracts the relevant information, and returns a clean summary. I get the context I need to form my feedback without managing tabs, scanning visually, or holding ten pieces of information in my head at once. Then I add my own experience on top of it.

### Phone-free communication

I need to follow up on a usability testing payment. The alternative is drafting an email while anxious about tone, or making a phone call where I might lose my words mid-sentence.

I tell Hermes to draft a polite follow-up about the payment I'm owed for last week's testing session. It writes a clean, professional email. I review it, adjust a word or two, and send it. No performance required. No guessing whether I'm being clear enough.

## What this system doesn't look like

This system isn't magic. It breaks, it requires maintenance, and it doesn't solve everything.

### AI gets things wrong

Hermes hallucinates sometimes. Copilot suggests code that doesn't work. Browser automation fails when Guava updates its page structure. I still have to read the output, verify it makes sense, and catch errors. The stack removes the initiation friction, but it doesn't replace the need to actually check the work. On bad pain days, even reviewing AI output takes energy I might not have.

### Infrastructure maintenance

None of this runs itself. Supermemory needs pruning. If I don't delete stale task artifacts, search returns garbage. Pieces settings need tuning when new capture types become noisy. Skills I save for Hermes get outdated when tools change. This is ongoing work. The payoff is that maintenance is text-based and keyboard-only, which means I can do it on days when I can't navigate a GUI, but it still costs something.

### It doesn't replace human connection

If anything, this system highlights how isolating it is to need all these bridges just to function at baseline. Every workaround is a reminder that the default setup wasn't built for me. AI makes the work possible, but it doesn't make it less lonely. I use the tools to participate in communities that still move too fast for me to keep up with in real time. The gap between what I can do alone and what I could do with a team is still wide.

## The closer

Most AI writing talks about boosting productivity or getting more done in less time. For me, it's different. It's about removing the friction that blocks baseline functioning in the first place. I don't use these tools to 10x my output. I use them so I can actually start the work instead of spending all my energy on just getting ready to do it.

Accessibility technology has lagged for decades. Screen readers get better, but the web breaks faster than it gets fixed. Physical accessibility tools are expensive, proprietary, and slow to adapt. AI is different. It's naturally text-first, keyboard-only, and automation-heavy. That matches exactly how blind and mobility-limited users already need to operate. In some ways, AI tools work better for disabled users than for the general population out of the box, because we already think in workflows that don't rely on dragging, clicking, or visual scanning.

I built this stack because nothing else covered the gaps. The productivity industry doesn't design for cognitive overload or chronic pain. They design for people who can sit at a desk, track their focus with apps, and remember what they did yesterday. I can't do those things reliably. So I built a system that does them for me.

If this post helps even one person figure out how to reduce their own friction, it was worth writing down.
