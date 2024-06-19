import random
import string

def random_value():
    """生成一个随机值，可以是整数、浮点数或字符串。"""
    value_type = random.choice(['int', 'float', 'str'])
    if value_type == 'int':
        return random.randint(0, 100)
    elif value_type == 'float':
        return random.uniform(0, 100)
    elif value_type == 'str':
        return ''.join(random.choices(string.ascii_letters, k=5))

def random_structure(depth=3):
    """生成一个随机嵌套的结构，包含列表和字典。"""
    if depth == 0:
        return random_value()

    structure_type = random.choice(['list', 'dict'])
    if structure_type == 'list':
        return [random_structure(depth - 1) for _ in range(random.randint(2, 5))]
    elif structure_type == 'dict':
        return {random_value(): random_structure(depth - 1) for _ in range(random.randint(2, 5))}

# 示例调用
random.seed(5)  # 设置随机种子以便复现结果
generated_structure = random_structure()
print(generated_structure)
