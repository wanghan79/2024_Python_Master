import random

def generate_random_structure(max_depth, current_depth=0):
    if current_depth >= max_depth:
        # If max depth is reached, return a simple int or str
        data_type = random.choice(['int', 'str'])
        if data_type == 'int':
            return random.randint(1, 100)
        else:
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10)))
    else:
        # Randomly choose to create a list or dictionary
        data_type = random.choice(['list', 'dict', 'int', 'str'])
        if data_type == 'list':
            return [generate_random_structure(max_depth, current_depth + 1)]
        elif data_type == 'dict':
            return {
                ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 5))): generate_random_structure(max_depth, current_depth + 1)
            }
        elif data_type == 'int':
            return 'int'
        else:  # str
            return 'str'

# Example usage
def Random_Input():
    len = random.randint(0, 99)
    random_structure = generate_random_structure(len)

    list = []
    list.append(random_structure)

    return list
