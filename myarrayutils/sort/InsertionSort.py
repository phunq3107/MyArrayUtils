from . import utils

def InsertionSort(arr: list, reverse: bool = False, cmp=None):
    """
        Sort input array with Insertion algorithm.

        Insertion sort is a sorting algorithm, which sorts the array by shifting the elements one at time.
        It iterates the input elements by growing the sorted array at each iteration.
        It compares the current element with the largest value in the sorted array.
        If the current element is greater, then it leaves the element in its place and moves on to the next element
        else it finds its correct position in the sorted array and moves it to that position.
        This is done by shifting all the elements, which are larger than the current element,
        in the sorted array to one position ahead

        Average Case Complexity: O(n^2)
        It occurs when the elements of an array are in jumbled order (neither ascending nor descending).

        Space complexity is O(1) because an extra variable key is used.

        NOTE: This sorting algorith is  STABLE

        :param arr: Input array
        :param reverse:if false or not mentioned, the algorithm will sort from smallest to largest.
        If want to sort from largest to smallest, set it to true

        :param cmp: used to sort more complex data
        """

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
