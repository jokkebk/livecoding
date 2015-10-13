import math

n, i = 600851475143, 2

while n > 1:
    if n % i == 0:
        print(i)
        n /= i
    else:
        i += 1
