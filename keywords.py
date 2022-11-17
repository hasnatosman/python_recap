def sum(*args):
    temp = 0
    for i in args:
        temp = temp + i
    return temp

value = sum(1, 3, 5, 7, 8)
print(value)
