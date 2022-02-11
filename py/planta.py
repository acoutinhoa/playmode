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
        'pw':1800,
        'ph':1140,
        'p0':(3640,900),
        'pp':(-3300,-750),
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
        humano=os.path.join(path,'img/escala/escala2_35.pdf')
    elif humano==1:
        humano=os.path.join(path,'img/escala/escala3_46.pdf')

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

def linha00(xy):
    stroke(0,1,0)
    line((0,0),(-xy[0],-xy[1]))
    text(str(xy),(-100,0))

def painel_giratorio(modulo,repeticao_w=1,repeticao_h=1,grid_w=0,grid_h=0,esp=3,gira=1,grid=0,intercalado=0,xy=(0,0),tipo='h',base=0,bw=10,bh=40):
    if modulo == 'obras':
        modulo=30
    
    # calcula dimensoes da cortina
    cw=(repeticao_w-1)*grid_w+modulo
    ch=(repeticao_h-1)*grid_h+modulo
    # print('cortina = %scm x %scm' % (cw, ch))

    save()
    translate(*xy)
    save()
    if tipo=='v':
        rotate(90)
    save()
    w=modulo+bw
    for l in range(repeticao_h):
        save()
        for m in range(repeticao_w):
            if not intercalado or not (l+m+repeticao_h)%2:
                # base
                if base:
                    if base==1:
                        esp=1.2
                        fill(None)
                        stroke(0.6)
                        strokeWidth(.2)
                    
                        save()
                        translate(-w/2,-bh/2)
                        rect(0,0,w,bh)
                        fill(0)
                        for bi in range(2):
                            rect(0,0,esp,bh)
                            translate(w-esp,0)
                        restore()
                        fill(0)
                        rect(-w/2,-esp/2,w,esp)
                    else:
                        esp=3
                        fill(0)
                        stroke(None)
                        rect(-base/2,-esp/2,base,esp)


                save()
                fill(None)
                stroke(0)
                strokeWidth(esp)
                if gira:
                    rotate(randint(0,360))
                    oval(-esp,-esp,2*esp,2*esp)
                # else:
                #     oval(-modulo/2,-esp,2*esp,2*esp)
                #     oval(modulo/2,-esp,-2*esp,2*esp)
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
    legenda='\n'
    if repeticao_h>1:
        legenda+= 'grid = %s x %s pontos\n' % (repeticao_w,repeticao_h)
        legenda+= 'modulo = %scm x %scm\n' % (grid_w,grid_h)
        legenda+= 'total = %scm x %scm\n' % (cw,ch)

    elif repeticao_w>1:
        legenda+='%s paineis\n' % repeticao_w
        legenda+='dist_eixos= %scm\n' % grid_w
    legenda+='tecido = %scm largura\n' % modulo
    if base==1:
        legenda+= 'base = %scm x %scm\n' % (w,bh)
    elif base>1:
        legenda+= 'barra = %scm largura\n' % (base)
    if intercalado:
        legenda+='paineis intercalados\n'
    if gira:
        legenda+='painel móbile\n'
    print(legenda)

    if grid:
        fill(None)
        strokeWidth(1)
        if not base:
            stroke(1,0,1)
            for i in range(repeticao_h):
                y=grid_h*i
                line((0,y),(cw-modulo,y))
            for i in range(repeticao_w):
                x=grid_w*i
                line((x,0),(x,ch-modulo))
    restore()
    if grid:
        # 0,0
        linha00(xy)
        # legenda
        stroke(None)
        fill(0,0,1)
        text(legenda,(0,-20-modulo/2))
    restore()    
    return cw,ch

