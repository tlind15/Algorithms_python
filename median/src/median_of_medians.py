from math import ceil
def median_of_medians(array):

    size = len(array)

    if size == 0:
        return None
    elif size == 1:
        return array[0]

    num_groups = size // 5 + min(1, size % 5)

    medians_array = []
    single_med_list = []

    for j in range(0, num_groups):
        for i in range(0, 5):
            single_med_list.append(array[j + i*(size//5)])

        single_med_list.sort()
        medians_array.append(single_med_list[2])
        #single_med_list.clear()

    if len(medians_array) <= 5:
        medians_array.sort()
        return medians_array

    else:
        median_of_medians(medians_array)


x = [1,2,3,4,5,6,7,8,9,10]
print(median_of_medians(x))

