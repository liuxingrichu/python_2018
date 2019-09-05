"""
    功能：用面向对象编程方式，编写二分查找程序，并调用运行，输出运行结果。
"""


class BinarhSearch(object):
    """
        二分查找
    """
    def get_index_ascend(self, src_list, number):
        """
            升序序列二分查找，返回索引
        """
        start = 0
        end = len(src_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if src_list[mid] == number:
                return mid
            elif src_list[mid] > number:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def get_index_descend(self, src_list, number):
        """
            降序序列二分查找，返回索引
        """
        start = 0
        end = len(src_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if src_list[mid] == number:
                return mid
            elif src_list[mid] > number:
                start = mid + 1
            else:
                end = mid - 1
        return -1

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6]
    object = 6
    b = BinarhSearch()
    result = b.get_index_ascend(test_list, object)
    if result >= 0:
        print("元素%s, 在目标列表的第 %d 个位置。" % (object, result + 1))
    else:
        print("元素%s, 在目标列表中不存在！" % object)

    test_list = [1, 2, 3, 4, 5, 6]
    test_list.sort(reverse=True)
    object = 6
    b = BinarhSearch()
    result = b.get_index_descend(test_list, object)
    if result >= 0:
        print("元素%s, 在目标列表的第 %d 个位置。" % (object, result + 1))
    else:
        print("元素%s, 在目标列表中不存在！" % object)
