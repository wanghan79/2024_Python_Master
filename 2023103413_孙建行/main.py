# main.py
import test_1
import test_2
import test_3

def main():
    """
    主函数，根据用户输入执行不同的模块示例或退出程序。
    """
    actions = {
        '1': test_1.run,
        '2': test_2.run,
        '3': test_3.run,
        'q': lambda: "exit"
    }

    while True:
        print("\n请选择要执行的模块：")
        print('输入1：执行随机结构生成函数示例')
        print('输入2：执行随机结构生成类示例')
        print('输入3：执行统计方法装饰器示例')
        print('输入q：退出程序')

        choice = input("您的选择：").strip().lower()

        if choice in actions:
            if choice == 'q':
                print("程序已退出。")
                break
            try:
                actions[choice]()
            except Exception as e:
                print(f"执行时发生错误: {e}")
        else:
            print('无效输入，请输入1, 2, 3或q。')

if __name__ == "__main__":
    main()