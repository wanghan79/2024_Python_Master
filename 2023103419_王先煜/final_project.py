import time
from functools import wraps
from faker import Faker
import random
from datetime import datetime

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"错误发生在 {func.__name__}: {e}")
            return None
    return wrapper

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 运行用了 {end_time - start_time:.6f} 秒.")
        return result
    return wrapper

fake = Faker()

class CustomDataGenerator:
    def __init__(self):
        self.fake = Faker()

    @timing_decorator
    @error_handler
    def generate_data(self, count, datatype, **kwargs):
        results = []
        for _ in range(count):
            data_instance = self.recursive_parse(kwargs)
            if datatype == 'string':
                result = ''.join(map(str, data_instance.values()))
            elif datatype == 'list':
                result = list(data_instance.values())
            elif datatype == 'dict':
                result = data_instance
            elif datatype == 'tuple':
                result = tuple(data_instance.values())
            results.append(result)
        return results[0] if count == 1 else results

    def recursive_parse(self, data):
        if isinstance(data, dict):
            return {key: self.recursive_parse(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.recursive_parse(item) for item in data]
        elif isinstance(data, tuple):
            return tuple(self.recursive_parse(item) for item in data)
        else:
            return data

generator = CustomDataGenerator()

template_data = {
    "name": fake.name(),
    "age": random.randint(18, 60),
    "contact": {
        "email": fake.email(),
        "phone": fake.phone_number()
    },
    "bio": fake.sentence(nb_words=10),
    "employment_history": [
        {
            "company": fake.company(),
            "position": fake.job(),
            "years": random.randint(1, 10),
            "start_date": fake.date_between(start_date="-10y", end_date="-1y"),
            "end_date": fake.date_between(start_date="-1y", end_date="today")
        }
        for _ in range(random.randint(1, 3))
    ],
    "education": [
        {
            "institution": fake.company(), 
            "degree": random.choice(["Bachelor's", "Master's", "PhD"]),
            "field_of_study": random.choice(["Computer Science", "Economics", "Mechanical Engineering"]),
            "graduation_year": random.randint(1995, 2019)
        }
        for _ in range(random.randint(1, 2))
    ],
    "skills": [random.choice(["Python", "Java", "C++", "SQL", "JavaScript"]) for _ in range(random.randint(3, 5))],
    "zhuanye": "Computer Science",
    "registration_date": datetime.now()
}

result_data = generator.generate_data(10, 'dict', data=template_data)
print("Generated Data:", result_data)
