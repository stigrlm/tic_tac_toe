class Player:
    """Class representing player in the game"""

    def __init__(self, mark):
        self.mark = mark

    def place_mark(self, board, x, y):
        board.grid[x][y] = self.mark

class CompPlayer(Player):
    # This class will hold logic of computer opponent
    pass
