import enum
import numpy as np


class TicTacTor_field(enum.Enum):
    _ = 0
    O = 1
    X = 2


symbol = {
    TicTacTor_field._: " ",
    TicTacTor_field.X: "X",
    TicTacTor_field.O: "O",
}


class TicTacToe_board():
    def __init__(self, array=[TicTacTor_field._ for i in range(9)]):
        self.array = np.array(array)

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, new_value):
        self.array[key] = new_value

    def symbol(self, i):
        return symbol[self[i]]

    def print_line(self, i):
        return f"{self.symbol(i*3)} ║ {self.symbol(i*3+1)} ║ {self.symbol(i*3+2)}"

    def __str__(self):
        return f"""
           1   2   3
        A  {self.print_line(0)}
           ══╬═══╬══
        B  {self.print_line(1)}
           ══╬═══╬══
        C  {self.print_line(2)}
        """

    @property
    def is_win(self):
        # Vertical
        for i in range(3):
            if self.array[i] != TicTacTor_field._ and np.all(self[i:i+9:3] == self.array[i]):
                return self.array[i]
        # Horizontal
        for i in range(3):
            if self.array[3*i] != TicTacTor_field._ and np.all(self[i*3:i*3+3] == self.array[3*i]):
                return self.array[3*i]
        # Diagonal \
        if self.array[0] != TicTacTor_field._ and np.all(self[0:9:4] == self.array[0]):
            return self.array[0]
        # Diagonal /
        if self.array[2] != TicTacTor_field._ and np.all(self[2:7:2] == self.array[2]):
            return self.array[2]
        return TicTacTor_field._

    @property
    def is_free_space(self):
        return np.any(self.array == TicTacTor_field._)

    @property
    def is_game_done(self):
        return not self.is_free_space or self.is_win != TicTacTor_field._