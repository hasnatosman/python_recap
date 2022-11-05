def dhaner_machine(dhan):
    print(dhan)
    return


# dhaner_machine('Ready Made Chal')

def sum(a, b, c):
    return a + b + c


value = sum(2, 5, 7)


def add(a, b, c=5):
    return a + b + c


total = add(5, 7)


# print(total)

def add(*args):
    temp = 0
    for number in args:
        temp = temp + number
    return temp


value = add(1, 4, 6, 7, 9)


# print('Total sum is :', value)


def add(*numbers):
    temp = 0
    for number in numbers:
        temp += number
    return temp


values = add(1, 3, 5, 7)


# print('Total is: ', values)


def add(**kwargs):
    tmp = 0
    for key in kwargs:
        tmp = tmp + kwargs[key]
    return tmp


values = add(a=1, b=3)


# print(values)


def even(**kwargs):
    temp = 0
    for i in kwargs:
        temp = temp + kwargs[i]
    return temp


values = even(a=5, b=7, c=9)
print(values)