def painel_texto(w,dist,xy=(0,0),tipo='h',humano=1,base=0,bh=40,bw=10,info=1,txt=[]):
    save()
    translate(*xy)

    # info
    legenda='\n'
    legenda+='tecido = %scm largura\n' % w
    if base:
        legenda+= 'base = %scm x %scm\n' % (bh,w+bw)
    legenda+= 'dist_paineis = %scm' % (dist)

    if grid:        
        # 0,0
        linha00(xy)
        # legenda
        if info:
            stroke(None)
            fill(0,0,1)
            text(legenda,(0,-20-modulo/2))

    if tipo=='v':
        translate(w,0)
        rotate(90)
    
    if grid and txt:
        dt=100
        fill(1,0,0)
        fontSize(15)
        text(txt[0]+' >',(-dt,w/2),align='right')
        text('< '+txt[1],(dist+dt,w/2))
            
    
    fill(None)
    stroke(0.6)
    strokeWidth(.2)

    if base:
        esp=1.2
        esp2=3
        save()
        translate(-bh/2,0)
        for bi in range(2):
            rect(0,0,bh,w+bw)
            save()
            fill(0)
            rect(bh/2,0,esp2,w+bw)
            for bj in range(2):
                rect(0,0,bh,esp)
                translate(0,w+bw-esp)
            restore()
            translate(dist-esp2,0)
        restore()
        translate(0,bw/2)
    
    linearGradient(
        (0, 0), # startPoint
        (dist, 0), # endPoint
        [(1,), (0.5,), (1,)], # colors
        [0, .5, 1], # locations
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
    dict(name="painel", ui="PopUpButton", args=dict(items=possibilidades)),
    dict(name="cortina", ui="PopUpButton", args=dict(items=possibilidades)),
    dict(name="porta", ui="PopUpButton", args=dict(items=possibilidades)),
    # dict(name="n_modulos", ui="EditText", args=dict(text='')),
    dict(name = "pessoas", ui = "CheckBox", args = dict(value = True)),
    dict(name = "painel_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "txt_mobile", ui = "CheckBox", args = dict(value = False)),
    dict(name = "cortina_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "porta_mobile", ui = "CheckBox", args = dict(value = True)),
    dict(name = "grid", ui = "CheckBox", args = dict(value = False)),
], globals())
    
# zoom
zoom=var(zoom,1,lista=areas,tipo='lista')

# proposta
versao=var(painel,3,lista=possibilidades,tipo='lista')
versao_cortina=var(cortina,3,lista=possibilidades,tipo='lista')
versao_porta=var(porta,3,lista=possibilidades,tipo='lista')

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
image(planta,(0,0),.25)
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
    dist_porta=50
    dist_parede=60

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

# desenha cortina
cw,ch=painel_giratorio(modulo,repeticao_w,repeticao_h,grid_w,grid_h,gira=painel_mobile,grid=grid,intercalado=1,xy=(dist_porta,dist_parede))
    
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
w=80
dist=150
x=700
y=100
painel_texto(w,dist,(x,y),base=1,txt=['titulo eixo1 en','txt curatorial pt'])
painel_texto(w,dist,(x,y+w+20),base=1,txt=['titulo eixo1 pt','txt curatorial en'])

painel_texto(w,100,(x-420,y+60),tipo='v',base=1,txt=['txt eixo1 en','txt eixo1 pt'])

restore()

# cortina
if versao_cortina == 1:
    m=60
    painel_giratorio(m,9,1,m+50,m,gira=cortina_mobile,grid=grid,xy=(160,790),base=1)
elif versao_cortina == 2:
    m=150
    painel_giratorio(m,3,1,m+200,m,gira=cortina_mobile,grid=grid,xy=(255,800),base=1,bh=60)
elif versao_cortina == 3:
    m=110
    janela=180
    dist=m+241
    dist=painel_giratorio(m,3,1,dist,m,gira=cortina_mobile,grid=grid,xy=(256,845),base=janela)

# texto obras
painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(140,550),base=1,tipo='v')
painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(870,580),base=1,tipo='v')

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
if versao_cortina == 1:
    m=60
    painel_giratorio(m,9,1,m+50,m,gira=cortina_mobile,grid=grid,xy=(160,60),base=1)
elif versao_cortina == 2:
    m=180
    painel_giratorio(m,3,1,m+240,m,gira=cortina_mobile,grid=grid,xy=(190,50),base=1,bh=60)
elif versao_cortina == 3:
    m=120
    janela=230
    dist=m+296
    dist=painel_giratorio(m,3,1,dist,m,gira=cortina_mobile,grid=grid,xy=(190,-2),base=janela)

# texto obras
painel_giratorio('obras',gira=txt_mobile,grid=grid,xy=(950,420),base=1,tipo='v')

# porta
translate(-80,290)
eixo()
if versao_porta==1:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(50,55),tipo='v',base=115)
    
elif versao_porta==2:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-90,55),tipo='v',base=1)

elif versao_porta==3:
    m=20
    painel_giratorio(m,repeticao_w=8,repeticao_h=2,grid_w=m,grid_h=m,esp=3,gira=1,grid=grid,intercalado=1,xy=(-60,-15),tipo='v')

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
dist=randint(100,200)
painel_texto(w,dist,(50,-300-dist),tipo='v',base=1,txt=['titulo eixo2 en','txt eixo2 en'])
dist=randint(150,300)
painel_texto(w,dist,(150,-900-dist),tipo='v',base=1,txt=['titulo eixo2 pt','txt eixo2 pt'])
restore()

# porta2
if versao_porta==1:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-32, 51),tipo='v',base=110)
else:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-150, 51),tipo='v',base=1)

# porta1
translate(-20,-2390)
eixo()
if versao_porta==1:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-18, 55),tipo='v',base=110)
else:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(80, 51),tipo='v',base=1)

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
painel_texto(w,randint(150,300),(-250,190),tipo='v',base=1,txt=['txt eixo3 en','titulo eixo3 en'])
painel_texto(w,randint(100,200),(-150,800),tipo='v',base=1,txt=['txt eixo3 pt','titulo eixo3 pt'])
restore()

# porta3
if versao_porta==1:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(-15, -105),tipo='v',base=110)
else:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(80, -107),tipo='v',base=1)

# porta2
translate(-215,1700)
eixo()
if versao_porta==1:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(55, 25),base=110)
else:
    painel_giratorio(80,gira=porta_mobile,grid=grid,xy=(55, -90),base=1)

restore()



#########################################

end = time.time()
print('\n>>>', end-start, 's')
