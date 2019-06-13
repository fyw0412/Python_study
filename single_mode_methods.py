#Python 中如何实现单例模式
#使用装饰器
def singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class Foo(object):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 == foo2)

#使用基类
#使用基类New是真正创建实例对象的方法，所以重写基类的new方法，以此保证创建对象的时候只生成一个实例

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton,cls).__new__(cls, *args, **kwargs)
        return cls._instance
class Foo1(Singleton):
    pass

foo3 = Foo1()
foo4 = Foo1()

print(foo3 == foo4)

#使用元类
#元类是用于创建类对象的类，类对象创建实例对象是一定要调用call方法，因此在调用call时候保证始终只创建一个实例即可，type是python的元类

class Singleton1(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton1,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo2(metaclass = Singleton1):
    pass

foo5 = Foo2()
foo6 = Foo2()
print( foo5 == foo6 )
