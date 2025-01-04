if __name__ == '__main__':
    firstname = input("Please enter your first name: \n")
    lastname = input("Please enter your last name: \n")
    fn = firstname.title()
    ln = lastname.title()
    print(f"Full name is {fn} {ln}")
    initials = fn[0].upper() + ln[0].upper()
    print(f"Initials: {initials}")
