from time import sleep


class TrafficLight:
    __colour = 'turned off'

    def running(self, iter_num=2):
        met_colour = TrafficLight.__colour
        if iter_num > 0:
            iter_num -= 1
        elif iter_num == 0:
            print('End code 0')
            return
        if met_colour == 'turned off' or met_colour == 'green':
            met_colour = 'red'
            print(met_colour)
            sleep(3.1)
        if met_colour == 'red':
            met_colour = 'yellow'
            print(met_colour)
            sleep(2.4)
        if met_colour == 'yellow':
            met_colour = 'green'
            print(met_colour)
            sleep(3.1)
        self.running(iter_num)


demo = TrafficLight()

demo.running(3)
