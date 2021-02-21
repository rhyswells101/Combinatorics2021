from sympy.combinatorics import Permutation
from sympy.core import Basic
from sympy.combinatorics.polyhedron import Polyhedron
from sympy.combinatorics.perm_groups import PermutationGroup
import sympy as sym
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics.named_groups import CyclicGroup
from sympy.combinatorics.permutations import Perm, Cycle
import pickle
import itertools
import time
import pandas as pd

start_time = time.time()


#Load in required data from Epsilon_P_4.py for database construction.Want Pn_1_tup_db
n=3
n_1=4
nset=list(range(1,n+1))
n_1set=list(range(1,n_1+1))
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

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

Pn = get_subsets(set(nset))
Pn_1=get_subsets(set(n_1set))

Pn.sort(key=len)

sub=[i for i in Pn if len(i)<2]
sub_1=[i for i in Pn_1 if len(i)<2]
Pn_tup_db=[tuple(item)  for item in Pn if item not in sub]
Pn_1_tup_db=[tuple(item)  for item in Pn_1 if item not in sub_1]
Pn_1_tup_db.append("S_n orbit index")
# print(Pn_1_tup_db)

Pn_1_tup = [tuple(j) for j in Pn_1]
Pn_1_tup.remove(())
# print(Pn_1_tup)

pickle_in = open("../P_n_Epsilon/P_4_extentions", "rb")
P_4_extentions = pickle.load(pickle_in)
P_4=P_4_extentions

# pickle_in = open("P_5_extentions","rb")
# P_5_extentions = pickle.load(pickle_in)
# P_5=P_5_extentions

G = SymmetricGroup(4)
# print(G.order())
perm_4 = list(G.generate_schreier_sims(af=True))
# print(list(G.generate_schreier_sims(af=True)),"\n")


