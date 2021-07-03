class Car:
    name = ''
    color = ''

    def start():
        print('Start the engine!')


Car.name = 'Axio'
Car.color = 'Black'

print('Name of the car: ', Car.name)
print('Color of the car: ', Car.color)

Car.start()
