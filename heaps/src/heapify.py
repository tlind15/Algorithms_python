from math import floor
# due to list indexing from zero


def left_child(index):
    return 2*index + 1


def right_child(index):
    return 2*index + 2


def get_parent(index):
    if index % 2 == 0:
        return floor(index/2 - 1)

    elif index % 2 == 1:
        return floor(index/2)


def max_heapify(array, current):
    size = len(array)

    if size == 0 or size == 1 or left_child(current) >= size:  # if it doesn't have a left child it must be a leaf
        return array

    max_idx = current

    left = left_child(current)
    if array[left] > array[max_idx]:
        max_idx = left

    if right_child(current) < size:
        right = right_child(current)
        if array[right] > array[max_idx]:
            max_idx = right

    if max_idx != current:
        array[current], array[max_idx] = array[max_idx], array[current]
        max_heapify(array, max_idx)

    return array


def build_heap(array):
    size = len(array)
    for i in range(size, 0, -1):
        array = max_heapify(array, i - 1)

    return array


def remove_root(array):
    size = len(array)
    if size == 0 or size == 1:
        return array

    array[size - 1], array[0] = array[0], array[size - 1]
    array.pop()

    build_heap(array)

    return array


def heap_sort(array):
    size = len(array)
    if size == 0 or size == 1:
        return array

    array = build_heap(array)
    sorted_array = []

    for i in range(0, size):
        sorted_array.append(array[0])
        array = remove_root(array)

    return list(reversed(sorted_array))