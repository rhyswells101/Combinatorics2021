l_l_tup_example=[[(1,), (1, 2), (1, 3)], [(2,), (1, 2), (2, 3)], [(3,), (1, 3), (2, 3)], [(1, 2)], [(1, 3)], [(2, 3)], [(1, 2, 3), (1,), (1, 2), (1, 3), (2,), (2, 3), (3,)]]
# l_l_tup_example is from fun3_1

#Todo: change to sets and strings to run faster.

for j in epsilon:
    # prelim_epsilon_set_no_rep= [set(i) for n, i in enumerate(epsilon) if i not in epsilon[:n]]
    # l_prelim_epsilon_no_rep = [list(i) for n, i in enumerate(prelim_epsilon_set_no_rep) if i not in prelim_epsilon_set_no_rep[:n]]
    # if j in l_prelim_epsilon_no_rep: #Todo: Working on to reduce repetitions.
    #     continue
    epsilon_minus = epsilon.copy()
    epsilon_minus.remove(j)
    # print("This is epsilion minus j",epsilon_minus)
    if j in epsilon_minus:
        continue
    if len(j) == len(Pn) - 1:
        continue
    elif len(j) != len(Pn) - 1:
        print(j)
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
                    epsilon.append(res_unionST)
epsilon_set = [set(i) for n, i in enumerate(epsilon) if i not in epsilon[:n]]
epsilon_set.append(
    x.keys())  # Adding in length EVERYTHING extension.As for fun3_3,fun3_4 & fun3_5 do not have full length extension (See Missing_functions.txt)
epsilon_set = [set(i) for n, i in enumerate(epsilon_set) if i not in epsilon_set[:n]]
epsilon_no_rep = [list(i) for n, i in enumerate(epsilon_set) if i not in epsilon_set[:n]]
l_empty_tup = [tuple([])]  # Here i am adding the empyty epsilon extension condition.
epsilon_no_rep.append(l_empty_tup)