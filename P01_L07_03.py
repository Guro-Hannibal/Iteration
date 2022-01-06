class Cell:

    def __init__(self, count):
        self.length = count

    def __add__(self, other):
        return Cell(self.length + other.length)

    def __sub__(self, other):
        return Cell(self.length - other.length)

    def __mul__(self, other):
        return Cell(self.length * other.length)

    def __truediv__(self, other):
        return Cell(int(self.length / other.length))

    def make_order(self, row_length):
        y = 0
        for i in range(self.length):
            print('*', end=' ')
            y += 1
            if y == row_length:
                print()
                y = 0


cell1 = Cell(33)

cell2 = Cell(11)

cell3 = cell1 * cell2

cell3.make_order(13)
