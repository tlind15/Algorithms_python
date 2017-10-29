from random import randint


def rand_array (array_size, lower_bound, upper_bound):
    if lower_bound >= upper_bound:
        return None

    return [randint(lower_bound, upper_bound) for i in range(array_size)]
