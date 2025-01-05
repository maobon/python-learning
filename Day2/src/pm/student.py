from buaaer import Buaaer


class Student(Buaaer):

    def __init__(self, name, number, college_num, td):
        super().__init__(name, number)
        self._college_num = college_num
        self._td = td

    def sign_td(self):
        self._td += 1
        print(f"{self.get_info()[0]}打卡成功, 当前TD次数{self._td}次")

    def add_td(self, count):
        self._td += count
        print(f"{self.get_info()[0]}增加{count}次打卡, 当前TD次数{self._td}次")

    def get_info(self):
        (name, num) = super().get_info()
        return name, num, self._college_num, self._td
