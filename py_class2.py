class Car:
    name = ''
    color = ''

    def start(self):
        print('Start the engine!!')


my_car = Car()

""" my_car is a object of Car class """


my_car.name = 'Allion'
my_car.color = 'Red'

print('Name of the car :', my_car.name)
print('Color of the car :', my_car.color)

my_car.start()