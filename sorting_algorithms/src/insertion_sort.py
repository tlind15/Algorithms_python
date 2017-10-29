from collections import deque


def insertion_sort(array):
    size = len(array)
    holder = None

    if size == 0:
        return None

    elif size == 1:
        return array

    i = 1
    while i < size:
        j = i - 1

        while j >= 0 and array[i] < array[j]:
            j -= 1

        if i - j > 1:
            holder = array[i]
            array[i] = None
            temp = deque(array[j+1:i+1])
            temp.rotate(1)  # shifts elements by one to put array[i] in proper position
            array[j+1:i+1] = temp
            array[j+1] = holder

        i += 1

    return array

