"""
TODO_LIST
待办任务列表
"""

USER_OPTIONS = ["显示待办事项", "添加待办事项", "删除待办事项", "退出"]


def list_traversal(l: list):
    """
    check list info use traversal
    :param l: list
    """
    print("\n")
    for i, element in enumerate(l):
        print(f"{i + 1}. {element}")


def prompt_hint():
    """
    prompt hint
    """
    print("------------------------\n")
    print("TODO 清单")
    for i, o in enumerate(USER_OPTIONS):
        print(f"{i + 1}. {o}")


if __name__ == '__main__':
    prompt_hint()
    todo_list = []

    while True:
        text = input("请选择操作:\n")
        if not text:
            prompt_hint()
            continue

        else:
            index = int(text)

            if index == 1:
                # 显示待办事项
                if len(todo_list) == 0:
                    print("待办事项列表为空")
                    prompt_hint()
                else:
                    list_traversal(todo_list)

            elif index == 2:
                # 添加待办事项
                detail_info = input("请输入要添加的待办事项: \n")
                todo_list.append(detail_info)
                print(f"已成功添加 '{detail_info}' 到待办事项列表\n")
                prompt_hint()

            elif index == 3:
                # 删除待办事项
                while True:
                    list_traversal(todo_list)
                    del_index = input("\n请输入要删除的待办事项编号: \n")
                    if del_index.isdigit() and 0 < int(del_index) < len(todo_list) + 1:
                        item_deleted = todo_list.pop(int(del_index) - 1)
                        print(f"已成功删除 '{item_deleted}'")
                    elif del_index == 'exit':
                        print("退出删除模式 ...\n")
                        prompt_hint()
                        break
                    else:
                        print("请输入合法的待办事项编号！\n")

            elif index == 4:
                # 退出
                print("Bye! 退出待办事项清单 ...")
                print("------------------------\n")
                exit(1)

            else:
                print("请输入合法的选项！\n")
                print("------------------------\n")
                continue
