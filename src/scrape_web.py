"""This module contains the logic for the scrape_web.py script."""
import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
from rich import print as pretty_print

from .character_data import CharacterData
from .characters import CharacterInput
from .processors import get_element, get_rarity, get_stats, get_weapon_type, get_weapons_and_artifacts


def build_characters_csv():
    """Build the characters.csv file."""
    with open("output/characters.csv", "w", encoding="utf-8") as csv_file:
        # pylint: disable=line-too-long
        csv_file.write(
            "name,imageUrl,rarity,elementId,weaponType,sandsStatOne,sandsStatTwo,sandsStatThree,gobletStatOne,gobletStatTwo,gobletStatThree,circletStatOne,circletStatTwo,circletStatThree,substatOne,substatTwo,substatThree,weaponOneId,weaponTwoId,weaponThreeId,weaponFourId,weaponFiveId,artifactSetOneIdFirst,artifactSetOneIdSecond,artifactSetTwoIdFirst,artifactSetTwoIdSecond,artifactSetThreeIdFirst,artifactSetThreeIdSecond,artifactSetFourIdFirst,artifactSetFourIdSecond,artifactSetFiveIdFirst,artifactSetFiveIdSecond\n"  # noqa: E501
        )


def _build_url(character_input: CharacterInput):
    """Build the url."""
    url_path = character_input.url_name if character_input.url_name else character_input.name.lower()
    return "https://genshin.gg/characters/" + url_path + "/"


def _build_sample_data_path(character_input: CharacterInput):
    """Build the sample data path."""
    url_path = character_input.url_name if character_input.url_name else character_input.name
    return "sample_data/" + url_path + ".html"


def scrape_web(character_input: CharacterInput, make_server_call=False) -> str:
    """Scrape the web for data."""
    if make_server_call:
        with urlopen(_build_url(character_input)) as page:  # nosec
            html = page.read().decode("utf-8")
    else:
        sample_data_path = _build_sample_data_path(character_input)
        if os.path.exists(sample_data_path):
            with open(sample_data_path, "r", encoding="utf-8") as file:
                html = file.read()
        else:
            with urlopen(_build_url(character_input)) as page:  # nosec
                html = page.read().decode("utf-8")
                with open(sample_data_path, "w", encoding="utf-8") as sample_data_file:
                    sample_data_file.write(html)

    soup = BeautifulSoup(html, "html.parser")
    character_data: CharacterData = CharacterData(name=character_input.name)

    get_rarity(soup, character_data)
    get_element(soup, character_data)
    get_weapon_type(soup, character_data)
    get_stats(soup, character_data)
    get_weapons_and_artifacts(soup, character_data)

    pretty_print(character_data)
    return html
