def cal_area(length, width) -> float:
    return length * width


if __name__ == '__main__':
    print('Rectangle\'s area calculator\n')

    params = input("Please type the length and width of the rectangle, use space:\n")
    params = params.split()

    area = cal_area(int(params[0]), int(params[1]))
    print(f'Rectangle\'s area: {params[0]} * {params[1]} = {area}')
