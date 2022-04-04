import myarrayutils.sort as sort

def test_MergeSort_empty_array():
    arr = []
    expected = []
    sort.MergeSort(arr)
    assert arr == expected
