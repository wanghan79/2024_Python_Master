import random
from functools import wraps

def process_data(*options):
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            sampled_data = func(**kwargs)
            processed_results = {'origin_data': sampled_data}
            
            for option in options:
                if option == 'AVG':
                    total_sum = sum(sum(row) for row in sampled_data)
                    num_elements = sum(len(row) for row in sampled_data)
                    processed_results['AVG'] = total_sum / num_elements if num_elements else 0
                if option == 'SUM':
                    total_sum = sum(sum(row) for row in sampled_data)
                    processed_results['SUM'] = total_sum
            
            return processed_results
        
        return wrapper
    return decorator

@process_data('SUM', 'AVG')
def sample_data(num_samples, data_structure):
    if num_samples < 1:
        raise ValueError('num must be at least 1.')
    if not data_structure:
        raise ValueError('struct must be provided.')

    samples = [
        [sample_field(data_structure[key]) for key in data_structure] 
        for _ in range(num_samples)
    ]
    return samples

def sample_field(field_spec):
    if field_spec['datatype'] == 'int':
        return random.randint(*field_spec['datarange'])
    elif field_spec['datatype'] == 'float':
        return random.uniform(*field_spec['datarange'])
    elif field_spec['datatype'] == 'str':
        return ''.join(random.SystemRandom().choice(field_spec['datarange']) for _ in range(field_spec['len']))
    else:
        raise ValueError(f"Unsupported datatype: {field_spec['datatype']}")


data_template = {
    '1': {'datatype': 'float', 'datarange': [18, 65]},
    '2': {'datatype': 'float', 'datarange': [18, 65]},
}

f = sample_data(num_samples=2, data_structure=data_template)
print(f)
