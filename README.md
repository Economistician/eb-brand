# Electric Barometer · Brand (`eb-brand`)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Canonical brand and visual identity assets for the Electric Barometer ecosystem.

---

## Overview

`eb-brand` contains the canonical visual identity assets for the Electric Barometer ecosystem. It serves as the single source of truth for logos, icons, favicons, color tokens, and related styling primitives used across repositories, documentation sites, and public-facing materials.

This repository is deliberately scoped to **static assets only**. It does not include executable code, UI components, or application-specific styling logic. Instead, it provides stable, reusable brand artifacts that downstream systems and repositories may reference, synchronize, or embed as needed.

By centralizing brand assets in a dedicated repository, Electric Barometer ensures visual consistency across its ecosystem while avoiding duplication, drift, or ad hoc reinterpretation of core identity elements.

---

## Role in the Electric Barometer Ecosystem

`eb-brand` defines the shared visual foundation used throughout the Electric Barometer ecosystem. Its assets are consumed by documentation sites, repositories, websites, and presentation materials to ensure consistent representation of the Electric Barometer identity.

This repository does not dictate layout, typography systems, UI composition, or application-specific styling behavior. Those concerns are handled by downstream consumers that incorporate these assets into their own interfaces or surfaces.

By separating brand identity from implementation concerns, `eb-brand` enables visual consistency without imposing coupling between repositories or technologies.

---

## Asset Conventions

Brand assets in this repository follow a small set of conventions to ensure predictable reuse:

- **SVG-first** — Vector formats are preferred wherever possible.
- **Transparent backgrounds** — Assets are designed to render correctly on light and dark surfaces.
- **Square variants** — Logos intended for icons or favicons are provided in square aspect ratios.
- **Explicit naming** — Filenames are descriptive and avoid ambiguous abbreviations.

Assets should not be modified locally in downstream repositories. Updates should be made here and propagated outward to ensure consistency.

---

## Usage Guidelines

Downstream repositories may consume assets from `eb-brand` in one of the following ways:

- Direct reference (e.g., documentation builds or static sites)
- Periodic synchronization via automation or scripts
- Manual import for presentation or publication purposes

Consumers should treat assets in this repository as authoritative. Local overrides, recoloring, or reshaping of logos and marks should be avoided unless explicitly required by context.

If alternate formats or variants are needed, they should be added here rather than recreated elsewhere.

---

## License

BSD 3-Clause License. © 2025 Kyle Corrie.
