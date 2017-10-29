from random import randint
from rand_array import rand_array
from time import clock


def linear_search (array, key):
    size = len(array)

    if size == 0:
        return None

    for index in range(0, size):
        if key == array[index]:
            return index

    return None


def linear_srch_runtime(array_size, lower, upper, userKey):

    array = rand_array(array_size, lower, upper)

    key = None
    if userKey is False:
        key = array[randint(0,array_size-1)]

    elif userKey is True:
        array[len(array) - 1] = 7000
        key = 7000

    start = clock() #finds the starting time point
    linear_search(array, key)
    return clock() - start #finds the end point and calculates difference in seconds


