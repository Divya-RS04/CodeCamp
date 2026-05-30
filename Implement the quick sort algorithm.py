def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)