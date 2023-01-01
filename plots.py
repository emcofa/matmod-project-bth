import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm


def normal_distribution():
    """
    Uppgift 3 - Beskrivande plottar
    Gör minst en graf till för att visuellt analysera er data. Det kan till exempel vara ett histogram som
    jämförs mot normalfördelningen eller ett lådagram för att vissa hur spridningen av data ser ut.
    """
    # Läs in csv-filerna till pandas dataframes
    df1 = pd.read_csv("./data/gladhammar.csv")
    df2 = pd.read_csv("./data/malilla.csv")
    df3 = pd.read_csv("./data/gotska-sando.csv")

    # Plocka ut kolumnen "value" från varje dataframe
    values1 = df1["value"]
    values2 = df2["value"]
    values3 = df3["value"]

    # Skapa ett histogram av datan i varje kolumn
    plt.hist(values1, bins=50, density=True, alpha=0.6, label="Gladhammar")
    plt.hist(values2, bins=50, density=True, alpha=0.6, label="Målilla")
    plt.hist(values3, bins=50, density=True, alpha=0.6, label="Gotska Sandö")

    # Beräkna medelvärdet och standardavvikelsen för varje kolumn
    mean1, std1 = norm.fit(values1)
    mean2, std2 = norm.fit(values2)
    mean3, std3 = norm.fit(values3)

    # Skapa en normalfördelning för varje kolumn baserat på medelvärdet och standardavvikelsen
    x1 = np.linspace(values1.min(), values1.max(), len(values1))
    y1 = norm.pdf(x1, mean1, std1)
    x2 = np.linspace(values2.min(), values2.max(), len(values2))
    y2 = norm.pdf(x2, mean2, std2)
    x3 = np.linspace(values3.min(), values3.max(), len(values3))
    y3 = norm.pdf(x3, mean3, std3)

    # Rita den normalfördelade kurvan för varje kolumn
    plt.plot(x1, y1, "blue", linewidth=2, label="Normalfördelning Gladhammar")
    plt.plot(x2, y2, "red", linewidth=2, label="Normalfördelning Målilla")
    plt.plot(x3, y3, "green", linewidth=2, label="Normalfördelning Gotska Sandön")

    # Lägg till etiketter och legend
    plt.xlabel("Temperatur")

    # Hur sannolikt det är att man kan hitta ett visst värde i datan:
    plt.ylabel("Sannolikhetsdensitet")
    plt.legend()

    # Visa histogrammet
    plt.show()


def box_plot():

    # Läs in csv-filerna till pandas dataframes
    df1 = pd.read_csv("./data/gladhammar.csv")
    df2 = pd.read_csv("./data/malilla.csv")
    df3 = pd.read_csv("./data/gotska-sando.csv")

    # Plocka ut kolumnen "value" från varje dataframe
    values1 = df1["value"]
    values2 = df2["value"]
    values3 = df3["value"]

    # Skapa en lådaplot med data från varje kolumn
    plt.boxplot(
        [values1, values2, values3], labels=["Gladhammar", "Målilla", "Gotska Sandö"]
    )

    # Lägg till etiketter
    plt.xlabel("Values")
    plt.ylabel("Value")

    # Visa lådaploten
    plt.show()
