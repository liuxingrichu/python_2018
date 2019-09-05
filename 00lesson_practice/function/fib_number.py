"""
    编写斐波那契数列函数
"""


def fib_nth(number):
    """
        功能描述：生成斐波那契数列前N项
        参数：
            number：项数
        返回值：元组，其元素为列表
    """
    count = 0
    a, b = 0, 1
    dst_list = []
    while count < number:
        dst_list.append(b)
        a, b = b, a + b
        count += 1
    return dst_list


def fib_in_number(number):
    """
        功能描述：生成N以内的斐波那契数列
        参数：
            number：自然数
        返回值：元组，其元素为列表
    """
    a, b = 0, 1
    tmp_list = []
    while b < number:
        tmp_list.append(b)
        a, b = b, a + b
    return tmp_list


def print_fib(sequence):
    for i in sequence:
        print(i, end=' ')
    print()


dst_seq = fib_nth(10)
print_fib(dst_seq)
dst_seq = fib_in_number(100)
print_fib(dst_seq)
