#https://projecteuler.net/problem=10

NUMBER = 2_000_000

def is_prime(number):
    prime = True
    for i in range(2, int(number ** 0.5)+2):
        if number % i == 0 and number != i:
            return False
    return True

primes = [x for x in range(2, NUMBER) if is_prime(x)]
######################## SOLUTION ##########################
print('SOLUTION 0010:', sum(primes))