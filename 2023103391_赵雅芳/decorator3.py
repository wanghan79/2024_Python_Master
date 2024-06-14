import random
import string
from functools import wraps

def randomize_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 随机化所有位置参数
        new_args = [randomize_element(arg) for arg in args]
        # 随机化所有关键字参数
        new_kwargs = {key: randomize_element(value) for key, value in kwargs.items()}
        # 调用原始函数，传递新的随机化参数
        return func(*new_args, **new_kwargs)
    return wrapper

def randomize_element(element):
    if isinstance(element, (list, tuple)):
        # 对于列表和元组，递归随机化每个元素
        return type(element)(randomize_element(x) for x in element)
    elif isinstance(element, dict):
        # 对于字典，递归随机化每个值
        return {key: randomize_element(value) for key, value in element.items()}
    elif isinstance(element, str):
        # 对于字符串，随机化每个字符
        return ''.join(random.choices(string.ascii_letters + string.digits, k=len(element)))
    elif isinstance(element, (int, float)):
        # 对于整数和浮点数，随机生成新的数值
        return random.randint(0, 100) if isinstance(element, int) else random.uniform(0, 100)
    elif hasattr(element, '__dict__'):
        # 对于拥有 __dict__ 属性的对象（如自定义类实例），递归随机化其属性
        new_element = element.__class__()
        for attr, value in element.__dict__.items():
            setattr(new_element, attr, randomize_element(value))
        return new_element
    else:
        # 对于其他类型的对象，保持不变
        return element

@randomize_input
def my_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# 测试
original_args = (5, 'b', 2.0), [10, [33, 220]], {'key1': 'value1', 'key2': 33}, type('Custom', (), {'attr1': 'value1', 'attr2': 3})()
randomized_args = my_function(*original_args)