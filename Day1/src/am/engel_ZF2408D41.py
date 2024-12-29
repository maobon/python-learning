# xinyi ZF2408D41

class Payout:
    def __init__(self, education_payout, food_payout, medical_payout, investment_payout, unexpected_payout):
        self.education_payout = education_payout
        self.food_payout = food_payout
        self.medical_payout = medical_payout
        self.investment_payout = investment_payout
        self.unexpected_payout = unexpected_payout

    def get_total_payout(self) -> float:
        return self.education_payout + self.food_payout + self.medical_payout + self.investment_payout + self.unexpected_payout


class FamilyInfo:
    def __init__(self, family_name, family_members_number, address):
        self.family_name = family_name
        self.family_members_number = family_members_number
        self.address = address
        self.family_payout = None

    def set_family_payout(self, family_payout):
        self.family_payout = family_payout

    def cal_engel_coefficient(self) -> float:
        return self.family_payout.food_payout / self.family_payout.get_total_payout()


if __name__ == '__main__':
    print("Engel's Coefficient calculator\n")

    name = input("Please input your family name: \n")
    num = input("Please input your family members number: \n")
    address = input("Please input your address: \n")

    family_info = FamilyInfo(name, num, address)

    items = ["education", "food", "medical", "investment", "unexpected"]
    payout_params = list()
    for item in items:
        payout_val = input(f"Please input {item}'s payout: \n")
        payout_params.append(int(payout_val))

    payout = Payout(payout_params[0], payout_params[1], payout_params[2], payout_params[3], payout_params[4])
    family_info.set_family_payout(payout)

    print(f"\nEngel's Coefficient for family {family_info.family_name}\n"
          f"value is {family_info.cal_engel_coefficient() * 100}%\n")
