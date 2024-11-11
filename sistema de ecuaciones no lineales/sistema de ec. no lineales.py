import math as mt
ep = 10**-6; itemax = 10; cont = 0; conite = 0; ban = 1; error = 1; h = 10**-4;
def u(x,y):
    f = 2*x*y - mt.cos(y)
    #f = (x - 4)**2 + (y - 4)**2 - 4 # problema 8
    #f= - x**3 + mt.sin(y + x) + 2*x**2 - 0.5 # problema 9
    
    return (f)
def v(x,y):
    f = 2*x*y - mt.sin(x)
    #f = x**2 + y**2 - 16 # problema 8
    #f = x**2 + y**3 - x*mt.cos(y**2) # problema 9
    return(f)
def dux(x,y):
    f = (u(x + (h/2),y) - u(x - (h/2),y))/(h)
    return (f)
def duy(x,y):
    f = (u(y,x + (h/2)) - u(x,y - (h/2)))/(h)
    return (f)
def dvx(x,y):
    f = (v(x + (h/2),y) - v(x - (h/2),y))/(h)
    return (f)
def dvy(x,y):
    f = (v(y,x + (h/2)) - v(x,y - (h/2)))/(h)
    return (f)
def j(x,y):
    f = dux(x,y)*dvy(x,y) - duy(x,y)*dvx(x,y)
    return (f)
def gx(x,y):
    f = x - (u(x,y)*dvy(x,y) - v(x,y)*duy(x,y))/(j(x,y))
    return f
def gy(x,y):
    f = y - (v(x,y)*duy(x,y) - u(x,y)*dvy(x,y))/(j(x,y))
    return f
while ban == 1 and cont < itemax:
    x0 = float(input('dame x0'))
    y0 = float(input('dame y0'))
    if j(x0,y0) != 0:
        ban = 0
    else: ban = 1 ; print('no converge')
    if u(x0,y0) == 0 and v(x0,y0) == 0:
        error = 0
        ban = 0
    else:ban=ban
    cont+=1
xant=x0
yant=y0
while ban == 0 and error > ep and conite < itemax:
    xact=gx(xant,yant)
    yact=gy(xant,yant)
    errorx= abs((xact - xant )/(xact))
    errory= abs((yact - yant )/(yact))
    if errorx >= errory:
        error=errorx
    else:error=errory
    if j(xact,yact) == 0:
        ban=1
        print('falla convergencia')
    else: ban = 0
    if u(xact,yact) == 0 and v(xact, yact) == 0:
        error = 0
    else: error=error
    conite+=1
    xant=xact
    yant=yact
print(f'Raiz\n{xact,yact}')
print(f'Evaluación\n{u(xact,yact),v(xact,yact)}')
print(f'Error\n{errorx,errory,error}')
print(f'Numero de iteraciones\n{conite}')



