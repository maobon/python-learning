def avg(data):
    if data is None or len(data) == 0:
        return None
    return sum(data) / len(data)


if __name__ == '__main__':
    print("调用求平均值函数打印平均值:")
    list_1 = [1, 3, 5, 7, 9]
    print(f"列表{list_1}的平均值: ", avg(list_1))
    list_2 = [2, 4, 6, 8, 10]
    print(f"列表{list_2}的平均值: ", avg(list_2))
    list_3 = [132, 32423, 5435, 643, 345]
    print(f"列表{list_3}的平均值: ", avg(list_3))
