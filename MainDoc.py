#input code from roam even if it is wrong. Put all of in here .
import math
import numpy as np # for array orientation, homogeneous terms. Faster than Python.
import matplotlib as plt
import pandas as pd
import more_itertools as iter
import itertools
from itertools import permutations
from itertools import chain, combinations
from more_itertools import powerset,set_partitions

n=3
nset=list(range(1,n+1))

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
Pn = get_subsets(set(nset))
print("The power set Pn is:\n", Pn, "\n")

#########: Finished: This states the subsets of length r ###############
empty3=[]
for j in range(1,len(nset)):
    empty = []
    for i in iter.distinct_combinations((nset),j):
        empty.append(i)
    empty = [list(k) for k in empty ]#list tuple. #change eah tuple to list.Done
    print("The",j,"-sets of", nset,"are: \n",empty, "\n")
    empty3.extend(empty) #extend adds th elements not the list as append does.
empty3.append(nset)
print("Reordering Pn by length and removing [] returns: \n", empty3, "\n")
#########: Finished: Obj: to give a list of all disjoint unions in Pn ###########

# Function to convert list to a string with spaces.
def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))

# Driver code
l_st_nset= [str(item) for item in nset]
st_nset_space=(listToString(l_st_nset))
st_nset=st_nset_space.replace(' ','')
#print(st_nset)

iterable = st_nset #string version of nset
empty2=[]
for part in set_partitions(iterable, 2):
    s1=''
    x=([s1.join(p) for p in part]) # How do store this
    # Convert string element back to list e.g [[1],[2,3,4]]
    # want to put these into list. currently in form x=['1', '2345']
    y = [list((word)) for word in x]
    #print(y)
    empty2.append([[int(i) for i in j] for j in y])# want to store all and put all into list.
djpair=empty2
print("The disjoint unions pairs of", nset,"are: \n",djpair)

### Attempt 1 at counting functions

# need a choice of base values for 2 -sets. e.g
#example seed material.

# func_s1([i])=0
# func_s2([1, 2]) = 1
# func_s2([1, 3])=0
# func_s2([2, 3])=0


#Set Pn as the powerset ordered by length.

OneSets0= [x for x in Pn if len(x)==1]
print(OneSets0)
dictempty={}
for i in OneSets0:
    dictempty[tuple(i)]=0
print(dictempty)

# def twosetfunction0(twoset): #assigns a choice of 2sets the value 1.
#     return {twoset:0}
# def twosetfunction1(twoset): #assigns a choice of 2sets the value 1.
#     return {twoset:1}
#Dictionaries store: string,number or tuple as keys and value can be anything.
#must change list to tuple before storage.
# L=tuple([1,3])
# make a choice for 2 sets with 0 and those with value 1.
# TwoSets0 = # x needs to be a tuple,string,
# TwoSets1 =
# #pass respectively through twosetfunction0 & twosetfunction1.
# value = twosetfunction1(L)
# TwoSetsValue0= {x: 0 for i in TwoSets0} # x needs to be a tuple,string,
# TwoSetsValue1= {x: 1 for i in TwoSets1}
# print(Merge(TwoSetsValue0,TwoSetsValue1))
#


#
#
# p1 = djpair[0] #  test: set p as first djpair
# djpair_funcval_0(p[0],p[1])
# def djpair_funcval_0(element1,element2): #for each element of djpair list.
# #takes in pair in djpair, outputs sum f(I)+f(J)
# def djpair_funcval_1
#
#
#
# # def msa2_function(element): #For subset I irrespective of decomp.
# def Merge(dict1, dict2):
#     return(dict2.update(dict1))
#
#
