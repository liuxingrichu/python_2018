"""
    功能：购物车
    需求：
        1. 启动程序后，输入用户名密码后，让用户输入购物卡金额，然后打印商品列表。
        2. 用户根据商品编号，购买商品。
        3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒。
        4. 可随时退出，退出时，若用户登录成功，则打印已购买商品和余额。
"""
import getpass
import os

USERNAME = "1"
PASSWORD = '1'
goods_list = [('python', 99), ('fly', 688), ('car', 639), ('coffee', 30),
              ('bike', 899)]


def user_confirm():
    """
        功能：用户身份认证
    """
    while True:
        username = input('Enter your name: ').strip()
        if not username:
            continue
        if 'q' == username.lower():
            return False
        password = getpass.getpass('Enter your password: ').strip()
        if not password:
            continue
        if 'q' == password.lower():
            return False
        elif USERNAME == username and PASSWORD == password:
            print("\tWelcome to %s for coming to shopping paradise!" %
                  username)
            return True
        else:
            print("\tPlease input your right username or password!")


def charge(username=USERNAME):
    """
        功能：购物卡充值
    """
    while True:
        recharge = input("Enter your recharge amount: ").strip()
        if not recharge:
            continue
        if 'q' == recharge.lower():
            return False
        elif recharge.isdigit():
            print("\tYou have recharged ￥{} into your shopping card, Mr. {}.".
                  format(recharge, username))
            return int(recharge)
        else:
            print(f"\tPlease input right recharge amount, Mr. {USERNAME}.!")


def print_goods(goods_list):
    """
        功能：输出商品信息
    """
    print("shopping goods".center(30, '-'))
    for i, good in enumerate(goods_list):
        print(f"{i+1}\t{good[0]}\t\t￥{good[1]}")
    print('end'.center(30, '-'))


def buy(money, goods_cart, username=USERNAME):
    while True:
        print_goods(goods_list)
        choice = input("Enter your choice goods: ").strip()
        if not choice:
            continue
        if 'q' == choice.lower():
            return money
        elif choice.isdigit():
            if int(choice) in range(1, len(goods_list) + 1):
                commodity = goods_list[int(choice) - 1]
                price = commodity[-1]
                if price <= money:
                    money -= price
                    goods_cart.append(commodity)
                    print(f"\tYou have bought {commodity[0]}, Mr. {username}.")
                else:
                    print("\tPlease recharge your shopping card!")
                    print(f"\tYou only have ￥{money} now, Mr. {username}.")
            else:
                print(
                    f"\tPlease input right commodity number, Mr. {username}!")
        else:
            print(f"\tPlease input right commodity number, Mr. {username}!")


def welcome(identity, goods_cart, money, username=USERNAME):
    # 欢送信息
    print('-' * 60)
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


def main():
    goods_cart = []  # 购物车
    money = 0
    flag = True
    while flag:
        identity = user_confirm()
        if identity:
            money = charge()
            if not money:
                money = 0
                flag = False
        else:
            flag = False
        while flag:
            money = buy(money, goods_cart)
            flag = False

    welcome(identity, goods_cart, money)
    # 调用Windows系统命令
    os.system("pause")


if __name__ == "__main__":
    main()
