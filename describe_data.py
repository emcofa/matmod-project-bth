import pandas as pd

def describe_data_csv():
    """
    Uppgift 2 - Beskrivande statistik
    Skriver ut en tabell med som innehåller
    medelvärde, standardavvikelse, max- och min-värde samt korrelationen mellan variablerna.
    """
    # Läs in data från CSV-filerna som Pandas DataFrames
    df1 = pd.read_csv("./data/gladhammar.csv")
    df2 = pd.read_csv("./data/malilla.csv")
    df3 = pd.read_csv("./data/gotska-sando.csv")

    # Plocka ut kolumnen "value" från varje DataFrame
    values1 = df1["value"]
    values2 = df2["value"]
    values3 = df3["value"]

    # Beräkna beskrivande statistik för varje kolumn
    stats1 = values1.describe().round(2)
    stats2 = values2.describe().round(2)
    stats3 = values3.describe().round(2)

    # Beräkna korrelationen mellan varje par av kolumner
    corr12 = values1.corr(values2).round(2)
    corr13 = values1.corr(values3).round(2)
    corr23 = values2.corr(values3).round(2)

    # Skapa en tabell som samlar all statistik
    stats = pd.DataFrame(
        {"Gladhammar": stats1, "Målilla": stats2, "Gotska Sandö": stats3},
        index=["mean", "std", "min", "max"],
    )
    stats["Korr(Gldhmr-Mlla)"] = corr12
    stats["Korr(Gldhmr-Gtsk Snd)"] = corr13
    stats["Korr(Mlla-Gtsk Snd)"] = corr23

    print(
        "----------------------------------------------------------"
        "----------------------------------------------------------"
    )
    print(stats)
    print(
        "----------------------------------------------------------"
        "----------------------------------------------------------"
    )
