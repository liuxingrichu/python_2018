"""
    编写列表元素偶数之和函数    
"""


def get_sum(seq):
    """
        功能：获取列表中的偶数元素之后
        参数：
            seq：列表
        返回值：偶数之和
    """
    sum = 0
    for i in seq:
        if not i % 2:
            sum += i
    return sum


if __name__ == "__main__":
    test_list = [i for i in range(101)]
    print(get_sum(test_list))
