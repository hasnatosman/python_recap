# constructing output list without................................
# using comprehensions............................................

input_list = [0, 55, 4, 66, 1, 2, 36, 77, 90, 22, 66 ,3, 5, 6, 7, 8, 9, 55, 33, 67, 88]
output_list = []
trash_list = []

for i in input_list:
    if i % 2 == 0:
        output_list.append(i)
    else:
        trash_list.append(i)
    pass


print(sorted(output_list))
print(sorted(trash_list))

# constructing output list ...............................
# using comprehensions...........................................

comp_list = [i for i in input_list if i % 2 == 0]
print(sorted(comp_list))