for num in range(1, 10):
    print(num)

x = int(input())
for i in range(1,x,2):
    print(i)

names = ['Sakib', 'Tamim', 'Santo', 'Mosaddek', 'Nurul']
for name in names:
    print(name)

for i in range(10):
    if i % 2 == 0:
        print(i)
print()

x = 1
while x < 10:
    if x % 2 != 0:
        print(x)
    x = x + 1


sum = 0
for i in range(12):
    sum = sum + i
print(sum)

x = int(input('Input a number: '))

for i in range(1,11):
    print(x, '*', i, '=', x*i)




