class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'drawing with {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'drawing with {self.title} and something uniq')


class Pencil(Stationery):
    def draw(self):
        print(f'drawing with f{self.title} and something uniq one more time')


class Handle(Stationery):
    def draw(self):
        print(f'drawing with f{self.title} and something uniq. Draw! Draw! Never ending coding!')


pen = Pen('pen')

pencil = Pencil('pencil')

handle = Handle('handle')

pen.draw()

pencil.draw()

handle.draw()
