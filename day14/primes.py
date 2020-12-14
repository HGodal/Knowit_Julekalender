from sympy import isprime

answer = 0
old = [0, 1]
nums = {0, 1}

for i in range(2, 1800813):
    prev = old[i % 2]

    a = prev - i
    if a < 0 or a in nums:
        a = prev + i

    nums.add(a)
    answer += isprime(a)
    old[i % 2] = a

print(f'Number of primes: {answer}')
