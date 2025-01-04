"""
tuple exercise
"""

tuple1 = ('ordinateur', 'Français', 123, True)
tuple2 = ('pomme', 'pomme de terre', (1, 2, 3))

if __name__ == '__main__':
    tuple3 = (*tuple1, *tuple2)
    print(tuple3)
    print(tuple3[1])
    print(tuple3[2:-1])

    tuple4 = tuple3[1:-2]
    print(tuple4)

    a, b, c, d = tuple4
    print(f'{a} {b} {c} {d}')
