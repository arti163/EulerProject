#https://projecteuler.net/problem=9

SUM_OF_THREE = 1000
isend = False

for a in range(1,999):
    for b in range(a+1, 999):
        if a+b >= 999:
            break
        c = SUM_OF_THREE-a-b
        if a ** 2 +b ** 2 == c ** 2:
            isend = True
            break
    if isend:
        break
######################## SOLUTION ##########################
print('SOLUTION 0009:', a*b*c)