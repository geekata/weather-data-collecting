import pathlib
import sys
from importlib.machinery import SourceFileLoader

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

from gen_py.Weather.Weather import *
from gen_py.Weather.ttypes import *

__HOST = 'localhost'
__PORT = 9090


class FormatHandler(Iface):
    def indicators(self, stationID, temperature, windSpeed, windSpeedMax,
                    windDirection, relHumidity, atmPressure, cloudiness,
                    downfall, type):

        res = Response()
        res.status = ""
        if stationID < 1:
            res.status = res.status + "wrong station ID;"

        if windSpeed < 0 or windSpeedMax < 0:
            res.status = res.status + "negative wind speed;"

        if windDirection not in Direction._VALUES_TO_NAMES.keys():
            res.status = res.status + "wrong direction;"

        if relHumidity < 0 or relHumidity > 100:
            res.status = res.status + "wrong humidity id;"

        if atmPressure < 0:
            res.status = res.status + "wrong atm pressure;"

        if cloudiness not in Clouds._VALUES_TO_NAMES.keys():
            res.status = res.status + "wrong cloud coef;"

        if downfall < 0:
            res.status = res.status + "wrong downfall;"

        if type not in Downfall._VALUES_TO_NAMES.keys():
            res.status = res.status + "wrong downfall type;"

        if len(res.status) == 0:
            res.status = "OK"
            data = Indicators(stationID, temperature, windSpeed, windSpeedMax,
                              windDirection, relHumidity, atmPressure, cloudiness,
                              downfall, type)
            print(data)
        else:
            res.status = res.status[:-1]

        return res


if __name__ == '__main__':
    processor = Processor(FormatHandler())
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TCompactProtocol.TCompactProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the RPC server at', __HOST, ':', __PORT)
    rpcServer.serve()
    print('done')
