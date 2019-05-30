class Singleton:
    """通过hasattr进行动态赋值"""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


c = Singleton()
d = Singleton()
print(c is d)


class Singletons:
    """将_instance设置为flog来进行设置singleton"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singletons, cls).__new__(cls)
        return cls._instance


a = Singletons()
b = Singletons()
print(a is b)
