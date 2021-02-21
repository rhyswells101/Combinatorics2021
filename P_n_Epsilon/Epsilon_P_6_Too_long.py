import scipy
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys
import pickle
# from Epsilon_Induction import P_4_extensions
start_time = time.time()

pickle_in = open("P_5_extentions", "rb")
P_5_extentions = pickle.load(pickle_in)
# print(len(P_5_extentions))
P_5=P_5_extentions

#Done: Put P_3 into into database pandas

# data=pd.DataFrame.from_dict(P_3,orient="columns")
#Done:Investigate: how to remove length 1 coulumns
n=5
n_1=6
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

Pn_1_tup = [tuple(j) for j in Pn_1]
Pn_1_tup.remove(())
# print(Pn_1_tup)

# data2 = pd.DataFrame(data,columns=Pn_tup_db) # power set minus empty and length 1 sets, tunred to tuples
# print(data2)

Pn.remove([])
Pn_tup = [tuple(i) for i in Pn]
blank = diff(Pn_1_tup,Pn_tup)
# print(blank) #used to extnd Pn functions with {key: 0}



extensions = []
for x in P_5:
    copy_no_extension=x.copy() # to get the complement of the extension from keys
    # print(copy_no_extension)
    #First we create the directed graph associated to the function x.
    # x=fun3_4 #e.g function will put into for loop after (indent  all)
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
                    red_edges.append((tuple(j),tuple(i))) # I swaped the order here. to account for downward closed.
    g.add_edges_from(green_edges)
    g.add_edges_from(red_edges)
    #we can plot and compare these to Jons diagrams.
    # nx.draw_networkx(g, with_labels=True)
    # plt.show()

    #Done: create the epsilon list# Pending on output.
    #Done: check output with Jons diagram: See Epsilon_combinations.py and Epsilon_in_1.txt

    #Second we create the epsilon list. i) starting with paths from a specific node.
    epsilon= []# this will look like [[(1,2)],[(1,),(1,2),(1,2,3)]]
    for i in Pn_tup:#For each node we see where we can walk to along edges.
        tree= nx.depth_first_search.dfs_tree(g,i)
        epsilon.append(list(tree.nodes))
    # print(epsilon,"\n")

    #ii) we now take combinations of paths for all nodes created in i).
    set_epsilon = set([frozenset(i) for i in epsilon])
    Back_to_list_epsilon = [list(i) for i in set_epsilon]
    # print(Back_to_list_epsilon,"\n")

    for j in Back_to_list_epsilon: #back_to_list may be locked in now
        #Todo: Working on to reduce repetitions.
        #
        epsilon_minus=Back_to_list_epsilon.copy()
        epsilon_minus.remove(j)
        # print("This is epsilion minus j",epsilon_minus)
        if j in epsilon_minus:
            continue
        if len(j)==len(Pn)-1:
            continue
        elif len(j)!=len(Pn)-1:
            # print(j)
            T = j
            T = [list(i) for i in T]
            for S in epsilon:
                S = [list(i) for i in S]
                if S == T:
                    continue
                elif len(S) == len(Pn) - 1:  # there wont be anything larger than pn-1
                    continue
                elif S != T and len(S) < len(Pn) - 1:
                    unionST = T + S
                    res_unionST_0 = [i for n, i in enumerate(unionST) if i not in unionST[:n]]
                    res_unionST = [tuple(i) for i in res_unionST_0]
                    if res_unionST not in epsilon:
                        # print("The term being appended to epsilon is:",res_unionST)
                        epsilon.append(res_unionST)
                        # print("The set of epsilon with new term added is:",Back_to_list_epsilon) #with new added term.

    epsilon_set = [set(i) for n, i in enumerate(epsilon) if i not in epsilon[:n]]
    l_empty_tup=[tuple([])] # Here i am adding the empyty epsilon extension condition.
    epsilon_set.append(l_empty_tup)
    epsilon_set.append(x.keys()) # Adding in length EVERYTHING extension.As for fun3_3,fun3_4 & fun3_5 do not have full length extension (See Missing_functions.txt)
    epsilon_no_rep = [list(i) for n, i in enumerate(epsilon_set) if i not in epsilon_set[:n]]



    # nx.draw_networkx(nx.depth_first_search.dfs_tree(g, (1,3)))
    # plt.show()
    #Done: Need a blank extension onto # fun3_4= {(1,):0,(2,):0,(3,):0,(1,2):0, (1,3):1, (2,3):0, (1,2,3):1}
    #take Pn+1 and add in key :value pairs where key has been extended to n+1.
    for i in blank:
        x[i]= 0
    #Todo: Given epsilon list extend current function. At end add to empty list
    extensions_epsilon = [] # After add the contents of this list to P_4.#Done: is [x] neccesary?: No see P_4 t P_3 sheet.
    counter_no_rep=0
    for l_tup in epsilon_no_rep:
        copyx = x.copy()  # may change x # Copy of current function with added keys for changing.
        if l_tup ==[()]: # Treating the empty extension seperately. #Todo:Still worried about if i have added this correctly.
            for i in [j for j in copy_no_extension.keys()]:  #Does extension by 0 part #See begining for details on copy_no_extension #Fixme: dont want to add blanks in here
                copyx[i + (n + 1,)] = copyx[i]
            # print(copyx)
        else:
            for tup in l_tup:
                if () in l_tup:
                    continue
                else:
                    extra_element=tup +(n+1,)
                    # print(extra_element)
                    copyx[extra_element]=copyx[tup]+1 # Need function with blank appended n+1 keys.
                    for i in [j for j in copy_no_extension.keys() if j not in l_tup]:#See begining for details on copy_no_extension #Fixme: dont want to add blanks in here
                        copyx[i + (n+1,)]=copyx[i]
        extensions_epsilon.append(copyx)
    extensions.extend(extensions_epsilon)
    # print(extensions_epsilon)
    # print(len(extensions_epsilon))
    print(P_5.index(x))  # print the function that has been done.
# print("\n","The list of all extentions P_5 is:"extensions,"\n")


# todo:pending: sort the order of dictionaryies for database.
data_ext=pd.DataFrame.from_dict(extensions,orient="columns")
data_ext_minus = pd.DataFrame(data_ext,columns=Pn_1_tup_db) # power set minus empty and length 1 sets, tunred to tuples
print(data_ext_minus)
data_ext_minus.to_excel(r'C:\Users\RhysL\PycharmProjects\Combinatorics2021\Epsilon_Extensions_P_6.xlsx', index = False)
print("--- %s seconds ---" % (time.time() - start_time))
# sys.stdout = open("P_5_extentions","w")
# print(extensions)
# sys.stdout.close()

pickle_out = open("P_6_extentions","wb")
pickle.dump(extensions, pickle_out)
pickle_out.close()
