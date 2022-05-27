'''
数据库迁移
file -> mongo

1. python语言
duck type鸭子类型
gua type语言

长的像鸭子，叫的也想鸭子，那你就是鸭子
2. 为什么duck type语言就不用设计模式了？
设计模式？
一些列的问题
1. 高耦合
2. 重构的时候非常痛苦，改一堆东西

1. 针对这些问题特定的解决方案
    a 名字
    b 场景
    c uml
    d 代码

    1. 高内聚
    2. 低耦合 依赖倒置

2. 什么导致了高耦合
    1. 类型 - 强类型
    monster hero hero_monster
    hero monster本身不是一个类型，统一成一种类型
    base class，xxx, hero 和monster都集成

mongo
1. 快
2. leveldb，kv，只能单机用
3. mongo本身多机用
4. 主从数据库的，落地


Model -> Mongo
首先要保持新的MongoModel的接口和老的Model一致就可以了
所有被使用到的老的Model接口，在新的MongoModel都有

1. new
2. find_by
3. find(id)
4. all
5. get
6. find_all

使用了gua哥写的orm
orm？sql，希望像操纵对象一样操纵数据库。
'''



class Duck(object):
    def bark(self):
        print("hahah")

    def swim(self):
        pass

class Dog(object):
    def bark(self):
        print('wangwangwang')

    def swim(self):
        pass

duck_list = []
for i in range(10):
    duck_list.append(Duck())
    duck_list.append(Dog())

for d in duck_list:
    d.bark()


