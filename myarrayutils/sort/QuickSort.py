from . import utils


def QuickSort(arr: list, reverse: bool = False, cmp=None):
    """
    Sort input array with Quicksort algorithm

    Quicksort belongs to the Divide and Conquer algorithm with O(nlog(n))
    average time complexity and O(n^2) in worst case.

    Using Quicksort when you need the best performance in the average case
    for most inputs.

    Note: This sorting algorithm NEED SPACE and NOT STABLE

    :param arr: Input array
    :param reverse:

    :param cmp:
    """
    if not cmp:
        cmp = utils.defaultComparator

    low = 0
    high = len(arr) - 1
    comparator = lambda obj1, obj2: cmp(obj2, obj1) if reverse else cmp(obj1, obj2)
    quickSort(arr, low, high, comparator)


def partition(arr, low, high, comparator):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot
    :param arr:
    :param low:
    :param high:
    :param comparator:
    :return:
    """
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if comparator(arr[j], pivot) < 1:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high, comparator):
    """

    :param arr:
    :param low:
    :param high:
    :param comparator:
    :return:
    """
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high, comparator)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1, comparator)
        quickSort(arr, pi + 1, high, comparator)


# a = [1, 6, 3, 5]
# QuickSort(a)
# print(a)
