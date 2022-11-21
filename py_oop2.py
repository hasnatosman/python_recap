# calculator class ..................................
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is not possible!'


# creating an object....................................
my_calculator = Calculator()

temp = my_calculator.add(5, 7)
print(temp)

temp = my_calculator.sub(50, 30)
print(temp)

temp = my_calculator.mul(6, 5)
print(temp)

temp = my_calculator.div(10,2)
print(temp)
