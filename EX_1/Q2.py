import doctest


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




if __name__ == '__main__':
    doctest.testmod()
    print("\n------------Q 2 ----------------- \n")
    print("1) start=(-1,-1) end=(2,1)")
    print("   ans 1 is : ",breadth_first_search(),"\n")
    print("2) start=(1,-2) end=(4,2)")
    print("   ans 2 is : ",breadth_first_search(start=(1,-2),end=(4,2)),"\n")
    print("3) start=(-5,-5) end=(2,1)")
    print("   ans 1 is : ", breadth_first_search(start=(-5,-5),end=(2,1)), "\n")
    print("4) start=(3,-6) end=(4,2)")
    print("   ans 2 is : ", breadth_first_search(start=(3,-6), end=(4, 2)), "\n")