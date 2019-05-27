"""
    需求：定时程序
    例如：
        小番茄 25分钟
        大番茄 50分钟
"""

import os
import sys
import time


def set_time(interval):
    flag = True
    start_time = time.time()
    sys.stdout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
    print(flush=True)
    while flag:
        if (time.time() - start_time) // 60 // interval:
            sys.stdout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
            print(flush=True)
            print("时间到！")
            flag = False


set_time(30)            
