import time
from functools import wraps

# 定义一个统计修饰器
def stats.decorator(func):
    # wraps(func)确保装饰器不会改变原始函数的元信息
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 每次调用方法时，增加调用次数
        wrapper.calls += 1
        # 记录方法开始执行的时间
        start_time = time.time()
        try:
            # 执行原始方法
            result = func(*args, **kwargs)
            # 如果方法成功执行，增加成功调用次数
            wrapper.successful_calls += 1
        except Exception as e:
            # 如果方法抛出异常，记录异常信息
            wrapper.exceptions.append((wrapper.calls, e))
            raise e  # 重新抛出异常，让调用者知道
        finally:
            # 记录方法结束执行的时间
            end_time = time.time()
            # 计算本次调用的运行时间
            run_time = end_time - start_time
            # 累计总运行时间
            wrapper.total_time += run_time
            # 更新最大运行时间
            wrapper.max_time = max(wrapper.max_time, run_time)
            # 更新最小运行时间
            wrapper.min_time = min(wrapper.min_time, run_time)
            # 记录本次调用的参数
            wrapper.args_history.append((wrapper.calls, args, kwargs))
            # 记录本次调用的返回值
            wrapper.returns_history.append((wrapper.calls, result))
            # 打印本次调用的运行时间
            print(f"方法 {func.__name__} 被调用了 {wrapper.calls} 次，本次运行时间：{run_time:.4f} 秒")
            # 返回方法的执行结果
            return result
    # 初始化统计变量
    wrapper.calls = 0
    wrapper.successful_calls = 0
    wrapper.total_time = 0.0
    wrapper.max_time = 0.0
    wrapper.min_time = float('inf')
    wrapper.exceptions = []
    wrapper.args_history = []
    wrapper.returns_history = []
    # 返回包装后的方法
    return wrapper

# 示例方法
@stats.decorator
def complex_method(x, y):
    """一个复杂的示例方法，用于演示修饰器的使用"""
    time.sleep(1)  # 模拟一个耗时的操作
    return x + y

# 调用方法
complex_method(3, 4)
complex_method(5, 6)

# 输出统计信息
print(f"方法 {complex_method.__name__} 被调用了 {complex_method.calls} 次")
print(f"成功调用次数：{complex_method.successful_calls}")
print(f"平均运行时间：{complex_method.total_time / complex_method.calls:.4f} 秒")
print(f"最大运行时间：{complex_method.max_time:.4f} 秒")
print(f"最小运行时间：{complex_method.min_time:.4f} 秒")
print("异常记录：", complex_method.exceptions)
print("参数记录：", complex_method.args_history)
print("返回值记录：", complex_method.returns_history)

