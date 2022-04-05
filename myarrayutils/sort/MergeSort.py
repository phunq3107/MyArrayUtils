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
       
def merge(arr, l, r, comparator):  
       if l >= r:
              return
       mid = (l + r)//2  
       # Finding the mid of the array
       merge(arr, l, m, comparator)  
       merge(arr, m + 1, r, comparator)  
       mergeSort(arr, l, r, m, comparator)
       
def mergeSort(arr, l, r, m, comparator):
              L = arr[l : mid + 1]
              # Dividing the array elements
              R = arr[mid + 1 : r + 1 ]
              # into 2 halves
              i = j = 0
              k = l
              # Copy data to temp arrays L[] and R[]
              while i < len(L) and j < len(R):
                     if comparator(L[i], R[j]) <= 0:
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
              merge(arr, 0, len(arr)-1, comparator)
