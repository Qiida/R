class Row:
    def __init__(self, date, MktRF, SMB, HML, RF):
        self.date = date
        self.MktRF = float(MktRF)
        self.SMB = float(SMB)
        self.HML = float(HML)
        self.RF = float(RF)
