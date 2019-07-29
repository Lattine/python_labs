# -*- coding: utf-8 -*-

# @Time    : 2019/7/29
# @Author  : Lattine

# ======================


def singleton(cls, *args, **kwargs):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student('Tom', 29)
print(stu1.name, stu1.age, stu1)
stu2 = Student('Jim', 30)
print(stu2.name, stu2.age, stu2)

print(stu1 == stu2)

# ------------- result ----------------
# Tom 29 <__main__.Student object at 0x0000017F7F7B12E8>
# Tom 29 <__main__.Student object at 0x0000017F7F7B12E8>
# True


# -------------- analysis ---------------
# Python中认为“一切皆对象”，类（元类除外）、函数都可以看作是对象，既然是对象就可以作为参数在函数中传递。
