import random
import string
from functools import wraps

class DataGenerator:
    def __init__(self, data_types):
        self.data_types = data_types  # 存储输入的数据类型和数量
        self.result = {}  # 存储生成的数据结构

    def generate_data(self):
        for data_type, num in self.data_types.items():  # 遍历输入的数据类型和数量
            if data_type == 'int':  # 如果数据类型是int
                self.result[data_type] = [random.randint(-1000, 1000) for _ in range(num)]  # 随机生成指定数量的int类型的数据并添加到结果字典中
            elif data_type == 'float':  # 如果数据类型是float
                self.result[data_type] = [random.uniform(-1000.0, 1000.0) for _ in range(num)]  # 随机生成指定数量的float类型的数据并添加到结果字典中
            elif data_type == 'str':  # 如果数据类型是str
                self.result[data_type] = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20))) for _ in range(num)]  # 随机生成指定数量的str类型的数据并添加到结果字典中
            elif data_type == 'list':  # 如果数据类型是list
                self.result[data_type] = [[random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))] for _ in range(num)]  # 随机生成指定数量的list类型的数据并添加到结果字典中
            elif data_type == 'tuple':  # 如果数据类型是tuple
                self.result[data_type] = [tuple([random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))]) for _ in range(num)]  # 随机生成指定数量的tuple类型的数据并添加到结果字典中
            elif data_type == 'set':  # 如果数据类型是set
                self.result[data_type] = [set([random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))]) for _ in range(num)]  # 随机生成指定数量的set类型的数据并添加到结果字典中
            elif data_type == 'dict':  # 如果数据类型是dict
                self.result[data_type] = [dict(zip([random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))], [random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))])) for _ in range(num)]  # 随机生成指定数量的dict类型的数据并添加到结果字典中
            elif data_type == 'bool':  # 如果数据类型是bool
                self.result[data_type] = [random.choice([True, False]) for _ in range(num)]  # 随机生成指定数量的bool类型的数据并添加到结果字典中
        return self.result  # 返回结果字典

def count_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        count = sum([len(v) for v in result.values()])
        print(f"生成了{count}个数据")
        return result
    return wrapper

data_types = input("请输入数据类型和数量，用逗号分隔，例如：int:3,float:2,str:4 ")
data_dict = {}
for item in data_types.split(','):
    key, value = item.split(':')
    data_dict[key] = int(value)
generator = DataGenerator(data_dict)
result = count_decorator(generator.generate_data)()
for r in result:
    print({r: result[r]})  # 输出结果的格式为{'数据类型名称':[元素1,元素2，......]}这种格式，每种类型的数据占一行
