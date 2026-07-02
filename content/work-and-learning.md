---
title: Work and Learning
slug: work-and-learning
date: 2026-03-31
description:
  A summary of my professional usability testing, self-paced Computer Science studies, and technical interests.
showDate: false
showTableOfContents: true
---

I don't focus on building polished products for show. Most of my work is exploratory, rooted in lived experience, or
focused on making systems hold up better in real life. This page highlights my active roles and the technical systems
I'm currently working through.

## Professional Usability Testing

I work as a **Freelance Accessibility Specialist and Usability Tester**. My work includes identifying barriers that
automated tools often miss, especially where multiple disabilities overlap.

**My testing focus includes:**

- **Screen Reader Logic:** Deep testing with NVDA (primary), JAWS, and VoiceOver.
- **Non-Visual Navigation:** Ensuring complex web apps and CLI tools are fully keyboard-navigable.
- **Cognitive Load & Sensory Design:** Evaluating if interfaces are predictable and respect user energy and focus.
- **Gaming Accessibility:** Testing incremental and text-based games for screen reader compatibility and "low-pressure"
  playability.

## Computer Science & Systems

I'm currently a self-paced student moving through a Computer Science curriculum. Rather than chasing the latest frontend
trends, I focus on the "bones" of computing:

- **Programming:** Working through the **Codecademy Computer Science path** (currently ~22% complete), with a focus on
  **Python, Lua, and SQL**.
- **Linux Mastery:** Running **openSUSE via WSL** as my primary development environment.
- **Environment Consistency:** Maintaining a stable, accessible CLI environment across Windows and Linux.
- **Environment Tooling:** Using **`uv`** for Python package management and **Docker** for isolated service testing.

## Structured Learning & Certifications

Alongside hands-on projects, I use structured courses to build a stronger foundation in backend development,
command-line workflows, accessibility, and assistive technology.

### Backend and Python Foundations

My current learning focus is Boot.dev’s backend-oriented curriculum, where I’ve completed courses and projects covering
Python, Linux, Git, object-oriented programming, functional programming, and command-line application development.

Recent completed work includes:

- **Learn to Code in Python:** Python fundamentals including variables, functions, scope, loops, data structures, error
  handling, unit testing, debugging, and type hints.
- **Build a Bookbot in Python:** A local command-line application that analyzes novels and other plain text files, then
  generates word and character count reports.
- **Build Asteroids with Python and Pygame:** A playable arcade-style game using Python, Pygame, object-oriented design,
  collision detection, keyboard input, and a real-time game loop.
- **Learn Object-Oriented Programming in Python:** Practice with classes, objects, methods, inheritance, encapsulation,
  and reusable code structure.
- **Learn Git:** Core version control workflows including repositories, staging, commits, branches, merges, conflict
  resolution, and project history.
- **Learn Linux:** Command-line workflows for navigating filesystems, managing files and directories, running scripts,
  using pipes and standard input/output, inspecting processes, permissions, and installing developer tools.
- **Learn Functional Programming in Python:** First-class functions, pure functions, immutability, recursion, closures,
  currying, decorators, function transformations, and sum types.

### Command Line and General Programming Foundations

Earlier coursework through Codecademy and Sololearn helped build my foundation in programming concepts, terminal
workflows, and developer vocabulary.

- **Codecademy Learn the Command Line:** Filesystem navigation, file and directory management, input/output redirection,
  and command-line environment configuration.
- **Codecademy Code Foundations Skill Path:** Introductory programming concepts across computer science, web
  development, and data science.
- **Sololearn C++ Tutorial Course:** Foundational programming concepts including syntax, variables, control flow,
  functions, object-oriented basics, and problem solving.

### Accessibility and Assistive Technology

I also hold NV Access certifications that support my accessibility testing work and lived experience with screen-reader
workflows.

- **NVDA Certified Expert:** General proficiency with the NVDA screen reader, nonvisual navigation, assistive technology
  support, and helping others use NVDA effectively.
- **NVDA Certified Expert with Microsoft Word:** Proficiency using NVDA with Microsoft Word through keyboard-based
  document workflows.

## Technical Projects & Advocacy

### Operational IT Support

I serve as the **IT Manager for Apache Restoration & Design**. This isn't just "fixing computers." It's about evaluating
software, creating accessible operational documentation, and keeping business systems functional for non-technical
users.

### The "Bandit" Wargames

I'm currently working through the **OverTheWire Bandit** games to sharpen my Bash and security fundamentals in a
hands-on, text-based environment.

### Community & Advocacy

My work also includes peer support and writing about the intersection of **faith, technology, and disability rights**. I
believe good technology should be an act of care, not just a feat of engineering.

## Repositories & Tracking

If you're interested in the "raw" side of my learning, you can find my experiments and configurations here:

- **[GitHub: RareBird15](https://github.com/RareBird15)** – My scripts, dotfiles, and learning projects.
- **[Code::Stats](https://codestats.net/users/RareBird15)** – A real-time look at the languages I'm currently
  practicing.

## Featured Projects

### Terminal Bible Reader

The **Bible Reader** is a lightweight, terminal-based workflow for daily scripture reading. It focuses on logic and
accessibility rather than visual polish, and it's built for users who prefer text-centric environments.

#### Core Functionality

The project turns complex digital formats into a simple, day-by-day terminal interface:

- **EPUB Processing**: It imports WorldBiblePlans-style EPUBs and converts them into a normalized markdown plan.
- **Modular Content**: The system splits full plans into individual files, separating scripture from commentary to allow
  for focused reading.
- **Progress Tracking**: It uses standard Linux (XDG) directories to maintain local state, tracking which day the user
  is on without cluttering the home folder.

#### Accessibility and Design Philosophy

Accessibility is treated as a core technical requirement, not a cosmetic feature:

- **Screen Reader Optimization**: Output is formatted as plain, readable text with predictable headings, avoiding
  decorative ASCII art or color-dependent information.
- **Low Cognitive Load**: The design emphasizes clarity and predictability, making it a good fit for users who value
  humane technology.
- **Keyboard-Centricity**: As a CLI tool, it's fully navigable via keyboard, fitting into a streamlined Linux
  development environment.

#### Integration and Tooling

Built as a modern Python package, it fits directly into a CLI-driven workflow:

- **Shell Integration**: The `maybe-read-bible` command can be added to shell startup files (like `.bashrc`), prompting
  the user to read exactly once per day.
- **State Management**: It uses file locking to prevent multiple terminal instances from overwriting progress
  concurrently.
- **Modern Stack**: The project is maintained using tools like `uv` for dependency management and `ruff` for code
  quality.

#### Project Purpose

This tool sits at the intersection of faith and technical systems, prioritizing robust code that serves the user's
specific needs over chasing frontend trends.

#### Link to Repository

- **[Terminal Bible Reader on GitHub](https://github.com/rarebird15/bible-reader)**: Explore the code, contribute, or
  use it for your own daily scripture reading.
