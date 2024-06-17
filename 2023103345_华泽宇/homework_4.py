import random
from functools import wraps

def random_structure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"生成的随机结构：{result}")
        return result
    return wrapper

@random_structure_decorator
def create_library_structure(categories):
    library_structure = {}
    for category in categories:
        num_books = random.randint(100, 500)  # 每个分类的书籍数量在100到500之间
        num_authors = random.randint(1, 20)  # 每个分类的作者数量在1到20之间
        authors = [f"作者{random.randint(1, 50)}" for _ in range(num_authors)]
        library_structure[category] = {
            "分类名称": category,
            "书籍数量": num_books,
            "作者列表": authors
        }
    return library_structure

# 测试函数
def main():
    categories = ["小说", "科普", "历史", "艺术"]  # 使用不同的书籍分类
    create_library_structure(categories)

if __name__ == "__main__":
    main()
