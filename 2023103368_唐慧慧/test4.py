import test1
import test2
import test3


def run():
    while True:
        print("请按需求输入数字进行对应模块的测试：")
        print('输入1：执行test1')
        print('输入2：执行test2')
        print('输入3：执行test3')
        print('输入q：退出程序')

        try:
            x = input()
            if x == '1':
                test1.run()
            elif x == '2':
                test2.run()
            elif x == '3':
                test3.run()
            elif x == 'q':
                break
            else:
                print('请输入正确的命令')
        except:
            raise Exception('Error!')

run()
