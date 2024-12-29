class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def get_name(self) -> str:
        return self.name

    def cal_bmi(self) -> float:
        return self.weight / (self.height * self.height)


def get_prompt(bmi) -> str:
    if bmi < 18.5:
        return "You are too light"
    elif bmi < 25:
        return "You are normal!perfect..."
    elif bmi < 30:
        return "You are overweight"
    elif bmi >= 30:
        return "You are too fat"


if __name__ == '__main__':
    print("BMI Index calculator\n")

    name = input("Please enter your name: \n")
    height = input("Please enter your height: \n")
    weight = input("Please enter your weight: \n")

    person = Person(name, int(height), int(weight))
    ret = person.cal_bmi()

    print(get_prompt(ret))
