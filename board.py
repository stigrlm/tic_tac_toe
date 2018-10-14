class Board:
    """Class representing board - the playground on which
    tic tac toe is played
    """

    def __init__(self, size):
        self.size = size
        self.grid = self.create_grid(size)
        self.fields_available = [x for x in range(1, (size**2)+1)]

    @staticmethod
    def create_grid(size):
        """Creates grid structure for board

        Parameters:
            size (int): size of the side of grid

        Returns:
            list: nested list representing grid structure
        """
        grid = []
        for i in range(size):
            grid.append([None for x in range(size)])
        return grid
