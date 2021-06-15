import requests
import config as cfg



def punjenje_popisa():
    popis= {}
    API_KEY = cfg.api['API_KEY_COINRANKING']

    url ="https://api.coinranking.com/v2/coins"

    headers= {
                'x-access-token': API_KEY
            }

    response = requests.request("GET", url, headers=headers)
    data=response.json()

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not found.')
    else:
        print('Error ', response.status_code)


    #data.coins.uuid"
    for coin in data["data"]["coins"]:
        new = {"id":coin["uuid"],
                "name":coin["name"], 
                "marketCap": coin["marketCap"]            
        }
        popis.setdefault(coin["symbol"],new)
    print(popis)
    return popis

    