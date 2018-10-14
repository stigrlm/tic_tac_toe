from argparse import ArgumentParser

class InputHandler(ArgumentParser):
    def __init__(self):
        super().__init__()

    def get_inputs(self):
        self.add_argument('--side_size', help="Specify size of the side of the board grid between 3-10",
                            type=int, default=3)
        self.add_argument('--win_count', help="Specify how many marks in the row are needed for win 3-5",
                            type=int, default=3)

        self.args = self.parse_args()

        if self.args.side_size not in range(3, 11):
            self.error("Size of board grid size has to be between 3-10")
        if self.args.win_count not in range(3, 6):
            self.error("Number marks needed for win has to be between 3-5")
