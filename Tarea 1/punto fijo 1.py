import math as mt
ep = 10**-6; itermax = 1000; inter = 0; iteraciones = 0; error = 1; h = 0.0001; ban = 0;
def f(x):
    y = mt.e**-x - (1/2)*mt.sin(x) - x + 5
    #y = mt.e**-x - mt.cos(8*x)#1-a)
    #y = x*mt.log(x,mt.e) - 5 #1-b)
    #y = 2**x - 5*x + 2 #1-c)
    #y = (((35 * x) ** 5 / 3) / (0.045 * (35 + 2 * x) ** 2 / 3)) * (mt.pi / 1800) ** 1 / 2  # problema 2
    #y = -600*mt.sin(x) + 1800*(mt.sin(x))**2 #problema 3
    #y = 40 * mt.tan(x) - ((9.8) * (40) ** 2) / (2 * 20 ** 2 * mt.cos(x)) + 1.8  # problema 4
    #y = 1650 - 450*x #problema 5
    #y = 10 * (1 - mt.e ** -0.04 * x) + 4 * mt.e ** -0.04 * x  # problema 6
    #y = -139.3441 + 1.575701 * 10 ** 5 / x - 6.642308 * 10 ** 7 / x ** 2 + 1.2438 * 10 ** 10 / x ** 3 - 8.621949 * 10 ** 11 / x ** 4  # problema 7
    return (y)
def g(x):
    y = mt.e**-x -(1/2)*mt.sin(x)+5
    #y = mt.acos(mt.e**-x)/8 #1-a)         #f(x) + x
    #y = mt.e**5/x #1-b)
    #y = (2**x + 2)/5 #1-c
    #y = ((0.045*(35+2*x)**2/3)/(35*x)**5/3)**3/5 #problema 2
    #y = mt.asin(600/1800) # problema 3
    #y = mt.atan(((9.8) * (40) ** 2) / (40*2 * 20 ** 2 * mt.cos(x)) + 1.8 ) # problema 4
    #y = mt.sqrt(x**2 - 1650 + 450*x)#problema 5
    #y = ((1/10)*mt.log(10,mt.e) +(-0.04*x)**(2/5)) /-0.04 #problema 6
    #y = 1 -139.3441/x + 1.575701 * 10 ** 5 / x**2 - 6.642308 * 10 ** 7 / x ** 3 + 1.2438 * 10 ** 10 / x ** 4 - 8.621949 * 10 ** 11 / x ** 5  # problema 7
    return (y)
def dg(x):
    y = (g(x + h/2) - g(x - h/2))/h
    return (y)
while ban == 0 and inter < itermax:
    xant = float(input('dame un valor de x0:'))
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