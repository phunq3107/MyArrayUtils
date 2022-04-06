from . import utils

def InsertionSort(arr: list, reverse: bool = False, cmp=None):
    if not cmp:
        cmp = utils.defaultComparator

    def comparator(obj1, obj2): return cmp(
        obj2, obj1) if reverse else cmp(obj1, obj2)

    process_InsertionSort(arr, cmp, comparator)

def process_InsertionSort(arr, cmp, comparator):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and comparator(key, arr[j]) == -1:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key

    pass
