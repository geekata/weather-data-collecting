from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def indicators(self, stationID, temperature, windSpeed, windSpeedMax, windDirection, relHumidity, atmPressure, cloudiness, downfall, type):
        """
        Parameters:
         - stationID
         - temperature
         - windSpeed
         - windSpeedMax
         - windDirection
         - relHumidity
         - atmPressure
         - cloudiness
         - downfall
         - type

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def indicators(self, stationID, temperature, windSpeed, windSpeedMax, windDirection, relHumidity, atmPressure, cloudiness, downfall, type):
        """
        Parameters:
         - stationID
         - temperature
         - windSpeed
         - windSpeedMax
         - windDirection
         - relHumidity
         - atmPressure
         - cloudiness
         - downfall
         - type

        """
        self.send_indicators(stationID, temperature, windSpeed, windSpeedMax, windDirection, relHumidity, atmPressure, cloudiness, downfall, type)
        return self.recv_indicators()

    def send_indicators(self, stationID, temperature, windSpeed, windSpeedMax, windDirection, relHumidity, atmPressure, cloudiness, downfall, type):
        self._oprot.writeMessageBegin('indicators', TMessageType.CALL, self._seqid)
        args = indicators_args()
        args.stationID = stationID
        args.temperature = temperature
        args.windSpeed = windSpeed
        args.windSpeedMax = windSpeedMax
        args.windDirection = windDirection
        args.relHumidity = relHumidity
        args.atmPressure = atmPressure
        args.cloudiness = cloudiness
        args.downfall = downfall
        args.type = type
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_indicators(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = indicators_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "indicators failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["indicators"] = Processor.process_indicators
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_indicators(self, seqid, iprot, oprot):
        args = indicators_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = indicators_result()
        try:
            result.success = self._handler.indicators(args.stationID, args.temperature, args.windSpeed, args.windSpeedMax, args.windDirection, args.relHumidity, args.atmPressure, args.cloudiness, args.downfall, args.type)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("indicators", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class indicators_args(object):
    """
    Attributes:
     - stationID
     - temperature
     - windSpeed
     - windSpeedMax
     - windDirection
     - relHumidity
     - atmPressure
     - cloudiness
     - downfall
     - type

    """


    def __init__(self, stationID=None, temperature=None, windSpeed=None, windSpeedMax=None, windDirection=None, relHumidity=None, atmPressure=None, cloudiness=None, downfall=0, type=None,):
        self.stationID = stationID
        self.temperature = temperature
        self.windSpeed = windSpeed
        self.windSpeedMax = windSpeedMax
        self.windDirection = windDirection
        self.relHumidity = relHumidity
        self.atmPressure = atmPressure
        self.cloudiness = cloudiness
        self.downfall = downfall
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.stationID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.temperature = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.windSpeed = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.windSpeedMax = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.windDirection = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.DOUBLE:
                    self.relHumidity = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.DOUBLE:
                    self.atmPressure = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.cloudiness = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.downfall = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('indicators_args')
        if self.stationID is not None:
            oprot.writeFieldBegin('stationID', TType.I32, 1)
            oprot.writeI32(self.stationID)
            oprot.writeFieldEnd()
        if self.temperature is not None:
            oprot.writeFieldBegin('temperature', TType.DOUBLE, 2)
            oprot.writeDouble(self.temperature)
            oprot.writeFieldEnd()
        if self.windSpeed is not None:
            oprot.writeFieldBegin('windSpeed', TType.DOUBLE, 3)
            oprot.writeDouble(self.windSpeed)
            oprot.writeFieldEnd()
        if self.windSpeedMax is not None:
            oprot.writeFieldBegin('windSpeedMax', TType.DOUBLE, 4)
            oprot.writeDouble(self.windSpeedMax)
            oprot.writeFieldEnd()
        if self.windDirection is not None:
            oprot.writeFieldBegin('windDirection', TType.I32, 5)
            oprot.writeI32(self.windDirection)
            oprot.writeFieldEnd()
        if self.relHumidity is not None:
            oprot.writeFieldBegin('relHumidity', TType.DOUBLE, 6)
            oprot.writeDouble(self.relHumidity)
            oprot.writeFieldEnd()
        if self.atmPressure is not None:
            oprot.writeFieldBegin('atmPressure', TType.DOUBLE, 7)
            oprot.writeDouble(self.atmPressure)
            oprot.writeFieldEnd()
        if self.cloudiness is not None:
            oprot.writeFieldBegin('cloudiness', TType.I32, 8)
            oprot.writeI32(self.cloudiness)
            oprot.writeFieldEnd()
        if self.downfall is not None:
            oprot.writeFieldBegin('downfall', TType.I32, 9)
            oprot.writeI32(self.downfall)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 10)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(indicators_args)
indicators_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'stationID', None, None, ),  # 1
    (2, TType.DOUBLE, 'temperature', None, None, ),  # 2
    (3, TType.DOUBLE, 'windSpeed', None, None, ),  # 3
    (4, TType.DOUBLE, 'windSpeedMax', None, None, ),  # 4
    (5, TType.I32, 'windDirection', None, None, ),  # 5
    (6, TType.DOUBLE, 'relHumidity', None, None, ),  # 6
    (7, TType.DOUBLE, 'atmPressure', None, None, ),  # 7
    (8, TType.I32, 'cloudiness', None, None, ),  # 8
    (9, TType.I32, 'downfall', None, 0, ),  # 9
    (10, TType.I32, 'type', None, None, ),  # 10
)


class indicators_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Response()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('indicators_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(indicators_result)
indicators_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Response, None], None, ),  # 0
)
fix_spec(all_structs)
del all_structs
