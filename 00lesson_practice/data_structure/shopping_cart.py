"""
    购物车：
        需求：
        1. 启动程序后，输入用户名密码后，让用户输入购物卡金额，然后打印商品列表。
        2. 用户根据商品编号购买商品。
        3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒。
        4. 可随时退出，退出时，若用户登录成功，则打印已购买商品和余额。
"""
import getpass  # 密码密文显示

flag = False  # 是否退出标志
# 商品清单
goods_list = [
    ('python', 99),
    ('fly', 688),
    ('car', 639),
    ('coffee', 30),
    ('bike', 899)
]
username = 'Jimmy'
password = '123'
identity = False
goods_cart = []  # 购物车
money = 0

info = f"""
    测试用户：{username}
    测试密码：{password}
    退出方式：q 或 Q
"""
print(info)

while not flag:
    # 用户身份认证
    while not flag:
        user = input('Enter your name: ').strip()
        if not user:
            continue
        if 'q' == user.lower():
            flag = True
            break
        passwd = getpass.getpass('Enter your password: ').strip()
        if not passwd:
            continue
        if 'q' == passwd.lower():
            flag = True
        elif username == user and password == passwd:
            print("\tWelcome to %s for coming to shopping paradise!" % username)
            identity = True
            break
        else:
            print("\tPlease input your right username or password!")
    
    # 购物卡充值
    while not flag:
        recharge = input("Enter your recharge amount: ").strip()
        if not recharge:
            continue
        if 'q' == recharge.lower():
            flag = True
        elif recharge.isdigit():
            print("\tYou have recharged ￥{} into your shopping card, Mr. {}.".format(recharge, username))
            money = int(recharge)
            break
        else:
            print(f"\tPlease input right recharge amount, Mr. {username}.!")

    while not flag:
        # 商品信息展示
        print("shopping goods".center(30, '-'))
        for i, good in enumerate(goods_list):
            print(f"{i+1}\t{good[0]}\t\t￥{good[1]}")
        print('end'.center(30, '-'))

        # 商品购物
        choice = input("Enter your choose goods: ").strip()
        if not choice:
            continue
        if 'q' == choice.lower():
            flag = True
        elif choice.isdigit():
            if int(choice) in range(1, len(goods_list)+1):
                commodity = goods_list[int(choice)-1]
                price = commodity[-1]
                if price <= money:
                    money -= price
                    goods_cart.append(commodity)
                    print(f"\tYou have bought {commodity[0]}, Mr. {username}.")
                else:
                    print("\tPlease recharge your shopping card!")
                    print(f"\tYou only have ￥{money} now, Mr. {username}.")
            else:
                print(f"\tPlease input right commodity number, Mr. {username}!")        
        else:
            print(f"\tPlease input right commodity number, Mr. {username}!")  

# 欢送信息
print('-'*60)
if identity: 
    if goods_cart:
        print(f"{username} shopping list".center(30, '-'))
        for i, good in enumerate(goods_cart):
            print(f"{i+1}\t{good[0]}\t\t￥{good[1]}")
        print('end'.center(30, '-'))
    else:
        print(f"\nYou don't buy any commodity, Mr. {username}.")
    print(f"You have ￥{money} in your shopping card, Mr. {username}.")
    print(f"Welcome to you next time, Mr. {username}.")
else:
    print("Please input your right information next time!")
