import enum

class TicTacTor_field(enum.Enum):
    _ = 0
    O = 1
    X = 2

class TicTacToe_board():
    def __init__(self, array):
        self.array = array

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, new_value):
        self.array[key] = new_value