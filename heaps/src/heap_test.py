from rand_array import rand_array
from selection_sort import selection_sort
from quick_sort import quick_sort
from time import clock
from heapify import *


print("Please input an array size: ")
arr_size = int(input())
while arr_size < 0:
    print("That is not a valid size. Insert an array size: ")
    arr_size = int(input())

lower = -7000
upper = 7000

array = rand_array(arr_size, lower, upper)

print("This is your array: %s" % array)
print("Result from heap sort is %s" % heap_sort(array))

time_total = 0
repititions = 100
array_size = 20
for i in range(repititions):
    new_arr = rand_array(array_size, lower, upper)
    start = clock()
    heap_sort(new_arr)
    final = clock() - start
    time_total += final

print("\nThe average run time for heap sort is %s seconds" % (time_total/repititions))

for j in range(repititions):
    new_arr = rand_array(array_size, lower, upper)
    start = clock()
    selection_sort(new_arr)
    final = clock() - start
    time_total += final

print("\nThe average run time for selection sort is %s seconds" % (time_total/repititions))

for k in range(repititions):
    new_arr = rand_array(array_size, lower, upper)
    start = clock()
    quick_sort(new_arr)
    final = clock() - start
    time_total += final

print("\nThe average run time for quick sort is %s seconds" % (time_total / repititions))


