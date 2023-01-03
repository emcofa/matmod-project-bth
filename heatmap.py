import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def heatmap():
    """
    Uppgift 2 - Beskrivande statistik
    Visar korrelationen i en heatmap
    """
    # Läser in data från CSV-filerna som Pandas DataFrames
    df1 = pd.read_csv("./data/gladhammar.csv")
    df2 = pd.read_csv("./data/malilla.csv")
    df3 = pd.read_csv("./data/gotska-sando.csv")

    # Plockar ut kolumnen "value" från varje DataFrame
    values1 = df1["value"]
    values2 = df2["value"]
    values3 = df3["value"]

    # Räknar korrelationen
    corr_matrix = pd.DataFrame([values1, values2, values3]).transpose().corr()

    # Skapar heatmap
    sns.heatmap(
        corr_matrix,
        annot=True,
        xticklabels=["Gladhammar", "Målilla", "Gotska Sandön"],
        yticklabels=["Gladhammar", "Målilla", "Gotska Sandön"],
    )

    plt.title("Korrelation mellan väderstationer")

    plt.show()
