from activereader import *


reader = Tcx.from_file('static/data/435340338.tcx')

records = [
  {
    'Distance parcourue': reader.distance_m,
    'Vitesse max': reader.laps,
    'Altitude': "assa",
  }
]
print(records)

