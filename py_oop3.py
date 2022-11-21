class Calculator:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'It is not possible!'


super_cal = Calculator(20,
                       5)
add = super_cal.addition()
print(add)
sub = super_cal.subtraction()
print(sub)
mul = super_cal.multiplication()
print(mul)
div = super_cal.division()
print(div)

