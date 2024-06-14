'''
Author: Runchang Liang
Date: 2024-06-14 10:45:46
LastEditors: liangrc666@nenu.edu.cn
LastEditTime: 2024-06-14 11:29:40
FilePath: \2023103409_FinalProject\work3\MyDecorator.py
Description: 

Copyright (c) 2024 by ${liangrc666@nenu.edu.cn}, All Rights Reserved. 
'''

import random
from faker import Faker

class RandomDataSampler:
    def __init__(self):
        self.fake = Faker()
        self.generated_data = []  # 用于存储生成的数据

    def _generate_random_int(self, datarange):
        return random.randint(*datarange)

    def _generate_random_float(self, datarange):
        return random.uniform(*datarange)

    def _generate_random_str(self, datarange, length):
        return ''.join(random.choice(datarange) for _ in range(length))

    def _generate_fake_data(self, key):
        if key == 'name':
            return self.fake.name()
        elif key == 'email':
            return self.fake.email()
        elif key == 'age':
            return self.fake.random_int(min=18, max=80)
        else:
            raise ValueError(f"Unsupported fake data type: {key}")
    
    def _store_data_decorator(func):
        def wrapper(self, *args, **kwargs):
            self.summed_data = func(self, *args, **kwargs)
            return self.summed_data
        return wrapper

    @_store_data_decorator  # 应用装饰器
    def struct_data_sampling(self, **kwargs):
        num = kwargs.get('num', -1)
        if num == -1:
            raise ValueError("Wrong number input")

        result = []
        for _ in range(num):
            element = []
            for key, value in kwargs.items():
                if key == 'RandomInt':
                    element.append(self._generate_random_int(value['datarange']))
                elif key == 'RandomFloat':
                    element.append(self._generate_random_float(value['datarange']))
                elif key == 'RandomStr':
                    element.append(self._generate_random_str(value['datarange'], value['len']))
                elif key in ['name', 'email', 'age']:
                    element.append(self._generate_fake_data(key))
                else:
                    continue
            result.append(element)
            self.generated_data.append(element)  # 存储生成的数据
        return result

    def sum_data(self):
        if not self.generated_data:
            return 0
        # 只对数字类型求和
        return sum(item for sublist in self.generated_data for item in sublist if isinstance(item, (int, float)))

    def average_data(self):
        if not self.generated_data:
            return 0
        total_sum = self.sum_data()
        total_count = sum(1 for sublist in self.generated_data for item in sublist if isinstance(item, (int, float)))
        return total_sum / total_count

# 使用示例
if __name__ == "__main__":
    sampler = RandomDataSampler()
    try:
        result = sampler.struct_data_sampling(num=5,
                                              RandomInt={"datarange": [1, 100]},
                                              RandomFloat={"datarange": [1.0, 100.0]},
                                              RandomStr={"datarange": ['a', 'b', 'c', 'd', 'e'], "len": 4},
                                              name=True,
                                              email=True,
                                              age=True)
        print("Generated Data:", result)
        print("Sum of Data:", sampler.sum_data())
        print("Average of Data:", sampler.average_data())
    except Exception as e:
        print(f"An error occurred: {e}")