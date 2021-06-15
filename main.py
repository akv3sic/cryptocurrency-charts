from price_history import price_history
from crypto_list import punjenje_popisa
from marketCap import marketCap


popis= punjenje_popisa()

print("Ako želite povijest cijena unesite 1 , ako želite odnos maksimalnog broja coinova i onih u trenutnom opticaju unesite 2")
odabir=int(input())


if odabir==1:

    print ("Unesite ime valute za koju želite analizu(kod 3 slova npr BTC za BITCOIN)")
    valuta=input()
    valute=[]
    valute.append(valuta)
elif odabir==2:
    print("Unesite imena više valuta koje želite uspoređivati odvojenih zarezom (npr BTC,ETH,ATOM)")
    unos=input()
    valute = unos.split(",")

    

odabrane_valute=[]
for valuta in valute:
    
    if valuta in popis:
        coin=popis[valuta]
        
        id = coin["id"]
        name= coin["name"]
        
        a= {"symbol":valuta,
            "id":coin["id"],
            "name":coin["name"],
            "marketCap":coin["marketCap"]
            }


        odabrane_valute.append(a)




    else:
        print("unijeli ste valutu koja ne postoji, unesite ponovno ")
        valuta=input()



if odabir==1:
    price_history(a["id"], a["name"])
elif odabir==2:
    marketCap(odabrane_valute)

else:
    print("Opcija nije podržana")

