import random

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
FUEL_INIT = 100
ENGIN_STATUS_INIT = True


class Boat:

    def __init__(self, curr_position_index, ammo, fuel, engin_status):
        self.curr_position_index = curr_position_index
        self.ammo = ammo
        self.fuel = fuel
        self.engin_status = engin_status

    def set_current_position(self, curr_position_index):
        self.curr_position_index = curr_position_index

    def set_destination(self, destination_index) -> dict[str, object]:
        curr_to_sun = list(destinations_arr[self.curr_position_index].values())[0]

        target = destinations_arr[destination_index]
        target_to_sun = list(target.values())[0]

        return {
            "target": list(target.keys())[0],
            "distance": abs(curr_to_sun - target_to_sun),
        }

    def desc_fuel(self) -> int:
        self.fuel -= random.randint(1, 10)
        if self.fuel <= 0:
            self.engin_status = False
        return self.fuel

    def get_fuel(self) -> int:
        return self.fuel

    def get_engin_status(self) -> bool:
        return self.engin_status

    def shoot(self):
        self.ammo -= 1

    def get_ammo(self) -> int:
        return self.ammo


if __name__ == '__main__':

    boat = Boat(POSITION_INIT, AMMO_INIT, FUEL_INIT, ENGIN_STATUS_INIT)

    print("Select your order\n")
    for i, operation in enumerate(operations):
        print(f"{i} - {operation}")

    while True:
        operation_index = int(input("enter your choice: "))

        # go
        if operation_index == 0:
            if boat.get_engin_status():

                for i, destination in enumerate(destinations_arr):
                    print(f"{i} -> {list(destination.keys())[0]}")

                des_id = int(input("select your choice: "))
                xx = boat.set_destination(des_id)
                print(xx)
                curr_fuel = boat.desc_fuel()


                if boat.get_engin_status():
                    print(f"space ship current fuel:{curr_fuel}\n"
                          f"already reached {xx['target']}")
                    boat.set_current_position(des_id)
                else:
                    print(f"space ship no fuel left, engine down!")
            else:
                print("no fuel available")

        # shoot
        elif operation_index == 1:
            shoot_count = int(input("input your shoot count: "))
            if shoot_count <= 0:
                print("no fuel available")
            elif shoot_count > boat.get_ammo():
                print("no ammo available")
            else:
                for i in range(shoot_count):
                    boat.shoot()
                print(f"left ammo:{boat.ammo}")

        # fuel
        elif operation_index == 2:
            print(f"space ship's fuel left:{boat.fuel}\n")


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
