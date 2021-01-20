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
    empty3.extend([empty]) #extend adds th elements not the list as append does.
empty3.append([nset])
len_r_subsets_Pn = empty3
print("Reordering Pn by length and removing [] returns: \n", len_r_subsets_Pn, "\n")
# Here len_r_subsets_Pn[0] = 1-sets, ect
#print(len_r_subsets_Pn[0])

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
print("The disjoint unions pairs of", nset,"are: \n",djpair, "\n")

### Attempt 1 at counting functions #######################
#A full dictionary of values will be called a function: we wish to count those.

#example seed material, for nset=[1,2,3].

# func_s1([i])=0: create dictionary for 1-sets with values.
OneSets0= len_r_subsets_Pn[0]
#print(OneSets0)
dictempty={}
for i in OneSets0:
    dictempty[tuple(i)]=0
#Dictionaries store: string,number or tuple as keys and value can be anything.
#must change list to tuple before storage.
dict1=dictempty
print("The initial f([i])=0 data is stored as:\n",dict1,"\n")

############# need a choice of base values for 2 -sets. e.g ##########################
#Finished given any choice of 2-sets outputs dictionary ready for use with MSA functions.

TwoSets= len_r_subsets_Pn[1]
def ts_function0(twoset): #assigns a choice of 2sets the value 1.
    return {tuple(twoset):0}
def ts_function1(twoset): #assigns a choice of 2sets the value 1.
    return {tuple(twoset):1}
#could split up TwoSets with those i assign 0 and those i assign 1. Will
#need to alter defs above

#Later permutate through all choices. of assignments of 0 or 1 for 2sets.

ts_power = get_subsets(TwoSets) # all configuration of assigning twoset 1
print("The power set of two-sets is: \n",ts_power,"\n This is useful in assigning values to 2-sets. \n")
for i in range(1,len(ts_power)):#removed [].
#for each choice apply ts_function1 and assign rest ts_function0
    for k in ts_power[i]:
        # for all elements in ts_power[i] append ts_function1(element) to dict1.
        var= ts_function1(k)
        dict1=dict1|var
    TwoSets_minus = [e for e in TwoSets if e not in ts_power[i]]
    for j in TwoSets_minus:
      # print(j)
        item = ts_function0(j)
        dict1 = dict1 | item
   #USEFUL  print("Initial choice for 2-set values setting",ts_power[i],"value 1 and the other 2-sets value 0   \n",dict1,"\n")
    # for all element in TwoSet setminus ts_power[i] append ts_function(element) to above dictionary

def seed_function(element):
    dictempty = {}
    for i in OneSets0:
        dictempty[tuple(i)] = 0
    dict1 = dictempty
    for k in element:
        # for all elements in ts_power[i] append ts_function1(element) to dict1.
        var= ts_function1(k)
        dict1=dict1|var
    TwoSets_minus = [e for e in TwoSets if e not in element]
    for j in TwoSets_minus:
        # print(j)
        item = ts_function0(j)
        dict1 = dict1 | item
        return dict1

#make choice of starting valuese.g [[1, 2], [1, 3]]

seed=seed_function([[1, 2], [1, 3]])
print("We write a given choice of 2-set values for example as: \n",seed)
############################################################################################


########## Define MSA function condition ##########


# p1 = djpair[0] #  test: set p as first djpair

#def djpair_funcval_0(element): #outputs possible disjoint pair values. Specific to djpair.
#     element[0],element[1] #call value of each I,J from most uptodate dictionary
# element[0] + element[1] # next will do element[0] + element[1] +1 with OR condition.
#either def another function that increments or have in one function.
#There will be work on comparing dictionaries.
#print(djpair_funcval_0(p1))


# # def msa2_function(element): #Checking function for all djpairs.For subset I irrespective of decomp.

