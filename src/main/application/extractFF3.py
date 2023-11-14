from src.main.data.FirmData import FirmData
from src.main.data.MarketDataFFM3 import MarketDataFFM3

from os.path import join

from src.directories import DATA_DIR
from src.directories import RESOURCES_DIR

firmData = FirmData(join(DATA_DIR, "02_FirmData.csv"))
marketData = MarketDataFFM3(
    path=join(RESOURCES_DIR, "F-F_Research_Data_Factors_daily.csv"),
    out=join(DATA_DIR, "MarketData_daily_FFM3.csv"),
    dates=firmData.dates
)
print("The End.")
