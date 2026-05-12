---
Title: "The Multiplicative Nature of Disability: Why 1+1 Equals a System Crash"
Date: 2026-05-11
Modified: 2026-05-11
Category: Advocacy
Tags:
  - Accessibility
  - Advocacy
  - Blindness
  - Neurodivergent
  - Chronic Illness
  - Disability
  - Philosophy
Slug: multiplicative-disability
Summary: >
  The common assumption is that multiple disabilities are additive: two disabilities means twice the difficulty.
  This is wrong. Disabilities compound multiplicatively, and accessibility design that ignores this causes active harm.
---

## Table of Contents

[TOC]

> **Sourcing Note:** The examples in this article are not hypotheticals. They are extracted from my own captured daily logs, technical sessions, and lived experiences. For a plain-language breakdown of the physical mechanics behind my diagnoses, see my [Human Terms summary]({filename}human-terms.md).

## The Comfortable Lie of the Sum

There's a model of disability that feels mathematically tidy and is almost entirely wrong.

It goes like this: a person has Disability A and Disability B. Their overall difficulty is therefore $A + B$. If we build an accommodation for A, we’ve reduced the total load to just $B$. Progress has been made. The spreadsheet balances. Everyone goes home feeling useful.

In reality, disability isn't an additive sum, but rather a **resource contention issue**. The correct relationship is closer to:

$$\text{Lived Difficulty} = (A \times B \times C) \cdot \text{System Design}$$

When the system design ignores the interaction between variables, when the accommodation built for Disability A requires a resource already depleted by Disability B, it acts as a multiplier. The result isn't a reduction in load; it’s a **buffer overflow**.

## System Specifications: Operating in "Manual Mode"

Most people experience their bodies like a high-level Python script: "batteries included." Breathing, swallowing, digestion, postural stability, and spatial awareness are handled by the standard library in the background. They're low-overhead, automated processes.

I operate in what I call **"Manual Mode."** My background processes aren't automated; I'm manually managing the event loop.

I'm totally blind, autistic (I think, though this is being reevaluated), and live with Topographical Agnosia (TA), meaning I have no mental map and must navigate using raw logic and tactile coordinates.

Among other conditions, I also manage Idiopathic Intracranial Hypertension (IIH), which feels like a balloon being over-inflated behind my eyes; fibromyalgia, which leaves my nervous system stuck on a high-pain setting; gastroparesis and esophageal dysmotility, which cause my digestive system to operate unpredictably; and a physical height of 4'10". My airway is compromised by severe allergies, and my swallowing reflex doesn't trigger automatically.

In a standard system, physiological survival is a background daemon. For me, it's a **blocking task** in the foreground. It requires constant, conscious CPU cycles. When an accessibility solution for one condition requires a capacity that another has already depreciated, the system triggers a `RecursionError` and crashes.

## Case One: The Spatial Audio Trap

Audiogames are consistently held up as the gold standard for blind accessibility. The design assumption is generous and logical: if a player cannot see a 3D space, give them directional audio. Let sound carry the spatial information.

For a blind player with a standard spatial mapping "driver," this works. For me, it is a second barrier built directly on top of the first.

Directional audio requires the listener to hear a sound, locate it in 3D space, translate that vector into a navigable direction, and execute a command under time pressure. Because of Topographical Agnosia, my brain doesn't have that spatial mapping library installed. I have to emulate it in software, manually calculating cardinal references, headings, and key-mappings.

This emulation is not free. It costs the exact same CPU cycles I use to maintain "Manual Mode."

When a game layers multiple simultaneous audio cues (enemy positions, environmental feedback, UI alerts) I'm not experiencing "immersive accessibility." I'm experiencing critical resource exhaustion. My cognitive scheduler is saturated trying to decode the spatial audio stack while simultaneously issuing the manual commands to swallow, breathe, and stay upright. Something gets dropped from the queue. Sometimes it's the game. Sometimes it's my airway.

## Case Two: Voice Interfaces and the Word-Finding Tax

Voice interfaces are marketed as the ultimate "hands-free" accessibility win. They remove visual and motor barriers. But for me, they represent a high-latency API call with a massive failure rate, creating an intersection of three simultaneous costs:

First, executive retrieval. My word-finding isn't always instant. A voice interface forces a real-time, high-priority retrieval call that my system may not have the memory to fulfill, particularly under cognitive load.

Second, the manual overhead. Speaking isn't "just talking." It's a sequence of manual motor commands:

