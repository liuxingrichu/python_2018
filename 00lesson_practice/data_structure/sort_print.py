"""
    输入三个整数x,y,z，请把这三个数由小到大输出。 
"""
NUM = 3
dst_list = list()


while True:
    src_str = input("Enter integer: ").strip()
    if not src_str:
        continue
    if src_str.isdigit():
        dst_list.append(int(src_str))
    else:
        print("\tPlease input integer number!")
    if len(dst_list) >= NUM:
        break
print(dst_list)
dst_list.sort()
print(dst_list)
