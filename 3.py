# Project Euler Solutions
# Problem 3 - Largest prime factor
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

# Using approach from http://stackoverflow.com/a/412942

def primeFactors(n):
    '''Return all prime factors of n'''
    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d**2 > n:
            if n > 1:
                factors.append(n)
                break
    return factors

       
if __name__ == "__main__":
    limit = 600851475143 
    factors = primeFactors(limit)
    print max(factors)