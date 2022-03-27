from . import utils


def BubbleSort(arr: list, reverse: bool = False, cmp=None):
    """
    Sort input array with BubbleSort algorithm
    It has O(n^2) average time complexity and also worst case.

    NOTE: This sorting algorith is NOT STABLE

    :param arr: Input array
    :param reverse: if false or not mentioned, the algorithm will sort from smallest to largest. 
    If want to sort from largest to smallest, set it to true
    :param cmp: used to sort more complex data
    """
    if not cmp:
        cmp = utils.defaultComparator

    def comparator(obj1, obj2): return cmp(
        obj2, obj1) if reverse else cmp(obj1, obj2)

    process_Bubble_Sort(arr, cmp, comparator)


def process_Bubble_Sort(arr, cmp, comparator):
    """
    this function will run the optimization bubble sort algorithm
    """
    has_swapped = True
    # This is a flag. It check if any swaps were made in the previous iteration.
    # If no swaps are made, the algorithm should stop
    num_of_iterations = 0
    # The first time we pass through the list the position n is guaranteed to be the largest element
    # the second time we pass through the position n-1 is guaranteed to be the second-largest element and so forth
    # This means that with each consecutive iteration we can look at one less element than before
    # More precisely, in the k-th iteration, only need to look at the first n - k + 1 elements
    # num_of_iterations is a variable to do that

    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - num_of_iterations - 1):
            if comparator(arr[i], arr[i+1]) >= 1:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
        num_of_iterations += 1
