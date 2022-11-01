from board import TicTacToe_board, O

class TicTacToe():
    def __init__(self, first_player = O):
        self.first_player = first_player

    def start(self):
        board = TicTacToe_board()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()