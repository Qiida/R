from os.path import join
from src.directories import ROOT_DIR
from src.results.data.EventFactory import EventFactory

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


data = pd.read_csv(
    join(
        ROOT_DIR, "results", "FFM3_50", "ar_results.csv"
    ), sep=";"
)

eventFactory = EventFactory(data=data)
events = eventFactory.events

figure, axis = plt.subplots()

plots = []
for event in events.values():
    plots.append(event.plotAR(axis))

plt.show()
plt.grid()
plt.legend(
    plots,
    [
        "1", "2", "3", "4",
        "5", "6", "7", "8",
        "9", "10", "11"
    ]
)

print("The End.")
