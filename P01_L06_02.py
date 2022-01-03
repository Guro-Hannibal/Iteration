class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def total(self):
        total = self.length * self.width * 25 * 5
        print(f'{total / 1000} тонн')


demo = Road(5000, 20)

demo.total()
