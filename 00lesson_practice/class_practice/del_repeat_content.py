"""
    功能：用面向对象编程方式，编写列表元素去重程序，并调用运行，输出运行结果.
"""


class RemoveContent(object):
    """
        列表元素去重
    """
    def get_unique_element(self, src_list):
        return list(set(src_list))


if __name__ == "__main__":
    r = RemoveContent()
    result = r.get_unique_element([1, 1, 2, 1])
    print(result)
