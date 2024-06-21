import random
import time

# 本实验构造了一个生成器版，和一个不带生成器版，并分别调用，并比较了一下运行时间，带生成器版用时更多

# 不带生成器的版本
def generate_random_data(count, data_type=int):
    if data_type == int:
        return [random.randint(0, 1000) for _ in range(count)]
    elif data_type == float:
        return [random.random() * 1000 for _ in range(count)]
    elif data_type == str:
        return [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)) for _ in range(count)]
    elif data_type == list:
        return [[random.randint(0, 1000) for _ in range(random.randint(1, 10))] for _ in range(count)]
    elif data_type == dict:
        return [{f'key_{i}': random.randint(0, 1000) for i in range(random.randint(1, 5))} for _ in range(count)]
    elif data_type == tuple:
        return [tuple(random.randint(0, 1000) for _ in range(random.randint(1, 10))) for _ in range(count)]
    else:
        raise ValueError("Unsupported data type")

# 带生成器的版本
def generate_random_data_with_yield(count, data_type=int):
    def generate_ints():
        for _ in range(count):
            yield random.randint(0, 1000)

    def generate_floats():
        for _ in range(count):
            yield random.random() * 1000

    def generate_strings():
        for _ in range(count):
            yield ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))

    def generate_lists():
        for _ in range(count):
            yield [random.randint(0, 1000) for _ in range(random.randint(1, 10))]

    def generate_dicts():
        for _ in range(count):
            yield {f'key_{i}': random.randint(0, 1000) for i in range(random.randint(1, 5))}

    def generate_tuples():
        for _ in range(count):
            yield tuple(random.randint(0, 1000) for _ in range(random.randint(1, 10)))

    if data_type == int:
        return generate_ints()
    elif data_type == float:
        return generate_floats()
    elif data_type == str:
        return generate_strings()
    elif data_type == list:
        return generate_lists()
    elif data_type == dict:
        return generate_dicts()
    elif data_type == tuple:
        return generate_tuples()
    else:
        raise ValueError("Unsupported data type")

# 装饰器函数，用于统计函数执行时间
def stats_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n函数 {func.__name__} 执行耗时 {end_time - start_time:.4f} 秒")
        return result
    return wrapper

# 主程序
if __name__ == '__main__':
    # 获取用户输入的数量
    int_count = int(input("输入想生成的整数随机数数量："))
    float_count = int(input("输入想生成的浮点数随机数数量："))
    string_count = int(input("输入想生成的字符串随机数数量："))
    list_count = int(input("输入想生成的列表随机数数量："))
    dict_count = int(input("输入想生成的字典随机数数量："))
    tuple_count = int(input("输入想生成的元组随机数数量："))

    # 使用不带生成器的版本
    @stats_decorator
    def test_generate_random_data():
        if int_count > 0:
            print("\n不带生成器生成整数版本：")
            random_ints = generate_random_data(int_count, int)
            print('生成的随机整数:', random_ints)

        if float_count > 0:
            print("\n不带生成器生成浮点数版本：")
            random_floats = generate_random_data(float_count, float)
            print('生成的随机浮点数:', random_floats)

        if string_count > 0:
            print("\n不带生成器生成字符串版本：")
            random_strs = generate_random_data(string_count, str)
            print('生成的随机字符串:', random_strs)

        if list_count > 0:
            print("\n不带生成器生成列表版本：")
            random_lists = generate_random_data(list_count, list)
            print('生成的随机列表:', random_lists)

        if dict_count > 0:
            print("\n不带生成器生成字典版本：")
            random_dicts = generate_random_data(dict_count, dict)
            print('生成的随机字典:', random_dicts)

        if tuple_count > 0:
            print("\n不带生成器生成元组版本：")
            random_tuples = generate_random_data(tuple_count, tuple)
            print('生成的随机元组:', random_tuples)

    test_generate_random_data()

    print("\n--------------------------------------------\n")

    # 使用生成器版本
    @stats_decorator
    def test_generate_random_data_with_yield():
        if int_count > 0:
            print("\n带生成器生成整数版本：")
            random_ints_gen = generate_random_data_with_yield(int_count, int)
            print('生成的随机整数:')
            for random_int in random_ints_gen:
                print(random_int, end=' ')

        if float_count > 0:
            print("\n带生成器生成浮点数版本：")
            random_floats_gen = generate_random_data_with_yield(float_count, float)
            print('生成的随机浮点数:')
            for random_float in random_floats_gen:
                print(random_float, end=' ')

        if string_count > 0:
            print("\n带生成器生成字符串版本：")
            random_strs_gen = generate_random_data_with_yield(string_count, str)
            print('生成的随机字符串:')
            for random_str in random_strs_gen:
                print(random_str, end=' ')

        if list_count > 0:
            print("\n带生成器生成列表版本：")
            random_lists_gen = generate_random_data_with_yield(list_count, list)
            print('生成的随机列表:')
            for random_list in random_lists_gen:
                print(random_list, end=' ')

        if dict_count > 0:
            print("\n带生成器生成字典版本：")
            random_dicts_gen = generate_random_data_with_yield(dict_count, dict)
            print('生成的随机字典:')
            for random_dict in random_dicts_gen:
                print(random_dict, end=' ')

        if tuple_count > 0:
            print("\n带生成器生成元组版本：")
            random_tuples_gen = generate_random_data_with_yield(tuple_count, tuple)
            print('生成的随机元组:')
            for random_tuple in random_tuples_gen:
                print(random_tuple, end=' ')

    test_generate_random_data_with_yield()


