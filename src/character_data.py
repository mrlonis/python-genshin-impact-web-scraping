"""This module contains the character data model information."""
from pydantic import BaseModel


class CharacterData(BaseModel):
    """Character data model."""

    sandsStatOne: str | None
    sandsStatTwo: str | None
    sandsStatThree: str | None
    gobletStatOne: str | None
    gobletStatTwo: str | None
    gobletStatThree: str | None
    circletStatOne: str | None
    circletStatTwo: str | None
    circletStatThree: str | None
    substatOne: str | None
    substatTwo: str | None
    substatThree: str | None
    weaponOneId: str | None
    weaponTwoId: str | None
    weaponThreeId: str | None
    weaponFourId: str | None
    weaponFiveId: str | None
    artifactSetOneIdFirst: str | None
    artifactSetOneIdSecond: str | None
    artifactSetTwoIdFirst: str | None
    artifactSetTwoIdSecond: str | None
    artifactSetThreeIdFirst: str | None
    artifactSetThreeIdSecond: str | None
    artifactSetFourIdFirst: str | None
    artifactSetFourIdSecond: str | None
    artifactSetFiveIdFirst: str | None
    artifactSetFiveIdSecond: str | None
