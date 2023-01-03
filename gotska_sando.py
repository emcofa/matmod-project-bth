#!/usr/bin/python3

from datetime import datetime
from smhi_open_data import SMHIOpenDataClient, Parameter
import pandas as pd
import requests


def gotska_sando_data():
    """
    Hämtar datan från SMHIs API Gotska Sandö
    """
    html_smhi = 'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/89230/period/latest-months/data.json'
    r = requests.get(html_smhi)
    data = r.json()

    # read data into a DataFrame from json response
    df = pd.DataFrame(data['value'])

    def convert_to_datetime(x):
        return datetime.fromtimestamp(x/1000)

    timstamp = df['date'][1]

    time = convert_to_datetime(timstamp)

    df['date'] = df['date'].apply(convert_to_datetime)
    print(df.to_csv('./data/gotska-sando.csv', sep=',', encoding='utf-8'))

