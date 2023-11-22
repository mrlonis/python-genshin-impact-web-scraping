"""This module contains the tests for the scrape_web.py script."""
from src.character_input import characters_list
from src.scrape_web import scrape_web


def test_scrape_web():
    """Test the scrape_web function."""
    print("test_scrape_web(): Starting...")
    html = scrape_web(character_input=characters_list[0], make_server_call=False)
    assert html is not None
    print(html)
    print("test_scrape_web(): Finished.")
