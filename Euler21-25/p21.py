d = lambda n: 1 + sum(i for i in range(2, n//2+1) if n%i==0)
s = 0

for i in range(1,10000):
    j = d(i)
    if j != i and i == d(j): s += i

print(s)
