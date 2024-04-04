import requests
import keys
import pandas as pd
import schedule
import time
import beepy
import chime



def get_crypto_rates(base_currency='INR',assets ='BTC,ETH,DOGE,MATIC,XRP,USDC,BUSD,SHIB,ATOM'):
    url = 'https://api.nomics.com/v1/currencies/ticker'


    payload = {'key': keys.NOMICS_API_KEY, 'convert': base_currency, 'ids': assets, 'interval': '1d'}
    response = requests.get(url,params=payload)
    data = response.json()


    crypto_currency,crypto_price,crypto_timestamp = [],[],[]


    #print(data)

    for asset in data:
        crypto_currency.append(asset['currency'])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(assets)


    raw_data ={
        'assets': crypto_currency,
        'rates': crypto_price,
        'timestamp':crypto_timestamp
    }

    df = pd.DataFrame(raw_data)
    print(df)
    return df

def set_alert(dataframe,asset,alert_hight_Price):
    crypto_vlaue = float(dataframe[dataframe['assets'] == asset]['rates'].item())

    details = f'{asset}: {crypto_vlaue}, Target: {alert_hight_Price}' 

    if crypto_value >= alert_hight_Price:
        print()


schedule.every(2).seconds.do(get_crypto_rates)

while True:
    schedule.run_pending()
    time.sleep(1)


