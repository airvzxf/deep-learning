# Created by wolf at 4/13/23
Feature: Play a game
  It will play a game with random values.

  Scenario: Play
    Given I want to run a new game
    When I start the game
    Then I got the results for the game
