# def foo():
#     bar_a = yield 1
#     print(bar_a)
#     bar_b = yield bar_a
#     print(bar_b)
#     yield "最后一个值，再迭代就要报StopIteration了"
#
#
# f = foo()
# print(f.send(None))
# print(f.send("我是send2"))
# print(next(f))
