import scipy
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys
import pickle

#Main goal: To extend the functions in the P_3 case to the P_4 case and output an excel doc to analyse.

start_time = time.time() #checks run time.

#load in the data

fun2_1={(1,):0,(2,):0,(1,2):0}
fun2_2={(1,):0,(2,):0,(1,2):1}

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

P_2=[fun2_1,fun2_2]
P_3= [fun3_1, fun3_2,fun3_3,fun3_4,fun3_5,fun3_6,fun3_7,fun3_8,fun3_9,fun3_10]

#Put P_3 into into database using pandas

# data=pd.DataFrame.from_dict(P_3,orient="columns")

#We aim to put P_4 into a database

#Preamble

#Next we fix the columns of the database and remove length 1 columns as they are unnecessary as value always 0.

n=3 #dimension of the space we want to extend
n_1=4 # dimension of the space we want.
nset=list(range(1,n+1))
n_1set=list(range(1,n_1+1))
def get_subsets(fullset): # this is used to output the powerset.
    listrep = list(fullset)
    subsets = []
    for i in range(2**len(listrep)):
        subset = []
        for k in range(len(listrep)):
            if i & 1<<k:
                subset.append(listrep[k])
        subsets.append(subset)
    return subsets

def diff(first, second): #This outputs the set difference.
    second = set(second)
    return [item for item in first if item not in second]

Pn = get_subsets(set(nset)) #Powerset of n=3
Pn_1=get_subsets(set(n_1set)) #Powerset of n=4.

Pn.sort(key=len) # Here we sort by length

#We remove length 1 subsets for the database at the end
sub=[i for i in Pn if len(i)<2]
sub_1=[i for i in Pn_1 if len(i)<2]
Pn_tup_db=[tuple(item)  for item in Pn if item not in sub] #removing length 1 subsets for the columns in final database.
Pn_1_tup_db=[tuple(item)  for item in Pn_1 if item not in sub_1] #similar

#Our functions with be in dictionary format, I chose to put elements of the powerset into tuples as they are immutable unlike sets.
Pn_1_tup = [tuple(j) for j in Pn_1] # We did not remove the length 1 subsets here (kept for completeness we remove at end).
Pn_1_tup.remove(()) #We remove the empty tuple.
# print(Pn_1_tup)

# data2 = pd.DataFrame(data,columns=Pn_tup_db) # power set minus empty and length 1 sets, tunred to tuples
# print(data2)

#To move from P_3 function to a P_4 one we need to add new single {key:value} pairs for each element in P4 not in P3.
Pn.remove([])
Pn_tup = [tuple(i) for i in Pn]
blank = diff(Pn_1_tup,Pn_tup)
# print(blank) #used to extnd Pn functions with {key: 0}

#End of Preamble

#We now construct a list of dictionaries. This will be our P_4.

extensions = []
for x in P_3: #We determine the extentions for each function.
    copy_no_extension=x.copy() # to get the complement of the extension from keys
    # print(copy_no_extension)

    #First we create the directed graph associated to the function x.
    #We now build the graph mentioned in MSA-Musings theory by Jon Woolf.

    g=nx.DiGraph()
    g.add_nodes_from(Pn_tup)
    green_edges = []
    red_edges = []
    #We now add the red and green edges to the graph.
    for i in Pn:
        for j in Pn:
            complement= diff(j,i) # may be empty
            if complement ==[]:
                continue
            elif set(i)==set(i).issubset(set(j)):
                continue
            elif set(i).issubset(set(j)):
                # add green  list
                if x[tuple(j)]==x[tuple(i)] + x[tuple(complement)]:
                    green_edges.append((tuple(i),tuple(j)))
                #add red list.
                elif x[tuple(j)] == x[tuple(i)] + x[tuple(complement)] +1:
                    red_edges.append((tuple(j),tuple(i))) # I swapped the order here to account for downward closed.
                    #given this swapped order wecan use a graph traversal to determine epsilon^-1 as mentioned in MSA Musings.
    g.add_edges_from(green_edges)
    g.add_edges_from(red_edges)
    #we can plot and compare these to Jons diagrams. I checked they output the same.
    # nx.draw_networkx(g, with_labels=True)
    # plt.show()

    #We now create the epsilon list
    # i) starting with paths from a specific node
    #ii) Then taking combinations of paths from a specific node in i).

    #i)
    epsilon= []# this will look like [[(1,2)],[(1,),(1,2),(1,2,3)]]
    for i in Pn_tup:#For each node we see where we can walk to along edges.
        tree= nx.depth_first_search.dfs_tree(g,i)
        epsilon.append(list(tree.nodes))
    # print(epsilon,"\n")

    #ii) we now take combinations of paths for all nodes created in i). This is what takes the most time.
    set_epsilon = set([frozenset(i) for i in epsilon]) #remove duplicates.
    Back_to_list_epsilon = [list(i) for i in set_epsilon]
    # print(Back_to_list_epsilon,"\n")

    #If these paths from distinct nodes are different we wish to take the union and add them to epsilon which changes Back_to_list_epsilon above effecting the for loop below.
    #We limit this to total length of the node set.
    #We are pridomantley working with epsilon here and aim to remove duplicates.

    for j in Back_to_list_epsilon:
        epsilon_minus=Back_to_list_epsilon.copy()
        epsilon_minus.remove(j) #We dont want combinations with itself.
        # print("This is epsilion minus j",epsilon_minus)
        if j in epsilon_minus: #incase there are multiple.
            continue
        if len(j)==len(Pn)-1: # if full length of nodes we want to skip.
            continue
        elif len(j)!=len(Pn)-1:
            # print(j)
            T = j
            T = [list(i) for i in T] #change tuples to lists.
            for S in epsilon: #Want to compare two terms in Back_to_list_epsilon and epsilon.
                S = [list(i) for i in S]
                if S == T: #if the combination already lives in epsilon want to skip.
                    continue
                elif len(S) == len(Pn) - 1:  # there wont be anything larger than pn-1
                    continue
                elif S != T and len(S) < len(Pn) - 1:
                    unionST = T + S
                    res_unionST_0 = [i for n, i in enumerate(unionST) if i not in unionST[:n]] #removes duplicates.
                    res_unionST = [tuple(i) for i in res_unionST_0]
                    if res_unionST not in epsilon: #If the term is new to epsilon we add it into  epsilon.
                        # print("The term being appended to epsilon is:",res_unionST)
                        epsilon.append(res_unionST)
                        # print("The set of epsilon with new term added is:",Back_to_list_epsilon) #with new added term.

