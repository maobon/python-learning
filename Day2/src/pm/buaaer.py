class Buaaer(object):

    def __init__(self, name, number):
        self._name = name
        self._number = number

    def change_num(self, number):
        print('编号已改变为: ', number)
        self._number = number

    def get_info(self):
        return self._name, self._number
