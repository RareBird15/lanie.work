---
Title: "Building a Franken-System: When Ecosystems Fail Disabled Users"
Date: 2026-04-04
Category: Technology
Tags:
  - Accessibility
  - Disability
  - Technology
  - Workflow
Slug: franken-system
Summary:
  A personal look at the "accessibility tax" and why multiply-disabled users are forced to build fragmented, fragile
  tech stacks just to function.
---

## Table of Contents

[TOC]

## The Myth of the Seamless Ecosystem

The modern tech industry is built on a specific promise: buy into one ecosystem, and your digital life will effortlessly
sync.

But that convenience is a privilege. When you live with blindness, multi-system chronic illness, neurodivergence, and
topographical agnosia (a spatial processing disability that prevents my brain from forming mental maps, making it as
easy to get lost in a complex software menu as it is on a physical street), brand loyalty is a luxury. You can't choose
a platform simply because it integrates well. You choose a platform because it allows you to function. You have to
constantly weigh the cognitive load of one operating system against the screen reader reliability of another.

Because no single tech giant has solved accessibility across all their products, I can't stay within one walled garden.
Instead, I have been forced to build a "Franken-System." By stitching together the most accessible parts of Windows,
Apple, Linux, and Google, I have built a tech stack that actually works for me. But it comes at a steep cost. I have
traded away seamless integration just to secure the basic ability to use my own devices.

## The Hardware Split (Windows PC and iOS)

My hardware setup is the clearest example of this compromise. For my desktop environment, Windows is the most accessible
platform because the assistive technology is abundant and reliable. I avoid Mac entirely due to its heavily spatial
design, high cost, and long-standing issues with VoiceOver on macOS. While I love the Linux command line, a native Linux
graphical desktop isn't a viable option for me. The Orca screen reader lacks the robust features of NVDA, there's far
less assistive software available, and the environment demands unpredictable, cognitively expensive configuration just
to get basic things working.

Then there is the mobile side. Between my coordination issues, topographical agnosia, fatigue, and blindness, I
generally dislike using phones. But when I must use one, the iPhone is my only practical choice. iOS provides the most
predictable screen reader behavior and a highly accessible app ecosystem. I avoid Android because the screen readers do
not work as well for me, and the operating system feels slower and less accessible overall.

This isn't just a tax on my time and energy; it's a financial tax. I can't opt for a budget Android phone or a cheap
ChromeOS laptop. I'm forced into higher price brackets simply because those are the only devices that offer the baseline
accessibility I need to function.

This split setup is where the integration tax hits hardest. Because I use an iPhone with a Windows PC, I completely lose
the continuity features that come with using a Mac. My workflow is full of friction points:

- **Messaging:** Integration is clunky and unreliable. It completely breaks for group messages.
- **Notifications:** I can see notifications on my PC, but clicking on them doesn't open the corresponding app or
  provide a seamless experience.
- **Audio Routing:** When calls come in, my phone audio sometimes starts playing through my PC speakers unexpectedly.
  This is disorienting and disruptive.
- **Hardware Gaps:** If I answer a call on my PC, the audio routes correctly, but my current desktop setup lacks a
  microphone to talk back.
- **Clipboard:** There is no native way to sync text between my iPhone and Windows PC. Third-party clipboard sync
  solutions exist, but they are often inaccessible or unreliable. This forces me to manually transfer links or notes
  using email or cloud storage.
- **File Management:** I can't easily access files stored on my PC from my iPhone. I have to use Google Drive as a
  middleman, which adds extra steps and potential points of failure.
- **App Ecosystem:** Many apps I use on my PC don't have iOS versions, and vice versa. This forces me to find
  alternative tools that may not be as effective or accessible.
- **Voice Assistants:** I can't use Siri on my iPhone to control my PC, and I can't use Copilot on my PC to control my
  iPhone. This lack of cross-device voice control is a missed opportunity for accessibility.
- **Ecosystem Features:** I miss out on features like Handoff, Universal Clipboard, and iCloud syncing that would make
  my workflow smoother if I were fully within the Apple ecosystem.

