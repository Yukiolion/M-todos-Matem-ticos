import math as mt
ep = 10**-6; itermax = 1000; inter = 0; iteraciones = 0; error = 1; h = 0.0001; ban = 0;
def f(x):
    y = 3*mt.e**-x - 5*x
    return (y)
def df(x):
    y = (f(x + h/2) - f(x - h/2))/h
    return (y)
def g(x):
    y = x - f(x)/df(x)
    return (y)
def dg(x):
    y = (g(x + h/2) - g(x - h/2))/h
    return (y)
while ban == 0 and inter < itermax:
    xant = int(input('dame un valor de x0:'))
    if abs(dg(xant)) >= 1:
        ban = 0
        print('falla por convergencia')
    else: ban =1
    if f(xant) == 0 :
        error = 0
        ban =1
        print(f'Raíz encontrada:\n{xant}')
    else: ban = ban
    inter += 1
while ban == 1 and error > ep and iteraciones < itermax:
    xact = g(xant)
    if f(xact) == 0:
        error = 0
    else: error = abs((xact-xant)/xact)
    if abs(dg(xact)) >= 1:
        ban = 0
        print('falla por convergencia')
    else: ban =1
    xant = xact
    iteraciones += 1
print(f'Raiz\n{xact}')
print(f'Evaluación\n{f(xact)}')
print(f'Error\n{error}')
print(f'Numero de iteraciones\n{iteraciones}')
