def pyprt(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns

        for j in range(0, i + 1):
            # printing stars
            print('*', end='')

        print('\r')


# driver code
n = 5
pyprt(n)
