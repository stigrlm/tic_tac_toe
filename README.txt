Tic tac toe game playable in command line, so far only for two live players.
My plan is to implement Computer opponent as a next step.

This project serves me as a basis to practice unit testing with pytest and test
driven development concepts. Command line interface is separated from core game
functionalities so GUI could be implemented more easily.

To run the tests:
  1. Clone the repository
  2. Create virtual environment and activate it
  3. Install project requirements - basically just pytest with its dependencies
  4. Excecute command "py.test" or "py.test -v" for more verbose test description
  5. Pytest will search for all "test*" files, execute all "test*" methods and
     present the output

To play the game:
  1. If not done yet, follow steps 1-3 above
  2. Execute "run_game.py" script

  Optional arguments:
    --side_size   size of the side of the board grid (3-10, default 3)
    --win_count   how many marks in the row are needed for win (3-5, default 3)

    example: run_game.py --side_size 6 --win_count 4
