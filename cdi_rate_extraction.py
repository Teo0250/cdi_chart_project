import os
import time
import json
from random import random
from datetime import datetime

import requests

def cdi_extraction():

    URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

    # Creating the date and time variables

    for _ in range(0, 10):
        date_time = datetime.now()
        date = datetime.strftime(date_time, '%Y/%m/%d')
        time_str = datetime.strftime(date_time, '%H:%M:%S')

        # Fetching CDI rate from B3 website

        try:
            response = requests.get(URL)
            response.raise_for_status()
        except requests.HTTPError as exc:
            print("Data not found, continuing.")
            cdi = None
        except Exception as exc:
            print("Error, stopping execution.")
            raise exc
        else:
            data = json.loads(response.text)
            cdi = float(data['taxa'].replace(',', '.')) + (random() - 0.5)

        # Checking if the "taxa-cdi.csv" file exists

        if os.path.exists('./taxa-cdi.csv') == False:

            with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
                fp.write('date,time,rate\n')

        # Saving data in the "taxa-cdi.csv" file

        with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{date},{time_str},{cdi}\n')

        time.sleep(2 + (random() - 0.5))

if __name__ == "__main__":
    cdi_extraction()
