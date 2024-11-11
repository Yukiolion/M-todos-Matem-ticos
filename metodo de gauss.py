import numpy as np
n=int(input('Valor de n:'))

mcoef = np.zeros((n,n+1))


mres=np.zeros((n,1))

print('Introduce la matriz de coeficientes y el vector solución')



for i in range(n):
    for j in range(n+1):
        mcoef[i][j]=float(input("Elemento a["+str(i+1)+","+str(j+1)+"] "))
print("Matriz de coeficientes")   
print(mcoef)

for k in range(n-1):
    for i in range(k+1,n):
        factor=(mcoef[i,k]/mcoef[k,k])
        
        for j in range(n+1):
            mcoef[i,j]=mcoef[i,j]-(factor*mcoef[k,j])

#sustitución hacia atrás

mres[n-1]=mcoef[n-1][n]/mcoef[n-1,n-1]

print(mcoef[n-1][n])



for i in range(n-2,-1,-1):
    suma=0
    for j in range(i+1,n):
        suma=suma+mcoef[i][j]*mres[j]
    mres[i]=(mcoef[i][n]-suma)/mcoef[i,i]







print(f"Resultado matriz \n{mcoef}")





print(f'Resultados: \n{mres}')