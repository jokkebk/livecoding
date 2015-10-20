def score(s):
    return sum(ord(ch)-64 for ch in s)

with open('p022_names.txt') as fin:
    s = fin.readline()
    names = [name[1:-1] for name in s.split(',')]
    total = 0
    for i,name in enumerate(sorted(names)):
        print(i+1, name, score(name))
        total += (i+1) * score(name)
    print(total)
