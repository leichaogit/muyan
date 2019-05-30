class Base(object):
    def __init__(self):
        print('Base')


class Medium1(Base):
    def __init__(self):
        super(Medium1, self).__init__()
        print('Medium1')


class Medium2(Base):
    def __init__(self, ):
        super(Medium2, self).__init__()
        print('Medium2')


class Leaf(Medium1, Medium2):
    def __init__(self):
        super(Leaf, self).__init__()
        print('Leaf')
