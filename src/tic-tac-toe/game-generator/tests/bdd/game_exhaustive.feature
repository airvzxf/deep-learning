Feature: Enumerate every game
  It generates every possible game once.

  Scenario: Every possible game
    When I enumerate every possible game
    Then I got 255168 different games
    And 46080 games with the winner 0
    And 131184 games with the winner 1
    And 77904 games with the winner 2
