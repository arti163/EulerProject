#https://projecteuler.net/problem=12

DIVISORS = 500

def triangles_(number):
    return sum(range(1,number+1))

def factors(number):
    facts = set()
    for i in range(1, int(number ** 0.5)+1):
        if number % i == 0:
            facts.add(i)
            facts.add(int(number / i))
    return facts

enough = False
num = 0
while not enough:
    num +=1
    if len(factors(triangles_(num))) > DIVISORS:
        enough = True


######################## SOLUTION ##########################
print('SOLUTION 0012:', triangles_(num))