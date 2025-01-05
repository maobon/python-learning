from buaaer import Buaaer
from student import Student

if __name__ == '__main__':
    zxx = Buaaer(name="周星星", number=9527)
    (name, number) = zxx.get_info()
    print(f"姓名: {name}, 编号: {number}")

    swk = Student("孙悟空", 23246666, 24, 0)
    (name, number, college_num, td_count) = swk.get_info()
    print(f"姓名: {name}, 编号: {number}, 系号: {college_num}")
    swk.sign_td()

    swk.add_td(12)
