def myFun(*args):
    """I love Python
I want to be a Pyhtonista"""
    for number in args:
        print(number)


myFun('Hasnat', 'Osman', 'Kazi')
print(myFun.__doc__)