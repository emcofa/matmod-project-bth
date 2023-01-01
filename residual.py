#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import statsmodels.formula.api as smf
import seaborn as sns


def residual():
    """
    Uppgift 6 - Residualanalys
    Beräkna residualerna, e= y−y^, för de två modellerna och plotta dessa. Hur ser de ut? Plotta
    residualerna mot normalfördelningen (i Python t.ex. genom Seaborn.distplot eller
    scipy.stats.probplot). Kommentera dessa plottar utseende och beskriv vilka slutsatser vi kan dra
    utifrån dessa. Finns det några beroenden? Hur väl följer residualerna en normalfördelning?
    Beräkna också deras varians och argumentera för vilken modell vi bör använda utifrån dina resultat.
    """
    # Läs in csv-filen och konvertera datevärdena till datumobjekt
    df = pd.read_csv("./data/gladhammar.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = mdates.date2num(df["date"])

    y = df["value"]

    y_min = np.min(y)
    constant = 10

    # Konvertera negativa värden till positiva
    if y_min < 0:
        df["log_value"] = np.log(y - y_min + constant)
    else:
        df["log_value"] = np.log(y)

    # Skapa och träna en ny regressionsmodell med 'log_value' som förklarande variabel och 'date' som beroende variabel
    exp_model = smf.ols("log_value ~ date", df)
    exp_results = exp_model.fit()

    # Kondifensintervall 95%
    alpha = 0.05
    exp_predictions = exp_results.get_prediction(df).summary_frame(alpha)

    # Transformera tillbaka modellen och förutsägelserna innan du plottar dem
    if y_min < 0:
        exp_model = np.exp(exp_predictions["mean"]) + y_min - constant
    else:
        exp_model = np.exp(exp_predictions["mean"])

    # Skapa och träna en ny linjär regressionsmodell med 'date' som förklarande variabel och 'value' som beroende variabel
    lin_model = smf.ols("value ~ date", df)
    lin_results = lin_model.fit()

    # Kondifensintervall 95%
    lin_predictions = lin_results.get_prediction(df).summary_frame(alpha)

    # Beräkna residualerna för linjär modell 𝑒= 𝑦−𝑦̂
    lin_residuals = df["value"] - lin_predictions["mean"]

    # Beräkna residualerna för exponentiell modell 𝑒= 𝑦−𝑦̂
    exp_residuals = df["value"] - exp_model

    date_formatter = mdates.DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_formatter)

    # Plotta residualerna för linjär modell
    plt.scatter(
        df["date"], lin_residuals, label="Linjär modell Residualer", s=6, color="blue"
    )
    plt.scatter(
        df["date"],
        exp_residuals,
        label="Exponentiell modell Residualer",
        s=6,
        color="green",
    )

    plt.xlabel("Datum")
    plt.ylabel("Residualer")
    plt.legend()
    plt.show()

    # Plotta residualerna för linjär modell mot normalfördelningen
    sns.distplot(lin_residuals, label="Linjär modell residualer")

    # Plotta residualerna för exponentiell modell mot normalfördelningen
    sns.distplot(exp_residuals, label="Exponentiell modell residualer")

    plt.xlabel("Residualer")
    plt.ylabel("Frekvens")
    plt.legend()
    plt.show()

    # Beräkna variansen för residualerna för linjär modell
    lin_variance = np.var(lin_residuals)

    # Beräkna variansen för residualerna för exponentiell modell
    exp_variance = np.var(exp_residuals)

    # Jämför variansen för de två modellerna och argumentera för vilken modell som är bäst lämpad för data
    print("Linjär varians:", lin_variance)
    print("Transformerad varians:", exp_variance)
    if lin_variance < exp_variance:
        print(
            "Linjär modellen ger residualer med lägre varians än exponentiell modellen, så den kan vara lämpligare för data."
        )
    else:
        print(
            "Exponentiell modellen ger residualer med lägre varians än linjär modellen, så den kan vara lämpligare för data."
        )
