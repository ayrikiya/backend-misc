import rpcstub
import client


class RPCClient(client.Client, rpcstub.RPCStub):
    pass