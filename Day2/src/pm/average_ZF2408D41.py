def average(data, print_flag=False):
    """
    calculate the average of data
    :param data: List
    :param print_flag: print check enable flag - default False
    :return: string
    """
    if data is None or len(data) == 0:
        if print_flag:
            print("列表为空")
        return None
    else:
        cal_result = f"列表{data}的平均值:{sum(data) / len(data)}"
        if not print_flag:
            return cal_result
        else:
            print(cal_result)


if __name__ == '__main__':
    list_1 = [1, 3, 5, 7, 9]
    list_2 = [2, 4, 6, 8, 10]
    list_3 = [132, 32423, 5435, 643, 345]

    print("调用求平均值函数打印平均值:")
    print(average(list_1))
    print(average(list_2))
    print(average(list_3))

    print_enable = True
    print("调用打印函数打印平均值:")
    average(list_1, print_enable)
    average(list_2, print_enable)
    average(list_3, print_enable)
