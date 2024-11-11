# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:54:21 2020

@author: Raven
"""

import numpy as np
n=int(input('Valor de n:'))

mcoef = np.zeros((n,n+1))



mres=np.zeros((n,1))

print('Introduce la matriz de coeficientes y el vector solución')

for i in range(n):
    for j in range(n+1):
        mcoef[i][j]=(input("Elemento a["+str(i+1)+","+str(j+1)+"] "))
    
print(mcoef)

for k in range(n):
    for i in range(n):
        if k==i :
            k=k
        else:
             factor=(mcoef[i,k]/mcoef[k,k])
             
             for j in range(n+1):
                 mcoef[i,j]=mcoef[i,j]-(factor*mcoef[k,j])
for i in range(n):
    mcoef[i][n]=mcoef[i][n]/mcoef[i,i]
    mcoef[i,i]=1
    









print(f"Resultado matriz \n{mcoef}")







print(f'Resultados: \n{mres}')