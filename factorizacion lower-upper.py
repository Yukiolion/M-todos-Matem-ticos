# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:04:21 2020

@author: Raven
"""

import numpy as np
n=int(input('Valor de n:'))

mcoef = np.zeros((n,n))

ml= np.zeros((n,n))
for i in range (0,n):
    ml[i,i]= 1


print('Introduce la matriz de coeficientes y el vector solución')

for i in range(0,n):
    for j in range(0,n):
        mcoef[(i),(j)]=(input("Elemento a["+str(i+1)+","+str(j+1)+"] "))
print(mcoef)

for k in range(0,n):
    for i in range(k+1,n):
        factor=(mcoef[i,k]/mcoef[k,k])
        ml[j,k]= factor
        
        for j in range(0,n):
            mcoef[i,j]=mcoef[i,j]-(factor*mcoef[k,j])
mu=mcoef












print(f"Resultado matriz \n{mcoef}")



print(f'Resultado matriz \n{ml}')




