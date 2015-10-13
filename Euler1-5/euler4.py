from itertools import product

def p(n):
    s = str(n)
    r = s[::-1]
    return s == r

#big = 0
#for i,j in product(range(100, 1000), repeat=2):
#    if p(i*j): big = max(big, i*j)
#print(big)

print(max(i*j for i,j in product(range(100, 1000), repeat=2) if p(i*j)))
