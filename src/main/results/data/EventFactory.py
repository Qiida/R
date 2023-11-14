import re

import pandas as pd

from src.results.data.Event import Event


class EventFactory:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.events = dict()

        for row in self.data.iterrows():
            self.__event = None
            series = row[1]

            for key in series.keys():
                self.__processKey(key, series)

            self.__addEvent()

    def __addEvent(self):
        self.events.update(
            {
                self.__event.ID: self.__event
            }
        )

    def __processKey(self, key, series):
        t, dType = self.__extractData(key)
        match dType:
            case "Event ID":
                ID = int(series.get(key))
                self.__event = Event(ID=ID)
            case "AR":
                self.__appendValue(
                    dictionary=self.__event.AR,
                    key=key, series=series, t=t
                )
            case "t-value":
                self.__appendValue(
                    dictionary=self.__event.TValue,
                    key=key, series=series, t=t
                )
            case "p-value":
                self.__appendValue(
                    dictionary=self.__event.PValue,
                    key=key, series=series, t=t
                )

    def __extractData(self, key):
        dType = self.match(
            regex=r"^[a-zA-Z-?\s?]+",
            string=key
        )
        t = self.match(
            regex=r"-?\d+",
            string=key
        )
        return t, dType

    @classmethod
    def __appendValue(cls, dictionary, key, series, t):
        value = float(series.get(key))
        dictionary.update(
            {
                int(t): value
            }
        )

    @classmethod
    def match(cls, regex, string):
        match = re.search(regex, string)
        if match is not None:
            return match.group(0)

