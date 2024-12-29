import random

destination_arr = ['Earth', 'Moon', 'Mars', 'Jupiter', 'Sun']
operations = ['go', 'shoot', 'fuel', 'motor', 'exit']

POSITION_INIT = 0
AMMO_INIT = 20
FUEL_INIT = 20
ENGIN_STATUS_INIT = True


class Boat:

    def __init__(self, curr_position, ammo, fuel, engin_status):
        self.curr_position = destination_arr[curr_position]
        self.ammo = ammo
        self.fuel = fuel
        self.engin_status = engin_status

    def set_destination(self, destination_id):
        self.curr_position = destination_arr[destination_id]

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

        if operation_index == 0:
            if boat.get_engin_status():
                for i, e in enumerate(destination_arr):
                    print(f"{i} - {e}")
                des_id = int(input("select your choice: "))
                boat.set_destination(des_id)
                curr_fuel = boat.desc_fuel()
                print(f"space ship go to {destination_arr[des_id]}\n")
                if boat.get_engin_status():
                    print(f"space ship current fuel:{curr_fuel}")
                else:
                    print(f"space ship no fuel left, engine down!")
            else:
                print("no fuel available")

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

        elif operation_index == 2:
            print(f"space ship's fuel left:{boat.fuel}\n")


        elif operation_index == 3:
            if boat.get_engin_status():
                print("space ship engin status OK!")
            else:
                print("space ship no engin status Down!")

        else:
            print("invalid operation")
