import random
import string

def generate_samples(num_samples, data_template):
    if num_samples < 1:
        raise ValueError("The number of samples must be at least 1.")
    
    samples = []
    for _ in range(num_samples):
        sample = {}
        for field, properties in data_template.items():
            if properties['type'] == 'int':
                sample[field] = random.randint(*properties['range'])
            elif properties['type'] == 'str':
                sample[field] = ''.join(random.choice(properties['characters']) for _ in range(properties['length']))
            elif properties['type'] == 'float':
                sample[field] = random.uniform(*properties['range'])
            else:
                raise ValueError(f"Unsupported data type: {properties['type']}")
        samples.append(sample)
    return samples

data_structure = {
    'field1': {
        'type': 'int',
        'range': [1, 200]
    },
    'field2': {
        'type': 'str',
        'characters': string.ascii_lowercase,
        'length': 4
    },
    'field3': {
        'type': 'float',
        'range': [0, 2]
    }
}

try:
    sample_data = generate_samples(num_samples=3, data_template=data_structure)
    print(sample_data)
except ValueError as e:
    print(e)
