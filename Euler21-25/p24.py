from itertools import permutations

i = 1
for p in permutations("0123456789", 10):
    if i==10**6:
        print(''.join(p))
        break
    i += 1
