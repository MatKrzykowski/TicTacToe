import enum

class TicTacTor_field(enum.Enum):
    _ = 0
    O = 1
    X = 2

class TicTacToe_board():
    def __init__(self, array=[TicTacTor_field._ for i in range(9)]):
        self.array = array

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, new_value):
        self.array[key] = new_value

    def symbol(self, i):
        if self[i] == TicTacTor_field._:
            return " "
        elif self[i] == TicTacTor_field.X:
            return "X"
        elif self[i] == TicTacTor_field.O:
            return "O"
        else:
            assert False

    def print_line(self, i):
        return f"{self.symbol(i*3)} | {self.symbol(i*3+1)} | {self.symbol(i*3+2)}"

    def __str__(self):
        return f"""
           1   2   3
        A  {self.print_line(0)}
           ---------
        B  {self.print_line(1)}
           ---------
        C  {self.print_line(2)}
        """