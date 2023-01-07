#https://projecteuler.net/problem=1
UPPER = 1000
######################## SOLUTION ##########################
print('SOLUTION 0001:', sum([x for x in range(1,UPPER) if (x % 3 == 0 or x % 5 == 0)]))