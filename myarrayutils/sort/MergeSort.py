from . import utils

       """
       Sort input array with MergeSort algorithm
       MergeSort belongs to the Divide and Conquer algorithm with O(n.(log(n)))
       average time complexity and also in worst case.
       This sorting algorithm NEED SPACE and STABLE
       :param arr: Input array
       """
       def MergeSort(arr):
              if len(arr) >1:
                     mid = len(arr)//2
                     L = arr[:mid]
                     R = arr[mid:]
                     mergeSort(L)
                     mergeSort(R)
                     i = j = k = 0
                     while i < len(L) and j < len(R):
                            if L[i] < R[j]:
                                   arr[k] = L[i]
                                   i+= 1
                            else:
                                   arr[k] = R[j]
                                   j+= 1
                                   k+= 1
                                   
