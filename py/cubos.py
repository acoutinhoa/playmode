import time
start = time.time()

import os
from base import var,formas

# caminho da pasta do playmode
path = '/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
# 1 inch = 2.54 cm
# cm = dpi/2.54
cm = 72/2.54
mm = cm/10

###############################

dado_grid = {
    1:[
        [0,0,0],
        [0,1,0],
        [0,0,0],
    ],
    2:[
        [0,0,1],
        [0,0,0],
        [1,0,0],
    ],
    3:[
        [0,0,1],
        [0,1,0],
        [1,0,0],
    ],
    4:[
        [1,0,1],
        [0,0,0],
        [1,0,1],
    ],
    5:[
        [1,0,1],
        [0,1,0],
        [1,0,1],
    ],
    6:[
        [1,0,1],
        [1,0,1],
        [1,0,1],
    ],
    9:[
        [1,1,1],
        [1,1,1],
        [1,1,1],
    ],
}

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

def desenha_cubo(m):
    save()
    fill(1)
    stroke(0)
    rect(0,0,m,m)
    restore()


###############################


fontes_do_pc = ['?',]+installedFonts()

tipos = [
    '?',
    '1_pilha',
    '2_prateleira-preta',
    '3_prateleira-branca',
    ]

faces = [
    '?',
    '1_repetida',
    '2_randomica',
    ]


Variable([
    dict(name = "w_cm", ui = "EditText", args = dict(text = '200')),
    dict(name = "h_cm", ui = "EditText", args = dict(text = '200')),
    dict(name = "cubo_cm", ui = "EditText", args = dict(text = '20')),
    dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
    dict(name = "pilha_max", ui = "EditText", args = dict(text = '7')),
    dict(name = "prateleira_mm", ui = "EditText", args = dict(text = '12')),
    dict(name = "cubo_simples", ui = "CheckBox", args = dict(value = True)),
    dict(name = "cubo_dado", ui = "CheckBox", args = dict(value = False)),
    dict(name = "cubo_escala", ui = "CheckBox", args = dict(value = True)),
    dict(name = "escala_max", ui = "EditText", args = dict(text = '10')),
    dict(name = "face", ui = "PopUpButton", args = dict(items = faces)),
    dict(name = "caracteres", ui = "EditText", args = dict(text = 'PLAYMODE')),
    dict(name = "fonte", ui = "PopUpButton", args = dict(items = fontes_do_pc)),
], globals())
    
    
# fundo
pw = int(var(w_cm,tipo = 'float')*cm)
ph = int(var(h_cm,tipo = 'float')*cm)

m = int(var(cubo_cm,tipo = 'float')*cm)

cubos = []
if cubo_simples:
    cubos.append('simples')
if cubo_dado:
    cubos.append('dado')
if cubo_escala:
    cubos.append('escala')

tipo = var(tipo,1,lista = tipos,tipo = 'lista')

n_max = var(pilha_max,tipo = 'int')
prat = int(var(prateleira_mm,tipo = 'float')*mm)
if tipo==1:
    prat = 0
else:
    prat_base = 10*cm
    prat_w = range(prat,pw,m+prat)[-1]
    prat_h = (m+prat)*n_max

e_max = var(escala_max,6,tipo = 'int')

face = var(face,1,lista = faces,tipo = 'lista')

fonte = var(fonte,'BodoniSvtyTwoITCTT-Book',lista = fontes_do_pc)
fs = m

print('fonte =', fonte)
print('tipo =', tipos[tipo])
print('cubos =', cubos)
print('face =', faces[face])
# print('fonte_size =', fs)


base = formas(caracteres,m,fs = 0,fonte = fonte)

size(pw,ph)

lados = list(base.keys())[:4]
letras = [i for i in caracteres]

# fundo
fill(0.8)
rect(0,0,pw,ph)

# cor dos graficos
fill(0)
stroke(None)

# desenha prateleira
# desenha prateleira
if prat:
    translate((pw-prat_w)/2,prat_base)
    save()
    if tipo == 3:
        fill(1)
    rect(0,0,prat_w,-prat_base)
    for x in range(0,prat_w,m+prat):
        rect(x,0,prat,prat_h)
    for y in range(-prat,prat_h,m+prat):
        rect(0,y,prat_w,prat)
    restore()


for x in range(prat,pw-m,m+prat):
    if prat:
        escolhe = 1
    else:
        escolhe = randint(0,10)
    if escolhe:
        for y in range(n_max):
            if prat:
                escolhe = randint(0,2)
            else:
                escolhe = randint(0,n_max-y)
            if escolhe:
                y = y*(m+prat)
                cubo = choice(cubos)
                car = choice(lados+[choice(letras)]+[''])
                save()
                translate(x,y)
                desenha_cubo(m)
                if car:
                    if cubo=='simples':
                        drawPath(base[car])
                    elif cubo=='dado':
                        scale(1/3)
                        numero = randint(1,6)
                        for j in dado_grid[numero]:
                            save()
                            for i in j:
                                if i:
                                    if face==2:
                                        car = choice(lados+[choice(letras)])
                                    drawPath(base[car])
                                translate(m,0)
                            restore()
                            translate(0,m)
                    elif cubo=='escala':
                        numero = randint(1,e_max+1)
                        scale(1/numero)
                        for j in range(numero):
                            save()
                            for i in range(numero):
                                if randint(0,e_max-numero+1):
                                    if face==2:
                                        car = choice(lados+[choice(letras)])
                                    drawPath(base[car])
                                translate(m,0)
                            restore()
                            translate(0,m)
                restore()
            else:
                if not prat:
                    break    
    

end = time.time()
print('\n>>>', end-start, 's')
