#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
The main class for the game.
"""
from typing import Optional, Sequence

from random import choice

from core.history import Record, History

WINNING_LINES: tuple = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),  # diagonals
)


def has_won(grid: Sequence[int], player: int) -> bool:
    """
    Check if the player has three marks in a row, column or diagonal.

    :type grid: Sequence[int]
    :param grid: The nine cells of the grid, with the player ID or 0 if the cell is empty.

    :type player: int
    :param player: The player ID.

    :rtype: bool
    :return: True if the player won.
    """
    return any(all(grid[index] == player for index in line) for line in WINNING_LINES)


class Game:
    """
    This class compute the Tic Tac Toe game.
    """
    __grid: list
    __player_1: int
    __player_2: int
    __turns: int
    __winner: int
    __history: History

    def __init__(self) -> None:
        """
        Construction method.

        :rtype: None
        """
        self.__grid = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
        ]
        self.__player_1 = 1
        self.__player_2 = 2
        self.__turns = 9
        self.__winner = 0
        self.__history = History()

    def play(self, cells: Optional[Sequence[int]] = None) -> int:
        """
        Start to play the game.

        :type cells: Optional[Sequence[int]]
        :param cells: The cells (1 to 9) marked in each turn. If it is None, every turn picks a random
        available cell. The game stops when a player wins, so the remaining cells are ignored.

        :rtype: int
        :return: Returns 0 if the game is drawn; 1 if won the player 1; 2 if won the player 2.
        """
        available_cells: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        turn: int
        for turn in range(1, self.__turns + 1):
            cell: int = choice(available_cells) if cells is None else cells[turn - 1]
            available_cells.remove(cell)
            player_id: int = self.__player_1 if turn % 2 else self.__player_2
            self.__grid[cell - 1] = player_id
            self.__history.append(Record(player=player_id, turn=turn, cell=cell))

            if turn >= 5 and has_won(self.__grid, player_id):
                self.__winner = player_id
                break

        return self.__winner

    def display_grid(self) -> None:
        """
        Display the grid results as a mathematical matrix.

        :rtype: None
        """
        print('=========')
        print('| GRID  |')
        print('=========')
        print(self.__grid[:3])
        print(self.__grid[3:6])
        print(self.__grid[6:])
        print()

    def display_winner(self) -> None:
        """
        Display the winner as a text.

        :rtype: None
        """
        if self.__winner == 0:
            print('Drawn game')
        elif self.__winner == 1:
            print('Won, player 1!')
        elif self.__winner == 2:
            print('Won, player 2!')
        else:
            print('Who won?')
        print()

    @property
    def grid(self) -> list:
        """
        Get the grid parameter.

        :rtype: list
        :return: Return the Grid
        """
        return self.__grid

    @property
    def history(self) -> History:
        """
        Get the history of the game.

        :rtype: History
        :return: Return the history
        """
        return self.__history

    @property
    def winner(self) -> int:
        """
        Get the winner of the game.

        :rtype: int
        :return: Return the winner
        """
        return self.__winner

    @staticmethod
    def get_headers_to_store() -> str:
        """
        Return the headers for the CSV file.

        :rtype: str
        :return: The headers.
        """
        headers: str = 'turn_1_player,turn_1_cell,turn_2_player,turn_2_cell,turn_3_player,turn_3_cell,' \
                       'turn_4_player,turn_4_cell,turn_5_player,turn_5_cell,turn_6_player,turn_6_cell,' \
                       'turn_7_player,turn_7_cell,turn_8_player,turn_8_cell,turn_9_player,turn_9_cell,' \
                       'winner'

        return headers

    def get_information_to_store(self) -> str:
        """
        Return the information of the game which is useful for the storage in the CSV file.
        The information is the turns history, and the winner.

        :rtype: str
        :return: Information about the game.
        """
        information: str = ''.join(
            f'{record.player},{record.cell},'
            for record in self.__history.records()
        )

        total_records: int = len(self.__history.records())
        for _ in range(total_records, 9):
            information += '0,0,'

        information += f'{self.__winner}'

        return information
