"""
    实现对列表数据排序
"""

lst = [8, 5, 6, 3, 5, 7, 1, 9, 0, 2]

# 方法一：使用列表排序方法
# print(lst)
# lst.sort()
# print(lst)

# 方法二：使用内置函数
# print(lst)
# lst = sorted(lst)
# print(lst)

# 方法三：筛选法，每次选择最小值，将数据放置到目标列表
# print(lst)
# dst_list = []
# for i in lst[:]:
#     min_data = min(lst)
#     dst_list.append(min_data)
#     index = lst.index(min_data)
#     del lst[index]
# print(dst_list)

# 方法四：插牌法，将数值插入到指定位置
print(lst)
obj_list = [lst[0]]
for i in lst[1:]:
    if i >= obj_list[-1]:
        obj_list.append(i)
    else:
        times = -1
        for j in obj_list:
            times += 1
            if j > i:
                obj_list.insert(times, i)
                break
print(obj_list)
