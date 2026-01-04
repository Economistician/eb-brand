from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "tokens" / "colors.json"
DIST = ROOT / "dist"


def flatten(prefix: str, obj: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    for k, v in obj.items():
        key = f"{prefix}-{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(key, v))
        else:
            out[key] = str(v)
    return out


def write_tokens_css(data: dict) -> None:
    lines = [":root {"]
    for mode in ("light", "dark"):
        flat = flatten(f"eb-{mode}", data[mode])
        for k, v in flat.items():
            lines.append(f"  --{k}: {v};")
    lines.append("}")

    (DIST / "tokens.css").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_mkdocs_material_css() -> None:
    css = """\
/* Auto-generated from eb-brand tokens */

/* ---------------------------
   Light mode (default)
--------------------------- */
:root {
  /* Header / primary */
  --md-primary-bg-color: var(--eb-light-background-header);
  --md-primary-bg-color--light: var(--eb-light-background-header);
  --md-primary-bg-color--dark: var(--eb-light-background-header);
  --md-primary-fg-color: var(--eb-light-text-on-brand);

  /* Accent */
  --md-accent-fg-color: var(--eb-light-brand-accent);

  /* Page */
  --md-default-bg-color: var(--eb-light-background-canvas);
  --md-default-fg-color: var(--eb-light-text-primary);
}

/* ---------------------------
   Dark mode (slate)
--------------------------- */
[data-md-color-scheme="slate"] {
  --md-primary-bg-color: var(--eb-dark-background-header);
  --md-primary-bg-color--light: var(--eb-dark-background-header);
  --md-primary-bg-color--dark: var(--eb-dark-background-header);
  --md-primary-fg-color: var(--eb-dark-text-on-brand);

  --md-accent-fg-color: var(--eb-dark-brand-accent);

  --md-default-bg-color: var(--eb-dark-background-canvas);
  --md-default-fg-color: var(--eb-dark-text-primary);
}
"""
    (DIST / "mkdocs-material.css").write_text(css, encoding="utf-8")


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)

    data = json.loads(TOKENS.read_text(encoding="utf-8"))
    write_tokens_css(data)
    write_mkdocs_material_css()

    print("Generated dist/tokens.css and dist/mkdocs-material.css")


if __name__ == "__main__":
    main()
