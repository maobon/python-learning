"""
集合 {} set 表示
列表 [] list 表示 和 Java不同
"""

if __name__ == '__main__':
    # python 中 用{}表示空集合被认为是字典
    set_empty = set()
    print("空集合: ", set_empty)

    set_1 = {1, 2, 3, 4, 5}
    print("集合1: ", set_1)

    set_2 = {4, 4, 5, 5, 6, 7, 7, 7, 8}
    print("集合2: ", set_2)

    set_1 = set_1.union({6})
    print("添加元素6后的集合1: ", set_1)

    # 交集
    set_3 = set_2.intersection(set_1)
    print("集合1和集合2的交集: ", set_3)

    # 并集
    set_4 = set_2.union(set_1)
    print("集合1和集合2的并集: ", set_4)

    # 差集
    set_5 = set_2.difference(set_1)
    print("集合1和集合2的差集: ", set_5)

    set_2.remove(8)
    print("移除集合2中的元素'8'并打印: ", set_2)

    five_in_set = 5 in set_3
    print("元素'5'是否在集合1和2的交集中: ", five_in_set)
