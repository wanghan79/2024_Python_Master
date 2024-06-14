'''
Author: Runchang Liang
Date: 2024-06-14 11:22:40
LastEditors: liangrc666@nenu.edu.cn
LastEditTime: 2024-06-14 11:26:06
FilePath: \2023103409_FinalProject\final_project\MyGenerator.py
Description: 

Copyright (c) 2024 by ${liangrc666@nenu.edu.cn}, All Rights Reserved. 
'''

import random
from faker import Faker

class RandomDataSampler:
    def __init__(self):
        self.fake = Faker()
        self._data_sum = 0
        self._data_count = 0
        self.fake_methods = {
            'name': None,
            'email': None,
            'age': lambda: None
        }

    def _record_data(self, data):
        # 累加所有数字类型的数据
        for value in data:
            if isinstance(value, (int, float)):
                self._data_sum += value
                self._data_count += 1

    def _generate_random_int(self, datarange):
        return random.randint(*datarange)

    def _generate_random_float(self, datarange):
        return random.uniform(*datarange)

    def _generate_random_str(self, datarange, length):
        return ''.join(random.choice(datarange) for _ in range(length))

    def _generate_fake_data(self, key):
        # 确保调用Faker的相应方法
        fake_methods = {
            'name': self.fake.name,
            'email': self.fake.email,
            'age': lambda: self.fake.random_int(18, 80)
        }
        return fake_methods.get(key, lambda: None)()  # 使用get方法并提供一个默认的lambda

    def data_saving_decorator(method):
        def wrapper(self, *args, **kwargs):
            # 装饰器应该能够处理生成器
            for data in method(self, *args, **kwargs):
                self._record_data(data)  # 记录数据
                yield data
        return wrapper

    @data_saving_decorator
    def struct_data_sampling(self, **kwargs):
        num = kwargs.get('num', 1)  # 获取生成数量，默认为1
        for _ in range(num):
            element = []
            for key, value in kwargs.items():
                if key == 'RandomInt':
                    element.append(self._generate_random_int(value['datarange']))
                elif key == 'RandomFloat':
                    element.append(self._generate_random_float(value['datarange']))
                elif key == 'RandomStr':
                    element.append(self._generate_random_str(value['datarange'], value.get('len', 5)))  # 给定默认长度
                elif key in self.fake_methods:
                    element.append(self._generate_fake_data(key))
            yield element  # 产生元素

    @property
    def sum_data(self):
        return self._data_sum

    @property
    def average_data(self):
        return self._data_sum / self._data_count if self._data_count else 0

# 使用示例
if __name__ == "__main__":
    sampler = RandomDataSampler()
    try:
        data_kwargs = {
            'num': 5,
            'RandomInt': {'datarange': (1, 100)},
            'RandomFloat': {'datarange': (1.0, 100.0)},
            'RandomStr': {'datarange': ('a', 'b', 'c', 'd', 'e'), 'len': 4},
            'name': True,
            'email': True,
            'age': True
        }
        generated_data = list(sampler.struct_data_sampling(**data_kwargs))
        print("Generated Data:", generated_data)
        print("Sum of Data:", sampler.sum_data)
        print("Average of Data:", sampler.average_data)
    except Exception as e:
        print(f"An error occurred: {e}")