import pandas as pd

def sample_data():
    """
    Uppgift 1 - Beskriv data
    Skriver ut ett urval av data från Gotska Sandö
    """
    # Läs in csv-filen till en pandas-dataframe
    df = pd.read_csv("./data/gotska-sando.csv")
    
    df.reset_index(inplace=False)

    # Visa upp de första fem raderna i tabellen
    print("Urval av data från väderstation Gotska Sandön")
    print("----------------------------------------------------")
    print(df.head())
    print("----------------------------------------------------")