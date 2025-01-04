if __name__ == '__main__':
    contains_upper = False
    contains_lower = False
    contains_numbers = False

    while True:
        password = input("Please input your password\n")
        for index, element in enumerate(password):
            if element.isupper():
                contains_upper = True
                continue

            if element.islower():
                contains_lower = True
                continue

            if element.isdigit():
                contains_numbers = True
                continue

        if contains_upper and contains_lower and contains_numbers:
            print("password set successfully...")
            break
