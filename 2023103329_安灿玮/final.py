# final.py
import hw1
import hw2
import hw3


def test():
    """
    测试函数，根据用户输入执行不同的模块示例或退出程序。
    """
    actions = {
        '1': hw1.run,
        '2': hw2.run,
        '3': hw3.run,
        'q': lambda: "exit"
    }

    while True:
        print("\n请按需求输入数字进行对应模块的测试：")
        print('输入1：执行：执行随机结构生成函数的封装示例')
        print('输入2：执行：随机结构生成类封装调用示例')
        print('输入3：执行：统计方法修饰类实现')
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


# 如果作为独立脚本运行，执行测试函数
if __name__ == "__main__":
    test()
