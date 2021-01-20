# #floor function
# import math
# x = 12.2
# fvalue = math.floor(x)
# cvalue = math.ceil(x)
# print(fvalue)
# print(cvalue)

import itertools
import more_itertools as iter
from itertools import permutations
from itertools import chain, combinations
from more_itertools import powerset,set_partitions
def subsets(iterable):
    "Generate the subsets of elements in the iterable, in order by length."
    items = list(iterable)
    for k in range(len(items) + 1):
        for subset in itertools.combinations(items, k+1):
            yield subset # outputs a value but keeps the loop going,
            # gives you item faster than waitnig for the full calcualtion.

print(list(subsets([1,2,3,4])))

#Want all partions of {1,..,n} into two.









