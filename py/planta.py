import time
start = time.time()

import os
from base import var

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
# 1 inch = 2.54 cm
# cm = dpi/2.54
cm = 72/2.54
mm = cm/10

###############################

medidas={
    1 : {
        'pw':6850,
        'ph':5410,
        'p0':(800,400),
        'pp':(-800,-400),
    },
    2 : {
        'pw':820,
        'ph':630,
        'p0':(4900,1660),
        'pp':(-4800,-1560),
    },
    3 : {
        'pw':1600,
        'ph':1140,
        'p0':(3640,1610),
        'pp':(-3450,-1470),
    },        
    4 : {
        'pw':1600,
        'ph':1140,
        'p0':(3640,900),
        'pp':(-3430,-760),
    },        
    5 : {
        'pw':1600,
        'ph':2840,
        'p0':(2190,4530),
        'pp':(-1580,-2070),
    },        
    6 : {
        'pw':1280,
        'ph':2540,
        'p0':(6360,3020),
        'pp':(-5860,-2340),
    },        
}

# escala humana
def escala_humana(x,y,humano=None,angulo=None):
    if not humano:
        humano=randint(0,1)
    if not angulo:
        angulo=randint(0,360)

    if humano==0:
        humano=os.path.join(path,'img/escala2_35.pdf')
    elif humano==1:
        humano=os.path.join(path,'img/escala3_46.pdf')

    save()
    blendMode('multiply')
    translate(x,y)
    rotate(angulo)
    image(humano,(0,0))
    restore()

def eixo(pnt=50):
    save()
    fill(None)
    stroke(1,0,1)
    line((-pnt/2,0), (pnt/2,0))
    line((0,-pnt/2), (0,pnt/2))
    restore()

def painel_giratorio(modulo,repeticao_w=1,repeticao_h=1,grid_w=0,grid_h=0,esp=3,gira=1,grid=0,intercalado=0,xy=(0,0),tipo='h'):
    if modulo == 'obras':
        modulo=30
    
    if not gira and tipo=='v':
        gira='90'
    # calcula dimensoes da cortina
    cw=(repeticao_w-1)*grid_w+modulo
    ch=(repeticao_h-1)*grid_h+modulo
    print('cortina = %scm x %scm' % (cw, ch))

    save()
    translate(*xy)
    save()
    for l in range(repeticao_h):
        save()
        for m in range(repeticao_w):
            if not intercalado or not (l+m+repeticao_h)%2:
                save()
                fill(None)
                stroke(0)
                strokeWidth(esp)
                if gira:
                    if gira=='90':
                        rotate(90)
                        gira=0
                    else:
                        rotate(randint(0,360))
                    oval(-esp,-esp,2*esp,2*esp)
                else:
                    oval(-modulo/2,-esp,2*esp,2*esp)
                    oval(modulo/2,-esp,-2*esp,2*esp)
                line((-modulo/2,0),(modulo/2,0))
                restore()
                
                if gira and grid:
                    fill(None)
                    stroke(0,1,1)
                    strokeWidth(1)
                    oval(-modulo/2,-modulo/2,modulo,modulo)
        
            translate(grid_w,0)
        restore()
        translate(0,grid_h)
    restore()
    #grid
    if grid:
        fill(None)
        stroke(1,0,1)
        strokeWidth(1)
        for i in range(repeticao_h):
            y=grid_h*i
            line((0,y),(cw-modulo,y))
        for i in range(repeticao_w):
            x=grid_w*i
            line((x,0),(x,ch-modulo))
    restore()
    
    return cw,ch

def painel_texto(w,dist,xy=(0,0),tipo='h',humano=1):
    save()
    translate(*xy)

    if tipo=='v':
        translate(w,0)
        rotate(90)

    stroke(0.6)
    strokeWidth(.2)
    linearGradient(
        (0, 0),                         # startPoint
        (dist, 0),                         # endPoint
        [(1,), (0.5,), (1,)],  # colors
        [0, .5, 1]                          # locations
        )
    rect(0,0,dist,w)
    
    # escala humana
    if humano:
        if randint(0,1):
            escala_humana(-randint(30,100),randint(10,w+10),humano=None,angulo=90)
        if randint(0,1):
            escala_humana(dist+randint(30,100),randint(10,w+10),humano=None,angulo=270)
    restore()

###############################

# imagens
path_img = os.path.join(path,'img/planta')

areas=[
    '?',
    '1_planta geral',
    '2_painel entrada',
    '3_sala1',
    '4_sala2',
    '5_eixo2',
    '6_eixo3',
    ]

possibilidades=[
    '?',
    '1_',
    '2_',
    '3_',
    ]


Variable([
    dict(name="zoom", ui="PopUpButton", args=dict(items=areas)),
    dict(name="proposta", ui="PopUpButton", args=dict(items=possibilidades)),
    # dict(name="n_modulos", ui="EditText", args=dict(text='')),
    dict(name = "pessoas", ui = "CheckBox", args = dict(value = True)),
    dict(name = "painel_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "txt_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "cortina_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "porta_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "porta_fora", ui = "CheckBox", args = dict(value = True)),
    dict(name = "grid", ui = "CheckBox", args = dict(value = False)),
], globals())
    
# cortina variaveis
zoom=var(zoom,1,lista=areas,tipo='lista')

# cortina variaveis
versao=var(proposta,3,lista=possibilidades,tipo='lista')

# planta
planta = os.path.join(path_img,'_planta.pdf')
planta_w,planta_h=imageSize(planta)

# escala
print('\n>>> 1px == 1cm')
e=8410.2/planta_w # 1px=1cm
pw=planta_w*e
ph=planta_h*e

################################

