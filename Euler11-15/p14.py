def terms(n):
    t = 1
    while n != 1:
        if n&1: n = 3*n+1
        else: n //= 2
        t += 1
    return t

print(max((terms(n), n) for n in range(1, 10**6))[1])
