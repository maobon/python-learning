num_list = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

if __name__ == '__main__':
    print("list1: ", num_list)
    print("list2: ", fruits)

    print("提取前三个元素的列表: ", num_list[:3])

    num_list.extend(fruits)
    print("合并后的列表: ", num_list)

    num_list[2] = num_list[1:4]
    print("替换第三个元素后的列表: ", num_list)

    num_list.remove(4)
    print("移除一个元素后的列表: ", num_list)

    print("列表中元素的个数: ", len(num_list))
