from random import randint
from rand_array import rand_array
from binary_search import *
from linear_search import *


print("Input a size: ")
size = int(input()) #takes in input

while size <= 0: #ensuring a valid size
    print("Not a valid size input a size: ")
    size = int(input())

array = rand_array(size, -100, 100)
key = array[randint(0, len(array)-1)] #randomly makes key as one of the array elements

#Linear Search Result
position = linear_search(array,key)
print("The position of the key is from Linear Search is %s" % position)

#Binary Search Result
array.sort()
position = binary_search(array,key)
print("The position of the key from Binary Search is %s" % position)

#Linear Search Average Time
run_time = 0
for i in range(30):
    run_time += linear_srch_runtime(1000, -100, 100, False)
avg_time = run_time/30

print("\nThe average run time for Linear Search is %s" % avg_time)

#Binary Search Average Time
run_time = 0
for j in range(30):
    run_time += binary_srch_runtime(1000, -100, 100, False)
avg_time = run_time/30

print("The average run time for Binary Search is %s" % avg_time)


