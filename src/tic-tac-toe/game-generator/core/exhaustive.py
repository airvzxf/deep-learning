#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Enumerate every possible Tic Tac Toe game.
"""
from typing import Iterator

from core.game import has_won


def all_games() -> Iterator[tuple]:
    """
    Generate every possible game, once each, as the sequence of marked cells (1 to 9).
    A game stops as soon as a player wins, so there are 255,168 different games.

    :rtype: Iterator[tuple[int, ...]]
    :return: The cells marked in each turn, in order.
    """
    grid: list = [0] * 9

    def walk(cells: tuple) -> Iterator[tuple]:
        player: int = 1 if len(cells) % 2 == 0 else 2
        cell_index: int
        for cell_index in range(9):
            if grid[cell_index]:
                continue
            grid[cell_index] = player
            game: tuple = cells + (cell_index + 1,)
            if has_won(grid, player) or len(game) == 9:
                yield game
            else:
                yield from walk(game)
            grid[cell_index] = 0

    yield from walk(())
