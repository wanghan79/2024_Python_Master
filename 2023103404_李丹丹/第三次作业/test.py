# def addLogging(decPara):#装饰器函数
#     def decrator(func):
#         def wrapper(*args,**kwargs):
#             print('%s is running'% func.__name__)
#             return func(*args,**kwargs)
#         return wrapper#wrapper(*args,**kwargs)
#     return decrator#input:func,return:wrapper(*args,**kwargs)
#
# def sum(x=2,y=2,*args):#定义求总和函数
#     sum=x+y
#     for arg in args:
#         sum=sum+arg
#     print('the sum  is %d' % sum)
#     return sum
#
# @addLogging('a level')
# def mean(x=3,y=2,*args):#定义求均值函数
#     sum=x+y
#     for arg in args:
#         sum = sum + arg
#     average=sum/len(args)
#     print('the average  is %d' % mean)
#     return mean



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


@addLogging('a level')
def sum(x,y,*args):
    return sum

@addLogging('a level')
def mean(x,y,*args):
    sum=0
    for arg in args:
        sum = sum + arg
    average = sum / len(args)
    print('the average  is %d' % average)
    return mean



if __name__ == '__main__':
    # sum()#不带参数
    sum(2, 2, 8)  # 计算总和
    mean(2, 2, 3)  # 计算均值

