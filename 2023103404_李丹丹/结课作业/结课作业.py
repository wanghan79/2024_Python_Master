
#结课作业，随机结构的生成器实现
import json
import random
import re
from functools import wraps

class RandomDataGenerator:
    def __init__(self, define):
        self.define = define

    def gen_int(self, define):
        return random.randint(define[1], define[2])

    def gen_float(self, define):
        return random.random() * (define[2] - define[1]) + define[1]

    # 支持reg的一个子集，即 (a | [a-z]) ( ? | {n} | {n, m} )?
    # parser 会将其分解为一个数组
    def reg_parse(self, reg: str):
        spans = []
        it = 0
        length = len(reg)
        while it < length:
            ch = reg[it]
            span = [ch, 1, 1]
            if ch == "[":
                pos = reg.find("]", it + 1)
                charset = reg[it + 1:pos]
                parsed_charset = []
                for group in re.findall(r"(.(-.)?)", charset):
                    char = group[0]
                    if len(char) == 1:
                        parsed_charset.append(char)
                    else:
                        parsed_charset.append((ord(char[0]), ord(char[2])))
                span[0] = parsed_charset
                it = pos + 1
            else:
                it = it + 1
            if it < length and reg[it] == "?":
                it = it + 1
                span[1] = 0
            elif it < length and reg[it] == "{":
                pos = reg.find("}", it + 1)
                param = reg[it + 1:pos]
                tuple = eval("(%s, %s)" % (param, param))
                span[1] = tuple[0]
                span[2] = tuple[1]
                it = pos + 1
            spans.append(span)
        return spans

    def gen_str(self, define):
        res = ""
        reg_spans = self.reg_parse(define[1])
        for span in reg_spans:
            l = random.randint(span[1], span[2])
            for i in range(l):
                if isinstance(span[0], str):
                    res += span[0]
                else:
                    total = 0
                    for ci in span[0]:
                        if isinstance(ci, str):
                            total += 1
                        else:
                            total += ci[1] - ci[0] + 1
                    nw = random.randint(1, total)
                    for ci in span[0]:
                        if isinstance(ci, str):
                            nw -= 1
                            if nw == 0:
                                res += ci
                                break
                        else:
                            nw -= ci[1] - ci[0] + 1
                            if nw <= 0:
                                res += chr(ci[1] + nw)
                                break
        return res

# 根据数据类型调用相应的生成函数
    def gen_dispatch(self, define):
        return {
            "int": self.gen_int,
            "float": self.gen_float,
            "string": self.gen_str,
        }[define[0]](define)
 #数据生成方法
    def gen_data(self):
        res = {}
        for name, define in self.define.items():
            res[name] = self.gen_dispatch(define)
        return res

    @staticmethod
    def data_generator(define):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                res = {}
                generator = RandomDataGenerator(define)
                for name, definition in generator.define.items():
                    res[name] = generator.gen_dispatch(definition)
                return func(res, *args, **kwargs)
            return wrapper
        return decorator

# 从外部文件读取数据结构
with open('random.json', 'r', encoding='utf-8') as f:
    define = json.load(f)

@RandomDataGenerator.data_generator(define)
def print_data(data):
    print(data)

# 生成并打印随机数据
for i in range(10):
    print("===========", " data #%d " % i, "===========")
    print_data()
