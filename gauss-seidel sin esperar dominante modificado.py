import numpy as np
eprop = 10**-6; imax=1000; ban=0; citer=0; cerror=0; cconver=0;
n=int(input('Valor de n:'))

mcoef = np.zeros((n,n+1))
mresant=np.zeros((n))
mresact=np.zeros((n))
merror=np.zeros((n,1))


print('Introduce la matriz de coeficientes')

for i in range(0,n):
    for j in range(0,n+1):
        mcoef[i][j]=(input("Elemento a["+str(i+1)+","+str(j+1)+"] "))
    

for i in range (0,n):
    mresant[i]=mcoef[i,n]/mcoef[i,i]
    
print(mcoef)

for i in range(0,n):
    suma=0
    
    for j in range(0,n):
        if i!=j:
            suma=suma + abs(mcoef[i,j])
        else:suma=suma
if abs(mcoef[i,i])>suma:
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
        mresact[i]=(mcoef[i,n+1]-suma)/mcoef[i,i]
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


print(f"Resultado matriz \n{mresact}")



print(f'las iteraciones \n{citer}')



print(f'la matriz error \n{merror}')


