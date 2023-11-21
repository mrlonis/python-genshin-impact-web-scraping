"""This module contains the logic for the scrape_web.py script."""
from src.characters import characters_list
from src.scrape_web import build_characters_csv, scrape_web

scrape_web(character_input=characters_list[0], make_server_call=False)
scrape_web(character_input=characters_list[1], make_server_call=False)
scrape_web(character_input=characters_list[2], make_server_call=False)
scrape_web(character_input=characters_list[3], make_server_call=False)
scrape_web(character_input=characters_list[4], make_server_call=False)
scrape_web(character_input=characters_list[5], make_server_call=False)
scrape_web(character_input=characters_list[6], make_server_call=False)
build_characters_csv()
