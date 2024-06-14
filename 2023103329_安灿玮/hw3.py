import random
import time


class StatsDecorator:
    """
    统计方法调用次数和平均执行时间的装饰器类。
    """

    def __init__(self, func):
        self.func = func
        self._call_count = 0
        self._total_time = 0.0

    def __call__(self, *args, **kwargs):
        """
        调用装饰器时执行的方法。
        """
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        self._call_count += 1
        self._total_time += (end_time - start_time)
        return result

    def stats_info(self):
        """
        获取统计信息，包括调用次数和平均执行时间。
        """
        avg_time = self._total_time / self._call_count if self._call_count > 0 else 0
        return {'call_count': self._call_count, 'avg_time': avg_time}


# 示例用法
@StatsDecorator
def my_function(*args, **kwargs):
    """
    示例函数，打印参数并模拟执行时间。
    """
    print("Args:", args)
    print("Kwargs:", kwargs)
    time.sleep(random.uniform(0.1, 0.5))  # 模拟执行时间随机延迟


def run():
    """
    执行示例函数，多次调用带装饰器的函数并打印统计信息。
    """
    for _ in range(5):
        my_function((1, 'a', 3.5), [21, [23, 556]], {'key1': 'value1', 'key2': 42},
                    custom_obj=type('Custom', (), {'attr1': 'value1', 'attr2': 2})())

    print("Function stats:", my_function.stats_info())


# 如果作为独立脚本运行，执行示例函数
if __name__ == "__main__":
    run()
