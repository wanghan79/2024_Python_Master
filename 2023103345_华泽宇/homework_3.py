import random
import time


class StatsDecorator:

    def __init__(self, func):
        self.func = func
        self._call_count = 0
        self._total_time = 0.0

    def __call__(self, *args, **kwargs):

        start_time = time.time()  # 记录开始时间
        result = self.func(*args, **kwargs)  # 执行被装饰的函数
        end_time = time.time()  # 记录结束时间

        self._call_count += 1
        self._total_time += (end_time - start_time)
        return result

    def stats_info(self):

        avg_time = self._total_time / self._call_count if self._call_count > 0 else 0
        return {'call_count': self._call_count, 'avg_time': avg_time}


@StatsDecorator
def example_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    time.sleep(random.uniform(0.1, 0.5))  # 模拟随机执行时间延迟


def main():
    """
    执行示例函数，多次调用带装饰器的函数并打印统计信息。
    """
    for _ in range(5):
        example_function((1, 'a', 3.5), [21, [23, 556]], {'key1': 'value1', 'key2': 42},
                         custom_obj=type('Custom', (), {'attr1': 'value1', 'attr2': 2})())

    print("Function stats:", example_function.stats_info())
if __name__ == "__main__":
    main()