from functools import wraps
import time

def statistics_decorator(func):
    """统计方法修饰器"""
    call_count = 0
    total_time = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count, total_time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        call_count += 1
        total_time += (end_time - start_time)

        avg_time = total_time / call_count if call_count > 0 else 0

        print(f"方法 {func.__name__} 被调用了 {call_count} 次。总执行时间：{total_time:.4f} 秒。平均执行时间：{avg_time:.4f} 秒。")

        return result

    return wrapper

# 示例类：计算器
class Calculator:
    @statistics_decorator
    def add(self, a, b):
        """加法方法"""
        time.sleep(0.1)  # 模拟处理时间
        return a + b

    @statistics_decorator
    def subtract(self, a, b):
        """减法方法"""
        time.sleep(0.2)  # 模拟处理时间
        return a - b

    @statistics_decorator
    def multiply(self, a, b):
        """乘法方法"""
        time.sleep(0.3)  # 模拟处理时间
        return a * b

    @statistics_decorator
    def divide(self, a, b):
        """除法方法"""
        time.sleep(0.1)  # 模拟处理时间
        if b == 0:
            return "除数不能为0"
        return a / b

# 测试
calculator = Calculator()
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(5, 3)
result_multiply = calculator.multiply(5, 3)
result_divide = calculator.divide(6, 3)

print(f"加法结果：{result_add}")
print(f"减法结果：{result_subtract}")
print(f"乘法结果：{result_multiply}")
print(f"除法结果：{result_divide}")

