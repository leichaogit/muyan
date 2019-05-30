from collections import Iterable
a = [1, 2, 3, [4, 5, 6, [7, 8, 9, [0, 0, 0]]]]


def print_list(num_list, ignore_type=(str, bytes)):
    """
    使用递归，首先需要判断对象是不是可迭代类型，并且不能为str或者是bytes类型
    :param num_list:
    :param ignore_type:
    :return:
    """
    for each_list in num_list:
        if isinstance(each_list, Iterable) and not isinstance(each_list, ignore_type):
            yield from print_list(each_list)
        else:
            yield each_list


ls = print_list(a)
for i in ls:
    print(i)
