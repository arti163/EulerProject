#https://projecteuler.net/problem=4

def is_palindrome(number):
    number = str(number)
    ispal = True
    for i in range(len(number)//2):
        if number[i] != number[-1-i]:
            return False
    return ispal

max_palindrome = 0

for num1 in range(999,99,-1):
    for num2 in range(999, 99, -1):
        if is_palindrome(num1*num2):
            max_palindrome = max(max_palindrome, num1*num2)
######################## SOLUTION ##########################
print('SOLUTION 0004:', max_palindrome)