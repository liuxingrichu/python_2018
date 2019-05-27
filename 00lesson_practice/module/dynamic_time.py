"""
    需求：动态输出系统时间
"""

import sys
import time

while True:
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sys.stdout.write(now)
    # \r 表示将光标的位置回退到本行的开头位置
    # flush=True 表示实时刷新
    print('\r', end='', flush=True)
    time.sleep(1)
