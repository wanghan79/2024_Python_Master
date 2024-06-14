from functools import wraps

def stats_decorator(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        total_sum = sum(args)
        result = func(*args, **kwargs)
        return result, total_sum

    return decorated

@stats_decorator
def sum_function(*args):
    return sum(args)

@stats_decorator
def mean_function(*args):
    return sum(args) / len(args) if args else 0

print(sum_function(1, 2, 3, 4, 5))  
print(mean_function(1, 2, 3, 4, 5))  