all_distinct_orbits_set=set()
for fun_var in P_4:
    #will need to cut up these wrt the number of each sets of length.
    q_1_sets=[]
    q_2_sets=[]
    q_3_sets=[]
    q_4_sets=[]
    # q_5_sets=[]
    for i in fun_var.items():
        # print(i[0])
        # print(i[0][0])
        if len(i[0])==1:
            for tup in perm_4:
                q = Permutation(tup)  # same as (2,3,1)
                tup_test = i[0]
                x = q(tup_test[0] - 1) #need to change into permuattion mode then do perm
                q_1_sets.append({tuple(sorted((x + 1,))):i[1] }) #need to change back to tuple in fucntino with +1. # this will give long line of permutations as in book!!!.
        elif len(i[0])==2:
            for tup in perm_4:
                q = Permutation(tup)  # same as (2,3,1)
                tup_test = i[0]
                x = q(tup_test[0] - 1)
                y = q(tup_test[1] - 1)
                q_2_sets.append({tuple(sorted((x+1,y+1))):i[1]})
        elif len(i[0])==3:
            for tup in perm_4:
                q = Permutation(tup)  # same as (2,3,1)
                tup_test = i[0]
                x = q(tup_test[0] - 1)
                y = q(tup_test[1] - 1)
                z = q(tup_test[2] - 1)
                q_3_sets.append({tuple(sorted((x+1,y+1,z+1))):i[1]})
        elif len(i[0])==4:
            for tup in perm_4:
                q = Permutation(tup)  # same as (2,3,1)
                tup_test = i[0]
                x = q(tup_test[0] - 1)
                y = q(tup_test[1] - 1)
                z = q(tup_test[2] - 1)
                w = q(tup_test[3] - 1)
                q_4_sets.append({tuple(sorted((x+1,y+1,z+1,w+1))):i[1]})
        # elif len(i[0])==5:
        #     for tup in perm_4:
        #         q = Permutation(tup)  # same as (2,3,1)
        #     tup_test = i[0]
        #     x = q(tup_test[0] - 1)
        #     y = q(tup_test[1] - 1)
        #     z = q(tup_test[2] - 1)
        #     w = q(tup_test[3] - 1)
        #     a = q(tup_test[4] - 1)
        #     q_5_sets.append({tuple(sorted((x+1,y+1,z+1,w+1,a+1))):i[1]})

    # print("The length of q_1_sets is:",len(q_1_sets))
    # print("The length of q_2_sets is:",len(q_2_sets))
    # print("The length of q_3_sets is:",len(q_3_sets))
    # print("The length of q_4_sets is:",len(q_4_sets))
    # print("The length of q_5_sets is:",len(q_5_sets))

    col1=q_1_sets[slice(24)]
    col2=q_1_sets[slice(24,48)]
    col3=q_1_sets[slice(48,72)]
    col4=q_1_sets[slice(72,96)]

    col5=q_2_sets[slice(24)]
    col6=q_2_sets[slice(24,48)]
    col7=q_2_sets[slice(48,72)]
    col8=q_2_sets[slice(72,96)]
    col9=q_2_sets[slice(96,120)]
    col10=q_2_sets[slice(120,144)]

    col11=q_3_sets[slice(24)]
    col12=q_3_sets[slice(24,48)]
    col13=q_3_sets[slice(48,72)]
    col14=q_3_sets[slice(72,96)]

    col15=q_4_sets[slice(24)]

    set_orbit=set()

    for i in range(G.order()): #check range
        l_keypairs_i=[col1[i],col2[i],col3[i],col4[i],col5[i],col6[i],col7[i],col8[i],col9[i],col10[i],col11[i],col12[i],col13[i],col14[i],col15[i]]
        dict1={}
        # make sure keys are in the right order here
        for i in l_keypairs_i:
            dict1=dict1|i
            #reorder dictionary
            # print(dict1)
        for key in fun_var.keys():
            dict1[key] = dict1.pop(key)
        set_orbit.add(tuple(dict1.items())) # to remove multiples.

    #testing to see if leaving dictionary in tuple format can get number of orbits.
    # orbit_fun=[]
    # for tup in set_orbit:
    #     funct = dict(tup)
    #     orbit_fun.append(funct)

    # print(set_orbit,"\n")
    all_distinct_orbits_set.add(frozenset(set_orbit))
    # all_distinct_orbits_list.append(frozenset(set_orbit))

# print(all_distinct_orbits_set)
print(len(all_distinct_orbits_set))
# print(len(all_distinct_orbits_list))

print("--- %s seconds ---" % (time.time() - start_time))



#Want to add a terms to distinguish S_n orbits similar to characteristic orbits.

orbit_fun=[]
for counter,tup in enumerate(all_distinct_orbits_set,1):
    l_tup=list(tup)
    empty=[]
    # print(l_tup)
    for i in l_tup:
        dict_a=dict(i) # This is used to change tuples of functions back to dictionaries.
        x={"S_n orbit index": int(counter)}
        dict_a=dict_a|x
        empty.append(dict_a)
    orbit_fun.append(empty)
# print(orbit_fun,"\n")
flattened_orbits  = [val for sublist in orbit_fun for val in sublist]
# print(flattened_orbits,"\n")

#Final output
# print(all_distinct_orbits_set,"\n")
print(len(all_distinct_orbits_set)) #the number of S_n orbits.

#Want to put into database and then excel. In order to track labels on S_n orbits. Want to investigate when a characterisitc is made of multiple S_n orbits.


data_ext=pd.DataFrame.from_dict(flattened_orbits,orient="columns")
#Todo: Add in S_n orbit index term to  Pn_1_tup_db
data_ext_minus = pd.DataFrame(data_ext,columns=Pn_1_tup_db) # power set minus empty and length 1 sets, tunred to tuples
print(data_ext_minus)
data_ext_minus.to_excel(r'C:\Users\RhysL\PycharmProjects\Combinatorics2021\Group_Action_P_4_Database.xlsx', index = False)



