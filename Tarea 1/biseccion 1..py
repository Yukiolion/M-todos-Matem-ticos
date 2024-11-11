import math as mt
ban=0; cont=0; intmax=100; ep=10**-8; nmax=1000; ite=0; error=1;
def f(x):
    y = 15*(x**4 + 5)**1/3 * mt.cos(3*x**2 + 4/2) - x**4/15 + 3
    #y = mt.e**-x - mt.cos(8*x)#1-a)
    #y = x*mt.log(x,mt.e) - 5 #1-b)
    #y = 2**x - 5*x + 2 #1-c)
    #y = (((35*x)**5/3)/(0.045 * (35 + 2*x)**2/3))*(1.745329*10**-3)**1/2   #problema 2
    #y =(50*0.045)**2 * ((((35+2*x)**2)/(35*x)**5))**2/3 #problema 2 probando otra forma
    #y = -600*mt.sin(x) + 1800*(mt.sin(x))**2 #problema 3
    #y = 40*mt.tan(x)-((9.8)*(40)**2)/(2*20**2 * mt.cos(x)) + 1.8 #problema 4
    #y = 1650 - 450*x #problema 5
    #y = 10*(1 - mt.e**-0.04*x) + 4*mt.e**-0.04*x # problema 6
    #y = -139.3441 + 1.575701*10**5/x - 6.642308*10**7/x**2 + 1.2438*10**10/x**3 - 8.621949*10**11/x**4

    return y
while ban == 0 and cont < intmax:
    a = float(input('dame a'))
    b = float(input('dame b'))
    if f(a)*f(b) < 0:
        ban = 1
    else: ban = 0
    if f(a)*f(b) == 0:
        if f(a) == 0:
            print(a)
        else: print(b)
        error = 0
        ban = 1
    else: ban = ban
    cont+= 1
xant = a
n = mt.log((b - a)/ep,2)
while ban == 1 and error > ep and ite < nmax:
    xact = (a + b)/2
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
        error = abs((xact - xant)/xact)
    else: error = error
    xant = xact
    ite+= 1
print(f'raíz \n{xact}')
print(f'la funcion de la raiz\n{f(xact)}')
print(f'error\n{error}')
print(f'iteraciones\n{ite}')
print(f'el n estimado es:\n{round(n)}')

