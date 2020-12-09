with open('numbers.txt') as f:
    for line in f:
        notFound = True
        i = 0
        while notFound:
            if str(i) not in line:
                print(i)
                notFound = False
            i += 1
