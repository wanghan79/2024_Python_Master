import random
import string

def random_string_generator(length=10):
    letters = string.ascii_letters
    while True:
        yield ''.join(random.choice(letters) for i in range(length))

def random_list_generator(size=10, min_val=0, max_val=100):
    while True:
        yield [random.randint(min_val, max_val) for _ in range(size)]

def random_dict_generator(size=10):
    while True:
        yield {''.join(random.choice(string.ascii_letters) for _ in range(5)): random.randint(0, 100) for _ in range(size)}

string_gen = random_string_generator()
list_gen = random_list_generator()
dict_gen = random_dict_generator()

print(next(string_gen))
print(next(list_gen))
print(next(dict_gen))
