from sympy import divisors
from math import sqrt

valid_count = 0

for n in range(1000000):
    if n % 10 not in (1, 3, 7, 9):
        divsum = sum(divisors(n))
        if divsum > n*2:
            if sqrt(abs(divsum-n*2)).is_integer():
                valid_count += 1

print(f'Number of valid numbers: {valid_count}')
