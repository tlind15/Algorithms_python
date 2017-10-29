def max_sub_array(array):
    size = len(array)

    if size == 0:
        return None

    if size == 1:
        return array[0]

    subarray_sum = 0
    max_sum = 0

    for i in range(0, size):

        if subarray_sum < subarray_sum + array[i]:
            subarray_sum = subarray_sum + array[i]

        if subarray_sum > max_sum:
            max_sum = subarray_sum

        else:
            subarray_sum = array[i]


    return max_sum

x = [1,-20,3,4]
print(max_sub_array(x))


