# Blood on the Clocktower

A small repository for generating edition-specific role scripts from a single master role dataset.

## Repository structure

- `roles.json`
  - Canonical role dataset.
  - Includes metadata and all character definitions across editions.
- `build_script.py`
  - Reads `roles.json` and writes edition JSON files under `scripts/`.
  - Builds each edition's image URLs and injects an `_meta` entry.
- `scripts/`
  - Contains edition-specific folders and generated JSON files.
  - Example editions: `Trouble Brewing`, `Bad Moon Rising`, `Carousel`, `Sects & Violets`, `Experimental Edition`, `Fabled`, `Loric`.

## How it works

1. `build_script.py` loads `roles.json`.
2. It groups roles by `edition`.
3. It prefixes each edition output with metadata:
   - `id: "_meta"`
   - `name`
   - `author`
4. It creates an `image` URL for each role using the edition and role ID.
5. Each generated file is written to `scripts/<Edition Name>/<Edition Name>.json`.

## Running the generator

From the repository root:

```powershell
python .\build_script.py
```

This regenerates any missing edition files under `scripts/`.

## Data format

Each edition JSON file is an array. The first element is metadata, followed by role objects with fields like:

- `id`
- `name`
- `edition`
- `team`
- `ability`
- `flavor`
- `reminders`
- `firstNightReminder`
- `image`

## Helpful links

- Token PDF generator: [https://botc-tokencrafter.miketilly.com/](https://botc-tokencrafter.miketilly.com/)
  - Add 10% margin
  - Scale icon to 120%
- Resources: [https://release.botc.app/resources/](https://release.botc.app/resources/)
- Official wiki: [https://wiki.bloodontheclocktower.com/Main_Page](https://wiki.bloodontheclocktower.com/Main_Page)

<img src="https://release.botc.app/resources/community/ccc-parchment.png" width="300" />
