import random
from functools import wraps
import time

from python.test import mean,sum


def addLogging(decPara):
    def decrator(func):
        def wrapper(*args,**kwargs):
            print('%s is running'% func.__name__)
            sum=0
            for arg in args:
                sum = sum + arg
            print('the sum  is %d' % sum)
            # average = sum /len(args)
            # print('the average  is %d' % average)
            return func(*args,**kwargs)
        return wrapper#wrapper(*args,**kwargs)
    return decrator#input:func,return:wrapper(*args,**kwargs)

class RandomDataStatistics:
    def __init__(self, count=10):
        self.random_numbers = []
        self.count = count

    @addLogging('a level')
    def sum(x, y, *args):
        return sum

    @addLogging('a level')
    def mean(x, y, *args):
        sum = 0
        average=0
        for arg in args:
            sum = sum + arg
            average = sum / len(args)
            print('the average  is %d' % average)
        return mean


# 使用示例
sum(4,5,9)#计算总和
mean(7,7,9)#计算均值