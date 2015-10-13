# [True, True, ..., True] (100 000 items)
prime = [True] * 2000000

for i in range(2, len(prime)):
    if not prime[i]: continue
    for j in range(i+i, len(prime), i):
        prime[j] = False
prime[0] = prime[1] = False

print(sum(i for i,isp in enumerate(prime) if isp))
