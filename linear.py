#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels.formula.api as smf

def linear_regression():
    """
    Uppgift 4 - Linjär regression 
    Utför en linjärregression av minst en av variablerna och ett tillhörande 95% konfidensintervall. 
    Rapportera variablerna a  och b i sambandet y=a+b∙x  samt punktskattningens 
    konfidensintervall av dessa. Visualisera detta i en graf med den linjära modellen, konfidensintervallet 
    och originaldata i samma figur. 
    """
    # Läs in csv-filen och konvertera datevärdena till datumobjekt
    df = pd.read_csv('./data/gladhammar.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = mdates.date2num(df['date'])

    print(df['value'])
    model = smf.ols('value ~ date', df)
    results = model.fit()
    
    a, b = results.params
    x = df['date']
    y = a + b * x

    conf_int = results.conf_int()
    
    #Kondifensintervall 95%
    alpha = 0.05
    predictions = results.get_prediction(df).summary_frame(alpha)

    print("-------------------------------------"
          "----------------------------------------")
    print("a: ", a)
    print("b: ", b)
    a_ci_lower, a_ci_upper = conf_int[0]
    print(f"Punktskattningens konfidensintervall för a (Intercept) är {a_ci_lower:.3f} ± {a_ci_upper:.3f}")
    b_ci_lower, b_ci_upper = conf_int[1]
    print(f"Punktskattningens konfidensintervall för b (date) är {b_ci_lower:.3f} ± {b_ci_upper:.3f}")
    print("-------------------------------------"
    "----------------------------------------")


    date_formatter = mdates.DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.plot(x, y, linewidth=1, label='Regressionslinje Gladhammar')
    plt.scatter(df['date'], df['value'], label='Originaldata Gladhammar', s=6, color='red')
    # plt.plot(df['date'], predictions['mean'], linewidth=1, label='Regressionslinje Gladhammar')
    plt.fill_between(df['date'], predictions['mean_ci_lower'], predictions['mean_ci_upper'], alpha=.5, label='Konfidensintervall 95% Gladhammar')

    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.legend()
    plt.show()
