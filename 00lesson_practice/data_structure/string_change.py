"""
    已知字符串”     hello, nice_to_meet_you      ”,
    编程实现转化成字符串“hi, nice to meet you”，使用两种编程思路实现.
"""

src_str = "     hello, nice_to_meet_you      "

# 方法一：通过字符替换
print(src_str)
dst_str = src_str.strip().replace('hello', 'hi').replace('_', ' ')
print(dst_str)

# 方法二：通过字符分割和替换
# print(src_str)
# dst_str = " ".join(src_str.strip().split('_')).replace('hello', 'hi')
# print(dst_str)

# 方法三：通过字符分割
# print(src_str)
# dst_list = ['hi,']
# tmp_list = src_str.strip().split('_')
# dst_list.append(tmp_list[0].split(',')[1].strip())
# dst_list.extend(tmp_list[1:])
# dst_str = " ".join(dst_list)
# print(dst_str)
