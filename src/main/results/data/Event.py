class Event:
    def __init__(self, ID):
        self.ID = ID
        self.AR = dict()
        self.PValue = dict()
        self.TValue = dict()




    def plotAR(self, axis):
        time = list(self.AR.keys())
        ar = list(self.AR.values())

        plot = axis.plot(
            time, ar
        )

        return plot


