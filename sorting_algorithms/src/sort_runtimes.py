from rand_array import rand_array
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from time import clock
from math import log2
import sys
sys.setrecursionlimit(10000)  # python gets hung on deep recursion so this apparently helps

print("Please input an array size: ")
arr_size = int(input())
while arr_size < 0:
    print("That is not a valid size. Insert an array size: ")
    arr_size = int(input())

lower = -7000
upper = 7000

array = rand_array(arr_size, lower, upper)

print("This is your array %s" % array)
print("\nResult from quick sort %s" % quick_sort(array))
print("Result from insertion sort %s" % insertion_sort(array))

new_size = 10 # python hangs up at size >= 25 bc of deep recursion
avg_quicksort = 0
avg_insertionsort = 0

for j in range(2):
    total_time = 0
    for i in range(100):
        new_array = rand_array(new_size, lower, upper)

        if j == 0:
            start = clock()
            quick_sort(new_array)
            time = clock() - start
            total_time += time

        elif j == 1:
            start = clock()
            insertion_sort(new_array)
            time = clock() - start
            total_time += time
    if j == 0:
        avg_quicksort = total_time/100

    elif j == 1:
        avg_insertionsort = total_time/100

print("\nThis is your average run time for quick sort is %s seconds" % avg_quicksort)
print("This is your average run time for insertion sort is %s seconds" % avg_insertionsort)
print("\nThe number of steps the machine runs per second is %s steps" % int(round((avg_insertionsort/log2(new_size)) ** -1)))
print("The time it takes this machine to run a single step is %s seconds" % (avg_quicksort/log2(new_size)))

