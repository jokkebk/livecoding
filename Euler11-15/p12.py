from collections import defaultdict

tri = 0
for i in range(1, 20000):
    tri += i

    num = tri
    factors = defaultdict(int)

    for n in range(2, 18):
        while num % n == 0:
            factors[n] += 1
            num //= n
        if num == 1: break

    prod = 1
    for f in factors: prod *= factors[f] + 1

    if prod > 500:
        print(tri, "can be factored", prod, "ways")
        break

# n = 2^3 * 7^2 * 11 = 4312
# 2^1 * 7^1 * 11^0
# ways: 4 * 3 * 2 = 24
