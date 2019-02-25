import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """

    a_list = range(n)
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    """function return search by sequential_search algorithm
    :return: [0]bool , [1]search processing time
    """
    pos = 0
    found = False
    start_time = time.time() #begin search
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time() #end search
    return found, end_time - start_time

def ordered_sequential_search(a_list, item):
    """ function return search by ordered_sequential_search algorithm
    :params: a_list: sort by ascending order
    :return: [0]bool , [1]search processing time
    """
    pos = 0
    found = False
    stop = False
    start_time = time.time()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    end_time = time.time()
    return found, end_time - start_time

def binary_search_interative(a_list, item):
    """ function return search by binary_search_interative algorithm
    :params: a_list: sort by ascending order
    :return: [0]bool , [1]search processing time
    """
    first = 0
    last = len(a_list) - 1
    found = False
    start_time = time.time()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()
    return found, end_time - start_time


def binary_search_recursive(a_list, item):
    """ function return search by binary_search_recursive algorithm
    :params: a_list: sort by ascending order
    :return: [0]bool , [1]search processing time
    """
    found = False
    start_time = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()
    return found, end_time - start_time

def main():
    """ main funtion print out each algorithm average search processing time. """
    list_size = [500, 1000, 10000]
    search_result = {'sequential':0, 'ordered_sequential':0, 'binary_interative':0, 'binary_recursive': 0}
    for i in list_size:
        list_count = 0
        while list_count < 100:
            random_number_list = get_me_random_list(i)
            search_result['sequential']+=sequential_search(random_number_list, -1)[1]
            random_number_list.sort() #make list ascending order
            search_result['ordered_sequential'] += ordered_sequential_search(random_number_list, -1)[1]
            search_result['binary_interative'] += binary_search_interative(random_number_list, -1)[1]
            search_result['binary_recursive'] += binary_search_recursive(random_number_list, -1)[1]
            list_count+=1

    for key, val in search_result.items():
        print('%s Search took %10.7f seconds to run, on average'%(key, val/100))

main()






















































































