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

# 示例类：银行账户
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    @statistics_decorator
    def deposit(self, amount):
        """存款方法"""
        time.sleep(0.1)  # 模拟处理时间
        self.balance += amount
        return self.balance

    @statistics_decorator
    def withdraw(self, amount):
        """取款方法"""
        time.sleep(0.2)  # 模拟处理时间
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "余额不足"

    @statistics_decorator
    def get_balance(self):
        """查询余额方法"""
        time.sleep(0.05)  # 模拟处理时间
        return self.balance

# 测试
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.get_balance()
