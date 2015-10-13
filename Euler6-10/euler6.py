square = 0
numsum = 0

for n in range(1, 101):
    numsum += n
    square += n*n
print(numsum**2 - square)
