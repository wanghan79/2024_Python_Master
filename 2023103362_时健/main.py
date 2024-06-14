from work1 import display_tree1
from work2 import display_tree2
from work3_1 import display_tree3_1
from work3_2 import display_tree3_2
from work4 import Random_Input

rand_input = ['int', ['str'], {'key': 'str', 'sj': 'int'}]

while (True):
    index = input("输入需要展示的作业号（1、2、3、4）:")
    if index == '1':
        print()
        display_tree1(rand_input)
        print()
    elif index == '2':
        print()
        display_tree1(rand_input)
        print()
    elif index == '3':
        index = input("输入需要调用的作业（3.1、3.2）:")
        if index == '3.1':
            print()
            display_tree3_1(rand_input)
            print()
        elif index == '3.2':
            print()
            display_tree3_2(rand_input)
            print()
        else:
            print('输入错误！')
    elif index == '4':
        rand_input = Random_Input()
        print('生成随机结构为 ： ',end = '')
        print(rand_input)
    else:
        print('输入错误！')