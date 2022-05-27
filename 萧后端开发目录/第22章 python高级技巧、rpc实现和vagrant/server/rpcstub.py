class RPCStub(object):
    def __init__(self):
        pass

    def foo(self, a, b, c):
        self
        print("foo:", a, b, c)

    def bar(self, a, b, c=10):
        self
        print("bar:", a, b, c)