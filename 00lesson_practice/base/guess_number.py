"""
    数字猜谜游戏
"""

object = 7

while True:
    guess = input("Please input your number: ")
    guess = int(guess)
    if guess == object:
        print("\tCongratulation!")
        print("\033[0;32m\tCongratulation!\033[0m")
        break
    elif guess > object:
        print("\tToo large! Please go on.")
        print("\033[0;31m\tToo large! Please go on.\033[0m")
    else:
        print("\tToo small! Please go on.")
        print("\033[0;31m\tToo small! Please go on.\033[0m")
