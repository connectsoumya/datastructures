def insertionsort(array):
    len_array = len(array)
    sorted = []
    for i in range(len_array):
        if i == 0:
            sorted.append(array[i])
        while array[i] < array[i - 1] and i - 1 > -1:
            a = array[i]
            array[i] = array[i - 1]
            array[i - 1] = a
            i = i - 1
    return array


if __name__ == '__main__':
    array = [4, 6, 1, 3, 8, 9, 3, 4, 6, 0, 1, 4, 8, 4, 9, 2, 4, 3, 7, 5, 9]
    print(insertionsort(array))
