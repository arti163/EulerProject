#https://projecteuler.net/problem=15

GRID = 2
#from math import comb - alternate solution
#paths = comb(GRID*2, GRID) - alternate solution

solved = dict()

def routes(m, n):
    if m == 0 or n == 0:
        return 1
    if (m,n) in solved:
        return solved[(m,n)]
    else:
        solved[(m,n)] = routes(m-1, n) + routes(m, n-1)
        return solved[(m,n)]

######################## SOLUTION ##########################
print('SOLUTION 0015:', routes(GRID, GRID), len(solved))