# Repository Guidelines

## Project Structure & Module Organization

This repository contains a Spanish-language poster generator for board-game sessions.

- `index.html` contains the session-poster editor, canvas rendering, and project persistence.
- `tipografico.html` contains Cartel a caja, its SVG renderer, effects, exports, and font management.
- `editors.css` styles the shared navigation; `fonts/tusker/` contains bundled fonts.
- `README.md` explains local use; `docs/cartel-a-caja.txt` contains the typography editor's detailed help.
- There is no test directory. Uploaded assets stay in the browser; Google Fonts requires connectivity.

Keep related changes within the existing HTML, style, and script sections. Avoid introducing a framework or build pipeline for small changes.

Preserve each editor's storage keys and JSON format. Explicit session-to-typography transfers use `sessionStorage`; ordinary navigation must retain independent drafts.

## Build, Test, and Development Commands

- Open `index.html` in a modern browser for direct use.
- Run `python3 -m http.server 8000` from the repository root, then visit `http://localhost:8000` for local HTTP development. Python 3 is required only for this option.
- Run `git diff --check` before committing to catch whitespace errors.

There is no dependency installation, compilation step, package manifest, or automated test command.

## Coding Style & Naming Conventions

Follow the surrounding vanilla HTML, CSS, and JavaScript style. Use two-space indentation for new CSS and JavaScript blocks, semicolons, and single-quoted JavaScript strings where practical. Prefer `const`; use `let` for reassignment.

Use camelCase for functions and variables, such as `buildFilename` and `portadaImage`, and hyphenated CSS classes such as `canvas-wrap`. Preserve existing Spanish control IDs and Spanish interface text. Keep IDs synchronized with DOM lookups and the `inputs` array when adding persisted controls. No formatter or linter is configured.

## Testing Guidelines

Validation is manual; no testing framework or coverage threshold is configured. For behavior changes, check:

- Live preview updates, all banner sizes, long text, and text scaling.
- Solid, gradient, and uploaded-image backgrounds, plus cover uploads.
- PNG and WebP downloads, including filenames and image dimensions.
- JSON save/load, persistence after reload, new-project creation, and reset.
- Narrow-screen layout and browser-console errors.
- Navigation, event transfer, bundled fonts, and typography PNG/SVG exports.

## Commit & Pull Request Guidelines

History uses short subjects such as `Update index.html`; no formal commit convention is established. Write concise, imperative subjects describing the behavior changed, for example `Fix title wrapping in wide posters`.

Pull requests should explain the change, list manual checks performed, link relevant issues, and include preview or exported-poster screenshots for visual changes.
