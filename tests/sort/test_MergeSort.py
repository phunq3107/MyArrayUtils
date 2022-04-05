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

    
def test_MergeSort_int_array_with_cmp():
    arr = [1, 4, 77, 5, 6, 12, 24]
    expected = [1, 4, 5, 6, 12, 24, 77]
    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.MergeSort(arr, cmp=cmp)
    assert arr == expected
