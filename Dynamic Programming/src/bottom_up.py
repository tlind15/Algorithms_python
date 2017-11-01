# Compare run time #3
#  In this algorithm we are comparing the value of every cut combination but we use the dictionary to store maximum values of cuts we have already computed.
#  In this algorithm, we iterate over a rod of length n with each piece of rod having n-1 possible cuts.
#  However since all the cuts for a rod of length < n have already been computed, the value of each of the n-1 cuts can be computed in O(1) time.
#  Thus, the running time for this algorithm will be O(n^2)
def rod_cutting():

    values = {0: 0, 1: 3, 2: 5, 3: 10, 4: 12, 5: 14}
    rod_length = len(values)

    if rod_length == 0:
        return 0

    elif rod_length == 1:
        return values[1]

    max_value_per_size = {}  # a table depicted the maximum value of a rod from size n
    cuts_for_max_per_size = {}  # a table depicting the relative position of a cut on a rod of size n that will produce the maximum value

    #  we find the maximum value of a rod of size 'length'
    #  we use the known maximum value of smaller rods to find the maximum for larger rods
    for length in range(0, rod_length):
        max_value = values[length]  # value of whole piece
        cut_pos = 1

        # we save time by not testing complimentary cuts of cases we have already tested
        # Ex: a single cut of the rod at position 1 will produce the same problem as making a single cut at position 4
        while length - cut_pos >= cut_pos:
            left_value = max_value_per_size[cut_pos]  # the value of the left half of the rod
            right_value = max_value_per_size[length - cut_pos]  # the value of the right half of the rod

            # determine max between the previous maximum and the aggregate value of the two cut pieces
            max_value = max(max_value, left_value + right_value)
            cut_pos += 1

        cuts_for_max_per_size[length] = cut_pos - 1
        max_value_per_size[length] = max_value

    print(cuts_for_max_per_size)
    return max_value_per_size[rod_length - 1]


print(rod_cutting())




