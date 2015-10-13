f, fp = 1, 1

s = 0
while True:
    f, fp = f+fp, f
    if fp >= 4e6: break
    print(fp)
    if (fp&1) == 0: s += fp
print(s)
