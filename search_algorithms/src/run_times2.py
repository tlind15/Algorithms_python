from random import randint
from rand_array import rand_array
from binary_search import *
from linear_search import *
from math import log2

print("Input a size: ")
size = int(input()) #takes in input

while size <= 0: #ensuring a valid size
    print("Not a valid size input a size: ")
    size = int(input())

array = rand_array(size, -5000, 5000)
array[len(array)-1] = 7000
key = 7000

#Linear Search Result
position = linear_search(array,key)
print("The position of the key is from Linear Search is %s" % position)

#Binary Search Result
array.sort()
position = binary_search(array,key)
print("The position of the key from Binary Search is %s" % position)

#Linear Search Worst Case
worst_time = linear_srch_runtime(10^6, -5000, 5000, True)
print("The worst case run time for linear search is %s seconds" % worst_time)
single_lin = worst_time/100000

#Binary Search Worst Case
worst_time = binary_srch_runtime(100000, -5000, 5000, True)
print("The worst case run time for binary search is %s seconds" % worst_time)
single_step = worst_time/log2(100000)

#Linear Search Projected Runtime
print("\nThe projected runtime for linear search for n= 10^6 is %s seconds" % (single_lin*1000000))
actual = linear_srch_runtime(1000000, -5000, 5000, True)
print("The actual runtime for linear search for n= 10^6 is %s seconds" % actual)

#Binary Search Projected Runtime
print("\nThe projected runtime for binary search for n=10^6 is %s seconds" % (single_step*log2(1000000)))
actual = binary_srch_runtime(1000000, -5000, 5000, True)
print("The actual runtime for binary search for n= 10^6 is %s seconds" % actual)




