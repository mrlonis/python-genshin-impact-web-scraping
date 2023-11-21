"""This module contains the logic for the scrape_web.py script."""
from urllib.request import urlopen

from bs4 import BeautifulSoup, ResultSet, Tag

from src.character_data import CharacterData


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
    character_data: CharacterData = CharacterData(
        sandsStatOne=None,
        sandsStatTwo=None,
        sandsStatThree=None,
        gobletStatOne=None,
        gobletStatTwo=None,
        gobletStatThree=None,
        circletStatOne=None,
        circletStatTwo=None,
        circletStatThree=None,
        substatOne=None,
        substatTwo=None,
        substatThree=None,
        weaponOneId=None,
        weaponTwoId=None,
        weaponThreeId=None,
        weaponFourId=None,
        weaponFiveId=None,
        artifactSetOneIdFirst=None,
        artifactSetOneIdSecond=None,
        artifactSetTwoIdFirst=None,
        artifactSetTwoIdSecond=None,
        artifactSetThreeIdFirst=None,
        artifactSetThreeIdSecond=None,
        artifactSetFourIdFirst=None,
        artifactSetFourIdSecond=None,
        artifactSetFiveIdFirst=None,
        artifactSetFiveIdSecond=None,
    )
    print(character_data)
    results: ResultSet[Tag] = soup.find_all("div", {"class": "character-build-weapon"})

    weapon_or_artifact = 0  # 0 = weapon, 1 = weapon, 2 = artifact
    for result in results:
        weapon_rank = result.find("div", {"class": "character-build-weapon-rank"})
        if weapon_rank:
            weapon_rank_text = int(weapon_rank.text)
            if weapon_rank_text == 1 and weapon_or_artifact == 0:
                print("WEAPON: INITIAL")
                print(weapon_rank_text)
                weapon_or_artifact += 1
            elif weapon_rank_text == 1 and weapon_or_artifact == 1:
                print("ARTIFACT: INITIAL")
                print(weapon_rank_text)
                weapon_or_artifact += 1
            elif weapon_or_artifact == 1:
                print("WEAPON: ELSE")
                print(weapon_rank_text)
            else:
                print("ARTIFACT: ELSE")
                print(weapon_rank_text)
        weapon_name: ResultSet[Tag] = result.find_all("div", {"class": "character-build-weapon-name"})
        if len(weapon_name) == 1:
            print(weapon_name[0].text)
        elif len(weapon_name) == 2:
            print(weapon_name[0].text)
            print(weapon_name[1].text)

    character_stats: ResultSet[Tag] = soup.find_all("div", {"class": "character-stats-item"})
    if len(character_stats) == 4:
        print(character_stats[0].text)
        print(character_stats[1].text)
        print(character_stats[2].text)
        print(character_stats[3].text)
    return html


scrape_web(url="https://genshin.gg/characters/ayaka/", make_server_call=False)
build_characters_csv()
