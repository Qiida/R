from src.main.data.Row import Row


class MarketDataFFM3:
    def __init__(self, path, out, dates):
        """
        This Class parses the raw Data from <F-F_Research_Data_Factors_daily.csv> into
        the input format for the R-Package EventStudy <02_FirmData.csv>.

        :param path: absolut path to input Data
        :param out: absolut path to output Data
        :param dates: list with observed dates
        """
        file = open(path)

        self.out = out
        self.dates = dates
        self.rows = list()
        self.__buildRows(file)
        self.__writeCSV()

        file.close()

    def __writeCSV(self):
        """
        Creates and writes a CSV-File with output-path
        :return: None
        """
        f = open(self.out, "w")
        for row in self.rows:
            f.write(
                f"{row.date};{row.MktRF};{row.SMB};{row.HML};{row.RF}\n"
            )
        f.close()

    def __buildRows(self, file):
        """
        Builds Row-Objects and stores them in a list
        :param file: opened from path
        :return: None
        """
        self.lines = file.readlines()
        for line in self.lines:
            values = line.split(";")
            date = self.__formatDate(values[0])
            if date in self.dates:
                self.rows.append(
                    Row(
                        date=date,
                        MktRF=values[1],
                        SMB=values[2],
                        HML=values[3],
                        RF=values[4].split("\n")[0]
                    )
                )

    @classmethod
    def __formatDate(cls, raw):
        """
        Formats raw Date into dd-mm-year
        : param raw: date in raw format
        :return: formatted Date
        """
        if len(raw) == 8:
            year = raw[0] + raw[1] + raw[2] + raw[3]
            month = raw[4] + raw[5]
            day = raw[6] + raw[7]
            return f"{day}.{month}.{year}"


if __name__ == '__main__':
    help(MarketDataFFM3)
