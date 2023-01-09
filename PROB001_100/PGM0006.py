#https://projecteuler.net/problem=6

NUMBERS = 100

sum_squares = sum([x**2 for x in range(1,NUMBERS+1)])
squares_sum = sum([x for x in range(1,NUMBERS+1)])**2
######################## SOLUTION ##########################
print('SOLUTION 0006:', squares_sum-sum_squares)