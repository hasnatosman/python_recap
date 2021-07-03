class Car:
    """ Define a class name as Car """
    name = 'Premio'
    color = 'Blue'
    model = 2021

    """ Some data of the class"""

    def start():
        print('Starting the engine !')

        """ Method called start"""


print('Name of the car: ', Car.name)
print('Color of the car: ', Car.color)
print('Model of the car: ', Car.model)

print()
print()

Car.start()
