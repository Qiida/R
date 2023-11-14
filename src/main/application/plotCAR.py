import re

import pandas
import matplotlib
from matplotlib import pyplot
from src.directories import ROOT_DIR

matplotlib.use("Tkagg")


carTableFilePath = ROOT_DIR + r"\resources\CARTable.csv"
csv: pandas.DataFrame = pandas.read_csv(carTableFilePath)

eventWindow: list = csv.Eventwindow.to_list()

data: dict = dict()
labels: list = list()

for key in csv.keys().to_list():
    if key not in ["Unnamed: 0", "Dates", "Eventwindow"]:
        rawLabel: str = key.split("CAR")[1]
        label: str = ""
        words = re.findall('[A-Z][^A-Z]*', rawLabel)
        if len(words) > 1:
            for word in words:
                label += word + " "
            label = label.rstrip()
        else:
            label = words[0]
        labels.append(label)
        data.update(
            {
                key: csv.get(key).to_list()
            }
        )

x: list = eventWindow
plots: list = list()
for key in data.keys():
    y = data.get(key)
    if key == "CARTransportation":
        plots.append(pyplot.plot(x, y, linewidth=3, color="darkslateblue")[0])
    else:
        plots.append(pyplot.plot(x, y, linewidth=3)[0])

for i in range(len(plots)):
    plot = plots[i]
    plot.set_label(labels[i])

figure = pyplot.gcf()
figure.set_size_inches(12, 11)
axes = figure.gca()
axes.set_xlabel("Event Window", fontname="Times New Roman", weight="bold", fontsize=14)
axes.set_ylabel("CAR", fontname="Times New Roman", weight="bold", fontsize=14)
pyplot.yticks(fontname="Times New Roman", fontsize=11)
pyplot.xticks(ticks=range(-10, 11), fontname="Times New Roman", fontsize=11)
matplotlib.rc('font', family='Times New Roman')

legend = axes.legend(loc='best', frameon=True, fontsize=12)
pyplot.setp(legend.texts, family="Times New Roman")
pyplot.xlim(-10, 10)
pyplot.grid("both")
# pyplot.show()
figure.savefig('20231108_CAREventWindow.svg', dpi=600, bbox_inches='tight')

for key in data:
    print(f"{key}\n{data.get(key)[-1]}\n")
print("\n\nThe End.")
