# AGENTS.md

## Scope

This repository is an asset-heavy Codex pet project, not a conventional application codebase. Treat the validated sprite atlas and its QA trail as the product.

## Source of truth

- The current release artifact is `final/spritesheet-extended.webp`.
- The current atlas format is v2: `1536 x 2288`, `8 x 11`, `192 x 208` cells, `spriteVersionNumber: 2`.
- Use `final/spritesheet-extended.json` and `final/validation-extended.json` to confirm layout details before documenting or changing anything.
- Treat `final/spritesheet.webp` and `final/spritesheet.png` as legacy 9-row outputs unless the user explicitly asks to work on backward compatibility.

## Working rules

- Make surgical changes only. Do not regenerate art, frames, prompts, or QA files unless the task explicitly requires it.
- Do not assume untracked generated outputs belong in the repo. Ask before staging things like `package/` or other new generated folders that were not explicitly requested.
- When editing docs, describe the tracked repository state, not a hypothetical future package layout.
- If you need install instructions, document the manual Codex pet folder format using the validated v2 atlas.

## Repository map

- `decoded/` intermediate generated row strips and look-direction assets
- `final/` final atlases plus atlas metadata and validation output
- `frames/` per-frame exports
- `prompts/` generation and retry prompts
- `qa/` review artifacts, contact sheets, previews, and direction checks
- `references/` canonical base art and layout guides
- `pet_request.json` pet specification
- `imagegen-jobs.json` generation job manifest

## Validation expectations

- Before calling a spritesheet "final", verify that the artifact path, dimensions, and row count match `final/spritesheet-extended.json` and `final/validation-extended.json`.
- Preserve the QA trail when making asset changes. A pet atlas change without refreshed QA is incomplete.
- For README or metadata updates, avoid touching QA JSON unless the content itself is wrong.

## Commit guidance

- This repo does not currently show a Jira issue prefix convention. If none is present in the branch name or recent commits, use a plain descriptive commit subject.
- Keep commit scope tight. Documentation-only changes should stay documentation-only unless the user asked for packaging or asset updates too.
