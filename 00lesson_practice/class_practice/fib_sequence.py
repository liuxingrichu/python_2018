"""
    功能：用面向对象编程方式，编写斐波那契数列程序，并调用运行，输出运行结果 ：
"""


class Fibonacci(object):
    """
        生成斐波那契数列
    """
    def get_in_number(self, number):
        """
            功能：获取指定数值内的斐波那契数列
        """
        a, b = 0, 1
        tmp_list = []
        while b < number:
            tmp_list.append(str(b))
            a, b = b, a + b
        return ' '.join(tmp_list)

    def get_number(self, number):
        """
            功能：获取指定个数的斐波那契数列
        """
        a, b = 0, 1
        tmp_list = []
        count = 0
        while count < number:
            tmp_list.append(str(b))
            a, b = b, a + b
            count += 1
        return ' '.join(tmp_list)


if __name__ == "__main__":
    f = Fibonacci()
    result = f.get_in_number(100)
    print(result)
    result = f.get_number(10)
    print(result)
