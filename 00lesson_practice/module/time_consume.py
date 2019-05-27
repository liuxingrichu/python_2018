"""
    需求：统计生成斐波那契数列前一万项的耗时时间。
"""

import time
import numpy  


def fib(number):
    a, b, count = 1, 1, 0
    while count < number:
        # print(a, end=' ')
        a, b = b, a+b
        count += 1

arr = list()
for i in range(100):
    start_time = time.time()
    fib(10000)        
    end_time = time.time()
    times = end_time - start_time
    # print('consume time %d: '% i,  times)
    arr.append(times)

#求均值: 样本集合的中间点
arr_mean = numpy.mean(arr)
#求方差: 方差则仅仅是标准差的平方
arr_var = numpy.var(arr)
#求标准差: 样本集合的各个样本点到均值的距离之平均
arr_std = numpy.std(arr, ddof=1)
print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为：%f" % arr_std)
