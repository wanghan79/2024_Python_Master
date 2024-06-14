'''
Author: Runchang Liang
Date: 2024-06-14 10:39:13
LastEditors: liangrc666@nenu.edu.cn
LastEditTime: 2024-06-14 10:57:04
FilePath: \2023103409_FinalProject\work1\RandomDataSampling_function.py
Description: 

Copyright (c) 2024 by ${liangrc666@nenu.edu.cn}, All Rights Reserved. 
'''
import random
from faker import Faker

fake = Faker()

def struct_data_sampling(**kwargs):
    num = kwargs.get('num', 1)
    if num < 1:
        raise ValueError("Wrong number input")
    
    result = []
    for _ in range(num):
        element = []
        for key, value in kwargs.items():
            if key == "RandomInt":
                element.append(random.randint(*value['datarange']))
            elif key == "RandomFloat":
                element.append(random.uniform(*value['datarange']))
            elif key == "RandomStr":
                element.append(''.join(random.choice(value['datarange']) for _ in range(value['len'])))
            elif key in ["name", "email"]:
                element.append(getattr(fake, key)())
            elif key == "age":
                element.append(fake.random_int(min=18, max=80))
        result.append(element)
    return result

def example():
    try:
        result = struct_data_sampling(num=4,
                                      RandomInt={"datarange": [1, 100]},
                                      RandomFloat={"datarange": [1.0, 100.0]},
                                      RandomStr={"datarange": ['a', 'b', 'c', 'd', 'e'], "len": 4},
                                      name=True,
                                      email=True,
                                      age=True)
        for i in result:
            print(i)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    example()