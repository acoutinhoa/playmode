import time
start = time.time()

import os
from base import var,cor
from docx import Document

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
# 1 inch = 2.54 cm
# cm = dpi/2.54
cm = 72/2.54
mm = cm/10

#####################################
# visualizar atributos do objeto
def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))
#####################################

def medidas(painel='',keys=False):
    dados={
        'pg1':{
            'w':410,
            'h':320,
            },
        'pg2':{
            'w':1250,
            'h':320,
            },
        'pg3':{
            'w':600,
            'h':320,
            },
        'painel_playmode':{
            'w':80,
            'h':220,
            'margem':8,
            'dist':4,
            'base':randint(20,60),
            'b2':randint(20,60),
            'suporte':'suspenso',
            },
        'painel_corredor':{
            'w':70,
            'h':220,
            'margem':6,
            'dist':20,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'suspenso',
            },
        'painel_cortina':{
            'w':60,
            'h':250,
            'margem':0,
            'dist':40,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'mobile',
            },
        'painel_obra3':{
            'w':30,
            'h':220,
            'margem':8,
            'dist':20,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'mobile',
            },
        'painel_obra2':{
            'w':30,
            'h':220,
            'margem':8,
            'dist':50,
            'base':70,
            'b2':0,
            'suporte':'obra2',
            },
        'painel_obra1':{
            'w':30,
            'h':250,
            'margem':8,
            'dist':20,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'suspenso',
            },
        'painel_entrada':{
            'w':20,
            'h':250,
            'margem':0,
            'dist':5,
            'base':5,
            'b2':randint(20,80),
            'suporte':'mobile',
            },
    }
    if painel:
        return dados[painel]
    elif keys:
        return list(dados.keys())

paineis_textos = [
    'painel_playmode',
    'painel_corredor',
]

paineis_obras = [
    'painel_obra1',
    'painel_obra2',
    'painel_obra3',
]


def tecido(largura, altura, base, b2,gira=0,b2c=(0.93,),img=None):
    save()
    translate(largura/2,0)
    x=-largura/2
    if gira:
        # fill(None)
        # stroke(.7)
        # strokeWidth(.2)
        # lineDash(1,4)
        # rect(x,b2,largura,altura-b2)
        # rect(x,base,largura,altura-base)
        eg=randint(10,100)/100
    else:
        eg=1
    scale(eg,1)
    
    lineDash(None)
    if b2 and b2<base:
        fill(*b2c)
        rect(x,b2,largura,altura-b2)
    
    if painel=='painel_entrada' and l%2:
        fill(.95)
    else:
        fill(1)
    
    if img:
        image(img,(x,base))
    else:
        rect(x,base,largura,altura-base)
    restore()

def suporte(tipo,largura,altura,ajuste=0,gira=0):
    g=0
    if tipo == 'mobile':
        stroke(0)
        strokeWidth(1.5)
        line((largura/2,altura),(largura/2,height()))
        stroke(None)
        if gira:
            g=1

    elif tipo == 'base_mobile':
        dh=30
        fill(None)
        stroke(0)
        strokeWidth(1.5)
        line((largura/2,altura),(largura/2,altura+dh))

        strokeWidth(1)
        rect(-ajuste/2,0,largura+ajuste,altura+dh)
        stroke(None)
        fill(0)
        rect(-ajuste/2,0,largura+ajuste,2)
        if gira:
            g=1

    elif tipo == 'obra2':
        stroke(0)
        strokeWidth(1.5)
        sw=-20
        sh=-5
        line((sw,altura+sh),(sw,height()))
        line((largura-sw,altura+sh),(largura-sw,height()))
        stroke(None)
        fill(0)
        rect(sw,altura,largura-2*sw,sh)

    elif tipo == 'base_obra2':
        fill(None)
        stroke(0)
        strokeWidth(1)
        rect(-ajuste/2,0,largura+ajuste,altura)
        stroke(None)
        fill(0)
        rect(-ajuste/2,0,largura+ajuste,2)

    elif tipo == 'suspenso':
        stroke(0)
        strokeWidth(1.5)
        sw=-2
        sh=-3
        line((sw,altura+sh),(sw,height()))
        line((largura-sw,altura+sh),(largura-sw,height()))
        stroke(None)
        fill(0)
        rect(sw,altura,largura-2*sw,sh)

    elif tipo == 'base_suspenso':
        fill(None)
        stroke(0)
        strokeWidth(1)
        rect(-ajuste/2,0,largura+ajuste,altura)
        stroke(None)
        fill(0)
        rect(-ajuste/2,0,largura+ajuste,2)
    return g


