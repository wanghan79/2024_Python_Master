import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def calculate_sum(data):
    result = []
    for i in range(len(data[0])):
        column_sum = sum(row[i] for row in data)
        result.append(column_sum)
    return result

def calculate_avg(data):
    sums = calculate_sum(data)
    return [s / len(data) for s in sums]

def add_logging(*order):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            sum_result = calculate_sum(result)
            avg_result = calculate_avg(result)
            output = {'result': result}
            if 'sum' in order:
                output['sum'] = sum_result
            if 'avg' in order:
                output['avg'] = avg_result
            return output
        return wrapper
    return decorator

@add_logging("sum", "avg")
def structDataSampling(num, struct):
    result = []
    for _ in range(num):
        element = []
        for _ in range(5):
            it = iter(struct['datarange'])
            tmp = random.uniform(next(it), next(it))
            element.append(tmp)
        result.append(element)
    return result

struct = {"datarange": (0, 50)}
a = structDataSampling(50, struct)
print("Results:", a['result'])
print("Sum:", a['sum'])
print("Average:", a['avg'])
