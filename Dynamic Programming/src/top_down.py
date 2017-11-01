# Run Time Explanation for #3
# In this algorithm we are comparing every cut combination for rods of length 1....n. The number of cut combinations
# in a rod of length n is 2^(n-1). We perform these 2^(n-1) cuts n times for rods of length 1 all the way to n.
# Thus the running time will be O(2^n).


def top_down(size):
    values = {0: 0, 1: 3, 2: 5, 3: 10, 4: 12, 5: 14}

    if size == 0:
        return 0

    elif size == 1:
        return values[1]

    max_value = None

    for length in range(0, size + 1): #  You need size + 1 because the range function is non-inclusive
        cut_pos = 1
        while length - cut_pos >= cut_pos: # same idea as the bottom up. For example, cuts at position 2 and position 3 yield the same problem and do not both need to be tested
            max_value = max(values[length], top_down(length - cut_pos) + top_down(cut_pos))
            cut_pos += 1

    return max_value

print(top_down(5))
