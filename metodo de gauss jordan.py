# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:23:31 2020

@author: Raven
"""

import numpy as np
n=int(input('Valor de n:'))

mcoef = np.zeros((n,n))

vec= np.zeros((n))

mres=np.zeros((n))

print('Introduce la matriz de coeficientes y el vector solución')

for i in range(0,n):
    for j in range(0,n):
        mcoef[(i),(j)]=(input("Elemento a["+str(i+1)+","+str(j+1)+"] "))
    vec[(i)]=(input('b['+str(i+1)+']: '))
print(mcoef)

for k in range(0,n):
    for i in range(0,n):
        if k==j :
            k=k
        else:
             factor=(mcoef[i,k]/mcoef[k,k])
             vec[i]=vec[i]-(factor*vec[k])
             for j in range(0,n):
                 mcoef[i,j]=mcoef[i,j]-(factor*mcoef[k,j])
for i in range(0,n):
    vec[n-1]=vec[n-1]/mcoef[n-1,n-1]
    mcoef[n-1,n-1]=1
    









print(f"Resultado matriz \n{mcoef}")



print(f'Resultado del vector \n{vec[n-1]}')



print(f'Resultados: \n{mres}')