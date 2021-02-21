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
import scipy
import pandas as pd


#Main goal: Give a count for the number of S_n orbits.
#Secondary goal: Testing to see if Phi orbits are made of S_n orbits.
#Comparision of characteristic and S_n orbits will be done of excel document accompanying.

#Load in required data from Epsilon_P_4.py for database construction. Want Pn_1_tup_db for database at the end.
n=2
n_1=3
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
print(Pn_1_tup_db)

Pn_1_tup = [tuple(j) for j in Pn_1]
Pn_1_tup.remove(())
# print(Pn_1_tup)

#Load in P_n data:

fun3_1= {(1,):0,(2,):0,(3,):0, (1,2):0, (1,3):0, (2,3):0, (1,2,3):0}
fun3_2= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):0, (2,3):0, (1,2,3):1}
fun3_3= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):0, (2,3):0, (1,2,3):1}
fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1}
fun3_5= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):0, (2,3):1, (1,2,3):1}
fun3_6= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):1, (2,3):0, (1,2,3):1}
fun3_7= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):1, (1,2,3):1}
fun3_8= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):0, (2,3):1, (1,2,3):1}
fun3_9= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):1, (2,3):1, (1,2,3):1}
fun3_10= {(1,):0,(2,):0,(3,):0,(1,2):1, (1,3):1, (2,3):1, (1,2,3):2}
P_3= [fun3_1, fun3_2,fun3_3,fun3_4,fun3_5,fun3_6,fun3_7,fun3_8,fun3_9,fun3_10]

#Here we write the load in data for the P_4,P_5 cases for later.
# pickle_in = open("P_4_extentions","rb")
# P_4_extentions = pickle.load(pickle_in)
# P_4=P_4_extentions
#
# pickle_in = open("P_5_extentions","rb")
# P_5_extentions = pickle.load(pickle_in)
# P_5=P_5_extentions

#The Group and its elements
G = SymmetricGroup(3)
perm_3 = list(G.generate_schreier_sims(af=True))
# print(list(G.generate_schreier_sims(af=True)),"\n")

#This is how the permutation works on the tuples (1,),(2,),(3,),(1,2),(1,3),(2,3) and (1,2,3)
# q = Permutation([1,2,0]) # same as the permutation (2,3,1)
# tup_test=(2,3) #our test tuple from the function
# x=q(tup_test[0]-1) #changing the first element into the correct format.
# y=q(tup_test[1]-1)
# print(x,y)
# print(x+1,y+1,"\n") # Changing it back to our tuple format. In this case we are donig (2,3,1)(2,3) = (3,1).

#We now consider the orbits of functions in P_3 by S_3.
#Are any orbits the same from differnet function?: Yes: there can be different S_n orbits within the same characterisitic.
# Therefore we use set to remove duplicate orbits from different functions.
all_distinct_orbits_set=set()

for fun_var in P_3:
    q_1_sets=[] #for list of acted of length 1 tuples with values. i.e all permutations of (1,) by S_3 with value of fun_var for (1,), all permutations of (2,)...
    q_2_sets=[] # Similar to above but for length 2 tuples (also called 2-sets) i.e for (1,2)
    q_3_sets=[]# for length 3 tuples: (1,2,3).
    # q_4_sets=[] # not needed yet as for the P_4 case.
    #will need to cut up q_i_sets wrt the number of each set of a given length: This is done as  e.g col2=q_1_sets[slice(6,12)]
    for i in fun_var.items(): #This gives the pair (1,):value ,(2,):value,(3,):value,(1,2):value,(1,3):value,(2,3) :value and (1,2,3):value.
        # print(i[0]) # takes the tuple of the item pair above without value.
        # print(i[0][0]) #gives first item of tuple e.g for (1,2) gives 1.
        if len(i[0])==1: #iterating by length of tuples and appending them to columns q_i_sets.
            for tup in perm_3: # doing the group action.
                q = Permutation(tup)  # permutating
                tup_test = i[0]
                x = q(tup_test[0] - 1) #need to change into permuattion mode then do perm
                # Ordering is an issue later with regards to dictionaries when we aim to remove duplicates. Therefore we sorted the tuples (just the tuples here, e.g (3,1,2) goes to (1,2,3) ) putting the keys in the standard format.
                q_1_sets.append({tuple(sorted((x + 1,))):i[1] }) #need to change back to tuple in fucntion with +1. # this will give a column of permutations for the corresponding tuple.
        elif len(i[0])==2:
            for tup in perm_3:
                q = Permutation(tup)  # same as (2,3,1)
                tup_test = i[0]
                x = q(tup_test[0] - 1)
                y = q(tup_test[1] - 1)
                q_2_sets.append({tuple(sorted((x+1,y+1))):i[1]})
        elif len(i[0])==3:
            for tup in perm_3:
                q = Permutation(tup)  # same as (2,3,1)
                tup_test = i[0]
                x = q(tup_test[0] - 1)
                y = q(tup_test[1] - 1)
                z = q(tup_test[2] - 1)
                q_3_sets.append({tuple(sorted((x+1,y+1,z+1))):i[1]})
        # elif len(i[0])==4:
        #     for tup in perm_3:
            #     q = Permutation(tup)  # same as (2,3,1)
            #     tup_test = i[0]
            #     x = q(tup_test[0] - 1)
            #     y = q(tup_test[1] - 1)
            #     z = q(tup_test[2] - 1)
            #     w = q(tup_test[3] - 1)
            #     q_4_sets.append({tuple(sorted((x+1,y+1,z+1,w+1))):i[1]})


