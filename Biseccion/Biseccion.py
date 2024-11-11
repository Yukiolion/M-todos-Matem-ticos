import math as mt
def f(x):
    '''y = mt.e**-x - x'''
    y = mt.e ** -x - mt.cos(8 * x)
    return(y)
error = 1; errop = 10**-6; nmax = 1000; ban = 0; itm = 10; count = 0; count2 = 0;
while ban == 0 and count < itm :
    a = float(input("dame a:"))
    b = float(input("dame b:"))
    if f(a) * f(b) < 0 :
        ban = 1
    else: ban = 0
    if f(a) * f(b) == 0:
        if f(a) == 0:
            print(a)
        else: print(b)
        error = 0
        ban = 1
    else :ban = ban
    count += 1
n = mt.log2((b-a)/errop)
xant = a
while ban == 1 and error > errop and count2 < nmax:
    xact = (a+b)/2
    if f(a)*f(xact) < 0:
        b = xact
    else: b = b
    if f(a)*f(xact) > 0:
        a = xact
    else: a = a
    if f(a)*f(xact) == 0:
        error = 0
    else: error = error
    if error != 0:
        error = abs((xact-xant)/xact)
    else: error = error
    xant = xact
    count2 += 1
print(f'la raiz es:\n{xact}')
print(f'la funcion de la raiz:\n{f(xact)}')
print(f'el error es:\n{error}')
print(f'cuantas iteraciones se hicieron:\n{count2}')
print(f'el n estimado es:\n{round(n)}')
