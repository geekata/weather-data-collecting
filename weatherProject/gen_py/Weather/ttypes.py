from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Direction(object):
    NORTH = 1
    NORTHWEST = 2
    NORTHEAST = 3
    SOUTH = 4
    SOUTHWEST = 5
    SOUTHEAST = 6
    WEST = 7
    EAST = 8

    _VALUES_TO_NAMES = {
        1: "NORTH",
        2: "NORTHWEST",
        3: "NORTHEAST",
        4: "SOUTH",
        5: "SOUTHWEST",
        6: "SOUTHEAST",
        7: "WEST",
        8: "EAST",
    }

    _NAMES_TO_VALUES = {
        "NORTH": 1,
        "NORTHWEST": 2,
        "NORTHEAST": 3,
        "SOUTH": 4,
        "SOUTHWEST": 5,
        "SOUTHEAST": 6,
        "WEST": 7,
        "EAST": 8,
    }


class Clouds(object):
    CLEAR = 1
    OCTANT1 = 2
    OCTANT2 = 3
    OCTANT3 = 4
    OCTANT4 = 5
    OCTANT5 = 6
    OCTANT6 = 7
    OCTANT7 = 8
    FULLCOVERED = 9
    DOWNFALL = 10

    _VALUES_TO_NAMES = {
        1: "CLEAR",
        2: "OCTANT1",
        3: "OCTANT2",
        4: "OCTANT3",
        5: "OCTANT4",
        6: "OCTANT5",
        7: "OCTANT6",
        8: "OCTANT7",
        9: "FULLCOVERED",
        10: "DOWNFALL",
    }

    _NAMES_TO_VALUES = {
        "CLEAR": 1,
        "OCTANT1": 2,
        "OCTANT2": 3,
        "OCTANT3": 4,
        "OCTANT4": 5,
        "OCTANT5": 6,
        "OCTANT6": 7,
        "OCTANT7": 8,
        "FULLCOVERED": 9,
        "DOWNFALL": 10,
    }


class Downfall(object):
    CLEAR = 1
    RAIN = 2
    DRIZZLE = 3
    SLEET = 4
    SMALLHAIL = 5
    SHOW = 6
    SHOWGRAINS = 7
    ICECRYSTALS = 8
    MIST = 9
    FOG = 10
    SMOKE = 11
    VOLCANICASH = 12
    SANDWHIRLS = 13
    SQUALL = 14
    TORNADO = 15
    FUNNELCLOUD = 16
    WATERSPOUT = 17
    SANDSTORM = 18
    DUSTSTORM = 19

    _VALUES_TO_NAMES = {
        1: "CLEAR",
        2: "RAIN",
        3: "DRIZZLE",
        4: "SLEET",
        5: "SMALLHAIL",
        6: "SHOW",
        7: "SHOWGRAINS",
        8: "ICECRYSTALS",
        9: "MIST",
        10: "FOG",
        11: "SMOKE",
        12: "VOLCANICASH",
        13: "SANDWHIRLS",
        14: "SQUALL",
        15: "TORNADO",
        16: "FUNNELCLOUD",
        17: "WATERSPOUT",
        18: "SANDSTORM",
        19: "DUSTSTORM",
    }

    _NAMES_TO_VALUES = {
        "CLEAR": 1,
        "RAIN": 2,
        "DRIZZLE": 3,
        "SLEET": 4,
        "SMALLHAIL": 5,
        "SHOW": 6,
        "SHOWGRAINS": 7,
        "ICECRYSTALS": 8,
        "MIST": 9,
        "FOG": 10,
        "SMOKE": 11,
        "VOLCANICASH": 12,
        "SANDWHIRLS": 13,
        "SQUALL": 14,
        "TORNADO": 15,
        "FUNNELCLOUD": 16,
        "WATERSPOUT": 17,
        "SANDSTORM": 18,
        "DUSTSTORM": 19,
    }


class Indicators(object):
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


    def __init__(self, stationID=None, temperature=None, windSpeed=None, windSpeedMax=None, windDirection=None, relHumidity=None, atmPressure=None, cloudiness=None, downfall=0, type=1,):
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
                if ftype == TType.I32:
                    self.temperature = iprot.readI32()
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
        oprot.writeStructBegin('Indicators')
        if self.stationID is not None:
            oprot.writeFieldBegin('stationID', TType.I32, 1)
            oprot.writeI32(self.stationID)
            oprot.writeFieldEnd()
        if self.temperature is not None:
            oprot.writeFieldBegin('temperature', TType.I32, 2)
            oprot.writeI32(self.temperature)
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


class Response(object):
    """
    Attributes:
     - status

    """


    def __init__(self, status=None,):
        self.status = status

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
                if ftype == TType.STRING:
                    self.status = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Response')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRING, 1)
            oprot.writeString(self.status.encode('utf-8') if sys.version_info[0] == 2 else self.status)
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
all_structs.append(Indicators)
Indicators.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'stationID', None, None, ),  # 1
    (2, TType.I32, 'temperature', None, None, ),  # 2
    (3, TType.DOUBLE, 'windSpeed', None, None, ),  # 3
    (4, TType.DOUBLE, 'windSpeedMax', None, None, ),  # 4
    (5, TType.I32, 'windDirection', None, None, ),  # 5
    (6, TType.DOUBLE, 'relHumidity', None, None, ),  # 6
    (7, TType.DOUBLE, 'atmPressure', None, None, ),  # 7
    (8, TType.I32, 'cloudiness', None, None, ),  # 8
    (9, TType.I32, 'downfall', None, 0, ),  # 9
    (10, TType.I32, 'type', None, 1, ),  # 10
)
all_structs.append(Response)
Response.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'status', 'UTF8', None, ),  # 1
)
fix_spec(all_structs)
del all_structs
