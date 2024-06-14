import random


class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def OverError():
    raise MyException("操作码无效")


def structDataSampling(**kwargs):
    results = []
    for _ in range(kwargs['num']):
        result = {}
        for key, value in kwargs['struct'].items():
            if isinstance(key, int):
                tmp = random.randint(value['datarange'][0], value['datarange'][1])
            elif isinstance(key, float):
                tmp = random.uniform(value['datarange'][0], value['datarange'][1])
            elif isinstance(key, str):
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                raise MyException(f"不支持的键类型: {type(key)}")
            result[key] = tmp
        results.append(result)
    print(f"生成的{kwargs['num']}组数据为{results}")
    return results


def addSum(arr):
    result = []
    for i, data in enumerate(arr, 1):
        tmp = sum(data.values())
        result.append(tmp)
        print(f"第{i}组数据的总和为{tmp}")
    total_sum = sum(result)
    print(f"数据的总和为{total_sum}")
    result.append(total_sum)
    return result


def avg(arr):
    tmp = addSum(arr)
    total_sum = tmp[-1]
    all_values_count = len(arr) * len(arr[0])
    all_values_sum = sum(tmp[:-1])

    group_avgs = []
    for i, data in enumerate(arr, 1):
        group_avg = sum(data.values()) / len(data)
        group_avgs.append(group_avg)
        print(f"第{i}组数据的平均值为{group_avg}")

    total_avg = all_values_sum / all_values_count
    print(f"总的平均值为{total_avg}")
    return total_avg


def dataProcess(*choices):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            result = {"data": data}
            if "sum" in choices:
                result["sum"] = sum(addSum(data)[:-1])
            if "avg" in choices:
                result["avg"] = avg(data)
            return result
        return wrapper
    return decorator


def run():
    while True:
        print("请输入一个操作码，1代表求和，2代表求平均数，3代表两者都求,0退出该程序")
        x = input().strip()
        if x == '1':
            func1()
        elif x == '2':
            func2()
        elif x == '3':
            func3()
        elif x == '0':
            print("程序已退出。")
            break
        else:
            print("无效的操作码，请重新输入。")


@dataProcess("sum")
def func1(**kwargs):
    return structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                             float: {'datarange': (0, 1.0)}})


@dataProcess("avg")
def func2(**kwargs):
    return structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                             float: {'datarange': (0, 1.0)}})


@dataProcess("sum", "avg")
def func3(**kwargs):
    return structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                             float: {'datarange': (0, 1.0)}})


if __name__ == '__main__':
    try:
        run()
    except MyException as e:
        print(f"Error: {e.value}")
    except Exception as e:
        print(f"程序发生错误: {str(e)}")
