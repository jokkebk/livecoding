# [True, True, ..., True] (100 000 items)
prime = [True] * 120000

for i in range(2, len(prime)):
    if not prime[i]: continue
    for j in range(i+i, len(prime), i):
        prime[j] = False

primes = [i for i,isp in enumerate(prime) if isp]
print(len(primes))
print(primes[1+10001])
