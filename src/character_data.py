"""This module contains the character data model information."""
from pydantic import BaseModel


def _convert_field_to_csv(field: str | int | None) -> str:
    """Convert the field to a CSV string."""
    if field is None:
        return ""
    if isinstance(field, int):
        return str(field)
    if "," in field:
        return f'"{field}"'
    return field


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

    def to_csv(self):
        """Convert the character data to a CSV string."""
        return (
            f"{_convert_field_to_csv(self.name)},"
            + f"{_convert_field_to_csv(self.image_url)},"
            + f"{_convert_field_to_csv(self.rarity)},"
            + f"{_convert_field_to_csv(self.element_id)},"
            + f"{_convert_field_to_csv(self.weapon_type)},"
            + f"{_convert_field_to_csv(self.sands_stat_one)},"
            + f"{_convert_field_to_csv(self.sands_stat_two)},"
            + f"{_convert_field_to_csv(self.sands_stat_three)},"
            + f"{_convert_field_to_csv(self.goblet_stat_one)},"
            + f"{_convert_field_to_csv(self.goblet_stat_two)},"
            + f"{_convert_field_to_csv(self.goblet_stat_three)},"
            + f"{_convert_field_to_csv(self.circlet_stat_one)},"
            + f"{_convert_field_to_csv(self.circlet_stat_two)},"
            + f"{_convert_field_to_csv(self.circlet_stat_three)},"
            + f"{_convert_field_to_csv(self.substat_one)},"
            + f"{_convert_field_to_csv(self.substat_two)},"
            + f"{_convert_field_to_csv(self.substat_three)},"
            + f"{_convert_field_to_csv(self.weapon_one_id)},"
            + f"{_convert_field_to_csv(self.weapon_two_id)},"
            + f"{_convert_field_to_csv(self.weapon_three_id)},"
            + f"{_convert_field_to_csv(self.weapon_four_id)},"
            + f"{_convert_field_to_csv(self.weapon_five_id)},"
            + f"{_convert_field_to_csv(self.artifact_set_one_id_first)},"
            + f"{_convert_field_to_csv(self.artifact_set_one_id_second)},"
            + f"{_convert_field_to_csv(self.artifact_set_two_id_first)},"
            + f"{_convert_field_to_csv(self.artifact_set_two_id_second)},"
            + f"{_convert_field_to_csv(self.artifact_set_three_id_first)},"
            + f"{_convert_field_to_csv(self.artifact_set_three_id_second)},"
            + f"{_convert_field_to_csv(self.artifact_set_four_id_first)},"
            + f"{_convert_field_to_csv(self.artifact_set_four_id_second)},"
            + f"{_convert_field_to_csv(self.artifact_set_five_id_first)},"
            + f"{_convert_field_to_csv(self.artifact_set_five_id_second)}"
        )
