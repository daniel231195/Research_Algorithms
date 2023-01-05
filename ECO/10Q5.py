import doctest
import statistics
import math


def compute_budget(toal_budget: float, citizen_votes: list[list]) -> list[float]:
    """
    Budget calculation with the help of a generalized median algorithm with linear increasing functions
    :param toal_budget:
    :param citizen_votes:
    :return:
    >>> ex1 =  [[100,0,0],[0,0,100]]
    >>> ex2 =  [[0,0,100],[100,0,0]]
    >>> ex3 =  [[100,100,0,50],[50,0,100,100]]
    >>> ex4 =  [[10,2,4],[2,4,10]]
    >>> compute_budget(100,ex1)
    [50.0, 0, 50.0]
    >>> compute_budget(100,ex2)
    [50.0, 0, 50.0]
    >>> compute_budget(250,ex3)
    [62.5, 62.5, 62.5, 62.5]
    >>> compute_budget(16,ex4)
    [6.0, 4, 6.0]
    """
    return binary_search(0,1,citizen_votes,toal_budget)


def func_voets(size: int, t: float, c: float) -> list:
    return list(c*min(1,i*t) for i in range(1,size))

def median(citizen_votes: list, const_votes: list):
    all_medians = []
    for m in range(len(citizen_votes[0])):
        arr_median= []
        arr_median += const_votes
        arr_median +=[current_vote[m] for current_vote in citizen_votes]
        all_medians.append(statistics.median(arr_median))
    return all_medians

def binary_search(low, high, citizen_votes: list[list],  toal_budget: float):
    if high >= low:
        mid = (high + low) / 2
        all_medians = median(citizen_votes, func_voets(len(citizen_votes), mid, toal_budget))
        sum_medians = sum(all_medians)
        if sum_medians > toal_budget:
            return binary_search(low,mid,citizen_votes,toal_budget)
        elif sum_medians < toal_budget:
            return binary_search(mid,high,citizen_votes,toal_budget)
        else:
            return all_medians
    else:
        return -1


def check_fairness(total_budget: float, citizen_votes: list[list[float]], budget: list[float]) -> bool:
    """

    :param total_budget:
    :param citizen_votes:
    :param budget:
    :return:
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100]]
    >>> citizen_votes2 = [[50, 50, 0], [0, 50, 50]]
    >>> budget = compute_budget(100, citizen_votes)
    >>> budget2 = compute_budget(100, citizen_votes2)
    >>> check_fairness(100,citizen_votes ,budget)
    True
    >>> check_fairness(100,citizen_votes2 ,budget2)
    False
    """
    num_citizens = len(citizen_votes)
    num_items = len(citizen_votes[0])

    # Count the number of citizens supporting each budget item
    support_counts = [0 for _ in range(num_items)]
    for vote in citizen_votes:
        for i, v in enumerate(vote):
            if v > 0:
                support_counts[i] += 1

    # Check if the allocated budget for each item is proportional to the number of citizens supporting it
    for i in range(num_items):
        if budget[i] / total_budget < support_counts[i] / num_citizens:
            return False
    return True




if __name__ == '__main__':
    doctest.testmod()
    # Test compute_budget for a budget with 3 subjects and a country with 10 citizens
    citizen_votes = [[100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100], [100, 0, 0], [0, 0, 100]]
    citizen_votes2 = [[50, 50, 0], [0, 50, 50]]

    budget = compute_budget(100, citizen_votes)
    budget2 = compute_budget(100, citizen_votes2)
    print(check_fairness(100,citizen_votes ,budget))  # should print False
    print(check_fairness(100,citizen_votes2 ,budget2))  # should print False

