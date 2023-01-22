import doctest
import random



def questionA():
    """
    What is the probability of a patient receiving a suitable kidney, without a kidney transplant?
At first the blood types are randomized, then the blood types are matched, each has one match, and then the probability is calculated    A -> A , O
    B -> B , O
    AB -> A ,B , O
    O -> O
    :return:
    """
    blood_types = ["A", "B", "AB", "O"]
    probabilities = [0.25, 0.25, 0.25, 0.25]
    people =[random.choices(blood_types, probabilities, k=1)[0] for i in range(1000)]
    temp_arr = [0 for i in range(len(people))]
    matching = []
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            if j!=i and temp_arr[i] < 1 and temp_arr[j] < 1:
                if people[i] == 'A' and  (people[j] == 'A' or 'O'):
                    temp_arr[j] +=1
                    temp_arr[i] +=1
                    matching.append((i,j))
                elif people[i] == 'B' and  (people[j] == 'B' or 'O'):
                    temp_arr[j] += 1
                    temp_arr[i] += 1
                    matching.append((i,j))
                elif people[i] == 'AB' and  (people[j] == 'A' or 'B' or 'O' ):
                    temp_arr[j] += 1
                    temp_arr[i] += 1
                    matching.append((i,j))
                elif people[i] == 'O' and  people[j] == 'O':
                    temp_arr[j] += 1
                    temp_arr[i] += 1
                    matching.append((i,j))
    return len(matching)/len(people)


def questionB():
    """
    At first the blood types are randomized with pair of  (getting,contributor)
     and match between to pair
    :return:
    """
    # key is  getting, value is contributor
    dict_match = {
        'A': ['A', 'O'],
        'B': ['B', 'O'],
        'AB': ['AB', 'A', 'B', 'O'],
        'O': ['O'],
    }
    blood_types = ["A", "B", "AB", "O"]
    probabilities = [0.25, 0.25, 0.25, 0.25]
    pair = [(random.choices(blood_types, probabilities, k=1)[0],random.choices(blood_types, probabilities, k=1)[0]) for i in range(1000)]
    matching = []
    temp_arr = [0 for i in range(len(pair))]
    for i in range(len(pair)):
        for j in range(len(pair)):
            if i != j and temp_arr[i] < 1 and temp_arr[j] < 1:
                if pair[i][0] in dict_match[pair[j][1]] and pair[j][0] in dict_match[pair[i][1]]:
                    temp_arr[j] += 1
                    temp_arr[i] += 1
                    matching.append((i,j))
    return len(matching)/len(pair)

def questionC():
    return

if __name__ == '__main__':
    print("result A is :",questionA())
    print("result B is :",questionB())
    print("result C is :",questionC())
