#!/usr/bin/env python3
"""Validate taxonomy consistency for site post content.

Rules:
- Exactly one category per post.
- 3 to 6 tags per post.
- Tags must be lowercase kebab-case.
- Tags must not duplicate the category (case-insensitive).
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
POST_DIRS = ["advocacy", "technology", "gaming", "education"]
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _front_matter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def _parse_list(front_matter: str, key: str) -> list[str]:
    lines = front_matter.splitlines()
    values: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(rf"^{re.escape(key)}\s*:", line):
            _, _, raw = line.partition(":")
            raw = raw.strip()

            # Inline list: tags: ["a", "b"]
            if raw.startswith("[") and raw.endswith("]"):
                body = raw[1:-1].strip()
                if not body:
                    return []
                parts = [p.strip().strip("\"'") for p in body.split(",")]
                return [p for p in parts if p]

            # Block list:
            i += 1
            while i < len(lines):
                item = lines[i]
                if not item.startswith("  - "):
                    break
                values.append(item[4:].strip().strip("\"'"))
                i += 1
            return values
        i += 1
    return values


def _post_files() -> list[Path]:
    files: list[Path] = []
    for section in POST_DIRS:
        section_dir = CONTENT / section
        if not section_dir.exists():
            continue
        for path in sorted(section_dir.glob("*.md")):
            if path.name == "_index.md":
                continue
            files.append(path)
    return files


def main() -> int:
    errors: list[str] = []

    for file_path in _post_files():
        content = file_path.read_text(encoding="utf-8")
        fm = _front_matter(content)
        if fm is None:
            errors.append(f"{file_path}: missing valid YAML front matter")
            continue

        categories = _parse_list(fm, "categories")
        tags = _parse_list(fm, "tags")

        rel = file_path.relative_to(ROOT)

        if len(categories) != 1:
            errors.append(
                f"{rel}: expected exactly 1 category, found {len(categories)}"
            )

        if not (3 <= len(tags) <= 6):
            errors.append(f"{rel}: expected 3-6 tags, found {len(tags)}")

        if len(set(tags)) != len(tags):
            errors.append(f"{rel}: has duplicate tags")

        for tag in tags:
            if not TAG_RE.match(tag):
                errors.append(
                    f"{rel}: invalid tag format '{tag}' (use lowercase kebab-case)"
                )

        if categories:
            cat_tag = categories[0].strip().lower().replace(" ", "-")
            if cat_tag in {t.strip().lower() for t in tags}:
                errors.append(
                    f"{rel}: redundant tag '{cat_tag}' duplicates category '{categories[0]}'"
                )

    if errors:
        print("Taxonomy checks failed:\n")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Taxonomy checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
