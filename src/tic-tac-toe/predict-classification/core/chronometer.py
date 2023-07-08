# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Create a chronometer which creat partial checks for every step.
"""
from datetime import timedelta
from time import monotonic


class Chronometer:
    """
    This chronometer checks partials stops for every step.
    """
    __time_line: list[tuple[str, float, float]]
    __start_time: float
    __last_check: float

    def __init__(self):
        self.__time_line = []
        self.__start_time = monotonic()
        self.__last_check = monotonic()

    def check(self, name: str) -> None:
        total_time: float = monotonic() - self.__start_time
        duration: float = monotonic() - self.__last_check
        self.__time_line.append((name, total_time, duration))
        self.__last_check = monotonic()

    def display_information(self):
        print()
        print('========================================')
        print('===     Summary of the time line     ===')
        print('========================================')
        row: tuple[str, float, float]
        for row in self.__time_line:
            name: str
            total_time: float
            duration: float
            name, _, duration = row
            print(f'{name}: {timedelta(seconds=duration)}')

        print(f'Total time: {timedelta(seconds=self.__last_check - self.__start_time)}')
