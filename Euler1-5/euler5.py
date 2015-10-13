
# 2520 = 2*3*5*7*3

# 1, 2, 3, 2*2, 5, 2*3, 7, 2*2*2, 3*3, 2*5
# 9*8*7*5 = 2520

# 2520*11*13*17*19*2 = 232792560
# 11, 13, 17, 19, 2
# 12=2*2*3, 15=2*7, 16, 18=2*3*3

n = 2520

for i in range(1, 100000):
    ok = True
    for j in range(11,21):
        if (n*i) % j:
            ok = False
            break
    if ok:
        print(n*i)
        break

exit(1) 

from collections import defaultdict

def factor(n):
    for i in range(2,n+1):
        if n%i: continue
        for p in range(1,6):
            if n % (i**p):
                yield(i, p-1)
                n //= i**(p-1)
                break
        if n < i: break

highest = defaultdict(int)

for i in range(1,20):
    print("Factor", i)
    for n,p in factor(i):
        print(n, p)
        highest[n] = max(highest[n], p)

mul = 1

for n in highest:
    mul *= n ** highest[n]

print(mul)
