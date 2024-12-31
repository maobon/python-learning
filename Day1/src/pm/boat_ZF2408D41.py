import random

# username and password
CONSTANT_USERNAME = "admin"
CONSTANT_PASSWORD = "root"

# targets between Sun distance unit AU
destinations_arr = [
    {"Sun": 0.0},
    {"Earth": 1.0},
    {"Mars": 2.52},
    {"Jupiter": 5.2},
    {"Pluto": 40.5}
]

# 1AU = 149600000km
CONSTANT_KM_ONE_AU = 149600000

operations = ['go', 'shoot', 'fuel', 'motor', 'exit']

POSITION_INIT = 1
AMMO_INIT = 100
TOTAL_AVAILABLE_DISTANCE = 10_000_000_000
ENGINE_STATUS_INIT = True


class Boat:

    def __init__(self, curr_position_index, ammo, avi_distance, engin_status):
        self.curr_position_index = curr_position_index
        self.ammo = ammo
        self.avi_distance = avi_distance
        self.engin_status = engin_status

    def set_current_position(self, curr_position_index):
        self.curr_position_index = curr_position_index

    def set_destination(self, destination_index) -> dict[str, float]:
        curr_to_sun = list(destinations_arr[self.curr_position_index].values())[0]

        target = destinations_arr[destination_index]
        target_to_sun = list(target.values())[0]

        return {
            "target": list(target.keys())[0],
            "distance": (abs(curr_to_sun - target_to_sun)) * CONSTANT_KM_ONE_AU
        }

    # return left fuel percent
    def consume_fuel(self, index, distance: float) -> float:
        if distance > self.avi_distance:
            self.engin_status = False
            return -1
        else:
            self.engin_status = True
            self.curr_position_index = index
            self.avi_distance -= distance
            return (self.avi_distance / TOTAL_AVAILABLE_DISTANCE) * 100

    def get_curr_left_fuel_percent(self) -> str:
        return f"fuel left: {(self.avi_distance / TOTAL_AVAILABLE_DISTANCE) * 100:.2f} %"

    def get_engin_status(self) -> bool:
        return self.engin_status

    def shoot(self):
        self.ammo -= 1
        print("target destroyed!") if random.choice([True, False]) else print("miss...")

    def get_ammo(self) -> int:
        return self.ammo


def login():
    username_retry_count = 2
    passwords_retry_count = 2

    while input("Please input your username:") != CONSTANT_USERNAME and username_retry_count > 0:
        print("Sorry, please input correct username")
        username_retry_count -= 1

    if username_retry_count == 0:
        print("Exit ...")
        exit(1)

    while input("Please input your password:") != CONSTANT_PASSWORD and passwords_retry_count > 0:
        print("Sorry, please input correct password")
        passwords_retry_count -= 1

    if passwords_retry_count == 0:
        print("Exit ...")
        exit(1)

    print("Login successfully...")


if __name__ == '__main__':
    login()

    # create boat instance
    boat = Boat(POSITION_INIT, AMMO_INIT, TOTAL_AVAILABLE_DISTANCE, ENGINE_STATUS_INIT)

    while True:

        print("Select your order\n")
        for i, operation in enumerate(operations):
            print(f"{i} - {operation}")

        operation_index = int(input("enter your choice: "))

        # go
        if operation_index == 0:
            if boat.get_engin_status():
                for i, destination in enumerate(destinations_arr):
                    print(f"{i} -> {list(destination.keys())[0]}")

                des_index = int(input("select your choice: "))
                dis = boat.set_destination(des_index).get("distance")

                fuel_left = boat.consume_fuel(des_index, dis)
                prompt_info = "left fuel not enough" if fuel_left < 0 else f"fuel left: {fuel_left:.2f} %"
                print(prompt_info, end="\n")

                print(f"{"Engine OK!\n" if boat.get_engin_status() else "Engine failure ...\n"}")
            else:
                print("no fuel available\n")

        # shoot
        elif operation_index == 1:
            shoot_count = int(input("input your shoot count: "))
            if shoot_count <= 0 or shoot_count > boat.get_ammo():
                print("no ammo available")
            else:
                for i in range(shoot_count):
                    boat.shoot()

                print(f"left ammo:{boat.ammo}")

        # fuel
        elif operation_index == 2:
            print(boat.get_curr_left_fuel_percent())


        # motor
        elif operation_index == 3:
            if boat.get_engin_status():
                print("space ship engin status OK!")
            else:
                print("space ship no engin status Down!")

        # exit
        elif operation_index == 4:
            exit(1)

        else:
            print("invalid operation")
