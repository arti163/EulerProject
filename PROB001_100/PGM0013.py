#https://projecteuler.net/problem=13

numbers = [x.strip() for x in open('../DATA/input0013.txt','r').readlines()]

def sum_numbers():
    LENGTH = len(numbers[0])
    counted = ''
    rest = 0
    for pos in range(-1,-LENGTH-1,-1):
        column = sum([int(num[pos]) for num in numbers])+rest
        counted = str(column)[-1] + counted
        rest = column // 10
    counted = str(rest)+counted
    return counted[:10]

######################## SOLUTION ##########################
print('SOLUTION 0013:', sum_numbers())