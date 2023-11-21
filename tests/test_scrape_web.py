"""This module contains the tests for the scrape_web.py script."""
from scrape_web import scrape_web
from src.characters import characters_list


def test_scrape_web():
    """Test the scrape_web function."""
    print("test_scrape_web(): Starting...")
    html = scrape_web(character_input=characters_list[0], make_server_call=False)
    assert html is not None
    print(html)
    print("test_scrape_web(): Finished.")
