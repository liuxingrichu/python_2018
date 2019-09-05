"""
    功能：请函数编写阶乘程序
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def multi_nth(n):
    multi = 1
    for i in range(1, n + 1):
        multi *= i
    return multi


if __name__ == "__main__":
    test_num = 8
    print(factorial(test_num))
    print(multi_nth(test_num))
