#https://projecteuler.net/problem=2
UPPER = 4_000_000

sequence = [1, 2]

next_ = sequence[-2]+sequence[-1]
while next_ < UPPER:
    sequence.append(next_)
    next_ = sequence[-2]+sequence[-1]

######################## SOLUTION ##########################
print('SOLUTION 0002:', sum([x for x in sequence if x % 2 == 0]))