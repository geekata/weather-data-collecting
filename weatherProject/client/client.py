import os
import pathlib
import sys


current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
new_path = current_directory + '/app'
sys.path.append(new_path)

from thrift import Thrift
from thrift.transport import TSocket, TSSLSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from gen_py.Weather.Weather import *

__HOST = 'localhost'
__PORT = 9090

if __name__ == '__main__':
    try:
        tsocket = TSocket.TSocket(__HOST, __PORT)
        transport = TTransport.TBufferedTransport(tsocket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)

        transport.open()
        res = client.indicators(1, 17, 5.0, 10.0, 3, 67.61, 101320, 4, 54, 2)
        print(res)

        transport.close()
    except Thrift.TException as ex:
        print(ex.message)
