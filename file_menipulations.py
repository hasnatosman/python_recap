# writing a file................................
my_file = open('test.txt','w')
my_file.write('I love my country so much.\nI want to do good thing for my country!')

my_file= open('test.txt','a')
my_file.write('\nWe must be proud for loving my country!')
my_file.close()

new_file = open('test.txt','r')
output = new_file.read()
print(output)
new_file.close()
print()
print()

with open('test.txt','r') as my_file:
    output = my_file.read()
    print(output)