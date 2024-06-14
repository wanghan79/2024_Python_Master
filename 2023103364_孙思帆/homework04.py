# 导入模块，这里假设homework1, homework2, homework3是已经定义好的模块
import homework1 as hw1
import homework2 as hw2
import homework3 as hw3

def main():
    while True:
        # 显示用户菜单
        print("请选择您想执行的模块：")
        print('1 - 执行随机结构生成函数封装示例')
        print('2 - 执行随机结构生成类封装调用示例')
        print('3 - 统计方法修饰类实现')
        print('q - 退出程序')

        # 接收用户输入
        user_choice = input("请输入选项：")
        
        # 根据用户输入执行相应模块的函数
        try:
            if user_choice == '1':
                hw1.run()
            elif user_choice == '2':
                hw2.run()
            elif user_choice == '3':
                hw3.run()
            elif user_choice == 'q':
                print("退出程序。")
                break
            else:
                print("无效的输入，请重新输入。")
        except ValueError:
            print("输入错误，请输入数字。")

if __name__ == "__main__":
    main()
