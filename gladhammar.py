#!/usr/bin/python3

from datetime import datetime
from smhi_open_data import SMHIOpenDataClient, Parameter
import pandas as pd
import requests

def gladhammar_data():
    """
    Hämtar datan från SMHIs API Gladhammar väderstation
    """
    html_smhi = 'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/76420/period/latest-months/data.json'
    r = requests.get(html_smhi)
    data = r.json()

    # read data into a DataFrame from json response
    df = pd.DataFrame(data['value'])

    def convert_to_datetime(x):
        return datetime.fromtimestamp(x/1000)

    timstamp = df['date'][1]

    time = convert_to_datetime(timstamp)

    print(time)

    df['date'] = df['date'].apply(convert_to_datetime)
    # print(df.head(2000).to_csv('./data/gladhammar-test.csv', sep=',', encoding='utf-8'))
    print(df.to_csv('./data/gladhammar.csv', sep=',', encoding='utf-8'))
