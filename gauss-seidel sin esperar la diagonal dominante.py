# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:38:00 2020

@author: Raven
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:55:26 2020

@author: Raven
"""

import numpy as np
eprop = 10**-6; imax=1000; ban=0; citer=0; cerror=0; cconver=0;
n=int(input('Valor de n:'))

mcoef = np.zeros((n,n))
vecoef= np.zeros((n))

mresant=np.zeros((n))
mresact=np.zeros((n))
merror=np.zeros((n))
for i in range (0,n):
    merror[i]= 1

print('Introduce la matriz de coeficientes y el vector solución')

for i in range(0,n):
    for j in range(0,n):
        mcoef[(i),(j)]=(input("Elemento a["+str(i+1)+","+str(j+1)+"] "))
    vecoef[(i)]=(input('b['+str(i+1)+']: '))

for i in range (0,n):
    mresant[i]=vecoef[i]/mcoef[i,i]
    
print(mcoef)

for i in range(0,n):
    suma=0
    
    for j in range(0,n):
        if i!=j:
            suma=suma + mcoef[i,j]
        else:suma=suma
if abs(mcoef[i,i])>abs (suma):
    cconver+=1
else:cconver=cconver
print(cconver)
if cconver==n:
    ban=1
else: 
    ban=0 
    print('no hay convergencia') 


while ban==1 and cerror<n and citer<imax:
    for i in range (0,n):
        suma = 0 
        for j in range (0,n):
            if i != j:
                suma = suma +  mcoef[i,j]*mresant[j]
            else:suma=suma
        mresact[i]=(vecoef[i]-suma)/mcoef[i,i]
        merror[i]=abs((mresact[i]-mresant[i])/mresact[i])
    cerror=0
    for i in range (0,n):
        if merror[i]<= eprop:
            cerror+=1
        else:cerror=cerror
    for i in range (0,n):
        mresant[i]=mresact[i]
    citer+=1
#preguntar como hacer que me muestre decismales ya que me redondea a cero todo
# y preguntar por que no me aparece el no hay convergencia si en mathematic aaparece

print(f"Resultado matriz \n{mresact}")



print(f'las iteraciones \n{citer}')



print(f'la matriz error \n{merror}')
