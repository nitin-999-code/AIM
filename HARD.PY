from itertools import permutations
from sympy import isprime

def largest_pandigital_prime(n):
    digits = ''.join(str(i) for i in range(1, n + 1))
    pandigital_nums = sorted([''.join(p) for p in permutations(digits)], reverse=True)

    for num in pandigital_nums:
        if isprime(int(num)):
            for i in range(n):
                for j in range(i + 1, n):
                    swapped = list(num)
                    swapped[i], swapped[j] = swapped[j], swapped[i]
                    if isprime(int(''.join(swapped))):
                        return num
    return -1

n = int(input())
print(largest_pandigital_prime(n))