def formas(caracteres,m,fs=0,fonte='CourierNewPSMT'):
    if not fs:
        fs=m
    base={}
    # formas geometricas
    car_lista=['#','o','t','x',]
    for c in car_lista:
        x,y=0,0
        bezier=BezierPath()
        if c == '#':
            c='quadrado'
            bezier.rect(x,y,m,m)
        elif c == 'o':
            c='circulo'
            bezier.oval(x,y,m,m)
        elif c == 't':
            c='triangulo'
            bezier.polygon((x,y),(x+m/2,y+m),(x+m,y))
        elif c == '+':
            c='cruz'
            bezier.rect(x+m/4,y,m/2,m)
            bezier.rect(x,y+m/4,m,m/2)
        elif c == '*':
            c='xis2'
            n=3
            bezier.polygon((x,y),(x+m/n,y),(x+m,y+m),(x+m-m/n,y+m))
            bezier.polygon((x+m-m/n,y),(x+m,y),(x+m/n,y+m),(x,y+m),)
        elif c == 'X':
            c='xis'
            n=4
            bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
            bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
        elif c == 'x':
            c='xis'
            n=6
            x1=BezierPath()
            x2=BezierPath()
            x1.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
            x2.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
            bezier=x1.union(x2)
        base[c]=bezier
    # caracteres
    for c in caracteres:
        bezier=BezierPath()
        bezier.textBox(c, (-m/2,-m+fs-m,2*m,2*m), font=fonte, fontSize=fs, align='center',)
        base[c]=bezier
    return base


#########################################

# # docx
# doc = os.path.join(path_txt,'Playmode—textos_parede_PT—EN_2022.docx')
# doc = Document(doc)
# dump(doc)

# imagens
path_img = os.path.join(path,'img/txt')

# textos
path_txt = os.path.join(path,'_/txt')

aberturas = os.path.join(path_txt,'aberturas.txt')
with open(aberturas, encoding="utf-8") as file:
    aberturas = file.read()

# textos
aberturas=aberturas.split('###')
aberturas={i:txt.split('___') for i,txt in enumerate(aberturas)}

print('>>> 1px == 1cm')

fontes_do_pc = ['?',]+installedFonts()

tipos = [
    '?',
    '0_playmode',
    '1_eixo1',
    '2_eixo2',
    '3_eixo3',
    '4_cortina',
    '5_obras',
    '6_paineis',
    '7_entrada',
    ]

Variable([
    dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
    dict(name = "altura_randomica", ui = "CheckBox", args = dict(value = True)),
    dict(name = "autoportante", ui = "CheckBox", args = dict(value = True)),
    dict(name = "fonte", ui = "PopUpButton", args = dict(items = fontes_do_pc)),
    dict(name = "alturas", ui = "CheckBox", args = dict(value = False)),
    dict(name = "gira", ui = "CheckBox", args = dict(value = True)),
    dict(name = "imagem", ui = "CheckBox", args = dict(value = True)),
    dict(name = "estampa", ui = "CheckBox", args = dict(value = False)),
], globals())
    
fonte=var(fonte,'HelveticaNeue',lista=fontes_do_pc)
print('fonte =', fonte)

