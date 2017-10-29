from statistics import median


def quick_sort(array):

    size = len(array)

    if size == 0 or size == 1:
        return array

    elif size == 2:
        if array[0] <= array[1]:
            return array

        else:
            array[0], array[1] = array[1], array[0]  # this is swap
            return array

    med = []
    med.append(array[0])
    med.append(array[size//2])
    med.append(array[size-1])
    pivot = median(med)  # finds median of those 3 numbers

    # This ensures that the pivot is swapped with the correct element
    # if there are repeats in the array then array.index will only return the first index in which that element is found
    index_of_pivot = None
    if med.index(pivot) == 0:
        index_of_pivot = 0
    elif med.index(pivot) == 1:
        index_of_pivot = size//2
    elif med.index(pivot) == 2:
        index_of_pivot = size-1

    array[index_of_pivot], array[size-1] = array[size-1], array[index_of_pivot]  # swap pivot with last element

    i = 0
    j = size - 2
    freeze_i = None
    freeze_j = None

    while i <= j:
        if array[i] < pivot and i <= j:
            i += 1
        else:
            freeze_i = True

        if array[j] > pivot and j >= i:
            j -= 1
        else:
            freeze_j = True

        if i < j and freeze_i and freeze_j:
            array[i], array[j] = array[j], array[i]  # swap left and right markers
            i += 1
            j -= 1
            freeze_i = False
            freeze_j = False

    # put pivot in position j and then run algorithm again on each half
    l_array = quick_sort(array[:i])
    r_array = quick_sort(array[i:size-1])

    return l_array + [pivot] + r_array

