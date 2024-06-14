import time
from functools import wraps

def method_stats(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Start timing
        start_time = time.time()
        # Call the actual method
        result = method(self, *args, **kwargs)
        # End timing
        end_time = time.time()
        
        # Update statistics
        method_name = method.__name__
        if method_name not in self._stats:
            self._stats[method_name] = {'count': 0, 'total_time': 0.0}
        self._stats[method_name]['count'] += 1
        self._stats[method_name]['total_time'] += (end_time - start_time)
        
        return result
    
    return wrapper

class RandomStructureGenerator:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self._stats = {}
    
    @method_stats
    def random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
    
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

# 示例调用
if __name__ == "__main__":
    generator = RandomStructureGenerator(seed=42)
    
    generator.random_string(15)
    generator.random_integer(10, 50)
    generator.random_list(8, 1, 10)
    generator.random_dict(3, 1, 20)
    generator.random_list(5, 1, 10)
    
    stats = generator.get_stats()
    for method, data in stats.items():
        print(f"方法 {method} 被调用 {data['count']} 次， 总耗时 {data['total_time']:.6f} 秒")