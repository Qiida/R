import matplotlib

import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate

from os.path import join

from src.directories import ROOT_DIR

matplotlib.use("TkAgg")



data = pd.read_csv(
    join(
        ROOT_DIR, "results", "FFM3_10", "ar_results.csv"
    ),
    sep=";"
)

print("The End.")


plt.plot()
