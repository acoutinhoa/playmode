import time
start = time.time()

import os
from base import var
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
        'painel_playmode':{
            'w':80,
            'h':250,
            'margem':8,
            'dist':4,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'suspenso',
            },
        'painel_corredor':{
            'w':70,
            'h':250,
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
            'h':250,
            'margem':8,
            'dist':20,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'mobile',
            },
        'painel_obra2':{
            'w':30,
            'h':250,
            'margem':8,
            'dist':50,
            'base':70,
            'b2':0,
            'suporte':'obra2',
            },
        'painel_obra1':{
            'w':30,
            'h':280,
            'margem':8,
            'dist':20,
            'base':randint(20,80),
            'b2':randint(20,80),
            'suporte':'suspenso',
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


def tecido(largura, altura, base, b2,gira=0):
    save()
    translate(largura/2,0)
    x=-largura/2
    if gira:
        fill(None)
        stroke(.6)
        strokeWidth(.2)
        lineDash(2,4)
        rect(x,b2,largura,altura-b2)
        rect(x,base,largura,altura-base)
        eg=randint(10,100)/100
    else:
        eg=1
    scale(eg,1)
    if b2 and b2<base:
        fill(0.7)
        rect(x,b2,largura,altura-b2)
    fill(1)
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
    '5_paineis',
    ]

Variable([
    dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
    dict(name = "altura_randomica", ui = "CheckBox", args = dict(value = True)),
    dict(name = "autoportante", ui = "CheckBox", args = dict(value = True)),
    # dict(name = "w_cm", ui = "EditText", args = dict(text = '300')),
    # dict(name = "h_cm", ui = "EditText", args = dict(text = '200')),
    # dict(name = "cubo_cm", ui = "EditText", args = dict(text = '30')),
    # dict(name = "pilha_max", ui = "EditText", args = dict(text = '6')),
    # dict(name = "prateleira_mm", ui = "EditText", args = dict(text = '12')),
    # dict(name = "cubo_dado", ui = "CheckBox", args = dict(value = False)),
    # dict(name = "cubo_escala", ui = "CheckBox", args = dict(value = True)),
    # dict(name = "escala_max", ui = "EditText", args = dict(text = '3')),
    # dict(name = "repeticao_forma", ui = "PopUpButton", args = dict(items = repeticoes)),
    # dict(name = "caracteres", ui = "EditText", args = dict(text = 'PLAYMODE')),
    dict(name = "fonte", ui = "PopUpButton", args = dict(items = fontes_do_pc)),
    dict(name = "alturas", ui = "CheckBox", args = dict(value = True)),
    dict(name = "gira", ui = "CheckBox", args = dict(value = True)),
], globals())
    
fonte=var(fonte,'HelveticaNeue',lista=fontes_do_pc)
print('fonte =', fonte)

tipo=var(tipo,lista=tipos, tipo='lista')-1

# medidas
meio=150

# pagina:
if tipo in [4,6]:
    dados = medidas('pg2')
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
    paineis=[('painel_corredor',aberturas[1]),('painel_obra1',['obra',]),('painel_obra2',['obra',]),('painel_obra3',['obra',]),]

############################

e_pg=1
newPage(pw*e_pg,ph*e_pg)
scale(e_pg)

fill(.8)
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
    
    if autoportante:
        suporte_tipo='base_'+suporte_tipo
        ajuste=10
        dist+=ajuste

    save()
    
    if tipo==5:
        translate(100*(i+1),0)
    if tipo==6:
        x0=90
        if i:
            translate(80*(i+1)+x0*2,0)
        else:
            translate(x0,0)
    elif painel in paineis_textos:
        translate(50,0)
    elif painel in paineis_obras:
        translate(310,0)
    else: 
        #centraliza
        tudo=len(texto)*(largura+dist)-dist
        translate((pw-tudo)/2,0)
        
        
    for l,abertura in enumerate(texto):
        if altura_randomica:
            base=medidas(painel)['base']
            b2=medidas(painel)['b2']

        # suporte
        g=suporte(suporte_tipo,largura,altura,ajuste,gira=gira)

        #tecido
        tecido(largura, altura, base, b2,gira=g)

        #grafico
        if tipo==0:
            grafico=os.path.join(path_img,'eixo0_0%s_%s.pdf' % (randint(1,4),l))
            print(grafico)
            gw,gh=imageSize(grafico)
    
            eg=largura/gw
            save()
            blendMode('multiply')
            translate(0,185)
            scale(eg)
            for i in range(1):
                grafico=os.path.join(path_img,'eixo0_0%s_%s.pdf' % (randint(1,4),l))
                image(grafico,(0,0))
                translate(0,gh/2.5)
            restore()
    

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
            
            save()
            translate(margem,meio)
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
for i in range(randint(1,2)):
    modulor = os.path.join(path,'img/escala/modulor%s.pdf' % randint(0,3))
    save()
    translate(randint(120,pw-120),0)
    scale(choice([-1,1]),1)
    image(modulor,(0,0))
    restore()


#########################################

end = time.time()
print('\n>>>', end-start, 's')
