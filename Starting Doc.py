#input code from roam even if it is wrong. Put all of in here .
import math
import numpy as np
import matplotlib as plt
import pandas as pd
import more_itertools as iter
import itertools
from itertools import permutations
from itertools import chain, combinations
from more_itertools import powerset,set_partitions



def get_subsets(fullset):
  listrep = list(fullset)
  subsets = []
  for i in range(2**len(listrep)):
    subset = []
    for k in range(len(listrep)):
      if i & 1<<k:
        subset.append(listrep[k])
    subsets.append(subset)
  return subsets
subsets = get_subsets(set([1,2,3,4]))
print(subsets)
print(len(subsets))

mylist= [[1], [1,2], [1,2,3]]
print(iter.distinct_combinations([1,2,3],2))


combinations = list(iter.distinct_permutations([i for i in range(len(mylist))]))
print(combinations)

for item in combinations:
  print([mylist[item[i]] for i in range(len(mylist))])
test = iter.distinct_permutations([1,2,3,4],2)
print(test)

for i in iter.distinct_permutations(([1,2,3])):
  print(i)

print(list(permutations(['1','2','3'],2)))
print(list(permutations('abc',3)))
list2 = [1,2,2,2,2,2,2,2,2]
print(len(list2))



for i in iter.distinct_combinations(([1,2,3]),2):
  print(i)

iterable = 'abc'
for part in set_partitions(iterable, 2):
   print([''.join(p) for p in part])

print()