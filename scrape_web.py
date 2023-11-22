"""This module contains the logic for the scrape_web.py script."""
from src.character_input import characters_list
from src.scrape_web import build_characters_csv, scrape_web

MAKE_SERVER_CALL = False

scrape_web(character_input=characters_list[0], make_server_call=MAKE_SERVER_CALL)
scrape_web(character_input=characters_list[1], make_server_call=MAKE_SERVER_CALL)
scrape_web(character_input=characters_list[2], make_server_call=MAKE_SERVER_CALL)
scrape_web(character_input=characters_list[3], make_server_call=MAKE_SERVER_CALL)
scrape_web(character_input=characters_list[4], make_server_call=MAKE_SERVER_CALL)
scrape_web(character_input=characters_list[5], make_server_call=MAKE_SERVER_CALL)
scrape_web(character_input=characters_list[6], make_server_call=MAKE_SERVER_CALL)
build_characters_csv()
