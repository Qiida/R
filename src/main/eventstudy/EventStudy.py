import eventstudy as es
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

es.Single.import_returns('returns.csv')
es.Single.import_FamaFrench('famafrench.csv')
event = es.Single.FamaFrench_3factor(
    security_ticker="AAPL",
    event_date=np.datetime64("2013-03-04"),
    event_window=(-2, +10),
    estimation_size=300,
    buffer_size=30
)

event.plot(AR=True)
plt.show()
