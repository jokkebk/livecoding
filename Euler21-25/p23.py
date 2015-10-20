def abundant(n):
    s = 1
    for i in range(2, n//2+1):
        if n%i: continue
        s += i
    return s > n

ab = [n for n in range(12, 28123) if abundant(n)]

impossible = {i for i in range(1,28123+1)}

for i,a in enumerate(ab):
    for b in ab[i:]: # b >= a
        impossible.discard(a+b)

print(sum(impossible))
