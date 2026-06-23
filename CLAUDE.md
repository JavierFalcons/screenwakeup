# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ScreenWakeUp is a static HTML website — no build system, no package manager, no dependencies. The entire application lives in a handful of plain HTML files.

## Architecture

**Single-file app pattern:** `index.html` is a 2000+ line self-contained file combining:
- Inline `<style>` block with CSS custom properties (design tokens) for dark/light theming
- Inline `<script>` block at the bottom with all application logic

**Localization:** All UI strings are in a `const LANG = { en, es, pt, fr, de, ja, ru }` object (~line 1169). `setLang(l)` applies translations by updating DOM element text. Language-specific subdirectories (`/es/`, `/fr/`, etc.) contain separate `index.html` copies for SEO, each with its own hreflang metadata — they are **not** auto-generated from the English version.

**Core features and where they live (all in `index.html`):**
- **Wake Lock** (`activate` / `deactivate`, ~line 1929): uses `navigator.wakeLock.request('screen')` with a hidden `<video>` fallback (`mkSilentVideo`) for browsers without WakeLock API
- **Anti-idle** (`startAntiIdle` / `stopAntiIdle`, ~line 2049): `setInterval` that simulates mouse movement via pointer events and dispatches `F15` keydown events
- **Pomodoro** (`togglePomodoro` / `tickPom`, ~line 2080): 25-min work / 5-min break timer
- **Fullscreen clock** (`enterFullscreen` / `exitFullscreen`, ~line 2127): uses Fullscreen API, updates a `<div>` with current time
- **Custom timer** (`applyCustomTimer`, ~line 2001): sets `selectedMin` and `durationMs`, drives the progress bar
- **Audio chime** (`playChime`, ~line 2029): creates an `AudioContext` oscillator in-browser

**Theming:** `data-theme="dark|light"` attribute on `<html>`, persisted to `localStorage` under key `ka-theme`. CSS variables in `:root` and `[data-theme="light"]` selectors drive all colors.

**Analytics:** Google Analytics 4 (`G-WKJ8R82KQZ`) is active. Google AdSense is commented out pending publisher ID.

**Feedback form:** Posts to a Formspree endpoint (look for the `fetch` in the `feedbackForm` submit handler).

## Editing Translations

To add or change a string: update **both** the `LANG` object in `index.html` and the corresponding language subdirectory's `index.html`. The subdirectory files are not auto-generated — they must be edited manually to stay in sync.

## Deployment

Static files — deploy by uploading the directory contents to any static host (Netlify, Vercel, GitHub Pages, etc.). No build step required.
