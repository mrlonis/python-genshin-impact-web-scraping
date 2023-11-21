"""This module contains the tests for the scrape_web.py script."""
from scrape_web import scrape_web


def test_scrape_web():
    """Test the scrape_web function."""
    print("test_scrape_web(): Starting...")
    url = "https://genshin.gg/characters/ayaka/"
    html = scrape_web(url=url, make_server_call=False)
    assert html is not None
    print(html)
    print("test_scrape_web(): Finished.")
