import random
import string
from functools import wraps

def calculate_sum_avg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # 提取数值元素
        if isinstance(result, list) or isinstance(result, tuple):
            numbers = [x for x in result if isinstance(x, int)]
        elif isinstance(result, dict):
            numbers = [x for x in result.values() if isinstance(x, int)]
        else:
            numbers = []

        # 计算总和和平均值
        total_sum = sum(numbers)
        avg = total_sum / len(numbers) if numbers else 0
        
        # 打印结果
        print(f'SUM: {total_sum}')
        print(f'AVG: {avg}')
        
        return result
    return wrapper

class RandomDataGenerator:
    def __init__(self, *args, **kwargs):
        #从参数中提取数量范围，若没有提供则使用默认值
        self.num_min = kwargs.get('num_min', 1)
        self.num_max = kwargs.get('num_max', 10)
        #生成随机数范围
        self.value_min = kwargs.get('value_min', 0)
        self.value_max = kwargs.get('value_max', 100)
        #生成字符串长度范围
        self.str_min_len = kwargs.get('str_min_len', 5)
        self.str_max_len = kwargs.get('str_max_len', 10)
        # 用于生成随机字符串的字符集
        self.use_uppercase = kwargs.get('use_uppercase', True)
        self.use_lowercase = kwargs.get('use_lowercase', True)
        self.use_digits = kwargs.get('use_digits', True)
        self.use_punctuation = kwargs.get('use_punctuation', False)
        
        self.characters = self._build_characters_set()

    def _build_characters_set(self):
        # 构建字符集
        characters = ''
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_punctuation:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character set must be enabled for string generation")
        
        return characters

    def generate_random_string(self, length):
        #生成随机字符串
        return ''.join(random.choice(self.characters) for _ in range(length))

    def generate_random_element(self):
        if random.choice([True, False]):
            # 生成随机数
            return random.randint(self.value_min, self.value_max)
        else:
            # 生成随机字符串
            str_len = random.randint(self.str_min_len, self.str_max_len)
            return self.generate_random_string(str_len)

    @calculate_sum_avg
    def dataSampling(self):
        if self.num_min > self.num_max:
            raise ValueError("num_min should be less than or equal to num_max")
        if self.value_min > self.value_max:
            raise ValueError("value_min should be less than or equal to value_max")
        if self.str_min_len > self.str_max_len:
            raise ValueError("str_min_len should be less than or equal to str_max_len")
        # 数字数量
        num_count = random.randint(self.num_min, self.num_max)
        # 随机类型获取
        random_elements = [self.generate_random_element() for _ in range(num_count)]
        # 随机结构获取
        structure_type = random.choice(['list', 'dict', 'tuple'])

        if structure_type == 'list':
            return random_elements
        elif structure_type == 'tuple':
            return tuple(random_elements)
        else:
            return {f'key_{i}': random_elements[i] for i in range(num_count)}
    
    def dataSamplingGenerator(self, iterations=1):
        # 生成一个新的数据样本，并通过yield语句返回该样本
        for _ in range(iterations):
            yield self.dataSampling()

# 示例调用
generator = RandomDataGenerator(num_min=5, num_max=15, value_min=10, value_max=50, str_min_len=5, str_max_len=15, use_punctuation=True)
data_generator = generator.dataSamplingGenerator(iterations=5)

for sample in data_generator:
    print(sample)

