"""
    删除列表中的重复元素
"""

lst = [1, 2, 4, 1, 2, 3, 3, 5]

# 方法一：利用集合去除重复元素
# print(lst)
# lst = list(set(lst))
# print(lst)

# 方法二：将数据排序，删除相应重复元素
# print(lst)
# lst.sort()
# for i in lst:
#     index = lst.index(i)
#     if index < len(lst) - 1:
#         if lst[index] == lst[index + 1]:
#             del lst[index+1]
# print(lst)

# 方法三：统计重复元素次数，并将其删除至无重复元素
# print(lst)
# for i in lst:
#     while lst.count(i) > 1:
#         lst.remove(i)
# print(lst)

# 方法四：依次取元素，遍历列表，删除与其重复的元素
print(lst)
times = -1
for i in lst:
    times += 1
    count = -1
    for j in lst[times+1:]:
        count += 1
        if i == j:
            del lst[times + count + 1]
print(lst)            