- Initiate controlled exhale
- Coordinate vocal cords
- Sustain pressure through the sentence
- Remember what I'm trying to say while doing all of the above
- Try not to trail off mid-command when I need to breathe or forget a word (voice interfaces don't understand mid-sentence corrections or sudden stops)
- Suppress the urge to cough
- Resume normal breathing

A voice command is a taxing system call.

Third, the retry cost. When a voice interface mishears me, there's no cache, no retry at a reduced cost. I have to re-execute the entire high-cost `try/except` block.

The accommodation designed to reduce input barriers (voice) directly multiplies the cost of the conditions it wasn't designed to account for: executive retrieval load, speech coordination difficulty, and neurological manual overhead.

## Case Three: The Environmental Deadlock of Overhead Reaching

The multiplicative nature of disability isn't limited to digital interfaces; it dictates my physical reality.

I'm 4'10". That's an immutable hardware constraint. In a standard-height world, reaching over my head is a global variable I encounter constantly, from top kitchen cabinets to the highest fridge shelves and the microwave.

I actively try to avoid reaching overhead because it's a high-cost physical function. Reaching over my head actively spikes my intracranial pressure. Doing it can easily trigger a multi-day system crash where I'm entirely nonfunctional. But avoiding it is incredibly difficult when the physical environment demands it.

Earlier today, this environmental mismatch created a classic system deadlock.

- **The Dependency:** I have seborrheic dermatitis on my scalp. Washing my thick hair is a non-negotiable maintenance task to prevent bleeding and infection. As it is, I already don't shower as often as I should because of the energy and resource cost. I'm doing well if I can manage two showers a week.
- **The Hardware Constraint:** Reaching my showerhead and scrubbing my own scalp requires prolonged overhead reaching.
- **The Software Conflict:** I was in the middle of a brutal IIH and fatigue flare. My IIH felt barely manageable. I wanted to stay functional, but I knew that executing the "reach overhead" motion would crash my system for the rest of the day.

In a single-disability, additive model, an occupational therapist might suggest adaptations: a long-handled scalp massager for the shower, or a grabber tool for the high kitchen cabinets.

We didn't have the scalp massager. But more importantly, the grabber solution is an incompatible API. Because I'm totally blind and have Topographical Agnosia, a visual grabber is useless, unless you want a mess of broken items. I can't visually target an item on the top shelf, and I don't have the internal spatial mapping grid required to guide a 3-foot pole to an object I can't see.

I was stuck in a deadlock: preserve my system uptime but risk an infection flare, or execute the reach and trigger a critical pressure crash.

The math looked like this:
$$\text{Environmental Demand (Overhead Reach)} \times \text{IIH Flare} \times \text{Missing Spatial API} = \text{System Lock}$$

I couldn't solve the equation alone. I had to wait for a "subroutine" (my mom coming home from work) to assist with the manual labor of washing my hair. This isn't a lack of "independence"; it's a failure of an environment that assumes a standard height, a single-threaded body with infinite energy reserves, and the ability to use standard visual adaptations.

## Case Four: The Medical Hardware Incompatibility (CPAP)

Standard medical devices often assume a baseline physiological API. When that API is non-standard, the device becomes completely unusable. My experience with a CPAP machine for sleep apnea is a textbook example of compounding hardware, physiological, and bureaucratic failures.

Because I breathe through both my mouth and nose, I'm forced to use a full-face mask. But my body doesn't have an automatic swallow reflex. Overnight, saliva pools on my face with nowhere to go, turning the inside of the mask into a mess and creating a constant physical irritant.

The compounding variables don't stop at fluid management:

- **Inaccessible UI:** The machine itself (a ResMed AirSense 10) was inaccessible. I had to rely on my mom to adjust the settings.
- **Missing Dependencies:** My severe allergies are worsened by dry air. The machine's built-in humidifier was ineffective without heated tubing.
- **Bureaucratic Multiplication:** Medicaid refused to cover the heated tubing, claiming it wasn't "medically necessary"—an additive-model policy that ignores the multiplicative reality of my allergies and airway. I had to pay the $134 cost out of pocket just to attempt to use the machine.
- **System Rejection:** The combination of the irritating straps (even with special covers), the pooling saliva, the dry air, and my sensory processing issues created an unbearable sensory load. I would take the mask off in the middle of the night without even realizing I had done it.

The math for this "solution" was:
$$\text{Full-Face Mask} \times \text{Missing Swallow Reflex} \times \text{Sensory Load} \times \text{Bureaucratic Denial} = \text{Hardware Rejection}$$

The CPAP has been packed in a box for years because it's functionally unusable. Instead, I now sleep in a hospital bed, a necessary environmental mitigation for the combined realities of my IIH, GI conditions, and unsupported sleep apnea.

## Case Five: Independence as a Force Multiplier for Harm

At age eighteen, I was enrolled in a transition program at the Texas School for the Blind designed to build independence skills. The program's design assumption was well-intentioned and purely additive: "Blindness accommodations + Increased Demands = A prepared, independent graduate."

The program wasn't designed for a student who was also autistic, managing undiagnosed IIH, and operating in a body that required conscious neurological oversight for basic survival functions.

They had no variable for resource competition. The increased independence demands consumed the cognitive and neurological reserves I required to manage every other system. My body began to collapse. Fibromyalgia symptoms emerged as a permanent system error. Neurological overload became my baseline state. The harder I tried to meet their standard of independence, the worse every other condition became, because their definition of independence required me to spend resources I was already allocating just to stay alive.

When I communicated this, the institution's additive model had no way to process it. Because their spreadsheet did not have a multiplication operator, my physical collapse was interpreted as resistance, psychological instability, and a failure of motivation. My valedictorian status was removed. My assistive technology was confiscated. Scholarships were withdrawn. Had my mom not intervened and fought for me to return the next year, I wouldn't have been allowed to walk the stage at graduation. The institution's failure to account for the multiplicative nature of my disabilities resulted in active punishment for the predictable consequences of their design choices.

This is what happens when a system designed for singly-disabled users applies the additive model to a multiply-disabled body: it produces institutional punishment for the predictable consequences of an unfunded mandate.

## Memory-Backed Evidence from Captures

The proof of this compounding friction exists throughout my daily logs. Using Pieces, an AI memory assistant running in my code editor, I can trace these conflicts in my own automated captures:

- **2026-04-15 (Browser capture, article review):** "The Barrier of Voice Interfaces... Between word-finding issues and the energy required to maintain the 'Manual Mode' of my breathing and speech, real-time voice commands are a huge neurological challenge."
- **2026-04-15 (Browser capture, article analysis):** "The Spatial Trap of Sound... Audiogames... rely on directional audio... My brain cannot process this data... [it] drains the same limited energy bank I use for manual mode physical survival."
- **2026-04-18 (Browser capture, dictation friction):** "Voice assistants don't understand unless the command is perfectly formed... if I forget a word, use the wrong one..." and "This is a classic accessibility mismatch."
- **2026-04-13 (Browser capture, contact preferences):** "Text over Voice: I do not do well with voice calls or ephemeral audio."

These captures show the same pattern repeating across contexts: an accessibility pathway that helps one user profile creates a higher resource tax for mine. That's multiplication, not addition.

## The Resource Conflict Is the Disability

My most consistent struggle is the intersection of **spatial demand** and **manual survival**.

Whether I'm navigating a physical room, parsing a deeply nested dictionary in Python, or trying to reach a microwave on a top shelf, my brain is emulating a missing capacity. This "Spatial Emulation" and "Manual Mode" compete for the exact same thread.

$$\text{Spatial Demand} \times \text{Manual Overhead} = \text{Physical Crisis}$$

A demanding cognitive or physical task doesn't just result in frustration or normal fatigue. It produces an intracranial pressure spike and a multi-day system outage. The interaction between these conditions isn't a nuisance; it's an **exponential threat**.

## Multiplicative Design: A New Baseline

The additive model produces a checklist. Does the tool have a screen reader API? Check. Keyboard navigation? Check. High contrast? Check. Reduced motion? Check. Switch control? Check. Audio descriptions? Check. Voice commands? Check. Accommodation complete.

The multiplicative model requires a fundamentally different question: **What happens when a user needs all of these features simultaneously, and they conflict?**

- What happens when the screen reader's verbosity settings create cognitive overload for a user with executive dysfunction?
- What happens when keyboard navigation requires spatial mental modeling that competes with the user's limited physical resource pool?
- What happens when the user would benefit from switch control, but it doesn't work with screen readers?
- What happens when the user has a condition affecting their ability to type but also needs a screen reader, which doesn't work with either voice commands or switch control?

Multiplicative design requires **modular architecture**:

- **Modular Accommodation:** Features must not be monolithic. A user should be able to toggle spatial audio *off* while keeping screen reader support *on*. Do not force one "win" at the cost of another.
- **Resource Awareness:** Understand that every accessibility layer has a "cost." An interface that requires 10 seconds of sustained vocal output from a user whose attention is partially allocated to breathing is not a "free" resource.
- **Intersection as the Norm:** When a system is designed with a "blind user" or "autistic user" as its primary persona, it's underspecified. The CDC estimates that over half of adults with disabilities have more than one. Designing for the intersection isn't an "advanced feature". It's **stable code**.
- **Transparency over Perfection:** Sometimes needs conflict. The solution isn't to declare one need more legitimate. Expose the configuration, accept incompleteness, and allow the user to manage their own resource allocation.

## Conclusion

Two disabilities aren't twice the difficulty. They're potentially the square of it, or the cube, depending on how deeply the resource pools and the system's own design choices interact.

The additive model is comfortable because it is legible. Line items are easy to audit, fund, and mark complete. The multiplicative model is uncomfortable because it demands we reason about collisions, compounding costs, and the reality that a solution for one user can be an active harm to another.

I'm not an edge case. I'm the predictable result of a world that designed for one disability at a time and then encountered a user running multiple high-overhead processes on a system with no reserve capacity.

The math was never going to balance using addition. It’s time to change the operator.

---

### Python-Focused Optimization (Dev Log)

To manage these multipliers, my technical environment is strictly optimized for **low cognitive load** and **keyboard-first** efficiency:

- **CLI over GUI:** I use `fzf`, `ripgrep`, and `fd` to find files. This replaces the "spatial" need to browse a visual folder tree with a simple, linear text-search task.
- **uv for Package Management:** The speed and reliability of `uv` reduce the "wait-time" and unexpected errors that often trigger sensory spikes during environment setup.
- **Structured Data:** I prefer Markdown and JSON over complex visual interfaces because they allow me to navigate via logical structure rather than visual layout, minimizing spatial emulation overhead.
