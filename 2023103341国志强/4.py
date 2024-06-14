import homework1
import homework2
import homework3

def test():
    actions = {
        '1': homework1.run,
        '2': homework2.run,
        '3': homework3.run,
        'q': lambda: "exit"
    }

    while True:
        print("\n请按需求输入数字进行对应模块的测试：")
        print('输入1：执行homework1：执行随机结构生成函数的封装示例')
        print('输入2：执行homework2：随机结构生成类封装调用示例')
        print('输入3：执行homework3：统计方法修饰类实现')
        print('输入q：退出程序')

        x = input("您的选择：").strip().lower()
        
        if x in actions:
            if x == 'q':
                print("程序已退出。")
                break
            try:
                actions[x]()
            except Exception as e:
                print(f"执行时发生错误: {e}")
        else:
            print('无效的输入，请输入1, 2, 3或q。')

if __name__ == "__main__":
    test()
