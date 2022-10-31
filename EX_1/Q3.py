import doctest

"""
    Question number 3
"""


def sort_dict(x):
    """
     Function for order dict with inner dict ,
    for example {"a":5 , "z": {"b": 2, "a": 1}}
    :param x:
    :return:
    """
    dict1 = sorted(x.items())
    newDict = {}
    for i in dict1:
        if isinstance(i[1], dict):
            sort_dict(i[1])
        else:
            newDict[i[0]] = i[1]
    return newDict


def sortByFirst(val):
    """
    function for getting the first index in a list or tuple
    for order list by the first index.
    :param val: is data struct
    :return: the first variable of data struct for order
    """
    if type(val) is int:
        return val
    if type(val) is dict:
        for i in val:
            return val[i]
    else:
        lst = sorted(val)
        return lst[0]


def sortListAndTuple(lst):
    """
    This function order list or tuple with an inner list or tuple,
    with the same kind of type, list for example [2,8,[5,9]]
    :param lst: lst is tuple or list with sub list or tuple
    :return: order of this struct
    """
    newLst = []
    for i in lst:
        typeI = type(i)
        if not typeI is int and not dict:
            newLst.append(sorted(i))
        elif type(i) is dict:
            newLst.append(sort_dict(i))
        elif type(i) is list or type(i) is tuple:
            newLst.append(sorted(i))
        else:
            newLst.append(i)
    newLst.sort(key=sortByFirst)
    return newLst


def print_sorted(x):
    """
    This function get a deep struct of data and does deep sort
    for all levels of struct
    :param x: is deep data struct
    :return:  order of data struct
    """
    """
           >>> print_sorted(x=[[8, 5], {0, 8, 9, 7, 5, 9}, 1, (3, 8, 2)])
           [{0, 5, 7, 8, 9}, 1, [2, 3, 8], [5, 8]]
           >>> print_sorted(x=[['c', 'b'], 't', ('m', 'f', 'a')])
           [['a', 'f', 'm'], ['b', 'c'], 't']
           >>> print_sorted(x=[8, 5, 0, {"b": 2, "a": 1}])
           [0, {'a': 1, 'b': 2}, 5, 8]
           >>> print_sorted(x={"a": 5, "c": (8, 9, 5, 6, 1, 7, 3), "b": {1, 3, 2, 4}, "z": {"b": 2, "a": 1}, "d": {5, 8, 3, 7, 1},
         "e": [1, 9, 6, 4]})))
           {'a': 5, 'b': [1, 2, 3, 4], 'c': [1, 3, 5, 6, 7, 8, 9], 'd': [1, 3, 5, 7, 8], 'e': [1, 4, 6, 9], 'z': {'a': 1, 'b': 2}}
           >>>print_sorted(x=[8, 5, 0])
           [0,5,8]
       """
    if type(x) is dict:
        dict1 = sorted(x.items())
        newDict = {}
        for i in dict1:  # move on all variable of data struct
            if type(i[1]) is int:
                newDict[i[0]] = i[1]
            else:
                if type(i[1]) is dict:
                    y = sort_dict(i[1])
                    newDict[i[0]] = y
                else:
                    b = sorted(i[1])
                    newDict[i[0]] = b
        return newDict
    elif type(x) is list or type(x) is tuple:
        return sortListAndTuple(x)



if __name__ == '__main__':
    doctest.testmod()
    print("\n------------Q 3 ----------------- \n")
    list1 = [[8, 5], {0, 8, 9, 7, 5, 9}, 1, (3, 8, 2)]
    print(" data 1 : ",list1)
    print(" ans 1 is :",print_sorted(list1),"\n")
    list2 = [['c', 'b'], 't', ('m', 'f', 'a')]
    print(" data 2 : ",list2)
    print(" ans 2 is : ",print_sorted(list2),"\n")
    list3 = [8, 5, 0, {"b": 2, "a": 1}]
    print(" data 3 : " , list3)
    print(" ans 3 is : ",print_sorted(list3),"\n")
    list4={"a": 5, "c": (8, 9, 5, 6, 1, 7, 3), "b": {1, 3, 2, 4}, "z": {"b": 2, "a": 1}, "d": {5, 8, 3, 7, 1},
         "e": [1, 9, 6, 4]}
    print(" data 4 : " , list4)
    print(" ans 4 is : ",print_sorted(list4))