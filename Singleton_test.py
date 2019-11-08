#!/usr/bin/env python
# coding=utf-8


'''
用类方法实现单例
'''
# import time
# import threading
#
# class Singleton(object):
#     _instance_lock = threading.Lock()
#
#     def __init__(self,*args,**kwargs):
#         time.sleep(1)
#
#     @classmethod
#     def get_instance(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton,'_instance'):
#                     Singleton._instance = Singleton(*args,**kwargs)
#
#         return Singleton._instance
#
# def task(arg):
#     obj = Singleton.get_instance(arg)
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
#
# obj = Singleton.get_instance()
# print(obj)

'''
用__new__方法实现单例
'''
# 实例化一个单例
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        #如果类数字__instance没有或者没有赋值
        #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
        #能够知道之前已经创建过对象了，这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18, "xxx")
b = Singleton(8, "xxx")

print(id(a))
print(id(b))

a.age = 19 #给a指向的对象添加一个属性
print(b.age)#获取b指向的对象的age属性


'''
用__new__方法实现单例2
'''
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(cls, "_instance"):
                    Singleton._instance = super().__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()


#创建单例时，只执行1次init方法
# 实例化一个单例
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(18, "xxx")
b = Singleton(8, "xxx")

print(id(a))
print(id(b))


print(a.age)
print(b.age)

a.age = 19
print(b.age)


