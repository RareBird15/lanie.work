---
Title: Work and Learning
Slug: work-and-learning
Date: 2026-03-31
Summary: A summary of my professional usability testing, self-paced Computer Science studies, and technical interests.
---

## Table of Contents

[TOC]

I don't focus on building polished products for show. Most of my work is exploratory, rooted in lived experience, or
focused on making systems more robust. This page highlights my active roles and the technical systems I'm currently
mastering.

## Professional Usability Testing

I work as a **Freelance Accessibility Specialist and Usability Tester**. My work involves identifying barriers that
automated tools often miss, with a focus on the intersection of multiple disabilities.

**My testing focus includes:**

- **Screen Reader Logic:** Deep testing with NVDA (primary), JAWS, and VoiceOver.
- **Non-Visual Navigation:** Ensuring complex web apps and CLI tools are fully keyboard-navigable.
- **Cognitive Load & Sensory Design:** Evaluating if interfaces are predictable and respect user energy and focus.
- **Gaming Accessibility:** Testing incremental and text-based games for screen reader compatibility and "low-pressure"
  playability.

## Computer Science & Systems

I'm currently a self-paced student moving through a rigorous Computer Science curriculum. Rather than chasing the latest
frontend trends, I focus on the "bones" of computing:

- **Programming:** Working through the **Codecademy Computer Science path** (currently ~22% complete), with a focus on
  **Python, Lua, and SQL**.
- **Linux Mastery:** Running **Arch Linux via WSL** as my primary development environment.
- **Dotfile Management:** Using **`chezmoi`** to maintain a consistent, accessible CLI environment across Windows and
  Linux.
- **Environment Tooling:** Utilizing **`uv`** for Python package management and **Docker** for isolated service testing.

## Technical Projects & Advocacy

### Operational IT Support

I serve as the **IT Manager for Apache Restoration & Design**. This isn't just "fixing computers". It's about software
evaluation, creating accessible operational documentation, and ensuring business systems remain functional for
non-technical users.

### The "Bandit" Wargames

I'm currently working through the **OverTheWire Bandit** games to sharpen my Bash and security fundamentals in a
hands-on, text-based environment.

### Community & Advocacy

My work extends into peer support and writing about the intersection of **faith, technology, and disability rights**. I
believe that good technology should be an act of care, not just a feat of engineering.

## Repositories & Tracking

If you're interested in the "raw" side of my learning, you can find my experiments and configurations here:

- **[GitHub: RareBird15](https://github.com/RareBird15)** – My scripts, dotfiles, and learning projects.
- **[Code::Stats](https://codestats.net/users/RareBird15)** – A real-time look at the languages I'm currently
  practicing.

## Featured Projects

### Terminal Bible Reader

The **Bible Reader** is a lightweight, terminal-based workflow designed for daily scripture reading. It focuses on logic
and accessibility rather than visual polish, serving as a practical tool for users who prefer text-centric environments.

#### Core Functionality

The project automates the transition from complex digital formats to a simple, day-by-day terminal interface:

- **EPUB Processing**: It imports WorldBiblePlans-style EPUBs and converts them into a normalized markdown plan.
- **Modular Content**: The system splits full plans into individual files, separating scripture from commentary to allow
  for focused reading.
- **Progress Tracking**: It utilizes standard Linux (XDG) directories to maintain local state, tracking which day the
  user is on without cluttering the home folder.

#### Accessibility and Design Philosophy

Accessibility is treated as a core technical requirement rather than a cosmetic feature:

- **Screen Reader Optimization**: Output is formatted as plain, readable text with predictable headings, avoiding
  decorative ASCII art or color-dependent information.
- **Low Cognitive Load**: The design emphasizes clarity and predictability, making it suitable for users who value
  humane technology.
- **Keyboard-Centricity**: As a CLI tool, it is fully navigable via keyboard, fitting into a streamlined Linux
  development environment.

#### Integration and Tooling

Built as a modern Python package, it integrates directly into a CLI-driven workflow:

- **Shell Integration**: The `maybe-read-bible` command can be added to shell startup files (like `.bashrc`), prompting
  the user to read exactly once per day.
- **State Management**: It uses file locking to prevent multiple terminal instances from overwriting progress
  concurrently.
- **Modern Stack**: The project is maintained using tools like `uv` for dependency management and `ruff` for code
  quality.

#### Project Purpose

This tool represents an intersection of faith and technical systems, prioritizing robust code that serves the user’s
specific needs over following frontend trends.

#### Link to Repository

- **[Terminal Bible Reader on GitHub](https://github.com/rarebird15/bible-reader)**: Explore the code, contribute, or
  use it for your own daily scripture reading.
