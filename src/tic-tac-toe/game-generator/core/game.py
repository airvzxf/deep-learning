#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
The main class for the game.
"""
from numpy import random

from core.file import File
from core.history import Record, History


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
    __csv_file: File

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

    def play(self) -> int:
        """
        Start to play the game.

        :rtype: int
        :return: Returns 0 if the game is drawn; 1 if won the player 1; 2 if won the player 2.
        """
        available_cells: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        turn: int
        for turn in range(1, self.__turns + 1):
            cell: int = random.choice(available_cells)
            available_cell_index: int = available_cells.index(cell)
            available_cells.pop(available_cell_index)
            cell_index: int = cell - 1
            player_id: int = self.__player_1 if turn % 2 else self.__player_2
            self.__grid[cell_index]: int = player_id
            record = Record(player=player_id, turn=turn, cell=cell)
            self.__history.append(record)

            if turn < 5:
                continue

            player: int
            for player in [self.__player_1, self.__player_2]:
                marks_to_win: list = [player, player, player]
                row_1: bool = self.__grid[:3] == marks_to_win
                row_2: bool = self.__grid[3:6] == marks_to_win
                row_3: bool = self.__grid[6:9] == marks_to_win
                column_1: bool = self.__grid[::3] == marks_to_win
                column_2: bool = self.__grid[1::3] == marks_to_win
                column_3: bool = self.__grid[2::3] == marks_to_win
                cross_1: bool = self.__grid[::4] == marks_to_win
                cross_2: bool = self.__grid[2:8:2] == marks_to_win
                if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or cross_1 or cross_2:
                    self.__winner: int = player
                    break

            if self.__winner:
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

    def store_information(self, filename: str, information: str, overwrite: bool = False) -> None:
        """
        Store the information into the CSV file.

        :type filename: str
        :param filename: The filename for the CSV file.

        :type information: str
        :param information: The text with the information which will be storage.

        :type overwrite: bool
        :param overwrite: If true, it will delete and create a new file for fist time.
        Otherwise, it appends the information.

        :rtype: None
        """
        if '__csv_file' not in self.__dict__:
            self.__csv_file = File(filename)

        if self.__csv_file.filename != filename:
            self.__csv_file = File(filename)

        if overwrite:
            self.__csv_file.delete(delete_one_time=True)

        self.__csv_file.create()
        self.__csv_file.append(information + '\n')
