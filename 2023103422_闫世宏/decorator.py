def method_stats_decorator(method):
    def wrapper(*args, **kwargs):
        print(f"调用方法：{method.__name__}")
        result = method(*args, **kwargs)
        print(f"返回结果：{result}")
        return result
    return wrapper

class StatsExample:
    @method_stats_decorator
    def add(self, a, b):
        return a + b

# 测试代码
example = StatsExample()
print(example.add(3, 4))
