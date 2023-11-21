"""This module contains the logic for the scrape_web.py script."""
from urllib.request import urlopen

from bs4 import BeautifulSoup
from rich import print as pretty_print

from src.character_data import CharacterData
from src.processors import get_element, get_rarity, get_stats, get_weapon_type, get_weapons_and_artifacts


def build_characters_csv():
    """Build the characters.csv file."""
    with open("output/characters.csv", "w", encoding="utf-8") as csv_file:
        # pylint: disable=line-too-long
        csv_file.write(
            "name,imageUrl,rarity,elementId,weaponType,sandsStatOne,sandsStatTwo,sandsStatThree,gobletStatOne,gobletStatTwo,gobletStatThree,circletStatOne,circletStatTwo,circletStatThree,substatOne,substatTwo,substatThree,weaponOneId,weaponTwoId,weaponThreeId,weaponFourId,weaponFiveId,artifactSetOneIdFirst,artifactSetOneIdSecond,artifactSetTwoIdFirst,artifactSetTwoIdSecond,artifactSetThreeIdFirst,artifactSetThreeIdSecond,artifactSetFourIdFirst,artifactSetFourIdSecond,artifactSetFiveIdFirst,artifactSetFiveIdSecond\n"  # noqa: E501
        )


def scrape_web(url: str, make_server_call=False) -> str:
    """Scrape the web for data."""
    if make_server_call:
        with urlopen(url) as page:  # nosec
            html = page.read().decode("utf-8")
    else:
        with open("sample_data/ayaka.html", "r", encoding="utf-8") as file:
            html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    character_data: CharacterData = CharacterData(name="", rarity=0, element_id="", weapon_type="")

    get_rarity(soup, character_data)
    get_element(soup, character_data)
    get_weapon_type(soup, character_data)
    get_stats(soup, character_data)
    get_weapons_and_artifacts(soup, character_data)

    pretty_print(character_data)
    return html


scrape_web(url="https://genshin.gg/characters/ayaka/", make_server_call=False)
build_characters_csv()
