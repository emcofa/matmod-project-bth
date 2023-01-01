#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import statsmodels.formula.api as smf


def transformation():
    """
    Uppgift 5 - Transformerad data
    Transformerar data till en exponentiell modell
    Transformeras sedan tillbaka för att kunna jämföra originaldata med linjär regression
    """
    # Läs in csv-filen och konvertera datevärdena till datumobjekt
    df = pd.read_csv('./data/gladhammar.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = mdates.date2num(df['date'])
    
    y = df['value']
    x = df['date']

    y_min = np.min(y)
    constant = 10
    
    if y_min < 0:
        df['log_value'] = np.log(y - y_min + constant)
    else:
        df['log_value'] = np.log(y)

    # Skapa och träna en ny regressionsmodell med 'log_value' som förklarande variabel och 'date' som beroende variabel
    exp_model = smf.ols('log_value ~ date', df)
    exp_results = exp_model.fit()
    
    # Kondifensintervall 95%
    alpha = 0.05
    exp_predictions = exp_results.get_prediction(df).summary_frame(alpha)
    
    if y_min < 0:
        exp_model = np.exp(exp_predictions['mean']) + y_min - constant
    else:
        exp_model = np.exp(exp_predictions['mean'])

    # Skapa och träna en ny linjär regressionsmodell med 'date' som förklarande variabel och 'value' som beroende variabel
    lin_model = smf.ols('value ~ date', df)
    lin_results = lin_model.fit()

    # Kondifensintervall 95%
    lin_predictions = lin_results.get_prediction(df).summary_frame(alpha)

    date_formatter = mdates.DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.scatter(x, y, label='Originaldata Gladhammar', s=6, color='red')
    plt.plot(x, lin_predictions['mean'], linewidth=1, color='blue', label='Linjär regressionslinje Gladhammar')
    plt.fill_between(x, lin_predictions['mean_ci_lower'], lin_predictions['mean_ci_upper'], alpha=.5, label='Konfidensintervall 95% Gladhammar')
    plt.plot(x, exp_model, linewidth=1, color='green', label='Exponentiell regressionslinje Gladhammar')

    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.legend()
    plt.show()

