import random
import string

def generate_random_password(**params):
    if 'length' in params and 'include_special' in params:
        length = params['length']
        include_special = params['include_special']

        characters = string.ascii_letters + string.digits
        if include_special:
            characters += string.punctuation

        random_password = ''.join(random.choice(characters) for _ in range(length))
        return random_password
    else:
        raise ValueError("Missing required parameters. Required: 'length', 'include_special'")

# 示例用法：
params1 = {'length': 10, 'include_special': False}
params2 = {'length': 12, 'include_special': True}

random_password1 = generate_random_password(**params1)
random_password2 = generate_random_password(**params2)

print("随机密码 1:", random_password1)
print("随机密码 2:", random_password2)
