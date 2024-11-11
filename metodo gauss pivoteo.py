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
    for i in range(k+1,n):
        factor=(mcoef[i,k]/mcoef[k,k])
        vec[i]=vec[i]-(factor*vec[k])
        for j in range(0,n):
            mcoef[i,j]=mcoef[i,j]-(factor*mcoef[k,j])

#sustitución hacia atrás

mres[n-1]=vec[n-1]/mcoef[n-1,n-1]

print(vec[n-1])

for i in range(n-2,-1,-1):
    suma=0
    for j in range(0,n):# aqui debe de ser n+1 pero no me deja ponerlo
        suma=suma+mcoef[i,j]*mres[j]
    mres[i]=(vec[i]-suma)/mcoef[i,i]







print(f"Resultado matriz \n{mcoef}")



print(f'Resultado del vector \n{vec}')



print(f'Resultados: \n{mres}')
