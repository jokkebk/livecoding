from functools import reduce
from operator import mul

print(sum(int(c) for c in str(reduce(mul, range(1,101)))))
