import myarrayutils.sort as sort

def test_MergeSort_empty_array():
    arr = []
    expected = []
    sort.MergeSort(arr)
    assert arr == expected
    
def test_MergeSort_int_array():
    arr = [1, 4, 77, 5, 6, 12, 24]
    expected = [1, 4, 5, 6, 12, 24, 77]
    sort.MergeSort(arr)
    assert arr == expected
