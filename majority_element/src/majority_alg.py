
def majority_element(array):
    size = len(array)

    if size == 0:
        return None

    elif size == 1:
        return array[0]

    maj_idx = 0
    count = 1
    candidate = array[maj_idx]

    for i in range(1,size):

        if candidate == array[i]:
            count += 1

        else:
            count -= 1

            if count == 0:
                maj_idx = i
                count = 1
                candidate = array[maj_idx]

    candidate_amount = 0
    for num in array:
        if candidate == num:
            candidate_amount += 1

    if candidate_amount > size // 2:
        return candidate

    else:
        None


x = [0,1,2,3,4,8,8,8,8,8]

print(majority_element(x))



