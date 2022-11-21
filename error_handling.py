try:
    with open('text.txt', 'r') as my_file:
        output = my_file.read()
        print(output)

except FileNotFoundError:
    print('There is no file like this.!')
