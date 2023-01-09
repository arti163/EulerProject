#https://projecteuler.net/problem=5

MAX_NUMBER = 20

number = 2520
is_divided = False

while is_divided is False:
    divs = set()
    number += 2520
    for i in range(1, MAX_NUMBER+1):
        if number % i == 0:
            divs.add(i)
    if len(divs) == MAX_NUMBER:
        is_divided = True


######################## SOLUTION ##########################
print('SOLUTION 0005:', number)