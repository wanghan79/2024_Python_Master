import random
import string

def generate_random_structure(*args, **kwargs):

    # 处理位置参数
    for arg in args:
        if isinstance(arg, int):
            yield random.randint(0, arg)
        elif isinstance(arg, float):
            yield random.uniform(0, arg)
        elif isinstance(arg, str) and arg == 'string':
            yield ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif isinstance(arg, list):
            yield random.choice(arg)

    # 处理关键字参数
    for key, value in kwargs.items():
        if isinstance(value, int):
            yield random.randint(0, value)
        elif isinstance(value, float):
            yield random.uniform(0, value)
        elif isinstance(value, str) and value == 'string':
            yield ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif isinstance(value, list):
            yield random.choice(value)

# 示例
if __name__ == "__main__":
    # 创建生成器对象，传入不同类型的参数
    random_generator = generate_random_structure(10, 5.5, 'string', [1, 2, 3, 4, 5], 
                                                 key1=100, key2=50.5, key3='string', key4=['a', 'b', 'c', 'd'])
    # 迭代生成器并打印生成的随机数据
    for random_value in random_generator:
        print(random_value)