pw=medidas[zoom]['pw']
ph=medidas[zoom]['ph']
p0=medidas[zoom]['p0']
pp=medidas[zoom]['pp']

# desenha planta na escala
size(pw,ph)
translate(*pp)
save()
scale(e)
image(planta,(0,0),.3)
restore()

#########################################
# painel entrada

# 1
if versao==1:
    # painel entrada
    modulo=160/8
    repeticao_w=24
    repeticao_h=5

    grid_h=modulo
    grid_w=modulo

    # ofset do p0
    dist_porta=40
    dist_parede=50

# 2
if versao == 2:
    # painel entrada
    modulo=int(160/3)
    repeticao_w=9
    repeticao_h=3

    grid_h=modulo-0
    grid_w=modulo-0

    # ofset do p0
    dist_porta=70
    dist_parede=60

# 3
elif versao == 3:
    # painel entrada
    modulo=160/8
    repeticao_w=19
    repeticao_h=4

    grid_h=modulo+10
    grid_w=modulo+5

    # ofset do p0
    dist_porta=60
    dist_parede=50


print('_____', areas[zoom])
print()

print('>>>', areas[2])
print('modulo = %s cm' % modulo)
print('grid = %s x %s' % (repeticao_w, repeticao_h))
print('espaçamento = %scm x %scm' % (grid_w, grid_h))

# 0,0
save()
translate(*medidas[2]['p0'])

#deleta linhas
fill(1)
stroke(None)
rect(-67,26,170,278)
rect(19,3,530,278)
rect(520,70,80,70)

# 0,0
eixo()

translate(dist_porta,dist_parede)

# desenha cortina
cw,ch=painel_giratorio(modulo,repeticao_w,repeticao_h,grid_w,grid_h,gira=painel_mobile,grid=grid,intercalado=1)
    
# escala humana
if pessoas:
    for i in range(randint(1,2)):
        escala_humana(randint(0,cw),randint(0,ch))
    for i in range(randint(1,2)):
        escala_humana(randint(0,cw),randint(ch,3*ch))

restore()
#########################################
# sala1

# 0,0
save()
translate(*medidas[3]['p0'])

#deleta linhas
fill(1)
stroke(None)
# fill(1,0,0)
# blendMode('darken')
rect(19,0,1030,278)

# 0,0
eixo()

# escala humana
salaw=1100
salah=760
if pessoas:
    for i in range(randint(1,4)):
        escala_humana(randint(100,salaw),randint(100,salah))

# texto entrada
save()
translate(770,100)
w=80
dist=150
painel_texto(w,dist,)
painel_texto(w,dist,(0,w+15))

painel_texto(w,100,(-420,60),tipo='v')

restore()

# cortina
m=60
painel_giratorio(m,11,1,m+20,m,gira=cortina_mobile,grid=grid,xy=(210,770))

# texto obras
painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(140,550))
painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(870,580))

restore()

#########################################
# sala2

# 0,0
save()
translate(*medidas[4]['p0'])

#deleta linhas
fill(1)
stroke(None)
# fill(1,0,0)
# blendMode('darken')
rect(19,8,1030,178)
rect(20,290,-130,113)
rect(67,492,1100,159)

# 0,0
eixo()

# escala humana
w=1100
h=600
# fill(1,0,0)
# rect(0,0,w,h)
if pessoas:
    for i in range(randint(1,4)):
        escala_humana(randint(100,w),randint(100,h))

# cortina
m=60
painel_giratorio(m,13,1,m+20,m,gira=cortina_mobile,grid=grid,xy=(120,90))

# texto obras
painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(950,420))

# porta
if porta_fora:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-133,346),tipo='v')
else:
    # painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(615,670))
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-30,345),tipo='v')

restore()

#########################################
# eixo2

# 0,0
save()
translate(*medidas[5]['p0'])

#deleta linhas
fill(1)
stroke(None)
# fill(1,0,0)
# blendMode('darken')
rect(-70,-30,-420,248)
rect(26,-130,192,60)
rect(19,-640,192,160)
rect(-140,-2420,80,170)

# 0,0
eixo()

# escala humana
w=200
h=2490
if pessoas:
    for i in range(randint(1,4)):
        escala_humana(randint(50,w),-randint(0,h+150)-150)

# texto
save()
w=70
dist=randint(100,300)
painel_texto(w,dist,(40,-300-dist),tipo='v')
dist=randint(150,400)
painel_texto(w,dist,(140,-900-dist),tipo='v')
restore()

# porta
if porta_fora:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-142, 51),tipo='v')
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(73, -2336),tipo='v')
else:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-32, 51),tipo='v')
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-36, -2336),tipo='v')

# # texto obras
# painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(140,550))
# painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(870,580))

restore()

#########################################
# eixo3

# 0,0
save()
translate(*medidas[6]['p0'])

#deleta linhas
fill(1)
stroke(None)
# fill(1,0,0)
# blendMode('darken')
rect(4,-5,283,-248)
rect(-64,880,-192,139)
rect(-69,1750,-192,100)

# 0,0
eixo()

# escala humana
w=200
h=1790
if pessoas:
    for i in range(randint(1,3)):
        escala_humana(-randint(100,w),randint(0,h+150)-150)

# texto
save()
w=70
painel_texto(w,randint(150,400),(-250,190),tipo='v')
painel_texto(w,randint(100,300),(-150,800),tipo='v')
restore()

# porta
if porta_fora:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(76, -107),tipo='v')
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-156, 1626))
else:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-16, -107),tipo='v')
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-156, 1726))

# # texto obras
# painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(140,550))
# painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(870,580))

restore()



#########################################

end = time.time()
print('\n>>>', end-start, 's')
