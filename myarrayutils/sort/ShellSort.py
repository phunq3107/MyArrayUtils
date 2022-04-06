from . import utils

def ShellSort(arr: list, reverse: bool = False, cmp=None):
    if not cmp:
        cmp = utils.defaultComparator

    def comparator(obj1, obj2): return cmp(
        obj2, obj1) if reverse else cmp(obj1, obj2)

    process_ShellSort(arr, cmp, comparator)

def process_ShellSort(arr, cmp, comparator):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    n = len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and comparator(arr[j-interval], temp) == 1:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2

    pass
