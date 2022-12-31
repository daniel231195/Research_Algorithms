import doctest

import cvxpy as cp

def Nash_budget(total:float, subjects:list, preferences:list[list]):
    """
    :param total:
    :param subjects:
    :param preferences:
    :return:
    >>> a = [['a', 'b'], ['b', 'c'], ['d', 'a'], ['d', 'b'], ['a','c']]
    >>> Nash_budget(1000,['a' , 'b' , 'c' , 'd'], a)
    ["Citizen 0 ,gives 99.99999999999973 to 'a' 100.00000000000027 to 'b' ", "Citizen 1 ,gives 199.9999022170668 to 'b' 9.778293321064433e-05 to 'c' ", "Citizen 2 ,gives 9.778293321066572e-05 to 'd' 199.9999022170668 to 'a' ", "Citizen 3 ,gives 9.778293321066519e-05 to 'd' 199.9999022170668 to 'b' ", "Citizen 4 ,gives 199.9999022170668 to 'a' 9.778293321064486e-05 to 'c' ", '']

    >>> b = [['d','a','c'], ['c','d','a'], ['d', 'a'], ['d', 'b'], ['d']]
    >>> Nash_budget(1000,['a' , 'b' , 'c' , 'd'], a)
    ["Citizen 0 ,gives 99.99999999999973 to 'a' 100.00000000000027 to 'b' ", "Citizen 1 ,gives 199.9999022170668 to 'b' 9.778293321064433e-05 to 'c' ", "Citizen 2 ,gives 9.778293321066572e-05 to 'd' 199.9999022170668 to 'a' ", "Citizen 3 ,gives 9.778293321066519e-05 to 'd' 199.9999022170668 to 'b' ", "Citizen 4 ,gives 199.9999022170668 to 'a' 9.778293321064486e-05 to 'c' ", '']

    >>> c = [['a', 'b','c', 'd'], ['e', 'f'], ['a', 'e'], ['f', 'b'], ['a', 'b','c', 'd','e','f']]
    >>> Nash_budget(1000,['a' , 'b' , 'c' , 'd','e','f'], a)
    ["Citizen 0 ,gives 100.00000000000014 to 'a' 99.99999999999986 to 'b' ", "Citizen 1 ,gives 199.9999895206395 to 'b' 1.0479360512051648e-05 to 'c' ", "Citizen 2 ,gives 1.0479360512054231e-05 to 'd' 199.9999895206395 to 'a' ", "Citizen 3 ,gives 1.047936051205426e-05 to 'd' 199.9999895206395 to 'b' ", "Citizen 4 ,gives 199.9999895206395 to 'a' 1.0479360512051619e-05 to 'c' ", '']

    >>> d = [['a', 'b','f', 'd'], ['e', 'f'], ['a'], ['f'], ['a', 'b','c', 'd','e','f'],['a', 'b','c', 'd','e','f'],['a','c','d'],['a', 'b','c', 'd']]
    >>> Nash_budget(1000,['a' , 'b' , 'c' , 'd','e','f'], a)
    ["Citizen 0 ,gives 100.00000000000014 to 'a' 99.99999999999986 to 'b' ", "Citizen 1 ,gives 199.9999895206395 to 'b' 1.0479360512051648e-05 to 'c' ", "Citizen 2 ,gives 1.0479360512054231e-05 to 'd' 199.9999895206395 to 'a' ", "Citizen 3 ,gives 1.047936051205426e-05 to 'd' 199.9999895206395 to 'b' ", "Citizen 4 ,gives 199.9999895206395 to 'a' 1.0479360512051619e-05 to 'c' ", '']

    """
    variable_subjects = {"var_subj_ " + str(i): cp.Variable() for i in subjects}
    M = cp.Variable()  # this variable care for the maximum
    objective = cp.Maximize(M)
    utilities = []
    for pre in preferences:
        utilities.append(cp.sum([variable_subjects["var_subj_ " + str(j)] for j in pre]))
    constraints = []
    # sum[i] log(u_i(d))
    constraints.append(M <= cp.sum([cp.log(u_i) for u_i in utilities]))
    # variable_subjects[i] ≥ 0
    for v_i in variable_subjects:
        constraints.append(variable_subjects[v_i] >= 0 )
    # total == ∑ variable_subjects[i]
    constraints.append(sum(variable_subjects.values()) == total)
    prob = cp.Problem(objective, constraints)
    result = prob.solve()
    res =""
    for i in range(0,len(preferences)):
        res += f"Citizen {str(i)} ,gives "
        for j in preferences[i]:
            res += f"{variable_subjects['var_subj_ ' + str(j)].value*(total / len(preferences) / utilities[i].value)} to '{j}' "
        res += "\n"
    return res.split('\n')
if __name__ == '__main__':
    doctest.testmod()
    #Nash_budget(500, ['a', 'b', 'c', 'd'], [['a', 'b'], ['b', 'c'], ['d', 'a'], ['d', 'b'], ['a','c']])
