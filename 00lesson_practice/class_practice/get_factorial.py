"""
    用面向对象编程方式，编写阶乘程序，并调用运行，输出运行结果。
"""


class Factorial(object):
    def get_factorial(self, number):
        if number < 0:
            return False
        elif number == 0 or number == 1:
            return 1
        else:
            return number * self.get_factorial(number - 1)

    def get_by_multiplic(self, number):
        if number < 0:
            return False
        elif number == 0 or number == 1:
            return 1
        else:
            multi = 1
            for i in range(1, number + 1):
                multi *= i
            return multi


if __name__ == "__main__":
    NUM = 8
    f = Factorial()
    result = f.get_factorial(NUM)
    if result:
        print("%d的阶乘结果: %d" % (NUM, result))
    else:
        print("负数没有阶乘！")
    result = f.get_by_multiplic(NUM)
    if result:
        print("%d的阶乘结果: %d" % (NUM, result))
    else:
        print("负数没有阶乘！")
