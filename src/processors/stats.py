"""This module contains the logic for the get_stats processor."""
from bs4 import BeautifulSoup, ResultSet, Tag

from src.character_data import CharacterData


def _process_sands_stats(sands_stats_raw: str, character_data: CharacterData):
    """Process the sands stats."""
    split_data = sands_stats_raw.split("/")
    print(split_data)
    i = 0
    while i < len(split_data):
        if i == 0:
            character_data.sands_stat_one = split_data[i].strip()
        elif i == 1:
            character_data.sands_stat_two = split_data[i].strip()
        elif i == 2:
            character_data.sands_stat_three = split_data[i].strip()
        i += 1


def _goblet_stats(goblet_stats_raw: str, character_data: CharacterData):
    """Process the goblet stats."""
    split_data = goblet_stats_raw.split("/")
    print(split_data)
    i = 0
    while i < len(split_data):
        if i == 0:
            character_data.goblet_stat_one = split_data[i].strip()
        elif i == 1:
            character_data.goblet_stat_two = split_data[i].strip()
        elif i == 2:
            character_data.goblet_stat_three = split_data[i].strip()
        i += 1


def _circlet_stats(circlet_stats_raw: str, character_data: CharacterData):
    """Process the circlet stats."""
    split_data = circlet_stats_raw.split("/")
    print(split_data)
    i = 0
    while i < len(split_data):
        if i == 0:
            character_data.circlet_stat_one = split_data[i].strip()
        elif i == 1:
            character_data.circlet_stat_two = split_data[i].strip()
        elif i == 2:
            character_data.circlet_stat_three = split_data[i].strip()
        i += 1


def _substats(substats_raw: str, character_data: CharacterData):
    """Process the substats."""
    split_data = substats_raw.split(">")
    print(split_data)
    i = 0
    while i < len(split_data):
        if i == 0:
            character_data.substat_one = split_data[i].strip()
        elif i == 1:
            character_data.substat_two = split_data[i].strip()
        elif i == 2:
            character_data.substat_three = split_data[i].strip()
        i += 1


def get_stats(soup: BeautifulSoup, character_data: CharacterData):
    """Get the stats of the character."""
    character_stats: ResultSet[Tag] = soup.find_all("div", {"class": "character-stats-item"})
    sands_stats_raw: str | None = None
    goblet_stats_raw: str | None = None
    circlet_stats_raw: str | None = None
    substats_raw: str | None = None
    if len(character_stats) == 4:
        sands_stats_raw = character_stats[0].text.split("Sands: ")[1]
        print(sands_stats_raw)
        goblet_stats_raw = character_stats[1].text.split("Goblet: ")[1]
        print(goblet_stats_raw)
        circlet_stats_raw = character_stats[2].text.split("Circlet: ")[1]
        print(circlet_stats_raw)
        substats_raw = character_stats[3].text.split("Substats: ")[1]
        print(substats_raw)
    else:
        print("ERROR: Character stats not found.")
        raise ValueError("Character stats not found.")

    _process_sands_stats(sands_stats_raw, character_data)
    _goblet_stats(goblet_stats_raw, character_data)
    _circlet_stats(circlet_stats_raw, character_data)
    _substats(substats_raw, character_data)
