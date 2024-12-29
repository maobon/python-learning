import math


def area(radius) -> float:
    return math.pi * radius ** 2


# if __name__ == '__main__':
#     radius_array = [5.1, 6.96, 10]
#     results = list()
#
#     for r in radius_array:
#         result = area(r)
#         results.append(result)
#
#     for i, result in enumerate(results):
#         print(f'circle radius={radius_array[i]} area={result:.2f}')

if __name__ == '__main__':
    r = int(input("Please enter radius: \n"))
    while r <= 0:
        r = int(input("Please enter radius: \n"))

    area = area(r)
    print(f"The area of the circle with radius {r} is {area:.2f}")
