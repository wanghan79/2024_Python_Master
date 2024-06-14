import time

def stats_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 的执行时间为: {execution_time} 秒")
        return result
    return wrapper

# 示例用法
@stats_decorator
def my_function():
    # 模拟函数执行时间较长的操作
    time.sleep(2)
    print("函数执行完毕")

my_function()
