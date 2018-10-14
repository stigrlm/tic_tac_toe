import os
from board import Board
from players import Player
from functools import reduce

class Game:
    """Class representing core functionality of tic tac toe game"""

    def __init__(self, board_size=3, win_count=3):
        self.board = Board(board_size)
        self.players = (Player('o'), Player('x'))
        self.win_count = win_count

    def eval_round(self):
        """Evaluates one round of the game

        Returns:
            str: symbol of winner if there is one
        """
        for x, row in enumerate(self.board.grid):
            for y, field in enumerate(row):
                if not field:
                    continue
                win_player = self.check_field(field, x, y)
                if win_player:
                    return win_player

    def check_field(self, field_mark, x, y):
        """Checks fields around given field

        For given field on grid(row x, position in row y), performs check
        in 4 directions - down, right, diagonal right down, diagonal rigt up,
        for winning state of the game

        Parameters:
            field_mark (str): starting fields mark
            x (int): row location of the field
            y (int): field position in the row

        Returns:
            str: symbol of winning player if one has reached winning condition
        """

        # offests to locate next field in row, column, diagonal down and diagonal up
        x_offs = [0, 1, 1, -1]
        y_offs = [1, 0, 1, 1]

        for x_off, y_off in zip(x_offs, y_offs):
            mark_count = 0
            # check number of fields needed to win game
            for i in range(self.win_count):
                # calculate location of next field to check
                new_x = x + (i * x_off)
                new_y = y + (i * y_off)
                # break cycle if location is negative, nested list could be
                # indexed with negative integers and it will not index expected
                # field
                if new_x < 0 or new_y < 0:
                    break
                # break if index is not existing on grid
                try:
                    field = self.board.grid[new_x][new_y]
                except IndexError:
                    break
                # break if next field does not have same mark as base field
                if field != field_mark:
                    break
                else:
                    mark_count += 1

            if mark_count == self.win_count:
                return field_mark

    def calc_options_to_check(self):
        """Computes number variations that needs to be checked to determine
        if one of the players has won the game

        Returns:
            int: number of variations
        """

        count_base = self.board.size - self.win_count + 1
        line_opts = (self.board.size * count_base)  * 2
        if count_base > 1:
            diag_lines_nums = [x for x in range(1, count_base)]
            diag_opts = 2 * (count_base + (2 * reduce(lambda x, y: x + y, diag_lines_nums)))
        else:
            diag_opts = 2 * count_base

        return line_opts + diag_opts

class KonsoleGame(Game):
    """Class representing tic tac toe game with command line interface"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        """Controls run of the game"""

        win_player = None
        # run the game while there are fields to chose and no winner yet
        while self.board.fields_available and not win_player:
            for player in self.players:
                self.show_grid()
                print('Player {} turn'.format(player.mark))
                # get input from current player
                chosen_field = self.get_player_input()
                # convert field number to indices for nested list
                x, y = self.convert_position(chosen_field)
                # place player's mark on the field
                player.place_mark(self.board, x, y)
                # remove field from available actions
                self.board.fields_available.remove(chosen_field)
                # check for winning player
                win_player = self.eval_round()
                # break the cycle if there is winning player or no empty fields
                if win_player or not self.board.fields_available:
                    break
        # print the grid for last time
        self.show_grid()
        # print the result of the game
        if win_player:
            print("Player {} won!".format(win_player))
        else:
            print("It's a draw!")

    def get_player_input(self):
        """Keeps player asking for where he wants to place his mark until
        number representing one of the available fields is imputted

        Returns:
            int: number of field chosen by player
        """

        player_input = None
        message = "Where do you want to place your mark?: "

        while not isinstance(player_input, int):
            try:
                player_input = int(input(message))

                if player_input > self.board.size**2:
                    player_input = None
                    message = "Enter number available on the board: "
                elif player_input not in self.board.fields_available:
                    player_input = None
                    message = "The chosen field is not empty, choose different: "
            except ValueError:
                message = "Enter number available on the board: "

        return player_input

    def convert_position(self, pos_num):
        """Converts field number to location on grid

        Parameters:
            pos_num (int): number of field chosen by player to place mark

        Returns:
            tuple: containing indices of field position on grid
        """

        row_num = (pos_num - 1) // self.board.size
        row_pos = (pos_num - 1) % self.board.size

        return (row_num, row_pos)

    def show_grid(self):
        """Prints grid to the command line interface"""

        cls_cmd_map = {'nt': 'cls',
                       'posix': 'clear'}

        os.system(cls_cmd_map[os.name])

        for i, row in enumerate(self.board.grid):
            fields =[]
            for j, mark in enumerate(row):
                if mark:
                    fields.append(' {} '.format(mark))
                else:
                    field_num = str((self.board.size*i) + (j+1))
                    if len(field_num) == 1:
                        fields.append(' {} '.format(field_num))
                    else:
                        fields.append(field_num + (' ' * (3 - len(field_num))))

            print_row = '|'.join(fields)
            print(print_row)
            if i < self.board.size - 1:
                print('-' * len(print_row))
            else:
                print('')
