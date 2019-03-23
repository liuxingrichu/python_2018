"""
    获取列表中索引为偶数的元素
"""

src_list = [1, 2, 1, 1, 3, 1, 4, 5, 6]

# 方法一：检测索引是否为偶数
# print(src_list)
# index_num = 0
# dst_list = list()
# for data in src_list:
#     if index_num % 2 == 0:
#         dst_list.append(data)
#     index_num += 1
# print(dst_list)

# 方法二：使用序列切片
print(src_list)
dst_list = list()
for data in src_list[::2]:
    dst_list.append(data)
print(dst_list)