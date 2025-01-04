if __name__ == '__main__':
    # method 1
    user_input = input("Please input something\n")
    print(f"user original input is: {user_input}")
    print(f"reverse user input text: {user_input[::-1]}")

    # method 2
    ret = []
    input_list = list(user_input)
    for i in range(len(input_list) - 1, -1, -1):
        ret.append(input_list[i])
    joined = "".join(ret)
    print(f"reverse user input text: {joined}")
