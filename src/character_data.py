"""This module contains the character data model information."""
from pydantic import BaseModel


class CharacterData(BaseModel):
    """Character data model."""

    name: str
    image_url: str | None = None
    rarity: int = 0
    element_id: str = ""
    weapon_type: str = ""

    sands_stat_one: str | None = None
    sands_stat_two: str | None = None
    sands_stat_three: str | None = None
    goblet_stat_one: str | None = None
    goblet_stat_two: str | None = None
    goblet_stat_three: str | None = None
    circlet_stat_one: str | None = None
    circlet_stat_two: str | None = None
    circlet_stat_three: str | None = None
    substat_one: str | None = None
    substat_two: str | None = None
    substat_three: str | None = None
    weapon_one_id: str | None = None
    weapon_two_id: str | None = None
    weapon_three_id: str | None = None
    weapon_four_id: str | None = None
    weapon_five_id: str | None = None
    artifact_set_one_id_first: str | None = None
    artifact_set_one_id_second: str | None = None
    artifact_set_two_id_first: str | None = None
    artifact_set_two_id_second: str | None = None
    artifact_set_three_id_first: str | None = None
    artifact_set_three_id_second: str | None = None
    artifact_set_four_id_first: str | None = None
    artifact_set_four_id_second: str | None = None
    artifact_set_five_id_first: str | None = None
    artifact_set_five_id_second: str | None = None