#We now have our extentions of P_4: We remove any duplicates again and add the empty and Everything epsilon extensions see MSA-Musings.

    epsilon_set = [set(i) for n, i in enumerate(epsilon) if i not in epsilon[:n]]
    l_empty_tup=[tuple([])] # Here i am adding the empyty epsilon extension condition.
    epsilon_set.append(l_empty_tup)
    epsilon_set.append(x.keys()) # Adding in length EVERYTHING extension.As for fun3_3,fun3_4 & fun3_5 do not have full length extension (See Missing_functions.txt)
    epsilon_no_rep = [list(i) for n, i in enumerate(epsilon_set) if i not in epsilon_set[:n]]

#Using these epsilon extensions we create the new functions of P_4 for each element of P_3.
#We use the blank to from the premable to get a blank extension e.g fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1} to get fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1, (4,):0, (1,4):0,(2,4):0...(124):0,...(1234):0}}
#take Pn+1 and add in key :value pairs where key has been extended to n+1.
    for i in blank:
        x[i]= 0

#We now add the values into the blank extentions corresponding to the extentions in epsilon_no_rep.
    #Todo: Given epsilon list extend current function. At end add to empty list
    extensions_epsilon = [] # After add the contents of this list to P_4.#Done: is [x] neccesary?: No see P_4 t P_3 sheet.
    for l_tup in epsilon_no_rep:
        copyx = x.copy()  # may change x # Copy of current function with added keys for changing.
        #We treat the empty eplsion separatly.
        if l_tup ==[()]: # Treating the empty extension seperately.
            for i in [j for j in copy_no_extension.keys()]:  #Does extension by 0 part #See begining for details on copy_no_extension
                copyx[i + (n + 1,)] = copyx[i]
            # print(copyx)
        else:
            for tup in l_tup:
                if () in l_tup:
                    continue
                else:
                    extra_element=tup +(n+1,) # Moving from (1,3) to (1,3,4) adding in extra element.
                    # print(extra_element)
                    copyx[extra_element]=copyx[tup]+1 #Adding one to the cases where we have eplsion {(1,3):0} -> {(1,3):1}
                    for i in [j for j in copy_no_extension.keys() if j not in l_tup]:#See begining for details on copy_no_extension #Fixme: dont want to add blanks in here
                        copyx[i + (n+1,)]=copyx[i] #Adding zero to the case where we dont have epsilon. ie retaining the value {(1,3):0} -> {(1,3):0}
        extensions_epsilon.append(copyx)
    extensions.extend(extensions_epsilon)
    # print(extensions_epsilon)
    # print(len(extensions_epsilon))
    print(P_3.index(x)) #print the function that has been done.
# print(extensions)

#Output: We build database, save to file and save P_4_extentions to be loaded in later.

# todo:pending: sort the order of dictionaryies for database.
data_ext=pd.DataFrame.from_dict(extensions,orient="columns")
data_ext_minus = pd.DataFrame(data_ext,columns=Pn_1_tup_db) # power set minus empty and length 1 sets, tunred to tuples
print(data_ext_minus)
data_ext_minus.to_excel(r'C:\Users\RhysL\PycharmProjects\Combinatorics2021\Epsilon_Extensions_P_4.xlsx', index = False)

print("--- %s seconds ---" % (time.time() - start_time)) #prints timer.
# print(extensions)

#We save the data so we dont have to run this file again:
pickle_out = open("P_4_extentions", "wb")
pickle.dump(extensions, pickle_out)
pickle_out.close()
