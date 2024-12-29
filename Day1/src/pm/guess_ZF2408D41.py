import random

RETRY_COUNT = 7

if __name__ == '__main__':
    num = random.randint(1, 100)
    print(f"欢迎参加参数子游戏！你有{RETRY_COUNT}次机会\n")
    # print(num)

    input_num = int(input("请猜一个1到100之间的数字: "))

    while num != input_num and RETRY_COUNT > 1:
        if num > input_num:
            print("猜的数字太小了，请再是一次！")
            input_num = int(input("请猜一个1到100之间的数字: "))
            RETRY_COUNT -= 1
        elif num < input_num:
            print("猜的数字太大了，请再是一次！")
            input_num = int(input("请猜一个1到100之间的数字: "))
            RETRY_COUNT -= 1

    if num != input_num:
        print(f"机会用完了，被猜的数字是{num}")
    elif num == input_num:
        print("恭喜，你猜对了！")
