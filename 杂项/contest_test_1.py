import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))
        return 'hello world'


with timethis('counting') as e:
    n = 0
    while n < 100:
        n += 1


class MakeTest:
    def __enter__(self):
        print('This is __enter__ method! ')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('This is __exit__ method!')

    def test(self):
        print("落霞与孤鹜齐飞，秋水共长天一色！")


# test是__enter__的返回对象
# __exit__将在程序结束的时候运行
with MakeTest() as test:
    test.test()


@contextmanager
def fuctest():
    """
    yield可以作为断点,作为上下文使用的时候不需要添加对象
    :return:
    """
    print('This is __enter__ method! ')
    try:
        yield
    finally:
        print('This is __exit__ method!')
        return '知道你在干什么嘛?'


with fuctest():
    print('*' * 20)


@contextmanager
def str_join():
    print('《', end='')
    try:
        yield
    finally:
        print('》', end='')


with str_join():
    print('你在干嘛', end='')
