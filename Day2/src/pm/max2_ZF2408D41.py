from max1_ZF2408D41 import max_of_two


def max_of_three(a: int, b: int, c: int) -> int:
    """
    get max of three integers
    :param a: int
    :param b: int
    :param c: int
    :return: max integer
    """
    maximum = max_of_two(a, b)
    return max_of_two(maximum, c)


def get_max_in_tuple(*args):
    """
    get max of tuple
    :param args: (,,,)
    :return: max integer
    """
    if args is None:
        return None

    maximum = -1
    for arg in args:
        if arg > maximum:
            maximum = arg
        else:
            continue

    return maximum


if __name__ == '__main__':
    print("两个数中的最大值: ", max_of_two(10, 20))
    print("三个数中的最大值: ", max_of_three(20, 40, 60))
    datas = (1, 2, 3, 324, 3242, 4234, 332, 432, 234)
    print("一系列数中的最大值: ", get_max_in_tuple(*datas))
