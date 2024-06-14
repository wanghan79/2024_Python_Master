from functools import wraps
import random
import string

def statistics_decorator(*subjects):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            # 初始化
            total_scores = {subject: 0 for subject in subjects}
            count = 0

            # 计算总分和计数
            for student in results:
                for subject, score in student.items():
                    if subject in subjects:
                        total_scores[subject] += score
                        count += 1

            # 计算平均分
            average_scores = {subject: total_scores[subject] / count for subject in subjects}

            # 打印统计结果
            print(f"{func.__name__} 统计结果 -")
            for subject in subjects:
                print(f"{subject} 总分: {total_scores[subject]}, 平均分: {average_scores[subject]}")

            return results

        return wrapper

    return decorator


# 使用修饰器
@statistics_decorator('语文', '数学', '英语')
def generate_students_scores(count):
    """生成指定数量的学生成绩信息列表。"""
    return [
        {
            '姓名': RandomDataGenerator().generate_random_string(3),
            '语文': RandomDataGenerator().generate_random_score(60, 100),
            '数学': RandomDataGenerator().generate_random_score(60, 100),
            '英语': RandomDataGenerator().generate_random_score(60, 100)
        }
        for _ in range(count)
    ]

class RandomDataGenerator:
    @staticmethod
    def generate_random_string(length=3):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def generate_random_score(min_score=60, max_score=100):
        return random.randint(min_score, max_score)


# 生成并打印学生成绩信息
student_scores = generate_students_scores(5)
for score in student_scores:
    print(score)