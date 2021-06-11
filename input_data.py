"""
here we will input data from users using input() function.

"""

x = input('Input a data: ')
print('Inputted data is ', x)
print(type(x))

y = input('Input something: ')
print('Inputted data is ', y)
print(type(y))

"""
if you try to sum ro multiply, you must mention the data type first,
either output will through a typeError.
"""

# type Casting or type conversion

x = int(input('Input a number: '))
y = int(input('Input a number: '))
z = x + y
print('Sum of x and y is ', z)

"""
If you mention the type before calling a variable, that is call type conversion or type casting,

Example: int(), float(), str(), tuple(), list() and so on............


"""

a = str()
print(type(a))
y = int()
print(type(y))

