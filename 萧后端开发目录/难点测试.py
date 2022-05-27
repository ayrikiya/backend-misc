# 默认参数陷阱
# def foo(a=[]):
#     a.append(1)
#     print(a)
#
#
# foo()
# foo()

# [1]
# [1, 1]

#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
# a = [1, 2, 3, ]
# b = a.copy()
# a.append(4)
# print(a)
# print(b)

################################################################
# 格式化问题
# class foo(object):
#     def __init__(self, form):
#         self.id = form.get('id', '')
#         self.content = form.get('content', '')
#
#
# form = {'id': '1', 'content': 'ddd'}
# a = foo(form)
#
# properties = ['{0} = {1}'.format(k, v) for k, v in a.__dict__.items()]
# for n in properties:
#     print(n)
#
# b = '<{0}: \n  {1}\n>'.format(a.__class__.__name__, '\n  '.join(properties))
# print(b)
# properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
# '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

################################################################
# 元类 orm
import numbers
class Field:  pass

class IntField(Field):
    def __init__(self, name):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        self._value = value

class StrField(Field):
    def __init__(self, name):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        self._value = value

class User(object):
    id = IntField('id')
    name = StrField('username')
    email = StrField('email')
    password = StrField('password')


u = User(id = 20180424, name = "xiaoming", email = "xiaoming@163.com", password = "abc123")
us = User(id = 20180111, name = "1xiaoming", email = "1xiaoming@163.com", password = "1abc123")
print(User.id)