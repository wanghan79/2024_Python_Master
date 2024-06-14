import homework1
import homework2
import homework3


def run():
    while True:
        print("请按需求输入数字进行对应模块的测试：")
        print('输入1：执行homework1：执行随机结构生成函数的封装示例')
        print('输入2：执行homework2：随机结构生成类封装调用示例')
        print('输入3：执行homework3：统计方法修饰类实现')
        print('输入q：退出程序')

        try:
            x = input()
            if x == '1':
                homework1.run()
            elif x == '2':
                homework2.run()
            elif x == '3':
                homework3.run()
            elif x == 'q':
                break
            else:
                print('请输入正确的命令')
        except:
            raise Exception('Error!')

run()
