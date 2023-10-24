import requests

def fetch_exchange_rate(api_key, source, target, date):
    url = f'http://api.exchangerate.host/historical?access_key={api_key}&date={date}&source={source}&currencies={target}&format=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if (source+target) in data['quotes']:
            return data['quotes']['BTCRUB'], data['timestamp']
    return None

def fetch_exchange_rate_live(api_key, source, target):
    url = f'http://api.exchangerate.host/live?access_key={api_key}&source={source}&currencies={target}&format=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if (source+target) in data['quotes']:
            return data['quotes']['BTCRUB'], data['timestamp']
    return None