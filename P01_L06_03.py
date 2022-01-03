class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}
        self.full_name = f'{name} {surname}'


class Position(Worker):

    def get_full_name(self):
        return self.full_name

    def total_income(self):
        return self.income['wage'] + self.income['bonus']


anon = Position('Gilgamesch', 'Barka', 'Emperor', 5000, 10000)

print(anon.get_full_name())

print(anon.total_income())
