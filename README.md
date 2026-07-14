# Minecraft Steve Codex Pet

Unofficial fan-made Codex pet assets based on Minecraft Steve.

![Steve contact sheet](qa/contact-sheet-extended.png)

This repository contains the working files used to generate, review, and validate a v2 Codex pet atlas for Steve: source prompts, reference material, decoded row strips, extracted frames, QA artifacts, and final spritesheets.

## Canonical asset

The primary release artifact in this repository is:

- `final/spritesheet-extended.webp`
- `pet.json`

That file is the validated v2 atlas:

- `1536 x 2288`
- `8` columns by `11` rows
- `192 x 208` per cell
- standard action rows plus `16` look directions

Supporting metadata for the v2 atlas lives in:

- `final/spritesheet-extended.json`
- `final/validation-extended.json`

The older `final/spritesheet.webp` and `final/spritesheet.png` are legacy 9-row outputs and should not be treated as the install target for this repo's current version.

## Animation layout

Rows `0` through `8` are the standard Codex pet actions:

1. `idle`
2. `running-right`
3. `running-left`
4. `waving`
5. `jumping`
6. `failed`
7. `waiting`
8. `running`
9. `review`

Rows `9` and `10` provide clockwise look directions:

- row `9`: `0` through `157.5` degrees
- row `10`: `180` through `337.5` degrees

## Manual install

Codex pets are installed as:

```text
~/.codex/pets/<pet-id>/
├── pet.json
└── spritesheet.webp
```

To install this pet manually:

1. Create `~/.codex/pets/steve/`.
2. Copy `final/spritesheet-extended.webp` to `~/.codex/pets/steve/spritesheet.webp`.
3. Copy `pet.json` to `~/.codex/pets/steve/pet.json`.

## Build package

For a ready-to-upload install bundle, run:

```bash
./scripts/build-package.sh
```

That script builds:

- `package/steve/`
- `dist/steve-codex-pet.zip`

The generated package output is intentionally ignored by git because it is reproducible from tracked source files.

## Repository layout

- `decoded/` generated strip images for each row and look-direction pass
- `final/` validated final atlases and atlas metadata
- `frames/` extracted per-frame PNGs used for review and packaging work
- `prompts/` base, row, retry, and look-repair prompts used during generation
- `qa/` contact sheets, previews, direction checks, and review JSON
- `references/` canonical identity art and layout guides
- `pet_request.json` high-level pet specification
- `imagegen-jobs.json` generation job log and dependency graph

## QA and review artifacts

The repo keeps the evidence used to approve the final atlas, including:

- `qa/contact-sheet-extended.png`
- `qa/look-directions.png`
- `qa/look-continuity.json`
- `qa/direction-blind-validation.json`
- `qa/review.json`

If you change the atlas, update the relevant QA artifacts in the same change so the repo stays auditable.

Do not ignore the whole `qa/` directory. Most of it is part of the review trail. The only ignored QA file is `qa/run-summary.json`, which is machine-local and includes absolute paths.

## GitHub automation

This repo uses GitHub Actions for packaging policy rather than committing install bundles:

- on pull requests and pushes to `main`, CI builds the install package and validates that the manifest, atlas metadata, and packaged sprite stay in sync
- on published GitHub releases, CI uploads `dist/steve-codex-pet.zip` as a release asset

For a public repo like this, that is the best balance: keep the canonical art and QA in git, keep reproducible package output out of git, and publish the zip from automation instead of maintaining it by hand.

## Related project

Another Steve-adjacent Codex pet repo is [`koka99cab/pet-steve`](https://github.com/koka99cab/pet-steve).

## Fan project note

This is an unofficial fan work inspired by Minecraft Steve. Minecraft, Steve, and related trademarks and character rights belong to Mojang Studios and Microsoft.
