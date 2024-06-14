import random
import string
def structDataSampling(**kwargs):
    result=list()
    for i in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == int:
                it = iter(value['datarange'])
                element.append({'key':key,'value':random.randint(next(it), next(it))})
            elif value['datatype']  == float:
                it = iter(value['datarange'])
                float_value = random.uniform(next(it), next(it))
                element.append({'key':key,'value':round(float_value, value.get('decimals', 2))})
            elif value['datatype'] == str:
                element.append({'key':key,'value':
                    ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))})
            elif value['datatype']  == bool:
                for ith in range(value["number"]):
                    element.append({'key':key,'value':random.choice((True, False))})
            else:
                continue
        result.append(element)
    return result
if __name__ == "__main__":
    para={'num':3,
          'struct':{
              'int_name':{'datatype':int,'datarange':[0,10]},
              'float_name': {'datatype':float,'datarange': [1.0, 5.0], 'decimals': 3},
              'str_name': {'datatype':str,'datarange': string.ascii_lowercase, 'strlen': 5},
              'bool_name': {'datatype':bool,'number': 3}
          }}
    para2= {'num': 3,
            'struct': {
                '学生姓名': {'datatype': 'str', 'datarange': string.ascii_lowercase, 'strlen': 10},
                '成绩': {'datatype': 'float', 'datarange': [0, 100], 'decimals': 3},
                '学号': {'datatype': 'str', 'datarange': string.ascii_lowercase, 'strlen': 5},
            }}
    results=structDataSampling(**para2)
    for result in results:
        print(result)