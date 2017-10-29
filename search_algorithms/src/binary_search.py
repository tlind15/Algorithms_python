from random import randint
from rand_array import rand_array
from time import clock


def binary_search(array, key):
    size = len(array)

    if size == 0:
        return None

    if size == 1:
        if key == array[0]:
            return 0

        else:
            return None

    first = 0
    last = size-1

    while first <= last:

        mid = (first + last)//2 #integer division

        if key == array[mid]:
            return mid

        elif key < array[mid]: #elif --> else if
            last = mid-1

        elif key > array[mid]:
            first = mid+1

    return None


def binary_srch_runtime(array_size, lower, upper, userkey):

    array = rand_array(array_size, lower, upper)

    key = None
    if userkey is False:
        key = array[randint(0, array_size-1)]

    elif userkey is True:
        array[len(array) - 1] = 7000
        key = 7000

    array.sort()

    start = clock() #finds the starting time point
    binary_search(array, key)
    return clock() - start #finds the end point and calculates difference in seconds
