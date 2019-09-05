"""
    用户认证
"""
username = 'root'
password = '1'

while True:
    user = input("Please enter your name: ")
    passwd = input("Please enter your password: ")
    if user == username and passwd == password:
        print("\tWelcome!")
        break
    else:
        print("\tPlease input right username and password!")
