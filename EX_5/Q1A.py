import doctest
import itertools


def bounded_subsets(s: list, c: int):
    """
        We get a list, sort it and take out all the big numbers.
         Then go through every possible combination and check if the conditions are ok
    :param s: list start
    :param c: max sum
    :return: print of all combo of list
    >>> bounded_subsets([1, 2, 3], 4)
    [[], [1], [2], [3], [1, 2], [1, 3]]
    >>> bounded_subsets(list(range(50,200)), 65)
    [[], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64]]
    >>> bounded_subsets(list(range(-2,2)), 2)
    [[], [-2], [-1], [0], [1], [-2, -1], [-2, 0], [-2, 1], [-1, 0], [-1, 1], [0, 1], [-2, -1, 0], [-2, -1, 1], [-2, 0, 1], [-1, 0, 1]]
    >>> bounded_subsets(list(range(0,11)), 10)
    [[], [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [3, 4], [3, 5], [3, 6], [3, 7], [4, 5], [4, 6], [0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5], [0, 1, 6], [0, 1, 7], [0, 1, 8], [0, 1, 9], [0, 2, 3], [0, 2, 4], [0, 2, 5], [0, 2, 6], [0, 2, 7], [0, 2, 8], [0, 3, 4], [0, 3, 5], [0, 3, 6], [0, 3, 7], [0, 4, 5], [0, 4, 6], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 3, 4], [1, 3, 5], [1, 3, 6], [1, 4, 5], [2, 3, 4], [2, 3, 5], [0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 2, 5], [0, 1, 2, 6], [0, 1, 2, 7], [0, 1, 3, 4], [0, 1, 3, 5], [0, 1, 3, 6], [0, 1, 4, 5], [0, 2, 3, 4], [0, 2, 3, 5], [1, 2, 3, 4], [0, 1, 2, 3, 4]]
    >>> bounded_subsets(list(range(0,3)), 3)
    [[], [0], [1], [2], [0, 1], [0, 2], [1, 2]]
    """
    s.sort()
    # remover all the biggest number
    while True:
        if s[len(s) - 1] >= c:
            s.pop(len(s) - 1)
        else:
            break
    subset = []
    # move on all range of list
    for i in range(0, len(s)):
        # make combo form list and len i
        for combo in itertools.combinations(s, i):
            if sum(combo) <= c:
               subset.append(list(combo))
    print(subset)

if __name__ == "__main__":
    doctest.testmod()
    print("1) [1, 2, 3], 4  :")
    print("ans 1 is ------> ")
    bounded_subsets([1, 2, 3], 4)
    print("2) range(50,200), 65  :")
    print("ans 2 is ------> ")
    bounded_subsets(list(range(50, 200)), 65)
    print("3) range(-2,2), 2  :")
    print("ans 3 is ------> ")
    bounded_subsets(list(range(-2, 2)), 2)