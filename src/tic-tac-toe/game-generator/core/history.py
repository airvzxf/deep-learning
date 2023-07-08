#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Structure of the history for each turn.
"""


class Record:
    """
    This class store the records for each turn.
    """
    __player: int
    __turn: int
    __cell: int

    def __init__(self, player: int, turn: int, cell: int) -> None:
        """
        Construction method.

        :type player: int
        :param player: Player ID.

        :type turn: int
        :param turn: The number of the turn where the player marked the cell.

        :type cell: int
        :param cell: Cell number of the position of the marked option.

        :rtype: None
        """
        self.__player = player
        self.__turn = turn
        self.__cell = cell

    @property
    def player(self) -> int:
        """
        Get the player ID, usually starting with 1.

        :rtype: int
        :return: Player ID.
        """
        return self.__player

    @property
    def turn(self) -> int:
        """
        Get the turn, starting with 1 and finished with 9, in case that the game is drawn.

        :rtype: int
        :return: The number of the turn.
        """
        return self.__turn

    @property
    def cell(self) -> int:
        """
        Get the cell position, when the player marked their selection.

        :rtype: int
        :return: Cell position.
        """
        return self.__cell


class History:
    """
    This class keep the record of the turns and the movements.
    """
    __records: list[Record]

    def __init__(self):
        self.__records: list[Record] = []

    def records(self) -> list[Record]:
        """
        Return the records of the history for each turn.
        """
        return self.__records

    def append(self, record: Record) -> None:
        """
        Add records to the history.

        :type record: Record
        :param record: The record which will added.

        :rtype: None
        """
        self.__records.append(record)
