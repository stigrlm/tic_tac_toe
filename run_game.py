from game import KonsoleGame
from inputs import InputHandler

input_handler = InputHandler()
input_handler.get_inputs()

game = KonsoleGame(board_size=input_handler.args.side_size,
                   win_count=input_handler.args.win_count)
game.run()
