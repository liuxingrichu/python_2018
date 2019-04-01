"""
    功能：三级菜单
    要求：
        可依次选择进入各子菜单；
        可从任意一层，回退到上一层；
        可从任意一层，退出程序。
"""

zone = {
    '山东' : {
        '青岛' : ['四方','黄岛','崂山','李沧','城阳'],
        '济南' : ['历城','槐荫','高新','长青','章丘'],
        '烟台' : ['龙口','莱山','牟平','蓬莱','招远']
    },
    '江苏' : {
        '苏州' : ['沧浪','相城','平江','吴中','昆山'],
        '南京' : ['白下','秦淮','浦口','栖霞','江宁'],
        '无锡' : ['崇安','南长','北塘','锡山','江阴']
    },
    '浙江' : {
        '杭州' : ['西湖','江干','下城','上城','滨江'],
        '宁波' : ['海曙','江东','江北','镇海','余姚'],
        '温州' : ['鹿城','龙湾','乐清','瑞安','永嘉']
    }
}

flag = True
LAST = 3
cache_list = [zone]

while flag:
    for k in cache_list[-1]:
        print(k)
    choice = input("Please enter your choice：（退出：q，返回：b） ").strip()
    if not choice:
        continue
    if 'q' == choice:
        print("\tWelcome to you next time, byebye!")
        flag = False
    elif 'b' == choice:
        if len(cache_list) > 1:
            cache_list.pop()
        else:
            print("\tYou have arrived the top floor!")
    elif choice not in cache_list[-1]:
        print("\tPlease input right content!")
        continue
    else:
        if len(cache_list) < LAST:
            cache_list.append(cache_list[-1][choice])
        else:
            print("\tYou have arrived the last floor!")
