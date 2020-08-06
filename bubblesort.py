def bubblesort(array):
    condition = True
    len_arr = len(array)
    while condition:
        condition = False
        for i in range(len_arr - 1):
            el1 = array[i]
            el2 = array[i + 1]
            if el2 < el1:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                condition = True
    return array


if __name__ == '__main__':
    array = [2, 3, 4, 56, 6, 8, 9, 6, 5, 3, 3, 6, 8, 9, 5, 3, 1, 3, 6, 9, 0, 7]
    array = bubblesort(array)
    print(array)