tipo=var(tipo,lista=tipos, tipo='lista')-1

# medidas
meio=140

# pagina:
if tipo in [4,6]:
    dados = medidas('pg2')
elif tipo == 7:
    dados = medidas('pg3')
else:
    dados = medidas('pg1')
pw=dados['w']
ph=dados['h']

# painel
if tipo == 0:
    paineis=[('painel_playmode',aberturas[0]),]
elif tipo == 1:
    paineis=[('painel_playmode',aberturas[1]),('painel_obra1',['obra',])]
elif tipo==2:
    paineis=[('painel_corredor',aberturas[2]),('painel_obra2',['obra',])]
elif tipo==3:
    paineis=[('painel_corredor',aberturas[3]),('painel_obra3',['obra',])]
elif tipo==4:
    paineis=[('painel_cortina',choice([9,])*['',])]
elif tipo==5:
    paineis=[('painel_obra1',['obra',]),('painel_obra2',['obra',]),('painel_obra3',['obra',]),]
elif tipo==6:
    paineis=[
        ('painel_corredor',aberturas[1]),
        ('painel_cortina',['',]), 
        ('painel_obra1',['obra',]),
        ('painel_obra2',['obra',]),
        ('painel_obra3',['obra',]),
        ('painel_obra1',['obra',]),
        ('painel_obra2',['obra',]),
        ('painel_obra3',['obra',]),
        ('painel_entrada',choice([7,])*['',]),
    ]
elif tipo==7:
    paineis=[('painel_entrada',19*['',])]

############################

e_pg=1
newPage(pw*e_pg,ph*e_pg)
scale(e_pg)

fundo=(0.8,)
fill(*fundo)
rect(0,0,pw,ph)

# meio + alturas
hs=[meio,]
if alturas:
    chaves=medidas(keys=True)
    for k in chaves:
        h=medidas(k)['h']
        if h not in hs:
            hs.append(h)

save()
fill(None)
stroke(.4)
lineDash(1,2)
for h in hs:
    line((0,h),(width(),h))
if alturas:
    fs=6
    fill(0,0,1)
    stroke(None)
    fontSize(fs)
    for h in hs:
        text(str(h)+'cm',(fs/2,h-1.5*fs))        
restore()

