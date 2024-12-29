

def collatz(n) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

if __name__ == '__main__':
    val = int(input("Press input your positive number\n"))
    print(f"started collatz: {str(val)}")

    strs = ""
    while val != 1:
        val = collatz(int(val))
        strs += str(val)
        strs += " "

    print(strs)
    print('Done ...')
