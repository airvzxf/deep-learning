#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Start the loop of the Tic Tac Toe games.
"""
from core.game import Game


def start(number_games: int, csv_filename: str) -> None:
    """
    Start the loop of the games.

    :type number_games: int
    :param number_games: Number of loops which repeat the game.

    :type csv_filename: str
    :param csv_filename: The path and filename where the information will be storage.

    :rtype: None
    """
    first_loop = True
    for _ in range(number_games):
        game = Game()
        game.play()

        if first_loop:
            headers = game.get_headers_to_store()
            game.store_information(csv_filename, information=headers, overwrite=True)
            first_loop = False

        information = game.get_information_to_store()
        game.store_information(csv_filename, information=information)
