from board import Board
from game import Game, KonsoleGame
from players import Player

# Board tests

def test_board_init():
    errors = []
    board = Board(size=3
            )
    if board.size != 3:
        errors.append('Board size is not 3')
    if not isinstance(board.grid, list):
        errors.append('Board is not of type list')

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_grid_size():
    grid = Board.create_grid(3)
    assert len(grid) == 3

def test_grid_type():
    grid = Board.create_grid(3)
    assert isinstance(grid, list)

def test_grid_row_type():
    grid = Board.create_grid(3)
    assert isinstance(grid[0], list)

def test_grid_cell_value():
    grid = Board.create_grid(3)
    assert grid[0][0] == None

# Player tests

def test_player_init():
    player = Player(mark='o')
    assert player.mark == 'o'

# Game tests

def test_game_init():
    errors = []
    game = Game(board_size=4)

    if game.board.size != 4:
        errors.append('Board size is not 4')
    if game.players[0].mark != 'o':
        errors.append('Player1 mark is not correct')
    if game.players[1].mark != 'x':
        errors.append('Player2 mark is not correct')
    if game.win_count != 3:
        errors.append('Wins count is not 3')

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_calc_options_to_check():
    game = Game(board_size=3, win_count=3)
    assert game.calc_options_to_check() == 8

def test_check_field_win_row_o():
    game = Game()
    game.board.grid[0][0] = game.players[0].mark
    game.board.grid[0][1] = game.players[0].mark
    game.board.grid[0][2] = game.players[0].mark

    assert game.check_field('o', 0, 0) == 'o'

def test_check_field_win_column_o():
    game = Game()
    game.board.grid[0][0] = game.players[0].mark
    game.board.grid[1][0] = game.players[0].mark
    game.board.grid[2][0] = game.players[0].mark

    assert game.check_field('o', 0, 0) == 'o'

def test_check_field_win_diagonal_o():
    game = Game()
    game.board.grid[0][0] = game.players[0].mark
    game.board.grid[1][1] = game.players[0].mark
    game.board.grid[2][2] = game.players[0].mark

    assert game.check_field('o', 0, 0) == 'o'

def test_check_field_win_diagonal_x():
    game = Game()
    game.board.grid[2][0] = game.players[1].mark
    game.board.grid[1][1] = game.players[1].mark
    game.board.grid[0][2] = game.players[1].mark

    assert game.check_field('x', 2, 0) == 'x'

def test_check_field_no_win():
    game = Game()
    game.board.grid[2][0] = game.players[1].mark
    game.board.grid[1][1] = game.players[0].mark
    game.board.grid[0][2] = game.players[1].mark

    assert game.check_field('x', 2, 0) == None

def test_eval_round_win():
    game = Game()

    game.board.grid[2][0] = game.players[1].mark
    game.board.grid[1][1] = game.players[1].mark
    game.board.grid[0][2] = game.players[1].mark

    assert game.eval_round() == game.players[1].mark

# KonsoleGame tests

def test_convert_position():
    game = KonsoleGame()

    assert game.convert_position(5) == (1, 1)
