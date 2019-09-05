"""
    编写删除列表中的重复元素函数    
"""


def remove_repeat_element(seq):
    return list(set(seq))


if __name__ == "__main__":
    result = remove_repeat_element([1, 1, 2])
    print(result)
