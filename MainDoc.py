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

n=4
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

#########  Finished: Objective Def function that: This states the subsets of length r #######################################################################################################
empty3=[]
for j in range(1,len(nset)):
    empty = []
    for i in iter.distinct_combinations((nset),j):
        empty.append(i)
    empty = [list(k) for k in empty ]#list tuple. #change eah tuple to list.Done
   # print("The",j,"-sets of", nset,"are: \n",empty, "\n") # Toggle this to print all k subsets of n.
    empty3.extend([empty]) #extend adds th elements not the list as append does.
empty3.append([nset])
len_r_subsets_Pn = empty3
#print("Reordering Pn by length and removing [] returns: \n", len_r_subsets_Pn, "\n") # Toggle this to see full reordered by length pn.
# Here len_r_subsets_Pn[0] = 1-sets, ect
#print(len_r_subsets_Pn[0])


def ksubsets(integer,n):
    nset = list(range(1, n + 1))
    empty3 = []
    for j in range(1, len(nset)):
        empty = []
        for i in iter.distinct_combinations((nset), j):
            empty.append(i)
        empty = [list(k) for k in empty]  # list tuple. #change eah tuple to list.Done
        empty3.extend([empty])  # extend adds th elements not the list as append does.
    empty3.append([nset])
    len_r_subsets_Pn = empty3
    return len_r_subsets_Pn[integer-1]

print("I have defined a function that give k subsets of Pn .E.g:\n",ksubsets(2,5),"\n")

#########: Finished: Obj: to give a list of all disjoint unions combination of nset ##############################################################################

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


############# Finished: Give a function that lists of all disjoint unions combination for each x in Pn #############################################################
#TODO Fix this !! :Why is nset apearing ?
def djpair_combin_function(item):
    # Driver code
    l_st_item = [str(i) for i in item]
    st_item_space = (listToString(l_st_item))
    st_item = st_item_space.replace(' ', '')
    #print(st_item) # do to here fine
#TODO Find up to here
    iterable = st_item  # string version of nset
    empty2 = []
    for part in set_partitions(iterable, 2): # possilbe issue here
        s1 = ''
        x = ([s1.join(p) for p in part])  # How do store this
        # Convert string element back to list e.g [[1],[2,3,4]]
        # want to put these into list. currently in form x=['1', '2345']
        print(x)
        y = [list((word)) for word in x]
        # print(y)
        empty2.append([[int(i) for i in j] for j in y])  # want to store all and put all into list.
        djpair = empty2
    return djpair

print("I have defined a function that outputs: all disjoint pairs, for input: of form [2,3,4,7]. E.g \n", djpair_combin_function([2,3,4,7]) )

#u= djpair_combin_function([1,2,3,4,5])
#print(u)

############# need a choice of base values for 2 -sets. e.g ########################################################################################################
#Finished: given any choice of 2-sets outputs dictionary ready for use with MSA functions.

OneSets0= len_r_subsets_Pn[0]
dictempty={}
for i in OneSets0:
    dictempty[tuple(i)]=0#Dictionaries store: string,number or tuple as keys and value can be anything #must change list to tuple before storage.
dict1=dictempty
#print("The initial f([i])=0 data is stored as:\n",dict1,"\n")

TwoSets= len_r_subsets_Pn[1]
def ts_function0(twoset): #assigns a choice of 2sets the value 1.
    return {tuple(twoset):0}
def ts_function1(twoset): #assigns a choice of 2sets the value 1.
    return {tuple(twoset):1}

#Now : permutate through all choices. of assignments of 0 or 1 for 2sets.
ts_power = get_subsets(TwoSets) # all configuration of assigning twoset 1
#print("The power set of two-sets is: \n",ts_power,"\n This is useful in assigning values to 2-sets. \n")

# print("Initial choice for 2-set values setting setting value 1 for choosen and the other 2-sets values 0")
# zero_assignment = ts_power[0]
# for j in TwoSets:
#     item = ts_function0(j)
#     dict1 = dict1 | item
# #print(dict1) # Toggle this to see all 0 2-set choice.
# # for all element in TwoSet setminus ts_power[i] append ts_function(element) to above dictionary
#
# for i in range(1,len(ts_power)):#removed [] #for each choice apply ts_function1 and assign rest ts_function0
#     for k in ts_power[i]:# for all elements in ts_power[i] append ts_function1(element) to dict1.
#         var= ts_function1(k)
#         dict1=dict1|var
#     TwoSets_minus = [e for e in TwoSets if e not in ts_power[i]]
#     for j in TwoSets_minus:
#         item = ts_function0(j)
#         dict1 = dict1 | item
#    # print(dict1) #Toggle this to see all starts of functions for 2-set choice # for all element in TwoSet setminus ts_power[i] append ts_function(element) to above dictionary

def seed_function(element):
    dictempty = {}
    for i in OneSets0:
        dictempty[tuple(i)] = 0
    dict1 = dictempty

    if element == []:
        for k in TwoSets:
            var= ts_function0(k)
            dict1=dict1|var
        return dict1
    else:
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
# input is choice of 2-sets e.g [[1,2],[2,4]].

#EXAMPLE:
seed1 = seed_function([[1, 2], [1, 3]])
print("Example: We write a given choice of 2-set values for example as: \n",seed1,"\n")
#print("We write a given choice of 2-set values for example as: \n",seed_function([]))


########## Define MSA function condition ########################################################################################################################################


print("\n \n \n Current")
#moving vertically
x= [[1,2]] #for i in ts_power: for seed function need to be inside [,] i,e [[1,2]]
seed = seed_function(x)    # take seed = seed_function(i)
print(seed)    # try and generate dictionary fully
    # if has all keys then store, otherwise move onto the next i. Store in list.
    #iterate through Pn (use AddDict) and use  djpair_combin_function() for subsets for 3-sets, 4-sets...


#Moving horizonatlly.
#def Add_Single_Dict(set): # input elements of Pn
dictempty = {} # wanting to have {[1,2,3]: 1} and more generaly of the form {[1,2,3]: 0,1}
#take for i in  [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]].. def function defining.
w=[1,2,3] # moves through all 3-sets,4-sets..
djCombos= djpair_combin_function(w) # put x as set when defing function
print(djCombos)
    # for j in djCombos:
    #     for k in djCombos[j]:
    #         # for all elements in ts_power[i] append ts_function1(element) to dict1.
    #         var= ts_function1(k)
    #         dict=dictempty|var
    #     TwoSets_minus = [e for e in TwoSets if e not in element]
    #     for j in TwoSets_minus:
    #         # print(j)
    #         item = ts_function0(j)
    #         dict = dict | item
    #     return dict

print("Hopefully this returns a single dictionary of the for {[1,2,3]: 1}\n",AddDict([1,2,3]))
# p1 = djpair[0] #  test: set p as first djpair

#def djpair_funcval_0(element): #outputs possible disjoint pair values. Specific to djpair.
#     element[0],element[1] #call value of each I,J from most uptodate dictionary
# element[0] + element[1] # next will do element[0] + element[1] +1 with OR condition.
#either def another function that increments or have in one function.
#There will be work on comparing dictionaries.
#print(djpair_funcval_0(p1))


# # def msa2_function(element): #Checking function for all djpairs.For subset I irrespective of decomp.

##########: In Progress: Moving vertically : Permuting through seed data #######


#Function = []
