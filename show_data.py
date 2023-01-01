import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


def visualize_data():
    """
    Uppgift 2 - Beskriv data
    En visuell representation av hur datamängden ser ut
    """
    # Läs in data från CSV-filerna som Pandas DataFrames
    df1 = pd.read_csv("./data/gladhammar.csv")
    df2 = pd.read_csv("./data/malilla.csv")
    df3 = pd.read_csv("./data/gotska-sando.csv")

    # Välj de kolumner som du vill använda som x- och y-värden för diagrammet
    x1 = df1["date"]
    y1 = df1["value"]
    x2 = df2["date"]
    y2 = df2["value"]
    x3 = df3["date"]
    y3 = df3["value"]

    datum1_dt = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in x1]
    datum2_dt = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in x2]
    datum3_dt = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in x3]

    # Konvertera datetime.datetime-objekt till datetime.date-objekt
    datum1_date = [d.date() for d in datum1_dt]
    datum2_date = [d.date() for d in datum2_dt]
    datum3_date = [d.date() for d in datum3_dt]

    plt.plot_date(
        datum1_date,
        y1,
        tz="Europe/Stockholm",
        xdate=True,
        fmt='o',
        color="r",
        markersize=2,
        label="Gladhammar väderstation",
    )
    plt.plot_date(
        datum2_date,
        y2,
        tz="Europe/Stockholm",
        xdate=True,
        color="g",
        markersize=2,
        label="Målilla väderstation",
    )
    plt.plot_date(
        datum3_date,
        y3,
        tz="Europe/Stockholm",
        xdate=True,
        color="b",
        markersize=2,
        label="Gotska Sandön väderstation",
    )
    
    x_ticks = datum1_date[::120]  # Varannat datum

    # Skapa en lista med etiketterna för de olika värdena
    x_labels = [d.strftime('%Y-%m-%d') for d in x_ticks]  # Formatera datumen

    # Lägg till etiketter och titel på diagrammet
    plt.xlabel("Date")
    plt.ylabel("Temperatur")
    plt.title("Uppmätta temperaturer (3 månaders intervall)")

    # Visa diagrammet
    plt.legend()
    plt.xticks(x_ticks, x_labels, rotation=70)
    plt.show()
