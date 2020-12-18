def palindrome(word):
    if len(word) < 3:
        return False
    if word == word[::-1]:
        return False

    left = word[:int(len(word)/2 + 0.5)]
    right = word[int(len(word)/2):]

    while len(left) > 1:
        if left[0] == right[-1]:
            left = left[1:]
            right = right[:-1]
        elif left[:2] == right[-2:]:
            left = left[2:]
            right = right[:-2]
        else:
            return False
    return True


count = sum(palindrome(n) for n in open('wordlist.txt').read().splitlines())

print(f'Number of palin-almost-dromes: {count}')
