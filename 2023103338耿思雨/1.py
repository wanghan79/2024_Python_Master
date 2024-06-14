import random


def random_data(data_types, data_cons):
    data = {}
    for data_con, data_type in zip(data_cons, data_types):
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


def multiple_samples(data_types, data_cons, num):
    samples = []
    for _ in range(num):
        sample = random_data(data_types, data_cons)
        samples.append(sample)
    return samples


def generate_samples(num_samples):
    data_types = ['int', 'str', 'float', 'dict', 'tuple']
    data_cons = ['年龄', '姓名', '体重', '爱好', '混合数据']

    samples = multiple_samples(data_types, data_cons, num_samples)
    return samples


num_samples = 10
samples = generate_samples(num_samples)
for i, sample in enumerate(samples, 1):
    print(f"序号{i}: {sample}")
