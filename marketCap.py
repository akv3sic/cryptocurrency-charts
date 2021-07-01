
import matplotlib.pyplot as plt #uvoz potrebnih biblioteka
import numpy as np


def marketCap(lista_cry):
    MC=[] #lista marketCapova
    imena=[] #lista imena kriptovaluta
    #print (lista_cry)
    for valuta in lista_cry:
        MC.append(float(valuta["marketCap"])/1000000000) #marketCap dijelim s milijardom radi ljepšeg izgleda dijagrama 
        imena.append(valuta["name"])
    plt.rcdefaults()
    
    
    fig, ax = plt.subplots() 
    y_pos = np.arange(len(imena)) #imena se raspoređuju po y osi 
    


    
    
    
    ax.barh(y_pos, MC,height=0.8, left= 0, align='center') #prvi argument je pozicija na y osi, drugi je veličina bara 
                                                            #treći debljina bara , left=0 postavlja početnu točku na x osi na 0, 
                                                            #align center centrira barove 
    ax.set_yticks(y_pos)
    
    ax.set_yticklabels(imena) #postavlja imena valuta uz njihove barove 
   # ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Market Cap (u milijardama $)')# tekst oko grafova 
    ax.set_title('Usporedba Market Capova')

    plt.show()  #poziv funkcije za prikaz 

    
