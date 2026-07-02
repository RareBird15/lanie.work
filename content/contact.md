---
title: Contact
description: How to reach me and what to expect regarding communication and energy-based planning.
showDate: false
---

The best way to reach me is through the **contact form** below or on **Mastodon**.

Because I manage my life and work using **energy-based planning**, I'm selective about my commitments and may take a few
days to respond. I value clear, direct, thoughtful communication.

## Where to Find Me

- **Mastodon:** [@RareBird15@allovertheplace.ca](https://allovertheplace.ca/@RareBird15): My main social home base for
  accessibility advocacy and tech talk.
- **Facebook:** [RareBirdLanie](https://www.facebook.com/RareBirdLanie/): Where I share visual updates and community
  posts.
- **Professional:** [LinkedIn](https://www.linkedin.com/in/laniecarmelo) or [GitHub](https://github.com/RareBird15).

## Communication Preferences

To respect my cognitive load and access needs:

1. **Text over Voice:** I don't do well with voice calls or "ephemeral" audio. Please send a text-based message so I can
   process it at my own pace.
2. **Explicit Context:** When reaching out, please be clear about your intent. "Query over memory" applies here too. I
   appreciate subject lines that tell me exactly what the message is about.
3. **Accessibility First:** If you're reaching out for feedback on a project, please include a link to your project or
   documentation so I can evaluate whether it fits my interaction model.

## Reporting Accessibility Issues

If you're reporting an accessibility issue on this site, these details help me fix it faster:

1. **Page URL:** The exact page where the issue happened.
2. **Device and browser:** For example, iPhone + Safari, Android + Chrome, Windows + Edge.
3. **Zoom or magnification level:** If relevant.
4. **What happened:** What was hard to use or confusing.
5. **What you expected instead:** What outcome would have made it work better.

## Send a Message

If the form below doesn't load or submit, or if Turnstile is blocking you, email me directly at
[lanie@lanie.work](mailto:lanie@lanie.work). That inbox is here as an accessibility fallback when the form isn't usable.

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>

<noscript>
  JavaScript is required for the form. If you're using a no-JS setup, email me directly at
  <a href="mailto:lanie@lanie.work">lanie@lanie.work</a>.
  This email option is the accessibility fallback for no-JS and form-failure cases.
</noscript>

<form action="/api/submit" method="POST">
  <div>
    <label for="name">Name:</label>
    <br>
    <input type="text" id="name" name="name" maxlength="100" autocomplete="name" required>
  </div>
  <br>
  <div>
    <label for="email">Email Address:</label>
    <br>
    <input type="email" id="email" name="email" maxlength="254" autocomplete="email" required>
  </div>
  <br>
  <div>
    <label for="subject">Subject:</label>
    <br>
    <input type="text" id="subject" name="subject" maxlength="150" required>
  </div>
  <div style="display:none;" aria-hidden="true">
    <label for="website_url">Leave this field blank</label>
    <input type="text" id="website_url" name="website_url" autocomplete="off" tabindex="-1">
  </div>
  <br>
  <div>
    <label for="message">Message:</label>
    <br>
    <textarea id="message" name="message" rows="5" maxlength="5000" required></textarea>
  </div>
  <br>

  <div
  class="cf-turnstile"
  data-sitekey="0x4AAAAAAC0wIh80xt8wpPtR"
  data-action="contact_form"
></div>
  <br>

<button type="submit">Submit Message</button>

</form>

_Thank you for respecting my time and energy._
