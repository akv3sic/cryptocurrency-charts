import requests #uvoz biblioteke
import config as cfg #uvoz configuracijskog filea 



def punjenje_popisa():
    popis= {}
    API_KEY = cfg.api['API_KEY_COINRANKING']# api key iz cfg 

    url ="https://api.coinranking.com/v2/coins"#url endpointa 

    headers= {
                'x-access-token': API_KEY #postavljanje api keya u header requesta
            }

    response = requests.request("GET", url, headers=headers) 
    data=response.json()

    if response.status_code == 200:#print poruke 
        print('Success!')
    elif response.status_code == 404:
        print('Not found.')
    else:
        print('Error ', response.status_code)


    
    for coin in data["data"]["coins"]: #parsiranje potrebnih podataka 
        new = {"id":coin["uuid"],
                "name":coin["name"], 
                "marketCap": coin["marketCap"]            
        }
        popis.setdefault(coin["symbol"],new)
   # print(popis)
    return popis

    