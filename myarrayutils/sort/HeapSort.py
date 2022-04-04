from . import utils


def HeapSort(arr: list, reverse: bool = False, cmp=None):
    """
    Sort input array with Heapsort algorithm.

    Heapsort is a comparison-based sorting technique based on
    Binary Heap data structure with nlog(n) average time complexity 
    and O(nlog(n)) in the worst case.

    Using Heapsort when you don't necessarily need very fast performance, 
    but guaranteed O(nlogn) performance with minimal usage memory.

    Note: This sorting algorith is NOT STABLE

    :param arr: Input array.
    :param reverse: If this param is False or not specified, 
    the array will be sorted in ascending order. Ortherwise, 
    it will be in descending order after sorted.

    :param cmp: Custom compare function, which receives two parameters, 
    computes the result and then make uses of the computation
    to compare and sort the array.
    """
    if not cmp:
        cmp = utils.defaultComparator

    def comparator(obj1, obj2): return cmp(
        obj2, obj1) if reverse else cmp(obj1, obj2)
    heapSort(arr, comparator)


def heapify(arr, n, i, comparator):
    """
    This function heapify a sub-tree rooted with node i, which is an index in arr.
    :param arr: Input array contains the sub-tree to heapify
    :param n: Size of the heap
    :param i: Index of root node in the sub-tree
    :param comparator: Custom compare function, which receives two parameters,
    computes the result and then make uses of the computation to compare two nodes.
    """
    largest = i #Initalize largest as root
    leftChild = 2 * i + 1 # Left children of node index i, if exits, is 2*i+1 
    rightChild = 2 * i + 2 # Left children of node index i, if exits, is 2*i+2
    
    #If left children is larger than root (or current largest)
    if leftChild < n and comparator(arr[largest], arr[leftChild]) < 0:
        largest = leftChild

    #If right children is larger than largest so far
    if rightChild < n and comparator(arr[largest], arr[rightChild]) < 0:
        largest = rightChild

    #If the largest is not root
    if largest != i:
        # Swap the largest and root
        arr[i], arr[largest] = arr[largest], arr[i]

        #Recursively heapify the affected sub-tree
        heapify(arr, n, largest, comparator)


def heapSort(arr, comparator):
    """
    :param arr: Input array
    :param comparator: Custom compare function, which receives two parameters,
    computes the result and then make uses of the computation to compare and sort the array.
    """
    n = len(arr)
    #Build heap (rearrange array)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, comparator)

    #One by one extract an element from heap 
    for i in range(n-1, 0, -1):
        #Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        #Heapify on the reduced array
        heapify(arr, i, 0,comparator)
