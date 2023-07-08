Feature: Play a game with not random
  It will play a game, but the values for each turn will be mocked related with the test list.

  Scenario Outline: Play with mock
    Given I want to run a new game
    And I provide the follow <grid turns cells> marked by players
    When I start the game
    Then I got the results for the game
    And The winner with <winner player ID>
    And The returned grid with <returned grid>
    # Player ID for the winner status: 0 for drawn; 1 for player one; 2 for player two.

    # The one dimension array is representing the grid of the game. It means:
    #  Single-Dimensional Array: which every number represents the turns.
    #  Odd numbers are the player 1, even player 2.
    #   Grid turns cells: [9, 8, 7, 6, 5, 4, 3, 2, 1]
    #    - Turn 1, marked cell 9 by Player 1.
    #    - Turn 2, marked cell 8 by Player 2.
    #    - Turn 3, marked cell 7 by Player 1.
    #    - Turn 4, marked cell 6 by Player 2.
    #    - Turn 5, marked cell 5 by Player 1.
    #    - Turn 6, marked cell 4 by Player 2.
    #    - Turn 7, marked cell 3 by Player 1.
    #    - Turn 8, marked cell 2 by Player 2.
    #    - Turn 9, marked cell 1 by Player 1.
    #  The visualization of the grid in the real world.
    #   Grid with position numbers:
    #   1 | 2 | 3
    #   ---------
    #   4 | 5 | 6
    #   ---------
    #   7 | 8 | 9
    #   Grid with marks by players, 1 is for player one, 2 for player two:
    #   1 | 2 | 1
    #   ---------
    #   2 | 1 | 2
    #   ---------
    #   1 | 2 | 1
    Examples: Get few amount of permutations
      | grid turns cells    | winner player ID | Comments       | returned grid       |
      | [1,4,2,5,3,6,7,8,9] | 1                | Match Row 1    | [1,1,1,2,2,0,0,0,0] |
      | [4,1,5,2,9,3,6,7,8] | 2                | Match Row 1    | [2,2,2,1,1,0,0,0,1] |
      | [4,1,5,2,6,3,7,8,9] | 1                | Match Row 2    | [2,2,0,1,1,1,0,0,0] |
      | [1,4,2,5,9,6,3,8,9] | 2                | Match Row 2    | [1,1,0,2,2,2,0,0,1] |
      | [7,1,8,2,9,3,4,5,6] | 1                | Match Row 3    | [2,2,0,0,0,0,1,1,1] |
      | [1,7,2,8,6,9,3,4,5] | 2                | Match Row 3    | [1,1,0,0,0,1,2,2,2] |
      | [1,2,4,3,7,5,6,8,9] | 1                | Match Column 1 | [1,2,2,1,0,0,1,0,0] |
      | [2,1,3,4,5,7,6,8,9] | 2                | Match Column 1 | [2,1,1,2,1,0,2,0,0] |
      | [2,1,5,3,8,4,6,7,9] | 1                | Match Column 2 | [2,1,2,0,1,0,0,1,0] |
      | [1,2,3,5,4,8,6,7,9] | 2                | Match Column 2 | [1,2,1,1,2,0,0,2,0] |
      | [3,1,6,2,9,4,5,7,8] | 1                | Match Column 3 | [2,2,1,0,0,1,0,0,1] |
      | [1,3,2,6,4,9,5,7,8] | 2                | Match Column 3 | [1,1,2,1,0,2,0,0,2] |
      | [1,2,5,3,9,4,6,7,8] | 1                | Match Cross 1  | [1,2,2,0,1,0,0,0,1] |
      | [2,1,3,5,4,9,6,7,8] | 2                | Match Cross 1  | [2,1,1,1,2,0,0,0,2] |
      | [3,1,5,2,7,4,6,8,9] | 1                | Match Cross 2  | [2,2,1,0,1,0,1,0,0] |
      | [1,3,2,5,4,7,6,8,9] | 2                | Match Cross 2  | [1,1,2,1,2,0,2,0,0] |
      | [1,2,5,3,6,4,7,9,8] | 0                | Match Drawn 1  | [1,2,2,2,1,1,1,1,2] |
      | [2,1,3,6,4,7,5,8,9] | 0                | Match Drawn 2  | [2,1,1,1,1,2,2,2,1] |
