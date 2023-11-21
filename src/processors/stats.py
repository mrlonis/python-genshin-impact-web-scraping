"""This module contains the logic for the get_stats processor."""
from bs4 import BeautifulSoup, ResultSet, Tag

from src.character_data import CharacterData


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
