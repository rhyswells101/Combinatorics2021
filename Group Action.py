from sympy.combinatorics import Permutation
from sympy.combinatorics.polyhedron import Polyhedron
from sympy.combinatorics.perm_groups import PermutationGroup
import sympy as sym
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics.named_groups import CyclicGroup

#Testing to see if Phi orbits are made of S_4 orbits.
x = sym.sqrt(8)
print(x)

f_4= {(1,): 0, (2,): 0, (3,): 0, (4,): 0, (1, 2): 1, (1, 3): 0, (1, 4): 0, (2, 3): 0, (2, 4): 0, (3, 4): 0, (1,2,3): 1, (1,2,4):1 , (2,3,4):0, (1,3,4):0, (1,2,3,4):1}
#todo: need representativites for Phi_2,phi_3,phi_4 orbits (obtained from tilde(P_4) by check on length asssign (phi_2,phi_3,phi_4 ) with enumerate).

f_3= {(1,): 0, (2,): 0, (3,): 0, (1, 2): 1, (1, 3): 0, (2, 3): 0, (1,2,3): 1}

G = SymmetricGroup(4)
print(G.is_group)
print(G.order())
print(list(G.generate_schreier_sims(af=True)))

#todo: figure out action of S_4 elements on keys of function.
#pseudocode

#Fix function f.
#orbit=set()
#for i in s_4
    #fix element of s_4
    #empty = {}
    #consider key k of f
        #if len = 1 append {key:value } to empty
        #else
            #s= take group action of i on key.
            #define acted_on = {s: k[value] in f}
            #append empty| acted_on  # want to build up new function: do list comprehension?/ look at MainDoc.
    #orbit.add(empty)
#print(orbit) # print(empty) #will get repeats.



