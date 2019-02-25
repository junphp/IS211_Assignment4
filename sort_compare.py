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

def insertion_sort(a_list):
    """ function return list sort by insertion sort algorithm
    :return: sort processing time
    """
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    end_time = time.time()
    return end_time - start_time


def shell_sort(a_list):
    """ funtion return list sort by shell sort algorithm
    :return: sort processing time
    """
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
            #print("After increments of size", sublist_count, "The list is",a_list)
        sublist_count = sublist_count // 2
    end_time = time.time()
    return end_time - start_time

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    """ python list ascending sort and return
    :return: sort processing time
    """
    start_time = time.time()
    a_list.sort()
    end_time = time.time()
    return end_time - start_time

def main():
    """ main funtion print out each algorithm average sort processing time. """
    list_size = [500, 1000, 10000]
    sort_result = {'insertion':0, 'shell':0, 'python':0}
    for i in list_size:
        list_count = 0
        while list_count < 100:
            random_number_list = get_me_random_list(i)
            sort_result['insertion']+=insertion_sort(random_number_list)
            sort_result['shell'] += shell_sort(random_number_list)
            sort_result['python'] += python_sort(random_number_list)
            list_count+=1

    for key, val in sort_result.items():
        print('%s sort took %10.7f seconds to run, on average'%(key, val/100))

main()





















































































