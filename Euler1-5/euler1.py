s = 0

for i in range(1,1000):
    # Number 4: 4%3=1 and 4%5=4
    # 12: 12%3 = 0 and 12%5 = 2
    if i%3==0 or i%5==0:
        print(i)
        s += i

print(s)
