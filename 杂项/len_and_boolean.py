class Test:
    def __len__(self):
        return 0


a = len(Test())
print(a)

b = ''
c = []
# print(b is None)
# print(c is None)

print(type(b))
print(type(c))
# python中一切皆对象，None也是一种对象类型
print(type(None))
if b:
    pass
if not b:
    pass
# 使用is进行判断就可能出现问题
if b is None:
    pass

print('-'*20)
print(not a)