# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import doctest
import sys
import queue

"""
    Question number 1
    
    First, we will check and save what type of arguments are in the function, 
    then we will go through each argument we received and check if they match,
     if not we will check that they are not in the function to which we sent 
     the arguments if so we will throw an error because the type does not match
    
"""


def f(x: int, y: float, z):
    return x + y + z


def safe_call(f, **kwargs):
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
    dict1 = sorted(x.items())
    newDict = {}
    for i in dict1:
        if isinstance(i[1], dict):
            sort_dict(i[1])
        else:
            newDict[i[0]] = i[1]
    return newDict

def sort_tuple(t):
    lst = str(list(t))
    return

def print_sorted(x):
    if type(x) is dict:
        dict1 = sorted(x.items())
        newDict = {}
        for i in dict1:
            if not type(i[1]) is int:
                if type(i[1]) is dict:
                    y = sort_dict(i[1])
                    newDict[i[0]] = y
                else:
                    b = sorted(i[1])
                    newDict[i[0]] = b
            else:
                newDict[i[0]] = i[1]
        print(newDict)

    # print(x)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #doctest.testmod()
    #print(str(sort_tuple((2,8,6,7,9, (1,5)))))
    #print(sorted(str([1,'a',5,'b'])))

    lst = [4, 6, 1, 7, 9]
    st = str(lst)
    sort_word = ' '.join(sorted(st, key=str.lower))
    print(sort_word)
    #print_sorted({"a": 5, "c": 6, "b": {1, 3, 2, 4}, "z": {"b": 2, "a": 1} , "d":{5,8,3,7,1},"e":[1,9,6,4]})
    # print(breadth_first_search())
    # print(safe_call(f, x=5, y=7.0, z=3))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
