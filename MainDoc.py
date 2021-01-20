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
print("The power set in order is", subsets)

something=[] # ask sam if there is a easier way to do this in general.
for i in subsets:
    if len(i)==1: # i want to interate through the length of subsets.
        something.append(i)
for i in subsets:
    if len(i)==2:
        something.append(i)
for i in subsets:
    if len(i)==3:
        something.append(i)
for i in subsets:
    if len(i)==4:
        something.append(i)
for i in subsets:
    if len(i)==5:
        something.append(i)
Pn = something
print("Reordering by length gives us: ", Pn, "\n")

empty = []
for i in iter.distinct_combinations(([1,2,3]),2):
    empty.append(i)
print(empty)

iterable = "1234"
for part in set_partitions(iterable, 2):
    print([''.join(p) for p in part])
    #branchtest
#test