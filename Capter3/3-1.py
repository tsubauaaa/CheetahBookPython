def get_max_num(array):
    ret = array[0]
    for i in range(1, len(array)):
        if array[i] > ret:
            ret = array[i]

    return ret


# print(get_max_num([1, 2, 3, 4, 5]))
