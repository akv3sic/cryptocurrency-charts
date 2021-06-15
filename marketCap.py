
import matplotlib.pyplot as plt
import numpy as np


def marketCap(lista_cry):
    MC=[]
    imena=[]
    print (lista_cry)
    for valuta in lista_cry:
        MC.append(float(valuta["marketCap"])/1000000000)
        imena.append(valuta["name"])
    plt.rcdefaults()
    
    
    fig, ax = plt.subplots()
    y_pos = np.arange(len(imena))
    


    
    
    
    ax.barh(y_pos, MC,height=0.8, left= 0, align='center')
    ax.set_yticks(y_pos)
    
    ax.set_yticklabels(imena)
   # ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Market Cap (u milijardama $)')
    ax.set_title('Usporedba Market Capova')

    plt.show()  

    