# 结果
# 输入想生成的整数随机数数量：500
# 输入想生成的浮点数随机数数量：2
# 输入想生成的字符串随机数数量：3
# 输入想生成的列表随机数数量：4
# 输入想生成的字典随机数数量：5
# 输入想生成的元组随机数数量：3
#
# 不带生成器生成整数版本：
# 生成的随机整数: [117, 1, 859, 612, 718, 249, 918, 445, 28, 551, 819, 330, 805, 435, 740, 839, 653, 143, 934, 903, 377, 617, 997, 296, 398, 700, 526, 962, 45, 47, 640, 203, 635, 422, 169, 70, 221, 285, 528, 733, 291, 241, 363, 187, 198, 945, 909, 987, 122, 160, 846, 196, 868, 982, 865, 873, 222, 442, 838, 122, 154, 23, 268, 396, 424, 89, 383, 78, 594, 900, 641, 807, 269, 559, 958, 787, 390, 21, 759, 416, 830, 427, 546, 897, 66, 980, 275, 298, 814, 933, 445, 413, 126, 207, 224, 519, 67, 773, 835, 95, 981, 547, 495, 920, 55, 34, 910, 446, 556, 956, 174, 953, 999, 435, 497, 619, 509, 923, 844, 511, 900, 524, 943, 798, 807, 200, 880, 615, 239, 517, 86, 731, 977, 240, 958, 582, 26, 763, 906, 305, 692, 72, 713, 788, 394, 847, 92, 171, 147, 959, 397, 392, 342, 322, 252, 646, 253, 601, 115, 996, 924, 838, 69, 44, 801, 166, 21, 402, 532, 792, 120, 183, 738, 460, 957, 499, 660, 210, 288, 772, 905, 527, 673, 970, 373, 886, 519, 278, 187, 237, 584, 327, 596, 374, 544, 845, 708, 162, 116, 950, 47, 256, 0, 791, 236, 88, 917, 736, 319, 64, 433, 614, 33, 489, 114, 645, 834, 185, 434, 564, 409, 587, 968, 849, 336, 954, 222, 504, 132, 668, 325, 117, 976, 311, 744, 39, 947, 499, 251, 731, 832, 519, 196, 565, 589, 416, 225, 354, 181, 876, 140, 873, 264, 107, 320, 155, 454, 778, 460, 854, 396, 195, 121, 823, 363, 676, 669, 349, 765, 315, 863, 621, 29, 889, 877, 126, 318, 243, 247, 370, 537, 927, 11, 709, 316, 609, 599, 869, 82, 646, 100, 574, 158, 743, 356, 72, 910, 588, 86, 531, 955, 55, 469, 65, 672, 296, 658, 309, 852, 623, 509, 646, 324, 947, 394, 545, 539, 336, 288, 675, 167, 526, 422, 322, 660, 644, 436, 26, 107, 538, 820, 155, 223, 126, 61, 868, 423, 521, 848, 895, 249, 182, 711, 624, 896, 245, 981, 115, 142, 657, 744, 161, 900, 273, 433, 222, 135, 345, 143, 361, 863, 614, 29, 860, 69, 381, 538, 987, 846, 460, 713, 7, 581, 290, 613, 590, 340, 287, 457, 39, 825, 799, 501, 780, 393, 743, 232, 288, 110, 459, 638, 933, 257, 300, 282, 333, 405, 70, 678, 54, 466, 958, 345, 640, 36, 311, 723, 622, 866, 331, 931, 430, 753, 492, 446, 251, 427, 61, 76, 801, 946, 378, 830, 571, 397, 290, 343, 942, 575, 497, 670, 528, 318, 52, 2, 647, 177, 953, 988, 931, 231, 145, 192, 693, 886, 158, 477, 577, 723, 795, 707, 853, 159, 544, 193, 584, 887, 311, 625, 763, 786, 948, 45, 699, 98, 293, 377, 262, 391, 744, 551, 574, 479, 706, 247, 937, 312, 364, 50, 44, 528, 47, 310, 170, 582, 116, 156, 725, 525, 43, 355, 725, 925, 541, 542, 14, 880, 266, 475, 657]
#
# 不带生成器生成浮点数版本：
# 生成的随机浮点数: [452.90081925492365, 138.0538824362708]
#
# 不带生成器生成字符串版本：
# 生成的随机字符串: ['ilarhkrszp', 'xexzfplohj', 'sjteydcuac']
#
# 不带生成器生成列表版本：
# 生成的随机列表: [[291, 603, 411, 698, 523], [94, 712, 997, 547, 901, 240, 278, 976, 915, 539], [917, 758], [376, 57]]
#
# 不带生成器生成字典版本：
# 生成的随机字典: [{'key_0': 146, 'key_1': 224}, {'key_0': 593, 'key_1': 608, 'key_2': 193, 'key_3': 34, 'key_4': 799}, {'key_0': 643, 'key_1': 889, 'key_2': 307, 'key_3': 78, 'key_4': 854}, {'key_0': 952, 'key_1': 912, 'key_2': 856}, {'key_0': 740}]
#
# 不带生成器生成元组版本：
# 生成的随机元组: [(495, 911, 422, 406, 132, 86, 602), (5, 415, 107), (664, 21, 437, 266, 256, 537, 475, 608, 907)]
#
# 函数 test_generate_random_data 执行耗时 0.0010 秒
#
# --------------------------------------------
#
#
# 带生成器生成整数版本：
# 生成的随机整数:[126 251 806 407 689 163 331 226 49 506 785 76 300 269 541 634 747 932 596 783 937 22 76 153 883 80 425 576 659 562 200 513 510 743 680 947 655 291 412 296 807 337 555 576 171 582 48 927 831 458 409 211 106 975 429 204 895 763 329 601 250 292 973 221 308 658 57 884 82 71 527 53 494 421 139 617 782 153 198 779 539 935 348 322 830 503 613 151 626 789 710 123 946 342 671 309 778 20 444 277 192 72 294 335 1 94 413 241 397 600 679 8 193 83 22 771 151 575 282 844 823 249 346 257 903 549 819 341 86 100 265 154 796 325 522 137 304 885 830 776 687 894 810 672 475 563 508 365 470 174 749 483 499 961 243 93 831 895 913 187 530 460 84 513 447 538 843 455 47 190 364 799 118 318 57 782 47 693 291 815 505 88 725 47 572 406 148 866 773 529 958 107 16 267 629 777 166 920 441 422 886 903 441 571 227 996 407 706 498 921 30 117 721 514 193 909 753 371 945 411 367 655 52 727 255 49 915 171 260 764 816 481 432 12 670 767 518 478 119 104 980 914 429 836 109 106 592 703 883 961 949 338 956 811 841 536 514 64 335 551 243 170 922 427 576 900 232 996 292 848 281 328 13 952 539 341 505 512 628 946 773 228 64 903 258 9 506 754 734 222 167 774 264 610 325 55 818 618 926 931 630 227 70 158 117 554 318 556 62 856 681 455 34 402 153 154 290 540 414 182 117 649 742 107 229 732 716 530 59 81 944 61 997 849 508 205 230 805 721 786 501 549 840 422 320 834 611 593 101 349 936 285 19 710 454 953 260 847 349 511 609 31 552 64 161 230 379 35 573 654 447 738 717 748 831 862 125 700 555 151 583 904 664 441 115 267 314 76 512 283 779 612 641 476 706 493 763 258 633 20 726 301 832 32 695 689 649 16 999 321 783 182 635 990 946 738 891 638 491 635 971 414 730 936 2 698 553 683 789 238 968 509 735 744 698 392 510 872 57 999 773 31 219 217 347 594 923 910 785 588 433 201 282 461 206 911 614 866 194 652 655 200 757 27 695 670 427 648 583 604 673 932 350 448 866 831 78 803 305 14 743 882 135 349 311 422 640 408 801 666 737 841 109 100 771 712 530 26 917 981]

# 带生成器生成浮点数版本：
# 生成的随机浮点数:[355.6539763442368 709.4779267579331]

# 带生成器生成字符串版本：
# 生成的随机字符串:[auubrhznba bipncorcnc biipsmjoob]

# 带生成器生成列表版本：
# 生成的随机列表:[[421] [283, 459] [156] [621, 505, 203, 553, 972, 500, 39]]

# 带生成器生成字典版本：
# 生成的随机字典:[ {'key_0': 262, 'key_1': 570, 'key_2': 921, 'key_3': 564} {'key_0': 35, 'key_1': 849, 'key_2': 581, 'key_3': 399} {'key_0': 982, 'key_1': 699, 'key_2': 12} {'key_0': 554, 'key_1': 845} {'key_0': 397, 'key_1': 679, 'key_2': 94, 'key_3': 818}]

# 带生成器生成元组版本：
# 生成的随机元组:[ (672, 691, 20, 974, 588, 196, 472, 616) (779, 1000) (338, 186)]

# 函数 test_generate_random_data_with_yield 执行耗时 0.0127 秒


#结果发现带生成器比较慢,但是会节省内存