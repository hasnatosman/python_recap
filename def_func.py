def add(*numbers):
    temp = 0
    for number in numbers:
        temp = temp + number
    return temp


values = add(2, 4, 6, 8, 9)
