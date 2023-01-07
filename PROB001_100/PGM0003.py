#https://projecteuler.net/problem=3
NUMBER = 600851475143

def factors(number):
    facts = list()
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            facts.append(i)
            facts.append(int(number / i))
    return facts

def are_primes(facts):
    primes = set()
    for number in facts:
        counter = 0
        for i in range(2, int(number ** 0.5)+1):
            if number % i == 0:
                counter += 1
                break
        if not counter:
            primes.add(number)
    return primes 
######################## SOLUTION ##########################
print('SOLUTION 0003:', sorted(are_primes(factors(NUMBER)))[-1])