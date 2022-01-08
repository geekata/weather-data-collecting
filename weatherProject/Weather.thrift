enum Direction {
  NORTH = 1,
  NORTHWEST = 2,
  NORTHEAST = 3,
  SOUTH = 4,
  SOUTHWEST = 5,
  SOUTHEAST = 6,
  WEST = 7,
  EAST = 8
}

enum Clouds {
  CLEAR = 1,
  OCTANT1 = 2,
  OCTANT2 = 3,
  OCTANT3 = 4,
  OCTANT4 = 5,
  OCTANT5 = 6,
  OCTANT6 = 7,
  OCTANT7 = 8,
  FULLCOVERED = 9,
  DOWNFALL = 10
}

enum Downfall {
  CLEAR = 1,
  RAIN = 2,
  DRIZZLE = 3,
  SLEET = 4,
  SMALLHAIL = 5,
  SHOW = 6,
  SHOWGRAINS = 7,
  ICECRYSTALS = 8,
  MIST = 9,
  FOG = 10,
  SMOKE = 11,
  VOLCANICASH = 12,
  SANDWHIRLS = 13,
  SQUALL = 14,
  TORNADO = 15,
  FUNNELCLOUD = 16,
  WATERSPOUT = 17,
  SANDSTORM = 18,
  DUSTSTORM = 19
}


struct Indicators {
  1: i32 stationID,
  2: i32 temperature,
  3: double windSpeed,
  4: double windSpeedMax,
  5: Direction windDirection,
  6: double relHumidity,
  7: double atmPressure,
  8: Clouds cloudiness,
  9: i32 downfall = 0,
  10: Downfall type = 1
}

struct Response {
  1: string status
}


service Weather {

   Response indicators(1: i32 stationID, 2: double temperature, 3: double windSpeed, 4: double windSpeedMax,
   5: Direction windDirection, 6: double relHumidity, 7: double atmPressure, 8: Clouds cloudiness,
   9: i32 downfall = 0, 10: Downfall type)

}
