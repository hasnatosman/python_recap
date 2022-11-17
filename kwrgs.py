def sum(**kwargs):
    temp = 0
    for i in kwargs:
        temp = temp + kwargs[i]
    return temp

value = sum(k = 8, x = 5, y = 8, a = 2)
print(value)