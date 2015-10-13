# rrdd
# rdrd
# rddr
# drrd
# drdr
# ddrr

# ways to choose 2 items out of 4 = C(4, 2) = 4! / (2! * 2!) = 4*3/2 = 6
# ways to choose 20 items out of 40 = C(40, 20) = 40! / (20! * 20!)

def prod(n):
    if n <= 1: return 1
    return n * prod(n-1)

print(prod(40)//prod(20)//prod(20))
