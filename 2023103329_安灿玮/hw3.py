# hw3.py
import time
from functools import wraps


class StatsDecorator:
    """
    统计方法调用次数和平均运行时间的修饰器类。
    """

    def __init__(self, func):
        self.func = func
        self._call_count = 0
        self._total_time = 0.0

    def __call__(self, *args, **kwargs):
        """
        调用修饰的函数，记录调用次数和运行时间。
        """
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        self._call_count += 1
        self._total_time += (end_time - start_time)
        return result

    def stats_info(self):
        """
        获取方法调用次数和平均运行时间的统计信息。
        """
        avg_time = self._total_time / self._call_count if self._call_count > 0 else 0
        return {'call_count': self._call_count, 'avg_time': avg_time}


# 示例用法
@StatsDecorator
def my_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


def run():
    """
    执行示例函数，调用被StatsDecorator修饰的函数并打印统计信息。
    """
    for _ in range(5):
        my_function((1, 'a', 3.5), [21, [23, 556]], {'key1': 'value1', 'key2': 42},
                    custom_obj=type('Custom', (), {'attr1': 'value1', 'attr2': 2})())

    print("Function stats:", my_function.stats_info())


# 如果作为独立脚本运行，执行示例函数
if __name__ == "__main__":
    run()
