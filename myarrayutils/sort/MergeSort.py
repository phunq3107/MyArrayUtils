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
       mergeSort(arr, comparator)
       
def mergeSort(arr, comparator):
       if len(arr) >1:
              mid = len(arr)//2
              # Finding the mid of the array
              L = arr[:mid]
              # Dividing the array elements
              R = arr[mid:]
              # into 2 halves
              mergeSort(L, comparator)
              # Sorting the first half
              mergeSort(R, comparator)
              # Sorting the second halft
              i = j = k = 0
              # Copy data to temp arrays L[] and R[]
              while i < len(L) and j < len(R):
                     if comparator(L[i], R[j]) < 0:
                            arr[k] = L[i]
                            i+= 1
                     else:
                            arr[k] = R[j]
                            j+= 1
                            k+= 1
              # Checking if any element was left 
              while i < len(L):
                     arr[k] = L[i]
                     i+= 1
                     k+= 1
              while j < len(R):
                     arr[k] = R[j]
                     j+= 1
                     k+= 1
