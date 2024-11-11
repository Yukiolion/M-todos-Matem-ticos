import numpy as np

#matriz=np.zeros((3, 2))
#print(matriz)

n= int(input("Ingres el numero de variables: "))
matrizCoef= np.zeros((n, n+1))
matrizRes=np.zeros((n, 1))

for i in range(n):
    for j in range (n+1):
        matrizCoef[i][j]= float(input(f"Dame el elemento {i+1},{j+1}: "))

print("Matriz de coeficientes")
print(matrizCoef)

for k in range(n-1):
    for j in range (k+1, n):
        fact=matrizCoef[j][k]/matrizCoef[k][k]
        for i in range(n+1):
            matrizCoef[j][i]=matrizCoef[j][i]-(fact*matrizCoef[k][i])

print("Matriz reducida")
print(matrizCoef)

matrizRes[n-1]=matrizCoef[n-1][n]/matrizCoef[n-1][n-1]

for i in range(n-2, -1, -1):
    suma=0
    
    for j in range (i+1, n):
        suma=suma+matrizCoef[i][j]*matrizRes[j]
    
    matrizRes[i]=(matrizCoef[i][n]-suma)/matrizCoef[i][i]

print("matriz reducida")
print(matrizCoef)
print("matriz de resultados")
print(matrizRes)

    
