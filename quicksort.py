def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop()
    less_than = []
    greater_than = []
    for i in array:
        if i > pivot:
            less_than.append(i)
        if i <= pivot:
            greater_than.append(i)
    return quicksort(greater_than) + [pivot] + quicksort(less_than)


if __name__ == '__main__':
    array = [4, 6, 1, 3, 8, 9, 3, 4, 6, 0, 1, 4, 8, 4, 9, 2, 4, 3, 7, 5, 9]
    print(quicksort(array))
