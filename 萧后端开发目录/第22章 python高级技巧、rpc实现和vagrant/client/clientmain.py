import rpcclient

c = rpcclient.RPCClient()
c.connect('127.0.0.1', 5000)
c.bar(1, 2, c=3)
