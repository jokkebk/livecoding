def write(n):
    small = 'zero one two three four five six seven eight nine \
            ten eleven twelve thirteen fourteen fifteen sixteen \
            seventeen eighteen nineteen'.split()
    tens = 'twenty thirty fourty fifty sixty seventy eighty ninety'.split()

    if n<20:
        return small[n]
    elif n<100:
        s = tens[n//10 - 2]
        if n%10:
            return "%s-%s" % (s, write(n%10))
        else:
            return s
    elif n<1000:
        s = "%s hundred" % small[n//100]
        return "%s and %s" % (s, write(n%100)) if n % 100 else s
        # Python: 'abc' if condition else 'xyz'
        # C/C++ etc.:condition ? 'abc' : 'xyz'
    else: return 'one thousand'

s = 0
for i in range(1,1001):
    s += sum(1 for ch in write(i) if ch >= 'a' and ch <= 'z')
print(s)
