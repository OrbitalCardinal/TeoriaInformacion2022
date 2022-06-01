from itertools import product
import numpy as np
import pandas as pd

def permutaciones(cadena,tam):
    caracteres = list(cadena)
    permutaciones = []


    for i in range(tam):
        if(i == 0):
            a=0
        else:
            for c in product(caracteres, repeat=i+1):
                    permutaciones.append(c)
                    #print(c)
            lst = [''.join(p) for p in permutaciones]
            decodificacion(lst)
            #print(lst)
        
    
    return permutaciones

def decodificacion(cadena):
    caracteres = list(cadena)
    alfa = []
    beta = []
    long = []

    for i in caracteres:
        long.append(1/len(caracteres))
        if(caracteres.index(i) == 0):
            alfa.append(0) 
        else:
            alfa.append(beta[caracteres.index(i)-1])       

        beta.append(long[caracteres.index(i)]+alfa[caracteres.index(i)])
    
    
    df = pd.DataFrame([alfa,beta,long], columns=[caracteres], index=["alfa","beta","long"])
    df.to_csv(r'C:\Users\Fernando\OneDrive - Universidad Autonoma de Nuevo León\Semestre 9\Teoria de la Informacion\Ordinadio\Aritmetica adaptativa\Programa\aritmetica.csv', index=False)
    print(df)

    
def decodificacion2(cadena):
    caracteres = list(cadena)
    alfa = []
    beta = []
    long = []

    for i in caracteres:
        long.append(1/len(caracteres))
        if(caracteres.index(i) == 0):
            alfa.append(0) 
        else:
            alfa.append(beta[caracteres.index(i)-1])       

        beta.append(long[caracteres.index(i)]+alfa[caracteres.index(i)])
        
        
    df = pd.DataFrame([alfa,beta,long], columns=[caracteres], index=["alfa","beta","long"])
    df.to_csv(r'C:\Users\Fernando\OneDrive - Universidad Autonoma de Nuevo León\Semestre 9\Teoria de la Informacion\Ordinadio\Aritmetica adaptativa\Programa\aritmetica0.csv', index=False)
    print(df)

    



cadena = input("Introduce la cadena: ")
decodificacion2(cadena)
permutaciones(cadena, len(cadena))




