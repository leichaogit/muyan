from contextlib import contextmanager


#
#
# @contextmanager
# def functest():
#     """
#     在该使用方法中,yield关键字用于占位
#     :return:
#     """
#     try:
#         print('1.程序开始,首先执行,卡在yield关键字处')
#         yield
#     finally:
#         print('3.最后执行')
#
#
# with functest():
#     print('2.开始执行测试用例,调用完成,执行行yield关键字后面')
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

# [:],copy都是属于浅拷贝,只是复制了引用
ls = [1, 2, 3, 4, 5]
with list_transaction(ls) as working:
    working.append('hello')
    working.append('world')
print(ls)

bls = [1, 2, 3, 4, 5]
with list_transaction(ls) as working:
    working.append('hello')
    working.append('world')
    try:
        raise NameError('反正就是错误')
    finally:
        print(bls)