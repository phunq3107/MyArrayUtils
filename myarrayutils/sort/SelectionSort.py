from . import utils
def SelectionSort(arr: list, reverse: bool = False, cmp=None):
    """
    Time Complexity: O(n2) as there are two nested loops.
    Auxiliary Space: O(1)
    The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
    Stability : The default implementation is not stable. However it can be made stable. Please see stable selection sort for details.
    :param arr: Input array
    :param reverse:if false or not mentioned, the algorithm will sort from smallest to largest.
    If want to sort from largest to smallest, set it to true

    :param cmp: used to sort more complex data
    """
    if not cmp:
        cmp = utils.defaultComparator

    low = 0
    high = len(arr) - 1
    comparator = lambda obj1, obj2: cmp(obj2, obj1) if reverse else cmp(obj1, obj2)
    selectionSort(arr, cmp, comparator)

def selectionSort(arr, cmp, comparator):
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
        1) The subarray which is already sorted.
        2) Remaining subarray which is unsorted.
    In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is
    picked and moved to the sorted subarray.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if comparator(arr[min_idx], arr[j]) >= 1:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
