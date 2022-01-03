class Car:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        if is_police:
            self.name = 'мусор'

    def go(self, gogo):
        self.speed += gogo

    def turning(self, direction):
        print(f'turning {direction}')

    def stop(self):
        self.speed -= self.speed

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости. Дави на газ или тормози)')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости. Дави на газ или тормози)')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


town_car = TownCar(50, 'black', 'tesla')

sport_car = SportCar(133, 'black and white', 'tesla cybertruck')

work_car = WorkCar(65, 'red', 'genesis')

police_car = PoliceCar(90, 'blue', 'BMW', True)

town_car.show_speed()
town_car.go(50)
town_car.show_speed()

print(f'{sport_car.colour}, {sport_car.speed}, {sport_car.name}, {sport_car.is_police}')

print(f'{police_car.speed}, {police_car.name}, {police_car.colour}, {police_car.is_police}')
