import myarrayutils.sort as sort

def test_MergeSort_empty_array():
    arr = []
    expected = []
    sort.MergeSort(arr)
    assert arr == expected
    
    
    
def test_MergeSort_empty_array_with_reverse():
    arr = []
    expected = []
    sort.MergeSort(arr, reverse=True)
    assert arr == expected

    
def test_MergeSort_int_array_with_reverse():
    arr = [1, 4, 77, 6, 12, 5, 24]
    expected = [77, 24, 12, 6, 5, 4, 1]
    sort.MergeSort(arr, reverse=True)
    assert arr == expected
