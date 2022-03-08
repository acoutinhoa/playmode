import time
start = time.time()

import os
from base import var

# caminho da pasta do playmode
path = '/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
# 1 inch = 2.54 cm
# cm = dpi/2.54
cm = 72/2.54
mm = cm/10

###############################


def formas(caracteres,m,fs = 0,fonte = 'CourierNewPSMT'):
    if not fs:
        fs = m
    base = {}
    # formas geometricas
    car_lista = ['#','o','t','x',]
    for c in car_lista:
        x,y = 0,0
        bezier = BezierPath()
        if c == '#':
            c = 'quadrado'
            bezier.rect(x,y,m,m)
        elif c == 'o':
            c = 'circulo'
            bezier.oval(x,y,m,m)
        elif c == 't':
            c = 'triangulo'
            bezier.polygon((x,y),(x+m/2,y+m),(x+m,y))
        elif c == '+':
            c = 'cruz'
            bezier.rect(x+m/4,y,m/2,m)
            bezier.rect(x,y+m/4,m,m/2)
        elif c == '*':
            c = 'xis2'
            n = 3
            bezier.polygon((x,y),(x+m/n,y),(x+m,y+m),(x+m-m/n,y+m))
            bezier.polygon((x+m-m/n,y),(x+m,y),(x+m/n,y+m),(x,y+m),)
        elif c == 'X':
            c = 'xis'
            n = 4
            bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
            bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
        elif c == 'x':
            c = 'xis'
            n = 6
            bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
            bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
        base[c] = bezier
    # caracteres
    for c in caracteres:
        bezier = BezierPath()
        bezier.textBox(c, (-m/2,-m+fs-m,2*m,2*m), font = fonte, fontSize = fs, align = 'center',)
        base[c] = bezier
    return base

def desenha_linha(x=0):
    save()
    cmykStroke(0,0,0,1)
    fill(None)
    line((x,0),(x,h))
    restore()

###############################

#dimensoes
portas={
    1:{
        'w':117*cm,
        'h':305*cm
        },
    2:{
        'w':145*cm,
        'h':337*cm
        },
}


tipos = [
    '0_117.0 x 305.0 cm',
    '1_145.0 x 337.0 cm',
    ]


Variable([
    dict(name = "escala_real", ui = "CheckBox", args = dict(value = False)),
    dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
    dict(name = "faixas_n", ui = "EditText", args = dict(text = '0')),
    # dict(name = "mais_largura_cm", ui = "EditText", args = dict(text = '')),
    # dict(name = "mais_altura_cm", ui = "EditText", args = dict(text = '')),
    # dict(name = "ordem", ui = "EditText", args = dict(text = '')),
    dict(name = "linhas", ui = "CheckBox", args = dict(value = False)),
    dict(name = "branco", ui = "CheckBox", args = dict(value = False)),
], globals())


# escala
if escala_real:
    e=1
else:
    e=1/cm 

porta=tipo+1

# w_ = var(mais_largura_cm,0,tipo = 'float')*cm
# h_ = var(mais_altura_cm,0,tipo = 'float')*cm

# aumenta tecido:
if tipo ==1:
    w_=145*cm
else:
    w_=0*cm
h_=0*cm

w=portas[porta]['w']+w_
h=portas[porta]['h']+h_

#faixas
faixas = var(faixas_n,0,tipo = 'int')
if not faixas:
    if porta==1:
        n=8
    else:
        n=7
    fw=w/n
else:
    fw=w/faixas
    
ordem=''
ordem=ordem.split(' ')

print('porta', tipos[porta-1])
print('w = %s cm' % round(w/cm,2))
print('h = %s cm' % round(h/cm,2))
print('faixas =', faixas)
print('largura_faixa = %s cm' % round(fw/cm,2))
print('ordem =', ' '.join(ordem))
print()

base = formas('',fw,)

qctx=list(base.keys())
qctx+=qctx[:2]*2+qctx[:1]*2


if branco:
    qctx+=['']

print(qctx)

size(w*e,h*e)
scale(e)
cmykFill(0,0,0,1)

ordem_=[]
if not faixas:
    tudo=n
    c=0
    while n>0:
        
        if ordem[0]:
            i=int(ordem[c])
            c+=1
        else:
            if n>3:
                m=3
            else:
                m=n
            i=randint(1,m)
            ordem_.append(str(i))
        
        print(i,i*fw/cm)
        base = formas('',fw*i,)

        x=(tudo-n)*fw
        n-=i

        if linhas:
            desenha_linha(x=x)
        
        cortina=BezierPath()
        
        for j in range(ceil((h/i)/(fw))):
            car=choice(qctx)
            if car:
                y=j*fw
                cortina.translate(-x,-y*i)
                cortina.appendPath(base[car])
                cortina.translate(x,y*i)

            cortina.removeOverlap()
            drawPath(cortina)

else:
    for i in range(faixas):
        x=i*fw

        if linhas:
            desenha_linha(x=x)

        cortina=BezierPath()

        for j in range(ceil(h/fw)):
            car=choice(qctx)
            if car:
                y=j*fw
                cortina.translate(-x,-y)
                cortina.appendPath(base[car])
                cortina.translate(x,y)

            cortina.removeOverlap()
            drawPath(cortina)


if linhas:
    fill(None)
    stroke(.5)
    lineDash(2*cm,4*cm)
    w-=w_
    h-=h_
    
    translate(width()/2/e,0)
    rect(-w/2,0,w,h)


print()
print('ordem =', ' '.join(ordem_))

end = time.time()
print('\n>>>', end-start, 's')
