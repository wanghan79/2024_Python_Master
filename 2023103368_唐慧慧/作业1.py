# coding=utf-8
import random
import string


def generate_random_value(value):
    """
    根据输入值的类型生成对应的随机值
    """
    if isinstance(value, int):
        # 如果输入是整数，生成0到100之间的随机整数
        return random.randint(0, 100)
    elif isinstance(value, float):
        # 如果输入是浮点数，生成0到100之间的随机浮点数
        return random.uniform(0, 100)
    elif isinstance(value, str):
        # 如果输入是字符串，生成一个长度与输入相同的随机小写字母字符串
        return ''.join(random.choices(string.ascii_lowercase, k=len(value)))
    elif isinstance(value, (list, tuple)):
        # 如果输入是列表或元组，递归生成随机值列表或元组
        return type(value)([generate_random_value(item) for item in value])
    elif isinstance(value, dict):
        # 如果输入是字典，递归生成包含随机值的字典
        return {key: generate_random_value(value) for key, value in value.items()}
    else:
        # 对于其他类型，返回None
        return None

    # 测试示例


original_data = {
    "name": "Kitty",
    "age": 20,
    "major": "computer",
    "scores": [80, 90, 88],
    "info": {
        "city": "Changchun",
        "email": "Kitty@em.com",
        "roommates": ["Alen", "Nanxi", "Make"]
    }
}

# 生成并打印两个随机数据实例
random_data_list = [generate_random_value(original_data) for _ in range(2)]
for data in random_data_list:
    print(data)