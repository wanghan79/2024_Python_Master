import random
import string
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
def randomedelta():
    """
    生成一个随机的timedelta对象。
    """
    days = random.randint(0, 365)
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def generate_random_data(data):
    """
    根据输入数据的类型和结构生成随机数据。
    """
    # 如果输入数据是整数类型，生成一个0到100之间的随机整数
    if isinstance(data, int):
        return random.randint(0, 100)
    # 如果输入数据是浮点数类型，生成一个0到10000之间的随机浮点数
    elif isinstance(data, float):
        return random.uniform(0, 10000)
    # 如果输入数据是字符串类型，生成一个同样长度的随机字符串
    elif isinstance(data, str):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(data)))
    # 如果输入数据是列表类型，递归地调用本函数生成一个列表
    elif isinstance(data, list):
        return [generate_random_data(item) for item in data]
    # 如果输入数据是元组类型，递归地调用本函数生成一个元组
    elif isinstance(data, tuple):
        return tuple(generate_random_data(item) for item in data)
    # 如果输入数据是字典类型，递归地调用本函数生成一个字典
    elif isinstance(data, dict):
        return {key: generate_random_data(value) for key, value in data.items()}
    # 如果输入数据是布尔类型，随机选择True或False
    elif isinstance(data, bool):
        return random.choice([True, False])
    # 如果输入数据是日期时间类型，生成一个随机日期时间
    elif isinstance(data, datetime):
        return datetime.now() - randomedelta(days=random.randint(0, 365))
    # 如果输入数据是日期类型，生成一个随机日期
    elif isinstance(data, date):
        return date.today() - randomedelta(days=random.randint(0, 365))
    # 如果输入数据是集合类型，递归地调用本函数生成一个集合
    elif isinstance(data, set):
        return {generate_random_data(item) for item in data}
    else:
        return None

def generate_original_data(num, template_data):
    """
    根据提供的模板数据生成指定数量的随机数据记录。
    """
    # 生成一个列表，包含num个根据模板数据生成的随机数据
    return [generate_random_data(template_data) for _ in range(num)]

# 模板数据结构
same_data = {
    "name": "Alice",            # 姓名
    "age": 18,                  # 年龄
    "scores": [10, 20, 30],     # 分数列表
    "info": {                   # 个人信息字典
        "city": "New York",      # 城市
        "email": "alice@example.com",  # 邮箱
        "is_student": True       # 是否是学生
    },
    "zhuanye": "jisuanji",       # 专业
    "graduation_date": date(2023, 6, 30),  # 毕业日期
    "last_login": datetime.now(),  # 上次登录时间
    "courses": {"math", "physics"}  # 所选课程集合
}

# 生成随机数据记录
random_data = generate_original_data(10, same_data)
for data in random_data:
    print(data)

