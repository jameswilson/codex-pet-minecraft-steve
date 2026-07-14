#!/bin/sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
PET_ID=steve
PACKAGE_DIR="$ROOT_DIR/package/$PET_ID"
DIST_DIR="$ROOT_DIR/dist"

mkdir -p "$PACKAGE_DIR" "$DIST_DIR"

cp "$ROOT_DIR/pet.json" "$PACKAGE_DIR/pet.json"
cp "$ROOT_DIR/final/spritesheet-extended.webp" "$PACKAGE_DIR/spritesheet.webp"

(
  cd "$ROOT_DIR/package"
  zip -qr "$DIST_DIR/$PET_ID-codex-pet.zip" "$PET_ID"
)

printf 'Built package in %s\n' "$PACKAGE_DIR"
printf 'Built zip in %s\n' "$DIST_DIR/$PET_ID-codex-pet.zip"
