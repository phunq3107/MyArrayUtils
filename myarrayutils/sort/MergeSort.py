from . import utils


def MergeSort(arr: list, reverse: bool = False, cmp=None):
    """
    Sort input array with MergeSort algorithm
    MergeSort belongs to the Divide and Conquer algorithm with O(n.(log(n)))
    average time complexity and also in worst case.
    This sorting algorithm NEED SPACE and STABLE
    :param arr: Input array
    :param reverse:

    :param cmp:
    """
    if not cmp:
        cmp = utils.defaultComparator

    def comparator(obj1, obj2): return cmp(
        obj2, obj1) if reverse else cmp(obj1, obj2)
    process_MergeSort(arr, comparator)


def process_MergeSort(array, comparator):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        process_MergeSort(L, comparator)
        process_MergeSort(M, comparator)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if comparator(L[i], M[j]) <= -1:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
