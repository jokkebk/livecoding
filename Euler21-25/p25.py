f1, f2 = 1, 1

for i in range(1,10**6):
    if len(str(f1)) >= 1000:
        print(i, f1)
        break
    f1, f2 = f2, f1+f2
