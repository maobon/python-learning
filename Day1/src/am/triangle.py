import math


def cal_triangle_longest(length, height) -> float:
    return math.sqrt(length * length + height * height)


if __name__ == '__main__':
    print("Rt triangle\'s longest calculator\n ")
    params = input("Please input length and height use space:\n")
    params = params.split()
    ret = cal_triangle_longest(int(params[0]), int(params[1]))
    print("triangle longest side is: ", ret)
