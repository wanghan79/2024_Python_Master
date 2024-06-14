import random
import string
from datetime import datetime

def generate_random_data(data):
    if isinstance(data, int):  
        return random.randint(0, 100)
    elif isinstance(data, float):  
        return round(random.uniform(0, 10000), 2)
    elif isinstance(data, str):  
        length = random.randint(5, 15)  
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    elif isinstance(data, list):  
        return [generate_random_data(item) for item in data]
    elif isinstance(data, tuple):  
        return tuple(generate_random_data(item) for item in data)
    elif isinstance(data, dict):  
        return {key: generate_random_data(value) for key, value in data.items()}
    elif isinstance(data, datetime):  
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        raise ValueError(f"不支持的数据类型: {type(data)}")

def generate_original_data(num, template_data):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("数量应为正整数")
    if not isinstance(template_data, (dict, list, tuple, str, int, float)):
        raise ValueError("数据结构需要有效")
    
    return [generate_random_data(template_data) for _ in range(num)]

template_data0 = {
    "name": "Bob",
    "age": 25,
    "scores": [88, 92, 75],
    "info": {
        "city": "San Francisco",
        "email": "bob@example.com"
    },
    "zhuanye": "电子信息",
    "hobbies": ["reading", "gaming", "hiking"],  
    "registration_date": datetime.now(), 
}
template_data1 = {
    "employee_name": "John Doe",
    "age": 30,
    "job_position": "Software Engineer",
    "employment_history": [
        {"company": "Company A", "years": 2},
        {"company": "Company B", "years": 3}
    ],
    "education": {
        "university": "State University",
        "degree": "Bachelor of Science",
        "graduation_year": datetime(2020, 5, 1)
    },
    "skills": ["Python", "Java", "SQL"],
    "start_date": datetime.now(),
    "salary": 85000.00
}

random_data = generate_original_data(10, template_data0)
for data in random_data:
    print(data)
random_employee_data = generate_original_data(10, template_data1)
for data in random_employee_data:
    print(data)
