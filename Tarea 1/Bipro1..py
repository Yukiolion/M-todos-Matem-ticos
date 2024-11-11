import math as mt
def f(x):
    y = 7 * mt.e ** -x * mt.sin(x) - 1
    #y = mt.e**-x - mt.cos(8*x)#1-a)
    #y = x*mt.log(x,mt.e) - 5 #1-b)
    #y = 2**x - 5*x + 2 #1-c)
    #y = (((35 * x) ** 5 / 3) / (0.045 * (35 + 2 * x) ** 2 / 3)) * (mt.pi / 1800) ** 1 / 2  # problema 2
    #y = -600*mt.sin(x) + 1800*(mt.sin(x))**2 #problema 3
    #y = 40 * mt.tan(x) - ((9.8) * (40) ** 2) / (2 * 20 ** 2 * mt.cos(x)) + 1.8  # problema 4
    #y = 1650 - 450*x #problema 5
    #y = 10 * (1 - mt.e ** -0.04 * x) + 4 * mt.e ** -0.04 * x  # problema 6
    #y = -139.3441 + 1.575701 * 10 ** 5 / x - 6.642308 * 10 ** 7 / x ** 2 + 1.2438 * 10 ** 10 / x ** 3 - 8.621949 * 10 ** 11 / x ** 4  # problema 7
    return(y)
error = 1; errop = 10**-6; nmax = 1000; ban = 0; itm = 50; count = 0; count2 = 0;
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
    xact = a- (f(a)*(b-a))/(f(b)-f(a))
    if f(a)*f(xact) < 0:
        b = xact
    else: b = b
    if f(a)*f(xact) > 0:
        a = xact
    else: a = a
    if f(a)*f(xact) == 0:
        error = 0
    else: error = error; xact = (a+b)/2
    if error != 0:
        xb = (a + b) / 2
        error = abs((xact-xant)/xact)
    else: error = error
    xant = xact
    count2 += 1
print('proporcion')
print(f'la raiz es:\n{xact}')
print(f'la funcion de la raiz:\n{f(xact)}')
print(f'el error es:\n{error}')
print(f'cuantas iteraciones se hicieron:\n{count2}')
print(f'el n estimado es:\n{round(n)}')
