"""
    功能：用面向对象编程方式，编写列表元素偶数之和程序，并调用运行，输出运行结果。
"""


class EvenSum(object):
    """
        列表元素偶数之和
    """
    def get_even_sum(self, src_list):
        """
            功能：列表元素偶数之和
        """
        sum = 0
        for content in src_list:
            if content % 2 == 0:
                sum += content
        return sum


if __name__ == "__main__":
    e = EvenSum()
    result = e.get_even_sum([1, 6, 8, 6])
    print(result)
