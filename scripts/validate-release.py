#!/usr/bin/env python3
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def fail(message: str):
    print(message, file=sys.stderr)
    raise SystemExit(1)


pet = load_json(ROOT / "pet.json")
atlas = load_json(ROOT / "final" / "spritesheet-extended.json")
validation = load_json(ROOT / "final" / "validation-extended.json")

expected_pet = {
    "id": "steve",
    "displayName": "Steve",
    "description": "A blocky pixel adventurer inspired by Minecraft Steve.",
    "spriteVersionNumber": 2,
    "spritesheetPath": "spritesheet.webp",
}

if pet != expected_pet:
    fail("pet.json does not match the expected Steve manifest")

if atlas.get("spritesheetPath") != "spritesheet-extended.webp":
    fail("final/spritesheet-extended.json does not point to spritesheet-extended.webp")

layout = atlas.get("spritesheetLayout", {})
if layout.get("columns") != 8 or layout.get("rows") != 11:
    fail("final/spritesheet-extended.json does not describe an 8x11 atlas")

if layout.get("cellWidth") != 192 or layout.get("cellHeight") != 208:
    fail("final/spritesheet-extended.json does not describe 192x208 cells")

if validation.get("ok") is not True:
    fail("final/validation-extended.json is not marked ok")

if validation.get("sprite_version_number") != 2:
    fail("final/validation-extended.json is not for sprite version 2")

if validation.get("width") != 1536 or validation.get("height") != 2288:
    fail("final/validation-extended.json does not describe a 1536x2288 spritesheet")

if validation.get("columns") != 8 or validation.get("rows") != 11:
    fail("final/validation-extended.json does not describe an 8x11 atlas")

for relative_path in [
    ROOT / "final" / "spritesheet-extended.webp",
    ROOT / "qa" / "contact-sheet-extended.png",
    ROOT / "qa" / "look-directions.png",
]:
    if not relative_path.exists():
        fail(f"Missing required file: {relative_path.relative_to(ROOT)}")

package_dir = ROOT / "package" / "steve"
package_pet = package_dir / "pet.json"
package_sprite = package_dir / "spritesheet.webp"

if not package_pet.exists() or not package_sprite.exists():
    fail("Package output is missing; run scripts/build-package.sh first")

if load_json(package_pet) != pet:
    fail("package/steve/pet.json does not match pet.json")

if package_sprite.read_bytes() != (ROOT / "final" / "spritesheet-extended.webp").read_bytes():
    fail("package/steve/spritesheet.webp does not match final/spritesheet-extended.webp")

print("Release validation passed.")
