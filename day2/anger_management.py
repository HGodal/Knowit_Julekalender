population = 5433000


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def highest_prime(i):
    for j in range(i, 0, -1):
        if is_prime(j):
            return j


i = 0
counter = 0
while i <= population:
    if '7' in str(i):
        i += highest_prime(i)
    else:
        counter += 1
    i += 1

print(counter)
