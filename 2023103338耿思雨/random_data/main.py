from random_data.generator import RandomDataGenerator, DataStats
def generate_samples(num_samples):
    data_types = ['int', 'str', 'float', 'dict', 'tuple']
    data_cons = ['年龄', '姓名', '体重', '爱好', '混合数据']

    generator = RandomDataGenerator(data_types, data_cons)
    samples = generator.multiple_samples(num_samples)
    stats = DataStats.calculate_stats(samples)
    return samples, stats


num_samples = 10
samples, stats = generate_samples(num_samples)
for i, sample in enumerate(samples, 1):
    print(f"序号{i}: {sample}")
print("统计结果:", stats)