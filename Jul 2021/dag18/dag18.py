def niklatz(n):
    yield n
    rule = 0
    while True:
        if rule:
            rule -= 1
        if n % 37 == 0:
            rule = 3

        n = n * 3 + 1 if (not n % 2 if rule else n % 2) else n // 2
        yield n
        if n == 1:
            return


def collatz(n):
    yield n
    while True:
        n = n * 3 + 1 if n % 2 else n // 2
        yield n
        if n == 1:
            return


diff = sum(sum(nik) for n in range(1, 1000000+1)
           if len((nik := list(niklatz(n)))) != len(list(collatz(n))))
print(diff)
