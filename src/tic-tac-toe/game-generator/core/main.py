#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Start the loop of the Tic Tac Toe games.
"""
from typing import Iterable, Optional

from core.exhaustive import all_games
from core.game import Game


def start(number_games: int, csv_filename: str, exhaustive: bool = False) -> int:
    """
    Play the games and store one CSV row for each one.

    :type number_games: int
    :param number_games: Number of random games. It is ignored when `exhaustive` is true.

    :type csv_filename: str
    :param csv_filename: The path and filename where the information will be stored.
    The file is overwritten.

    :type exhaustive: bool
    :param exhaustive: If true, it stores every possible game once instead of random games.

    :rtype: int
    :return: The number of stored games.
    """
    games: Iterable[Optional[tuple]] = all_games() if exhaustive else (None for _ in range(number_games))

    total: int = 0
    with open(csv_filename, 'w', encoding='utf-8') as csv_file:
        csv_file.write(Game.get_headers_to_store() + '\n')
        cells: Optional[tuple]
        for cells in games:
            game = Game()
            game.play(cells)
            csv_file.write(game.get_information_to_store() + '\n')
            total += 1

    return total