#Here we slice the q_i_sets which hold the acted on tuples with their values.

#The prints are testing data which is usefull in determining the slicing in later cases P_4,P_5.
#This follows the binomial triangle for this: 3,3,1 # n=4 is 4,6,4,1 and for n=5 similar.

    # print(q_1_sets,"\n")

    col1=q_1_sets[slice(6)] # For (1,)
    col2=q_1_sets[slice(6,12)] #For (2,)
    col3=q_1_sets[slice(12,18)] #For (3,)

    # print(q_2_sets,"\n")

    col4=q_2_sets[slice(6)] #For (1,2)
    col5=q_2_sets[slice(6,12)] #For (1,3)
    col6=q_2_sets[slice(12,18)] #For (2,3)

    # print(q_3_sets,"\n")

    col7=q_3_sets #no slicing necessary here # For (1,2,3).

    # print(q_4_sets,"\n") #Not needed yet.


#Here we compile the functions from the columns.
    set_orbit=set()# We again use set to remove duplicates in the orbits of a given function here.

    for i in range(G.order()): #Each colum has order of G elements.
        l_keypairs_i=[col1[i],col2[i],col3[i],col4[i],col5[i],col6[i],col7[i]] # we put {key:Value} into a list before merging.
        dict1={} # Here we build the functions from l_keypairs
    #Here is where we make use of the sorted tuples we did earlier to make sure keys are in the right order.
        for i in l_keypairs_i:
            dict1=dict1|i #take item from list and put into dictionary this is our function.
        for key in fun_var.keys():
            dict1[key] = dict1.pop(key) # Here we put the keys in the right order (1,),(2,),(3,),(1,2),(1,3),(2,3) and (1,2,3).

        # There is no frozen dictionary so we need a work around, we change to tuples.
        set_orbit.add(tuple(dict1.items())) # we add the corresponding tuple to a set to remove multiples.

    #We can leave our new function/dictionary in tuple format to get the number of orbits: Yes this works.

    #This is used to change tuples of functions back to dictionaries.
    # orbit_fun=[]
    # for tup in set_orbit:
    #     funct = dict(tup)
    #     orbit_fun.append(funct)

    # print(set_orbit,"\n")

    #Here We bundled the orbits together in set_orbit, and add to another set at the begining. This removes the cases where we obtained the same orbit for different functions.
    all_distinct_orbits_set.add(frozenset(set_orbit))

#Want to add a terms to distinguish S_n orbits similar to characteristic orbits.
#Also to output xlsx file, need a list of dictionaries from the all_distinct_orbits_set.

orbit_fun=[]
for counter,tup in enumerate(all_distinct_orbits_set,1): #Consider all distinct orbits in tuple form
    l_tup=list(tup)
    empty=[] # we create a list to get of dictionaries all functions so we can output an xlsx file.
    # print(l_tup)
    for i in l_tup:
        dict_a=dict(i) # This is used to change tuples of functions back to dictionaries.
        x={"S_n orbit index": int(counter)} # We add the index term to distinguish orbits.
        dict_a=dict_a|x # add this S_n orbit index
        empty.append(dict_a)
    orbit_fun.append(empty)
# print(orbit_fun,"\n")
flattened_orbits  = [val for sublist in orbit_fun for val in sublist] # turns lists of lists into a single list of elements of those lists.
# print(flattened_orbits,"\n")

#Final output
# print(all_distinct_orbits_set,"\n")
print(len(all_distinct_orbits_set)) #the number of S_n orbits.

#Want to put into database and then excel. In order to track labels on S_n orbits. Want to investigate when a characterisitc is made of multiple S_n orbits.


data_ext=pd.DataFrame.from_dict(flattened_orbits,orient="columns") #database for excel
#Todo: Add in S_n orbit index term to  Pn_1_tup_db
data_ext_minus = pd.DataFrame(data_ext,columns=Pn_1_tup_db) #Remove length 1 columns with power set minus empty and length 1 sets
print(data_ext_minus)
# data_ext_minus.to_excel(r'C:\Users\RhysL\PycharmProjects\Combinatorics2021\Group_Action_P_3_Database.xlsx', index = False)
#This write xlsx file with data.

