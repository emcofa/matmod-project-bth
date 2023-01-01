import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def heatmap():
    """
    Uppgift 2 - Beskrivande statistik
    Visar korrelationen i en heatmap
    """
    # Läs in data från CSV-filerna som Pandas DataFrames
    df1 = pd.read_csv("./data/gladhammar.csv")
    df2 = pd.read_csv("./data/malilla.csv")
    df3 = pd.read_csv("./data/gotska-sando.csv")

    # Plocka ut kolumnen "value" från varje DataFrame
    values1 = df1["value"]
    values2 = df2["value"]
    values3 = df3["value"]

    # Räkna korrelationen
    corr_matrix = pd.DataFrame([values1, values2, values3]).transpose().corr()

    # Skapa heatmap
    sns.heatmap(
        corr_matrix,
        annot=True,
        xticklabels=["Gladhammar", "Målilla", "Gotska Sandön"],
        yticklabels=["Gladhammar", "Målilla", "Gotska Sandön"],
    )

    plt.title("Korrelation mellan väderstationer")

    plt.show()
