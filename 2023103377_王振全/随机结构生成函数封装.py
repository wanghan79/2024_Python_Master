import random
import string

def generate_data(data_types):
    result = {}  # 存储生成的数据结构
    for data_type, num in data_types.items():  # 遍历输入的数据类型和数量
        if data_type == 'int':  # 如果数据类型是int
            result[data_type] = [random.randint(-1000, 1000) for _ in range(num)]  # 随机生成指定数量的int类型的数据并添加到结果字典中
        elif data_type == 'float':  # 如果数据类型是float
            result[data_type] = [random.uniform(-1000.0, 1000.0) for _ in range(num)]  # 随机生成指定数量的float类型的数据并添加到结果字典中
        elif data_type == 'str':  # 如果数据类型是str
            result[data_type] = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20))) for _ in range(num)]  # 随机生成指定数量的str类型的数据并添加到结果字典中
        elif data_type == 'list':  # 如果数据类型是list
            result[data_type] = [[random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))] for _ in range(num)]  # 随机生成指定数量的list类型的数据并添加到结果字典中
        elif data_type == 'tuple':  # 如果数据类型是tuple
            result[data_type] = [tuple([random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))]) for _ in range(num)]  # 随机生成指定数量的tuple类型的数据并添加到结果字典中
        elif data_type == 'set':  # 如果数据类型是set
            result[data_type] = [set([random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))]) for _ in range(num)]  # 随机生成指定数量的set类型的数据并添加到结果字典中
        elif data_type == 'dict':  # 如果数据类型是dict
            result[data_type] = [dict(zip([random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))], [random.choice([random.randint(-1000, 1000), random.uniform(-1000.0, 1000.0), ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))]) for _ in range(random.randint(1, 20))])) for _ in range(num)]  # 随机生成指定数量的dict类型的数据并添加到结果字典中
        elif data_type == 'bool':  # 如果数据类型是bool
            result[data_type] = [random.choice([True, False]) for _ in range(num)]  # 随机生成指定数量的bool类型的数据并添加到结果字典中
    return result  # 返回结果字典

data_types = input("请输入数据类型和数量，用逗号分隔，例如：int:3,float:2,str:4 ")
data_dict = {}
for item in data_types.split(','):
    key, value = item.split(':')
    data_dict[key] = int(value)
result = generate_data(data_dict)
for r in result:
    print({r: result[r]})  # 输出结果的格式为{'数据类型名称':[元素1,元素2，......]}这种格式，每种类型的数据占一行
