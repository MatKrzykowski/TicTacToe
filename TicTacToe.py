from board import TicTacToe_board, EMPTY, O, X


class TicTacToe:
    def __init__(self, first_player=O):
        self.player = first_player
        self.board = None
        self.is_done = False

    def start(self):
        self.board = TicTacToe_board()
        self.next_turn()

    def next_turn(self):
        self.move()
        print(self.board)
        self.handle_win_state()
        if not self.is_done:
            self.update_player()
            self.next_turn()

    def move(self):
        i = self.parse_move()
        if i == -1:
            print("Invalid statement, please insert proper value!")
            self.move()
        elif self.board[i] != EMPTY:
            print("Invalid move, please insert different value!")
            self.move()
        else:
            self.board[i] = self.player

    def parse_move(self):
        data = input("Please specify field, e.g. A1 or C2\n")
        if len(data) != 2:
            return -1
        if data[0] not in ("A", "B", "C") and data[1] not in ("1", "2", "3"):
            return -1
        result = int(data[1]) - 1
        if data[0] == "A":
            return result
        elif data[0] == "B":
            return result + 3
        else:
            return result + 6

    def handle_win_state(self):
        if self.board.is_game_done:
            winner = self.board.is_win
            if winner in (O, X):
                print(f"Player {self.player} won!")
            else:
                print("Draw!")
            self.is_done = True
        else:
            print("The game continues")

    def update_player(self):
        if self.player == O:
            self.player = X
        elif self.player == X:
            self.player = O
        else:
            assert False


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
