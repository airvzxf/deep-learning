#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Steps for the game feature using BDD tests.
"""
from json import loads
from unittest import TestCase
from unittest.mock import patch

from behave import *

from core.game import Game

use_step_matcher("re")

test_case = TestCase()


@given("I want to run a new game")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.game = Game()


@step("I provide the follow (?P<grid_turns_cells>.+) marked by players")
def step_impl(context, grid_turns_cells):
    """
    :type context: behave.runner.Context
    :type grid_turns_cells: str
    """
    context.turn_cells = loads(grid_turns_cells)


@when("I start the game")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with patch('core.game.random.choice') as mock_random_choice:
        mock_random_choice.side_effect = context.turn_cells
        context.game.play()


@then("I got the results for the game")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    grid_size_expected = 9
    winner_results_expected = [0, 1, 2]

    test_case.assertEqual(
        grid_size_expected,
        len(context.game.grid),
        f'Expected {grid_size_expected}, got {len(context.game.grid)}'
    )

    test_case.assertIn(
        context.game.winner,
        winner_results_expected,
        f'Expected {winner_results_expected}, got {context.game.winner}'
    )


@step("The winner with (?P<winner_player_id>.+)")
def step_impl(context, winner_player_id):
    """
    :type context: behave.runner.Context
    :type winner_player_id: str
    """
    test_case.assertEqual(
        int(winner_player_id),
        context.game.winner,
        f'Expected {int(winner_player_id)}, got {context.game.winner}'
    )


@step("The returned grid with (?P<returned_grid>.+)")
def step_impl(context, returned_grid):
    """
    :type context: behave.runner.Context
    :type returned_grid: str
    """
    test_case.assertEqual(
        loads(returned_grid),
        context.game.grid,
        f'Expected {returned_grid}, got {context.game.grid}'
    )
