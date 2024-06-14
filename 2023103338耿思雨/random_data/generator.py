import random
from functools import wraps


class DataStats:
    @staticmethod
    def calculate_stats(samples):
        age_sum = sum(sample['年龄'] for sample in samples)
        weight_sum = sum(sample['体重'] for sample in samples)
        mixed_data_int_sum = sum(sample['混合数据'][0] for sample in samples)
        mixed_data_float_sum = sum(sample['混合数据'][2] for sample in samples)

        stats = {
            '年龄总和sum': age_sum,
            '年龄平均值avg': age_sum / len(samples) if samples else 0,
            '体重总和sum': weight_sum,
            '体重平均值avg': weight_sum / len(samples) if samples else 0,
            '混合数据int类型总和': mixed_data_int_sum,
            '混合数据int类型平均值': mixed_data_int_sum / len(samples) if samples else 0,
            '混合数据float类型总和': mixed_data_float_sum,
            '混合数据float类型平均值': mixed_data_float_sum / len(samples) if samples else 0
        }

        return stats


class RandomDataGenerator:
    def __init__(self, data_types, data_cons):
        self.data_types = data_types
        self.data_cons = data_cons

    def random_data(self):
        data = {}
        for data_con, data_type in zip(self.data_cons, self.data_types):
            if data_type == 'str':
                data[data_con] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            elif data_type == 'int':
                data[data_con] = random.randint(1, 100)
            elif data_type == 'float':
                data[data_con] = round(random.uniform(100.0, 200.0), 2)
            elif data_type == 'dict':
                hobbies = ['唱歌', '跳舞', '写作', '弹吉他']
                data[data_con] = random.choice(hobbies)
            elif data_type == 'tuple':
                data[data_con] = (random.randint(1, 100), ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)),
                                  round(random.uniform(100.0, 200.0), 2))
        return data

    def multiple_samples(self, num):
        samples = []
        for _ in range(num):
            sample = self.random_data()
            samples.append(sample)
        return samples