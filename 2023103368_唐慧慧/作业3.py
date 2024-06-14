from functools import wraps


# 定义一个装饰器，用于在函数执行前后进行统计操作
def statistic_decorator(func):
    # 保留原始函数的元数据
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在执行函数前显示一条消息
        print(f"开始执行 '{func.__name__}'...")

        # 计算位置参数的总和，作为一个统计示例
        total_sum = sum(args)
        print(f"计算得到提供的参数总和：{total_sum}")

        # 使用给定的参数调用原始函数
        result = func(*args, **kwargs)

        # 在函数执行完成后提供反馈
        print(f"'{func.__name__}' 已成功完成执行。")

        # 返回函数调用的结果
        return result

    # 返回修改后的函数
    return wrapper


# 将装饰器应用于这些函数
@statistic_decorator
def calculate_sum(*args):
    """计算可变数量参数的总和。"""
    return sum(args)


@statistic_decorator
def calculate_mean(*args):
    """计算可变数量参数的平均值。"""
    if args:
        return sum(args) / len(args)
    else:
        return 0


# 测试装饰过的函数
print("测试 'calculate_sum'：")
print(calculate_sum(1, 2, 3, 4, 5))  # 预期输出：15
print("\n测试 'calculate_mean'：")
print(calculate_mean(1, 2, 3, 4, 5))  # 预期输出：3.0