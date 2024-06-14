from functools import wraps

def stats_decorator(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        # 函数执行前
        print(f"{function.__name__} is running...")

        # 执行一些统计（例如：计算总和）
        args_sum = sum(args)
        print(f"The sum of arguments is: {args_sum}")

        # 执行函数
        result = function(*args, **kwargs)

        # 函数执行后
        print(f"{function.__name__} finished.")

        return result

    return decorator

# 使用装饰器的示例
@stats_decorator
def calculate_sum(*args):
    return sum(args)

@stats_decorator
def calculate_mean(*args):
    if args:
        return sum(args) / len(args)
    else:
        return 0

# 测试装饰过的函数
print(calculate_sum(1, 2, 3, 4, 5))  # 输出: 15
print(calculate_mean(1, 2, 3, 4, 5))  # 输出: 3.0
