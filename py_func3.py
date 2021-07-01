def add_numbers(numbers):
    result = 0
    for number in numbers:
        result = result + number
    return result


result = add_numbers([1, 2, 3, 4, 5])
print('Total is:', result)