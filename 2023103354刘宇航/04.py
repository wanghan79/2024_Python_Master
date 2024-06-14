import random
import string
import time
from functools import wraps

# 定义统计方法调用的装饰器
def method_stats(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()
        
        method_name = method.__name__
        if method_name not in self._stats:
            self._stats[method_name] = {'count': 0, 'total_time': 0.0}
        self._stats[method_name]['count'] += 1
        self._stats[method_name]['total_time'] += (end_time - start_time)
        
        return result
    
    return wrapper

# 随机结构生成类
class RandomStructureGenerator:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self._stats = {}
    
    @method_stats
    def random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
    
    @method_stats
    def random_integer(self, min_val=0, max_val=100):
        return random.randint(min_val, max_val)
    
    @method_stats
    def random_list(self, length=10, min_val=0, max_val=100):
        return [self.random_integer(min_val, max_val) for _ in range(length)]
    
    @method_stats
    def random_dict(self, num_keys=5, min_val=0, max_val=100):
        keys = [self.random_string(5) for _ in range(num_keys)]
        return {key: self.random_integer(min_val, max_val) for key in keys}
    
    def get_stats(self):
        return self._stats
    
    def generate_random_structure(self, structure_type, **kwargs):
        if structure_type == 'string':
            yield self.random_string(**kwargs)
        elif structure_type == 'integer':
            yield self.random_integer(**kwargs)
        elif structure_type == 'list':
            yield self.random_list(**kwargs)
        elif structure_type == 'dict':
            yield self.random_dict(**kwargs)
        else:
            raise ValueError("Unsupported structure type")

# 示例调用
if __name__ == "__main__":
    generator = RandomStructureGenerator(seed=42)
    
    # 生成随机字符串
    string_gen = generator.generate_random_structure('string', length=15)
    print("随机字符串:", next(string_gen))
    
    # 生成随机整数
    int_gen = generator.generate_random_structure('integer', min_val=10, max_val=50)
    print("随机整数:", next(int_gen))
    
    # 生成随机列表
    list_gen = generator.generate_random_structure('list', length=8, min_val=1, max_val=10)
    print("随机列表:", next(list_gen))
    
    # 生成随机字典
    dict_gen = generator.generate_random_structure('dict', num_keys=3, min_val=1, max_val=20)
    print("随机字典:", next(dict_gen))
    
    # 获取统计数据
    stats = generator.get_stats()
    for method, data in stats.items():
        print(f"方法 {method} 被调用 {data['count']} 次，总耗时 {data['total_time']:.6f} 秒")