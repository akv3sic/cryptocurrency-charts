from price_history import price_history #uvoz funkcije koja vizualizira povijest pojedine kriptovalute
from crypto_list import punjenje_popisa #uvoz fukcije za dohvat osnovnih podataka o kriptovalutama 
from marketCap import marketCap #uvoz funkcije za vizualizaciju marketCapa
import sys 


popis= punjenje_popisa()   #dohvaćanje popisa kriptovaluta s API-a radi dohvata ID-a (Potreban za poziv na endpoint koji dohvaća povijest kriptovalute)

print("Ako želite povijest cijena unesite 1. \nAko želite usporediti marketCap više kriptovaluta unesite 2")# izbornik na terminalu 
odabir=int(input()) #zapisivanje unosa sa tipkovnice


if odabir==1: #u slučaju odabira povijesti 

    print ("Unesite ime valute za koju želite analizu(kod 3 slova npr BTC za BITCOIN)")
    valuta=input()
    valute=[]
    valute.append(valuta) #iako je 1 stavka stavljam je u niz da bi mogao koristiti istu funkciju za spremanje podataka u obliku riječnika
elif odabir==2:   #u slučaju odabira marketCapa
    print("Unesite imena više valuta koje želite uspoređivati odvojenih zarezom (npr BTC,ETH,ATOM)")
    unos=input()
    unos=''.join(unos.split())  #uklanjanje whitespacea 
    unos= unos.upper()  #pretvaranje u velika slova


    valute = unos.split(",")

else : #u slučaju odabira nepostojeće opcije i gasi program
    print("Nedozvoljen unos")
    sys.exit()
    

odabrane_valute=[] #inicijalizacija niza u koji će se spremati riječnici sa podatcima o odabranim kriptovalutama nakon provjere
for valuta in valute:
    
    if valuta in popis:#provjera postoji li valuta u popisu povučenom s API-a, ako postoji sprema se u popis 
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
        print("unijeli ste valutu koja ne postoji ")
        sys.exit() #ako neka valuta ne postoji izbacuje iz programa 
        


#poziv funkcija sa proslijeđenim argumentima 
if odabir==1:
    price_history(a["id"], a["name"])
elif odabir==2:
    marketCap(odabrane_valute)



