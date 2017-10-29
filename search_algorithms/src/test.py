from random import randint
from rand_array import rand_array
from binary_search import *
from linear_search import *
from math import log2

#Binary Search Worst Case
worst_time = binary_srch_runtime(100000, -5000, 5000, True)
print("The worst case run time for binary search is %s seconds" % worst_time)
single_step = worst_time/log2(100000)
print(single_step)

#Linear Search Worst Case
worst_time = linear_srch_runtime(100000, -5000, 5000, True)
print("The worst case run time for linear search is %s seconds" % worst_time)
single_lin = worst_time/100000
print(single_lin)
