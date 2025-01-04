USER_OPTIONS = ["显示待办事项", "添加待办事项", "删除待办事项", "退出"]


def list_traversal(l: list):
    """
    check list info use traversal
    :param l: list
    """
    for i, element in enumerate(l):
        print(f"{i + 1}. {element}")


def prompt_hint():
    """
    prompt hint
    """
    for i, o in enumerate(USER_OPTIONS):
        print(f"{i + 1}. {o}")


if __name__ == '__main__':

    prompt_hint()

    todo_list = ["task1", "task2"]

    while True:
        index = int(input("\nSelect Main Option:\n"))
        print(f"Item {index} selected...\n")

        if index == 1:
            # 显示待办事项
            if len(todo_list) == 0:
                print("待办事项列表为空")
            else:
                list_traversal(todo_list)

        elif index == 2:
            # 添加待办事项
            detail_info = input("Please input your task detail information.\n")
            todo_list.append(detail_info)
            print("task added successfully.\n")
            prompt_hint()

        elif index == 3:
            # 删除待办事项
            while True:
                list_traversal(todo_list)

                del_index = input("\ninput index to delete\n")
                if del_index.isdigit() and 0 < int(del_index) < len(todo_list) + 1:
                    todo_list.pop(int(del_index) - 1)

                elif del_index == 'exit':
                    print("exit delete mode ...\n")
                    prompt_hint()
                    break
                else:
                    print("invalid index, please try again.\n")

        elif index == 4:
            # 退出
            print("bye...")
            exit(1)

        else:
            print("Invalid input, please try again.\n")
            continue
