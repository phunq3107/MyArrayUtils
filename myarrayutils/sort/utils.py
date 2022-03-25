def defaultComparator(obj1, obj2) -> int:
    """
        Default comparator
    :param obj1:
    :param obj2:
    :return:
        -1 if obj1 < obj2
        0 if obj1 = obj2
        1 if obj1 > obj2
    """
    if obj1.__lt__(obj2):
        return -1
    if obj1.__gt__(obj2):
        return 1
    return 0
