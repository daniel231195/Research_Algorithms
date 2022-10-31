# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import doctest
import operator
import sys
import queue



def f(x: int, y: float, z):
    return x + y + z


def safe_call(f, **kwargs):
    """
     First, we will check and save what type of arguments are in the function,
    then we will go through each argument we received and check if they match,
     if not we will check that they are not in the function to which we sent
     the arguments if so we will throw an error because the type does not match
    :param f: function
    :param kwargs: argument with name
    :return: the ans from f
    """
    """
        >>> safe_call(f, x=5, y=7.0, z=3)
        15.0
        >>> safe_call(f, x=5.0, y=7.0, z=3)
        Traceback (most recent call last):
            ...
        Exception: raises an exception
        >>> safe_call(f, x="a", y=7.0, z=3)
        Traceback (most recent call last):
            ...
        Exception: raises an exception
        >>> safe_call(f, x=5, y=7.0, z=3.0)
        15.0
    """
    try:
        annotations = f.__annotations__
        for key in kwargs:
            if key in annotations and type(kwargs[key]) is annotations[key]:
                1
            elif key in annotations:
                raise Exception("raises an exception")
        return f(**kwargs)
    except:
        raise Exception("raises an exception")


"""
    Question number 2
    
    Neighbors function as you showed in the example,
    Implementing breadth-first search using pseudocode from Wikipedia.
    After finding the final vertex it is sent to the route finding function using a dictionary 
    which saves the next vertex. 
    Finally in the track function I go through the entire track from end to start and then put it in the list.
"""


def four_neighbor_function(node: any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]


def breadth_first_search(start=(-1, -1), end=(2, 1), neighbor_function=four_neighbor_function):
    """
        >>> breadth_first_search()
        [(-1, -1), (0, -1), (1, -1), (2, -1), (2, 0), (2, 1)]
        >>> breadth_first_search(start=(0,0),end=(2,2))
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
        >>> breadth_first_search(start=(0,-2),end=(2,3))
        [(0, -2), (1, -2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (2, 3)]
        >>> breadth_first_search(start=(-2,-2),end=(4,4))
        [(-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), (3, -2), (4, -2), (4, -1), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        >>> breadth_first_search(start=(0,0),end=(10,10))
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
    """
    prev = {}
    q = []
    q.append(start)
    visited = [start]
    while q:
        currentNode = q.pop(0)
        lst = neighbor_function(currentNode)
        if currentNode == end:
            return get_path(prev, start, end)
        for i in lst:
            if i not in visited:
                visited.append(i)
                q.append(i)
                prev[i] = currentNode


def get_path(path, start, end):
    lst_path = []
    lst_path.append(end)
    current = path[end]
    while current != start:
        lst_path.append(current)
        current = path[current]
    lst_path.append(start)
    new_lst = []
    for i in reversed(lst_path):
        new_lst.append(i)
    return new_lst


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
    list1 = [[8, 5], {0, 8, 9, 7, 5, 9}, 1, (3, 8, 2)]
    print(print_sorted(list1))
    list2 = [['c', 'b'], 't', ('m', 'f', 'a')]
    print(print_sorted(list2))
    list3 = [8, 5, 0, {"b": 2, "a": 1}]
    print(print_sorted(list3))
    print_sorted(list3)
    print(print_sorted(
        {"a": 5, "c": (8, 9, 5, 6, 1, 7, 3), "b": {1, 3, 2, 4}, "z": {"b": 2, "a": 1}, "d": {5, 8, 3, 7, 1},
         "e": [1, 9, 6, 4]}))
    print(breadth_first_search())
    print(safe_call(f, x=5, y=7.0, z=3))
