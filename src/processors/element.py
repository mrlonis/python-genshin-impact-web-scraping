"""This module contains the logic for the get_element processor."""
from bs4 import BeautifulSoup, Tag

from src.character_data import CharacterData


def get_element(soup: BeautifulSoup, character_data: CharacterData):
    """Get the element of the character."""
    element_result = soup.find("img", {"class": "character-element"})
    element: str | None = None
    if element_result and isinstance(element_result, Tag):
        element = element_result.attrs["alt"]
        character_data.element_id = element
    else:
        error_message = f"Element not found for {character_data.name}."
        print(f"ERROR: {error_message}")
        raise ValueError(error_message)
