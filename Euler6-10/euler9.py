import math

sq = {i*i: i for i in range(1, 1000) }

for a in range(1, 500):
    for b in range(a, 500):
        c2 = a*a + b*b
        if c2 in sq:
            c = sq[c2]
            if a+b+c == 1000:
                print(a, b, c, a*b*c)
