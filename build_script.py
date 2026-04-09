import json
from pathlib import Path

fullname_dict = {
    'tb': 'Trouble Brewing',
    'experimental': 'Experimental Edition',
    'bmr': 'Bad Moon Rising',
    'snv': 'Sects & Violets',
    'taf': 'Traveller & Fabled',
    'fabled': 'Fabled',
    'loric': 'Loric',
    'carousel': 'Carousel',
}

if __name__ == "__main__":
    base_url = "https://release.botc.app/resources/characters"
    with open("roles.json", "r", encoding="utf-8") as f:
        data = json.load(f)


    editions = set(role.get("edition") for role in data if role.get("edition"))

    
    for edition in editions:
        metadata = {
            "id": "_meta",
            "name": fullname_dict[edition],
            "author": "Official",
        }
        edition_characters = [role for role in data if role.get("edition") == edition]
        for character in edition_characters:
            team = character['team']
            if team in ['townsfolk', 'outsider']:
                alignment = '_g'
            elif team in ['minion', 'demon']:
                alignment = '_e'
            elif team in ['traveller']:
                alignment = ''
            else:
                # "traveller",
                # "fabled",
                # "loric"
                continue
                # raise NotImplementedError(team)

            url = f'{base_url}/{edition}/{character["id"]}{alignment}.webp'
            character['image'] = [url]
        edition_characters.insert(0, metadata)
        with open(f"scripts/{fullname_dict[edition]}.json", "w", encoding="utf-8") as f:
            json.dump(edition_characters, f, indent=4)
        print(f"Done {fullname_dict[edition]}")