from tcxreader.tcxreader import TCXReader, TCXTrackPoint


class Runner:

    def __init__(self, file=None, name=None):
        self.__file = file
        self.__name = name

        tcx_reader = TCXReader()

        self.__data = tcx_reader.read(self.__file)
        self.__track = []
        self.__calorie = 0
        self.__elevation = []
        self.__heartrate = []
        self.__speed = []
        self.read_data()

    def read_data(self):
        all_coord = []
        elevation = []
        heartrate = []
        speed = []
        for i in self.__data.trackpoints:
            all_coord.append((i.latitude, i.longitude))
            elevation.append(i.elevation)
            heartrate.append(i.hr_value)
            if i.tpx_ext.get('Speed'):
                speed.append(i.tpx_ext.get('Speed')*1.60934)
            else:
                speed.append(None)

        self.__speed = speed
        self.__heartrate = heartrate
        self.__track = all_coord
        self.__elevation = elevation

    @property
    def get_track(self):
        return self.__track

    @property
    def get_elevation(self):
        return self.__elevation

    @property
    def get_heartrate(self):
        return self.__heartrate

    @property
    def get_speed(self):
        return self.__speed