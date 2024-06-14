import random

def generate_samples(num_samples, data_structure):
    if num_samples < 1:
        raise ValueError('Parameter num must be at least 1.')
    
    samples = []
    for _ in range(num_samples):
        sample = {}
        for field, properties in data_structure.items():
            if properties['type'] == 'int':
                sample[field] = random.randint(*properties['range'])
            elif properties['type'] == 'float':
                sample[field] = random.uniform(*properties['range'])
            elif properties['type'] == 'str':
                sample[field] = ''.join(random.SystemRandom().choice(properties['characters']) for _ in range(properties['length']))
        samples.append(sample)
    return samples


data_template = {
    'field1': {
        'type': 'int',
        'range': [1, 200]
    },
    'field2': {
        'type': 'str',
        'characters': 'abcdefghijklmnopqrstuvwxyz',
        'length': 4
    },
    'field3': {
        'type': 'float',
        'range': [0, 2]
    }
}


sample_data = generate_samples(3, data_template)
print(sample_data)
