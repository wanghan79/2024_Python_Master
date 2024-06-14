import homework1
import homework2
import homework3


def run():
    while True:
        print("请按需求输入数字进行对应模块的测试：")
        print('输入1：执行homework1：执行封装函数的调用示例')
        print('输入2：执行homework2：采用修饰器技术对作业1随机数据结构生成函数进行修饰，执行所有生成随机数的不同操作的调用示例')
        print('输入3：执行homework3：')
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
