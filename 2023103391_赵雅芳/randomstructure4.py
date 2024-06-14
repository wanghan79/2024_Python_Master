import random

def randomize_element(element):
    if isinstance(element, list):
        return [randomize_element(item) for item in element]
    elif isinstance(element, tuple):
        return tuple(randomize_element(item) for item in element)
    elif isinstance(element, dict):
        return {key: randomize_element(value) for key, value in element.items()}
    elif isinstance(element, str):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=len(element)))
    elif isinstance(element, (int, float)):
        return random.randint(0, 100) if isinstance(element, int) else random.uniform(0, 100)
    elif hasattr(element, '__dict__'):
        new_element = element.__class__()
        for attr, value in element.__dict__.items():
            setattr(new_element, attr, randomize_element(value))
        return new_element
    else:
        return element

def generate_random_structure(nested_structure):
    return randomize_element(nested_structure)

# 测试
nested_structure = [{'a': 1, 'b': [2, 3], 'c': {'d': 4, 'e': 5}}]
random_nested_structure = generate_random_structure(nested_structure)
print(random_nested_structure)