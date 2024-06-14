import random
import string


class MLMethod:
    def __init__(self, model):
        self.model = model

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 执行机器学习方法
            print("Running machine learning method:", self.model)
            result = func(*args, **kwargs)

            return result

        return wrapper


class EvaluationMetric:
    def __init__(self, metric):
        self.metric = metric

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 执行精度指标操作
            print("Running evaluation metric:", self.metric)
            result = func(*args, **kwargs)
            return result

        return wrapper


@MLMethod("CNN")
@EvaluationMetric("RECALL")
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.randint(0, value))
        elif key == 'float':
            result.append(random.uniform(0, value))
        elif key == 'str':
            length = value
            result.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    return result
