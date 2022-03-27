from . import utils


def BubbleSort(arr: list, reverse: bool = False, cmp=None):
    """
    Sort input array with BubbleSort algorithm

    :param arr: Input array
    :param reverse:
    :param cmp:
    """
    if not cmp:
        cmp = utils.defaultComparator

    def comparator(obj1, obj2): return cmp(
        obj2, obj1) if reverse else cmp(obj1, obj2)

    process_Bubble_Sort(arr, cmp, comparator)


def process_Bubble_Sort(arr, cmp, comparator):
    """
    this function will run the bubble sort algorithm
    """
    has_swapped = True
    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - num_of_iterations - 1):
            if comparator(arr[i], arr[i+1]) <= -1:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
        num_of_iterations += 1
