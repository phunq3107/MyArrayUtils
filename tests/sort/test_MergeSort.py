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
