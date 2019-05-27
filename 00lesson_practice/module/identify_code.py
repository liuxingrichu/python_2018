"""
    需求：生成由大写字母或数字组成的6位验证码。
"""

import random


def verify_code(number=6):
    code_list = []
    for i in range(number):
        if random.randint(0, 6) % 2:
            num = str(random.randint(0, 9))
        else:
            num = chr(random.randint(65, 90))
        code_list.append(num)
    random.shuffle(code_list)
    return ''.join(code_list)    


result = verify_code()    
print("验证码：", result)
