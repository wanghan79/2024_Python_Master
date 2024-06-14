import random
import string

class RandomPasswordGenerator:
    def __init__(self, length=8, include_special=False):
        self.length = length
        self.include_special = include_special

    def generate_password(self):
        characters = string.ascii_letters + string.digits
        if self.include_special:
            characters += string.punctuation

        random_password = ''.join(random.choice(characters) for _ in range(self.length))
        return random_password

# 示例用法：
# 创建一个不包含特殊字符的密码生成器
password_generator1 = RandomPasswordGenerator(length=10, include_special=False)
random_password1 = password_generator1.generate_password()

# 创建一个包含特殊字符的密码生成器
password_generator2 = RandomPasswordGenerator(length=12, include_special=True)
random_password2 = password_generator2.generate_password()

print("随机密码 1:", random_password1)
print("随机密码 2:", random_password2)
