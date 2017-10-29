def selection_sort(array):
    size = len(array)

    if size == 0 or size == 1:
        return array

    min_idx = None

    for i in range(0, size):
        min_idx = i
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return array



