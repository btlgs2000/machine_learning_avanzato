import requests
import json
import pickle
import datetime
from pathlib import Path
import os
from tqdm import tqdm
import time

import pandas as pd

TODAY = datetime.datetime.now().strftime('%Y_%m_%d')
TARGET_FOLDER = Path(r'F:\Documenti\machine_learning_avanzato\esercizi\SP100\Data')


NOW = int(time.time())

SP500_ASSETS = [
    'AAPL','ABBV','ABT','ACN','ADBE','AIG','ALL','AMGN','AMT','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','BRK-B', 'C','CAT','CHTR','CL','CMCSA','COF','COP','COST','CRM','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTX','SBUX','SLB','SO','SPG','T','TGT','TMO','TXN','UNH','UNP','UPS','USB','V','VZ','WBA','WFC','WMT','XOM'
]

SP500_ASSETS_REMAINING = [
    'C','CAT','CHTR','CL','CMCSA','COF','COP','COST','CRM','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTX','SBUX','SLB','SO','SPG','T','TGT','TMO','TXN','UNH','UNP','UPS','USB','V','VZ','WBA','WFC','WMT','XOM'
]

# YAHOO_AZIMUT_ASSETS = ['BMW.DE']
# INTERNAL_CODES = ['80009']

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "ad0c31dcbdmsh44a9a0734698e76p1a9740jsn19860d7766f5"
    }

for asset_code in tqdm(SP500_ASSETS_REMAINING):
    querystring = {"frequency":"1d","filter":"history","period1":"0","period2": NOW,"symbol":asset_code}
    print(querystring)


    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    
    # file_name = f'{internal_code}_EOD.pickle'
    # with open(TARGET_FOLDER / file_name, 'wb') as f:
    #     pickle.dump(response_obj, f)
    
    filtered_data = [elem for elem in data['prices'] if 'close' in elem]
    df = pd.DataFrame(filtered_data)
    df['date'] = pd.to_datetime(df['date'], unit='s').dt.normalize()
    
    df.sort_values(by=['date'], inplace=True, ignore_index=True)

    
    df.to_csv(TARGET_FOLDER / f'{asset_code}.csv')