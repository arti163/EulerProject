#https://projecteuler.net/problem=7

SUCCESIVE = 10_001
SUCCESIVE = 6

primes = set()
number = 1
def is_prime(number):
    prime = True
    for i in range(2, int(number ** 0.5)+2):
        if number % i == 0 and number != i:
            return False
    return True

while len(primes) < SUCCESIVE:
    number += 1
    if is_prime(number):
        primes.add(number)

######################## SOLUTION ##########################
print('SOLUTION 0007:', number)