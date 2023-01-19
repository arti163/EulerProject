#https://projecteuler.net/problem=14

NUMBER_MAX = 1_000_000

solved = {1:1}

def collatz_(num):
    if num in solved:
        return solved[num]
    else:
        if num % 2 == 0:
            solved[num] = 1+collatz_(int(num/2))
        else:
            solved[num] = 1+collatz_((int(3*num+1)))
    return solved[num]

colls = list(map(collatz_, range(1,NUMBER_MAX+1)))
position = colls.index(max(colls))+1
######################## SOLUTION ##########################
print('SOLUTION 0014:', position)