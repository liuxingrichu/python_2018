"""
    输出 9*9 乘法口诀表
"""

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            if j == 1:
                print("%s * %s = %s" % (j, i, i*j), end=' '*2)
            else:
                print("%s * %s = %2s" % (j, i, i*j), end=' '*2)
    print()