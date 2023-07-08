#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Entry point of the execution in this application.
"""
from argparse import ArgumentParser

from core.main import start

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Tic Tac Toe game generator',
        epilog='Created by Israel Roldan (2023). https://github.com/airvzxf/',
        description='This application runs the Tic Tac Toe game a finite number of times.'
                    ' In each iteration it stores the records in a CSV file (Comma Separated Value).'
    )
    parser.add_argument('-n', '--number-games', type=int, default=1000000,
                        help='Number of times that the game will play.')
    parser.add_argument('-f', '--csv-filename', type=str, default='tic-tac-toe-records.csv',
                        help='The filename of the CSV which will store the records.')
    args = parser.parse_args()
    number_games = args.number_games
    csv_filename = args.csv_filename

    start(number_games, csv_filename)
