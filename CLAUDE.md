# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ScreenWakeUp is a static HTML website. The core app is one self-contained file; there is no package manager, no bundler, and no runtime dependencies. The only build tooling is a Python script that generates the translated SEO landing pages and the sitemap (see Commands).

## Commands

There is no test/lint suite. The single build step regenerates the non-English SEO landing pages and rewrites `sitemap.xml`:

```bash
python3 scripts/generate_landing_pages.py   # run from repo root
```

- Source of truth for landing-page copy is `scripts/landing_content.py` (`CONTENT[slug][lang]` dicts).
- The script writes `<lang>/<slug>/index.html` for the 6 non-English languages, injects an idempotent hreflang block into the hand-written English landing pages, and rebuilds `sitemap.xml`.
- It covers **only** the 4 landing slugs: `prevent-teams-away`, `caffeine-alternative`, `keep-screen-awake-iphone`, `prevent-zoom-idle`. It does **not** touch the main app pages (`index.html` or `<lang>/index.html`).

To preview locally, serve the directory (e.g. `python3 -m http.server`) and open `index.html` — nothing to compile.

## Architecture

**Single-file app pattern:** `index.html` (~2,230 lines) combines everything:
- Inline `<style>` block with CSS custom properties (design tokens) for dark/light theming
- Inline `<script>` block at the bottom with all application logic

Line numbers below are approximate — the file changes often, so grep for the function name rather than trusting the number.

**Localization:** All UI strings live in a `const LANG = { en, es, pt, fr, de, ja, ru }` object (~line 1036). `setLang(l)` (~line 1513) applies translations by updating DOM element text. The `<lang>/index.html` app copies (e.g. `/es/index.html`) are separate hand-maintained files for SEO with their own hreflang metadata — **not** auto-generated (the landing-page script does not touch them).

**Core features and where they live (all in `index.html`):**
- **Wake Lock** (`activate` / `deactivate`, ~line 1837): `navigator.wakeLock.request('screen')` with a hidden `<video>` fallback (`mkSilentVideo`, ~line 1751) for browsers without the WakeLock API; re-acquires the lock on `visibilitychange`.
- **Picture-in-Picture mini-window** (`togglePiP` ~line 1953, `pipWarmup` ~line 1920): a canvas-driven `<video>` streamed into an always-on-top PiP clock. Safari-critical detail: the PiP video must be created and warmed up **before** the click (on hover/focus), because calling `play()` inside the click handler consumes the user-activation Safari needs to open the window. Do not move video creation back into `togglePiP`.
- **Pomodoro** (`togglePomodoro` ~line 2091 / `tickPom` ~line 2114): 25-min work / 5-min break timer.
- **Fullscreen clock** (`enterFullscreen` / `exitFullscreen`, ~line 2139): Fullscreen API, updates a `<div>` with the current time.
- **Custom timer** (`applyCustomTimer`, ~line 2036): sets `selectedMin` / `durationMs`, drives the progress bar; `0` means run indefinitely.
- **Audio chime** (`playChime`, ~line 2065): in-browser `AudioContext` oscillator, played at timer expiry.

Honesty positioning: the site deliberately does **not** simulate mouse/keyboard input (browsers block it, and the copy says so). Do not add fake-activity / jiggler code — it contradicts the product's stated stance in the FAQ and translations.

**Theming:** `data-theme="dark|light"` attribute on `<html>`, persisted to `localStorage` key `ka-theme`. CSS variables in `:root` and `[data-theme="light"]` drive all colors.

**Analytics:** Google Analytics 4 (`G-WKJ8R82KQZ`) is active; events go through a `track()` helper. There is no ad code anywhere in the site and there must not be: the copy promises "no ads" in several places (index.html and the donation strings), so do not add ad scaffolding.

**Feedback form:** Posts to Formspree (`https://formspree.io/f/xlgqdzqj`) via `fetch` in the `feedbackForm` submit handler (present on the main page and es/pt/fr/de — not ja/ru). Success is shown only on HTTP 200; failures show the localized `feedbackErr` message.

## Page inventory

- `index.html` — the app (English / x-default).
- `<lang>/index.html` — full app translations (es, pt, fr, de, ja, ru), hand-maintained.
- `<slug>/index.html` and `<lang>/<slug>/index.html` — SEO landing pages for the 4 slugs; non-English ones are generated (see Commands).
- `about/`, `privacy/`, `terms/` — static content pages.

## Editing Translations

To add or change an app UI string: update **both** the `LANG` object in the root `index.html` **and** the matching `<lang>/index.html`. These are not auto-generated and must be kept in sync manually. To change landing-page copy, edit `scripts/landing_content.py` and re-run the generator.

## Deployment

Static files — deploy by uploading the directory contents to any static host (Netlify, Vercel, GitHub Pages, etc.). Run the landing-page generator first if landing copy or the page set changed.

Production is Cloudflare Pages deploying the repo root on every push to `main`, so tooling files (`CLAUDE.md`, `scripts/`, `.gitignore`) are served publicly too. `_headers` marks `/*.md` and `/scripts/*` as `noindex` and de-indexes the `*.pages.dev` mirror; keep those rules if the site is ever moved into a dedicated output folder (the proper fix, which needs the Pages build-output setting changed).
