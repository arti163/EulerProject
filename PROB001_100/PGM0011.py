#https://projecteuler.net/problem=11

grid = [list(map(int,x.strip().split(' '))) for x in open('../DATA/input0011.txt','r').readlines()]
NUMBERS = 4
SIZE = len(grid)

maximum = {'max':0}

def product(numbers):
    prod = 1
    for n in numbers:
        prod *= n
    maximum['max'] = max(prod, maximum['max'])

def get_digits_left():
    for i in range(SIZE):
        for j in range(SIZE):
            if j<=SIZE-NUMBERS:
                product([grid[i][j+x] for x in range(NUMBERS)])
                product([grid[j+x][i] for x in range(NUMBERS)])
            if i<=SIZE-NUMBERS:
                if j<=SIZE-NUMBERS:
                    product([grid[i+x][j+x] for x in range(NUMBERS)])
                if j>=NUMBERS-1:
                    product([grid[i+x][j-x] for x in range(NUMBERS)])


get_digits_left()
######################## SOLUTION ##########################
print('SOLUTION 0011:', maximum['max'])