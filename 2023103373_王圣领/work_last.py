import random
from functools import wraps

def random_structure_decorator(func):
    """随机结构生成器的修饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"生成的随机结构：{result}")
        return result
    return wrapper

@random_structure_decorator
def generate_library_structure(categories):
    """生成图书馆书籍分类结构的函数"""
    library_structure = {}
    for category in categories:
        books = random.randint(100, 500)  # 假设每个分类的书籍数量在100到500之间
        authors = [f"作者{random.randint(1, 50)}"] * random.randint(1, 20)  # 假设作者数量在1到20之间
        library_structure[category] = {
            "分类名称": category,
            "书籍数量": books,
            "作者列表": authors
        }
    return library_structure

# 测试
categories = ["小说", "科普", "历史", "艺术"]  # 使用不同的书籍分类
generate_library_structure(categories)

