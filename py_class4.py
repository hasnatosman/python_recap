class Car:

    name = ''
    color = ''

    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print('Start the engine!')


my_car = Car('Corolla', 'Black')
print(my_car.name)
print(my_car.color)
my_car.start()