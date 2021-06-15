'''
bitcoin price history - 1 year
'''
import config as cfg
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import mplcursors


def price_history(id, name):

    API_KEY = cfg.api['API_KEY_COINRANKING']
    #url = "https://api.coinranking.com/v2/coin/Qwsogvtv82FCd/history?timePeriod=1y"
    
    url = "https://api.coinranking.com/v2/coin/"+id+"/history?timePeriod=1y"

    headers = {
            'x-access-token': API_KEY
        }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not found.')
    else:
        print('Error ', response.status_code)

    # extracting data
    response = response.json()
    prices = []
    timestamps = []

    price_history = response['data']['history']

    for item in price_history:
        prices.append(round(float(item['price']), 2))
        timestamp = datetime.fromtimestamp(item['timestamp'])
        timestamps.append(timestamp.strftime('%Y-%m-%d'))

    # print('Prices:', prices)
    # print('Timestamps:', timestamps)
    change = response['data']['change']
    change_str = '+' + str(change) + '%' if float(change) > 0  else '-' + str(change) + '%'
    title =''+ name + ' price history - last 1 year ' + '(' + change_str + ')'
    title_color = 'green' if float(change) > 0 else 'red'

    fig, ax = plt.subplots()
    ax.plot(timestamps, prices)
    ax.grid(True)
    ax.set_title(title, color = title_color)
    ax.set_ylabel('Price (USD)')

    ax.xaxis.set_major_locator(plt.MaxNLocator(12))
    plt.xticks(rotation=45)

    crs = mplcursors.cursor(ax, hover=True)     # label appears when hovering mouse over a line
    crs.connect("add", lambda sel: sel.annotation.set_text(
        'Date: {}, Price: {} $'.format(timestamps[int(sel.target.index)], round(sel.target[1], 2))))

    plt.show()
