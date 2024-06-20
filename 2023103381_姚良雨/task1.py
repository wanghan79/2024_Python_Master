import random

#随机数结构生成函数封装
#随机数int 和 float类型分别为单个  而str 和list 以及dict里面随机生成五个元素
def  generate_date(date_type):
    match date_type:
        case 'int' :
            return random.randint(0,10)
        case 'float':
            return random.uniform(0.0,100.0)
        case 'str' :
            return ''.join(random.choices('abcdefghigklmnopqrstuvwxyz',k=5))
        case 'list':
            return [random.randint(0,100) for _ in range(5)]
        case 'dict':
            return {f'key_{i}':random.randint(0,100) for i in range(5)}
        case _:
            return None

date_type=input("请输入数据类型（int、float、str、list、dict）：")
random_date=generate_date(date_type)
print('随机生成的数据为：',random_date)