This lack of integration creates a constant friction point in my workflow. I'm forced to find workarounds for tasks that
should be seamless.

## The Developer's Compromise (Linux via WSL)

Even though a native Linux desktop is inaccessible to me, I still need Linux. As a developer, working in plain text is
highly accessible and efficient. I spend most of my time writing Python and Bash scripts, and the Linux command line is
the best place to do that.

When my last PC died, I actually tried to set up a dedicated Linux machine using a Raspberry Pi running Stormux (based
on Arch Linux ARM). It was a failed experiment. Because the accessibility support was so poor, a task that took one step
on Windows took ten steps on the Pi. It demanded far too much cognitive energy and physical fatigue, making it a
completely unsustainable environment.

This is where my Franken-System requires a compromise. Instead of fighting with dedicated Linux hardware, I use Windows
Subsystem for Linux (WSL). WSL is the perfect bridge. It allows me to stay inside the accessible Windows desktop
environment while giving me full access to the powerful Arch Linux command line tools I need. I get the best parts of
Linux without ever having to navigate an inaccessible graphical interface. I can run my Python scripts, use fzf for
fuzzy finding, and manage my development environment all within WSL.

## The AI Barrier

The latest layer of my Franken-System is Artificial Intelligence. AI has the potential to be a massive cognitive
prosthetic, helping with everything from word-finding to summarizing complex documents. But even here, the walled
gardens are closing in.

Windows integrates Copilot, but I have found it lacking in memory and flexibility. There is no way to swap it out for a
different AI provider that might better suit my needs. Apple is the same. iOS uses Siri, and if you want more advanced
features, your only option is ChatGPT. This lack of choice means I can't tailor my AI assistance to my specific
disabilities.

Furthermore, the AI features that could help me the most (like Recall for memory support or better native text
suggestions) are often locked behind specific hardware. On Windows, many of these features require a Copilot+ PC. These
devices use ARM-based processors. While these processors are efficient, ARM-based Windows is notorious for poor
compatibility with specialized assistive technology. While major screen readers are starting to add support, many of the
smaller, specialized tools I rely on simply don't work. I'm forced to choose between the cutting-edge AI that could
support my neurodivergence and the stable hardware I need just to run my screen reader.

## The Service Disconnect (Google and Amazon)

The software layer of my setup is just as fragmented. I rely heavily on Google services like Drive, Search, and Gemini.
However, I have to run them on Apple hardware because the screen readers on Android and ChromeOS fall short for my
needs. Using Google services on an iPhone creates a functional but highly disconnected workflow. I'm constantly jumping
between apps that were never built to work together.

Then there is the frustration of voice control. Smart assistants like Amazon Alexa have massive potential to save my
physical and cognitive energy. But in reality, current voice assistants punish non-standard speech. If I stumble over a
word, pause to think, or speak less clearly due to fatigue, the assistant simply times out or throws an error. A tool
that could be life-changing is rendered mostly unusable because it expects me to speak with robotic perfection.

Because this system is held together by digital duct tape, it's incredibly fragile. A single update from any one of
these companies can break a workaround I have relied on for years. I live in a constant state of low-level anxiety,
knowing that my ability to work or communicate depends on companies that don't even know my specific configuration
exists.

## Conclusion

Maintaining this Franken-System is exhausting. Beyond the technical hurdles, there is a significant cognitive cost to
this setup. Switching my brain from the keyboard-driven logic of NVDA on Windows to the touch-based gestures of
VoiceOver on iOS is a constant context switch. It adds a layer of mental fatigue that a unified ecosystem would normally
eliminate.

A disabled user should not have to choose between a device they can actually operate and a workflow that integrates
smoothly. The tech industry needs to move beyond walled gardens. We need better cross-platform accessibility standards
and true interoperability. Until companies prioritize open integration over locking users into a single brand,
multiply-disabled people will be forced to keep piecing together our own fragmented solutions just to participate in the
digital world.