for i,info in enumerate(paineis):
    painel,texto=info
    
    dados = medidas(painel)
    ajuste=0
    
    largura=dados['w']
    altura=dados['h']
    margem=dados['margem']
    dist=dados['dist']
    base=dados['base']
    b2=dados['b2']
    suporte_tipo=dados['suporte']
    
    save()
    
    if tipo==5:
        translate(100*(i+1),0)
    elif tipo==6:
        x0=90
        if not i:
            translate(x0,0)
        elif i==1:
            translate(80*(i+1)+x0*2,0)
        elif i in [5,6,7]:
            autoportante=False
            translate(70*(i+1)+x0*3.5,0)
        elif i==8:
            autoportante=False
            translate(70*(i+1)+x0*4,0)
        else:
            translate(70*(i+1)+x0*3.1,0)
        if alturas:
            save()
            translate(0,meio)
            rotate(90)
            fontSize(6)
            fill(1,0,0)
            text(paineis[i][0],(2,10))
            restore()

    elif painel in paineis_textos:
        translate(50,0)
    elif painel in paineis_obras:
        translate(310,0)
    else: 
        #centraliza
        tudo=len(texto)*(largura+dist)-dist
        translate((pw-tudo)/2,0)
        
    if tipo==7:
        autoportante=False
    
    if autoportante:
        suporte_tipo='base_'+suporte_tipo
        ajuste=10
        dist+=ajuste

    for l,abertura in enumerate(texto):
        if altura_randomica:
            base=medidas(painel)['base']
            b2=medidas(painel)['b2']

        # suporte
        g=suporte(suporte_tipo,largura,altura,ajuste,gira=gira)

        ################################################
        ################################################
        ################################################
        #tecido
        if tipo==7:

            # painel entrada
            imgs_entrada=[
                'c_01',
                # 'c_02',
                'pm_01',    
                'pm_02',    
                # 'pm_03',    
                # 'pm_04',
                # 'grafico',
                # 'playmode',
            ]

            save()
            if imagem:
                img=choice(imgs_entrada)
                if img=='grafico':
                    pass
                elif img=='playmode':
                    pass
                else:
                    img=os.path.join(path,'img/txt/entrada/%s/%s.pdf' % (img,l))
                    tecido(largura, altura, base, b2, gira=g, b2c=cor('b'),img=img)
            else:
                for n in range(2):
                    tecido(largura, altura, base, b2, gira=g, b2c=cor('rgb'))
            restore()
        else:
            tecido(largura, altura, base, b2,gira=g)
        ################################################
        ################################################
        ################################################

        #grafico
        if tipo==0:
            if estampa:
                # estampa
                estampa=1
                grafico=os.path.join(path_img,'0/estampa_%s.pdf' % (randint(1,7)))
                print(grafico)
                gw,gh=imageSize(grafico)
                eg=largura/gw

                save()
                blendMode('multiply')
                translate(0,base)
                scale(eg)
                image(grafico,(0,0))
                restore()

            else:
                # grafico em cima
                grafico=os.path.join(path_img,'0/%s.pdf' % (randint(1,14)))
                print(grafico)
                gw,gh=imageSize(grafico)
                eg=largura/gw
                imh=30
                save()
                blendMode('multiply')
                translate(0,altura-imh)
                scale(eg)
                image(grafico,(0,0))
                restore()
            
            
            # limpa resto de imagem rara
            fill(*fundo)
            rect(-1,altura+.5,largura+2,ph-altura)
    

        #texto
        if painel in paineis_textos:
            abertura=abertura.split('\n')
            while '' in abertura:
                abertura.remove('')

            hyphenation(False)
            c=2
            ec=3
            fs=2
            lh=3.5
            
            tit = FormattedString()
            tit.append(abertura[0].upper()+'\n\n',font="CourierNewPS-BoldMT",fontSize=fs+1,lineHeight=lh+.5,align='right')
            
            if not l:
                fonte='HelveticaNeueLTStd-Roman'
            else:
                fonte= 'HelveticaNeueLTStd-Lt'

            txt = FormattedString()
            txt.align(None)
            for i,t in enumerate(abertura[1:]):
                if i:
                    txt.append('\n')
                txt.append(t, font=fonte, fontSize=fs,paragraphTopSpacing=fs,lineHeight=lh,)

            txt.append('◼︎●▴×\n\n', font=fonte, fontSize=2,paragraphTopSpacing=2,lineHeight=3.5,)

            tw=(largura-2*margem-(c-1)*ec)/c
            tw,th=textSize(txt, width=tw)
            th=(th/c)/2
            
            twt,tht=textSize(tit, width=tw)
            
            save()
            translate(margem,meio)
            
            if estampa:
                me=14
                save()
                fill(1)
                rect(-margem,-th-me,largura,2*th+tht+2*me)
                restore()
            alinha=['left','right']
            for n in range(c):
                txt=textBox(txt,((tw+ec)*n,-th,tw,2*th),align=alinha[n%2])

            twt,tht=textSize(tit, width=tw)
            textBox(tit,(0,th,tw,tht))

            restore()
            
            
        translate(largura+dist,0)

    restore()


# modulor
blendMode('darken')
for i in range(randint(1,1)):
    modulor = os.path.join(path,'img/escala/modulor%s.pdf' % randint(0,3))
    save()
    translate(randint(220,pw-120),0)
    scale(choice([-1,1]),1)
    image(modulor,(0,0))
    restore()


#########################################

end = time.time()
print('\n>>>', end-start, 's')
