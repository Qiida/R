class FirmData:
    def __init__(self, path):
        self.dates = []

        file = open(path)

        self.lines = file.readlines()
        self.__findDates()

        file.close()

    def __findDates(self):
        for line in self.lines:

            rows = line.split(";")
            date = rows[1]

            if self.__foundAllDates(date):
                return
            else:
                self.dates.append(date)

    def __foundAllDates(self, date):
        if len(self.dates) > 0 and date == self.dates[0]:
            return True

