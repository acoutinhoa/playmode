import time
start = time.time()

##########################################################
import os
from base import var,dgd

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
cm = 72/2.54
mm = cm/10

# _____________________________________
# _____________________________________
# _____________________________________

repete_x=2
repete_y=1

ajuste_texto=-1

# # logo
# pw=1000
# ph=900
# faixas=10
# modulos=[2**i for i in range(0,5)] # n_modulos/faixa

# # cartaz
# pw=42*cm
# ph=60*cm
# faixas=10
# modulos=[2**i for i in range(1,6)] # n_modulos/faixa

# # painel entrada
# faixas=19
# pw=faixas*200
# ph=2500
# modulos=[2**i for i in range(1,5)] # n_modulos/faixa

# # texto abertura
# pw=800
# ph=2200
# # ph=350
# faixas=2
# modulos=[1,]+[2**i for i in range(0,6)] # n_modulos/faixa

# # cortina
# faixas=8
# pw=800*faixas
# ph=2500
# modulos=[2**i for i in range(0,5)] # n_modulos/faixa

# # portas
# faixas=2
# pw=800
# ph=2500
# modulos=[2**i for i in range(0,3)] # n_modulos/faixa

# # estampa
# faixas=4
# pw=800
# ph=2000
# modulos=[2**i for i in range(0,6)] # n_modulos/faixa

# obra
faixas=4
pw=30*cm
ph=60*cm
modulos=[1,1,]+[2**i for i in range(0,6)] # n_modulos/faixa
# modulos=[1,2,1,16,32,]

# caracteres='PPLLAAYYMMOODDEE'
caracteres='PLAYMODE'

# cores
# 'rgbcmykw' / (0-1,0-1,0-1,0-1) / [ (0-1,0-1,0-1,0-1),(0-1,0-1,0-1,0-1) ]
cor_0='k' 
cor_1='k'
cor_bg='w'
cor_txt='b'

sw=0.5 # espessura da linha (px) --- versao: com_linhas


# _____________________________________
# ______legenda imagens
# 'path' : 'str'
# 'x' : int / 'c'= centralizado / 'r'=randomico
# 'y' : int / 'c'= centralizado / 'r'=randomico
# 'zoom' : float. / 'w'= ajusta a largura / 'h'=ajusta a altura
# 'inverte_cores' : True / False
# 'brilho' : float. (-1,1)
# 'contraste' : float. (1,3)
# _____________________________________

imagens={
    
    # 'playmode logo':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/painel_1.png',
    #     'x':'c',
    #     'y':'c',
    #     'zoom':'w',
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'qctx logo':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/painel_3.png',
    #     'x':'c',
    #     'y':'c',
    #     'zoom':'w',
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    'obra_taca_2x1_estampa':{
        'path':'/Users/alien/x3/x/qdd/playmode/img/obras/taca.jpeg',
        'x' : 'c',
        'y' : 'r',
        'zoom' : randint(100,180)/100,
        'inverte_cores':False,
        'brilho':-0.10,
        'contraste':1,
    },

    # 'q_estampa':{
    #     'path':'pixel_q_100.png',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(2,10),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },
    # 'c_estampa':{
    #     'path':'pixel_c_100.png',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(2,10),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },
    # 't_estampa':{
    #     'path':'pixel_t_100.png',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(2,10),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },
    # 'x_estampa':{
    #     'path':'pixel_x_100.png',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(2,10),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },


    # 'playmode_abertura_3':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/painel_1.png',
    #     'x':0,
    #     'y' : -95.22566995768688,
    #     'zoom' : 'w',
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'playmode_entrada_3':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/painel_1.png',
    #     'x':0,
    #     'y' : 'c',
    #     'zoom' : 'w',
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'bh entrada':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/playmode_2_BodoniSvtyTwoITCTT-BookIta.png',
    #     # 'x' : -50831,
    #     # 'y' : -22768,
    #     # 'zoom' : 58,
    #     'x':'r',
    #     'y':'r',
    #     'zoom':randint(50,80),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'obra_bandeira_entrada':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/bandeira.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(70,140)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.0,
    #     'contraste':1,
    # },

    # 'bh cortina':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/playmode_2_BodoniSvtyTwoITCTT-BookIta.png',
    #     # 'x' : -33755,
    #     # 'y' : -1399,
    #     # 'zoom' : 50,
    #     'x':'r',
    #     'y':'r',
    #     'zoom':randint(40,80),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'playmode_cortina_3':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/painel_1.png',
    #     'x':0,
    #     'y' : -95.22566995768688,
    #     'zoom' : 'w',
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'c_porta':{
    #     'path':'pixel_c_100.png',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(10,50),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'obra_bandeira':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/bandeira.jpeg',
    #     'x' : -randint(0,700),
    #     'y' : 'r',
    #     'zoom' : randint(25,30)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.0,
    #     'contraste':1,

    # 'obra_bandeira_2x1_cartaz':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/bandeira.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(13,30)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.0,
    #     'contraste':1,
    # },

    # 'obra_cubo_2x1_cartaz':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/cubo.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(20,40)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.10,
    #     'contraste':1,
    # },

    # 'obra_bandeira_2x1_cortina':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/bandeira.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(30,50)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.0,
    #     'contraste':1,
    # },

    # 'obra_cubo_2x1_cortina':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/cubo.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(60,90)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.20,
    #     'contraste':1,
    # },

    # 'obra_triangulo_2x1_cortina':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/triangulo.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(40,70)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.0,
    #     'contraste':1,
    # },

    # 'obra_taca_2x1_cortina':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/obras/taca.jpeg',
    #     'x' : 'r',
    #     'y' : 'r',
    #     'zoom' : randint(20,40)/10,
    #     'inverte_cores':False,
    #     'brilho':-0.10,
    #     'contraste':1,
    # },

}


# _____________________________________
# _____________________________________
# _____________________________________


# # # CMYK

# # # questoes:
# # #     outras formas? seta?

##########################################################

def cria_pasta(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print('>>> pasta criada \n>>>',path)

def car_texto(car,car_c,i,j,texto,ajuste=0):
    if texto == 2: # alinhado vertical
        car_n=(car_c+i+ajuste)%len(car)
    if texto == 3: # alinhado horizontal
        car_n=(car_c+j+ajuste)%len(car)
    elif texto == 4: # alinhado diagonal
        car_n=(car_c+i+j+ajuste)%len(car)
    elif texto == 5: # na sequencia
        car_n=car_c%len(car)
        car_c+=1
    car=car[car_n]
    return car,car_c

def pixel(ponto,m,car_c,bezier,formas,texto,ajuste_txt=0):
    car,x,y,i,j = ponto

    if car not in formas.keys():
        car,car_c=car_texto(car,car_c,i,j,texto,ajuste_txt)
    
    bezier.translate(-x,-y)
    bezier.appendPath(formas[car])
    bezier.translate(x,y)

    return bezier,car_c

def playmode(vezes,pontos,layer,c=0,ajuste_txt=0,car_c=0):
    for n in range(vezes):
        desenho=BezierPath()
        for pt in pontos:
            if pt[0] in layer:
                if com_linha:
                    if n==0 and c<len(px_lista):
                        desenho,car_c=pixel(pt,m,car_c,desenho,base,texto)
                    elif n==1 and c>=len(px_lista):
                        pt[0]=pt[0][:-1]
                        desenho,car_c=pixel(pt,m,car_c,desenho,base,texto)
                else:
                    desenho,car_c=pixel(pt,m,car_c,desenho,base,texto,ajuste_txt)
        
        if unir_formas:
            desenho.removeOverlap()

        if ver==0:
            if txt_colorido and layer[0] not in ps2:
                cor_=cor(cor_txt,cmyk=cmyk)
            else:
                cor_=dgd(cor0,cor1,c,len(ordem)-1)
                
            if n==0:
                if cmyk:
                    cmykFill(*cor_)
                else:
                    fill(*cor_)
                stroke(None)
            elif n==1:
                fill(None)
                if cmyk:
                    cmykStroke(*cor_)
                else:
                    stroke(*cor_)
                strokeWidth(sw)
                miterLimit(sw)
            drawPath(desenho)
    return car_c

def formas(caracteres,m,fs=0,fonte='CourierNewPSMT'):
    if not fs:
        fs=m
    base={}
    # formas geometricas
    car_lista=['#','o','t','x','+']
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
            c = 'cruz'
            esp=m/4.3
            dist=(m-esp)/2
            x1=BezierPath()
            x2=BezierPath()
            x1.rect(x+dist,y,esp,m)
            x2.rect(x,y+dist,m,esp)            
            bezier=x1.union(x2)

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

def cor(cores,cor_repetida=None,cmyk=False):
    if type(cores) == type(''):
        c_lista=[c for c in cores]
        c=choice(c_lista)
        if c == 'r':
            if cmyk:
                c=(0,1,1,0)
            else:
                c=(1,0,0)
        elif c == 'g':
            if cmyk:
                c=(1,1,0,0)
            else:
                c=(0,1,0)
        elif c == 'b':
            if cmyk:
                c=(1,0,1,0)
            else:
                c=(0,0,1)
        elif c == 'c':
            if cmyk:
                c=(1,0,0,0)
            else:
                c=(0,1,1)
        elif c == 'm':
            if cmyk:
                c=(0,1,0,0)
            else:
                c=(1,0,1)
        elif c == 'y':
            if cmyk:
                c=(0,0,1,0)
            else:
                c=(1,1,0)
        elif c == 'k':
            if cmyk:
                c=(0,0,0,1)
            else:
                c=(0,0,0)
        elif c == 'w':
            if cmyk:
                c=(0,0,0,0)
            else:
                c=(1,1,1)
        else:
            c='cor nao definida'
        
        while c == cor_repetida:
            c=cor(cores,cor_repetida,cmyk=cmyk)
    elif type(cores) == []:
        c=choice(cores)
    else:
        c=cores
        
    return c

##########################################################

# imagens
path_img = os.path.join(path,'img/ultimate')
cria_pasta(path_img) # cria pasta 1

# visualizar
opcoes = [
    '0_textura',
    '1_imagens',
    ]

fontes_do_pc = ['?',]+installedFonts()

# tipos de texto
tipos_txt=[
    '?',
    '1_caracteres',
    '2_texto alinhado vertical',
    '3_texto alinhado horizontal',
    '4_texto diagonal',
    '5_texto na sequencia',
    ]
# tipos_txt=[
#     '?',
#     '1_caracteres',
#     '2_texto alinhado',
#     '3_texto horizontal+vertical',
#     '4_texto corrido',
#     ]

unir_formas=False

Variable([
    dict(name="cmyk", ui="CheckBox", args=dict(value=True)),
    # dict(name="unir_formas", ui="CheckBox", args=dict(value=False)),
    dict(name="ver", ui="PopUpButton", args=dict(items=opcoes)),
    dict(name="grid", ui="CheckBox", args=dict(value=False)),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="texto", ui="PopUpButton", args=dict(items=tipos_txt)),
    dict(name="quadrado", ui="CheckBox", args=dict(value=True)),
    dict(name="circulo", ui="CheckBox", args=dict(value=True)),
    dict(name="triangulo", ui="CheckBox", args=dict(value=True)),
    dict(name="xis", ui="CheckBox", args=dict(value=True)),
    dict(name="cruz", ui="CheckBox", args=dict(value=False)),
    dict(name="com_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="degrade", ui="CheckBox", args=dict(value=False)),
    dict(name="faixas_randomicas", ui="CheckBox", args=dict(value=False)),
    dict(name="bg_randomico", ui="CheckBox", args=dict(value=False)),
    dict(name="txt_colorido", ui="CheckBox", args=dict(value=False)),
], globals())

#formas geometricas
ps1=[quadrado,circulo,triangulo,xis,cruz]
ps2=['quadrado','circulo','triangulo','xis','cruz']

px_lista=[]
for i,botao in enumerate(ps1):
    if botao:
        px_lista.append(ps2[i])

# cores
cor0=cor(cor_0,cmyk=cmyk)
if degrade:
    cor1=cor(cor_1,cmyk=cmyk)
else:
    cor1=cor0
bg=cor(cor_bg,cor0,cmyk=cmyk)

# fonte
fonte_px=var(fonte,'CourierNewPS-BoldMT', lista=fontes_do_pc)

#caracteres
texto=var(texto,lista=tipos_txt,tipo='lista')
ajuste_txt=ajuste_texto

if texto>1 and caracteres:
    if texto==5:
        px_lista.append(caracteres)
    else:
        px_lista+=caracteres.split(' ')
else:
    px_lista+=[car for car in caracteres]

##########################################################
print('faixas = ', faixas)
print('modulos = ', modulos)
print()
print('imgs =', list(imagens.keys()))
print('fonte =', fonte_px)
print('cor0 =', cor0)
print('cor1 =', cor1)
print('bg =', bg)
print('texto =', tipos_txt[texto])
##########################################################

# largura da faixa
fw=pw/faixas

# estampa
ph=ph/repete_y
pw=pw/repete_x

for i in imagens:
    i=imagens[i]
    
    i_path=i['path']
    
    if len(i_path.split('/')) == 1:
        i_path=os.path.join(path_img,i_path)
        i['path']=i_path
        
    imgw,imgh=imageSize(i_path)
    i['w']=imgw
    i['h']=imgh

    x=i['x']
    y=i['y']
    e=i['zoom']
    inverte=i['inverte_cores']
    brilho=i['brilho']
    contraste=i['contraste']
    
    # escala
    if e == 'w':
        e=pw/imgw
    if e == 'h':
        e=ph/imgh
    
    imgw=imgw*e
    imgh=imgh*e

    # centraliza imagem
    if x == 'c':
        x=(pw-imgw)/2
    elif x == 'r':
        w=imgw-pw
        x=randint(0,abs(int(w)))
        if w>0:
            x=x*-1

    if y == 'c':
        y=(ph-imgh)/2
    elif y == 'r':
        h=imgh-ph
        y=randint(0,abs(int(h)))
        if h>0:
            y=y*-1

    i['x']=x
    i['y']=y
    i['zoom']=e

    # imagem
    img = ImageObject()
    with img:
        size(pw,ph)
        if cmyk:
            cmykFill(*cor('w',cmyk=cmyk))
        else:
            fill(*cor('w',cmyk=cmyk))
        rect(0,0,pw,ph)
        translate(x,y)
        scale(e)
        image(i_path,(0,0))
        
    img.colorMonochrome(color=(1,1,1,1), intensity=None)
    img.colorControls(saturation=None, brightness=brilho, contrast=contraste)
    if inverte:
        img.colorInvert()
    
    i['img']=img


# visualiza imagens
if ver==1:
    for i in imagens:
        img=imagens[i]
        newPage(pw*repete_x,ph*repete_y)
        for rx in range(repete_x):
            for ry in range(repete_y):
                image(img['img'],(rx*pw,ry*ph))

else:
    
    # #gif
    # gif=1
    # while gif<50:
    #     modulos=[gif,]
    
    # cria dicionario com formas basicas formas basicas pra cada zoom
    bases={}
    for nm in modulos:
        m=fw/nm
        b=formas(caracteres,m,fonte=fonte_px)
        bases[nm]=b

    if com_linha:
        vezes=2
        px_lista2=[px+'_' for px in px_lista]
        px_lista2.reverse()
        ordem=px_lista+px_lista2+['']
    else:
        vezes=1
        ordem=px_lista+['']
    print('ordem =',ordem)

    newPage(pw*repete_x,ph*repete_y)

    if bg and not faixas_randomicas:
        if cmyk:
            cmykFill(*bg)
        else:
            fill(*bg)
        rect(0,0,pw*repete_x,ph*repete_y)

    save()
    for rx in range(repete_x):
        save()
        car0=0
        translate(0,height()-ph)
        for ry in range(repete_y):
            if texto in [3,4]:
                car_c=car0
            else:
                car_c=0
            for f in range(faixas):
                nm=choice(modulos)
                m=fw/nm
                m0=m/2 # ponto central do modulo para verificacao da cor
            
                # imagem
                img_i=choice(list(imagens.keys()))
                img=imagens[img_i]['img']
    
                print()
                print('>>> faixa', f)
                print('imagem =', img_i)
                print('n_modulos =', nm)
    
                # cores
                if faixas_randomicas:
                    cor0=cor(cor_0,cmyk=cmyk)
                    if degrade:
                        cor1=cor(cor_1,cmyk=cmyk)
                    else:
                        cor1=cor0
                if bg_randomico:
                    bg=cor(cor_bg,cor0,cmyk=cmyk)

                    if cmyk:
                        cmykFill(*bg)
                    else:
                        fill(*bg)
                    rect(f*fw,0,fw,ph)
    
                # formas
                base=bases[nm]
    
                # cria lista de pontos
                pontos_x=[f*fw+m0+m*x for x in range(nm)]
                pontos_y=[m0*y for y in range(ceil(ph/m0)) if y%2]
                pontos_y.reverse() # inverte a lista vertical para desenha de cima para baixo
            
                pontos=[]
                for j,y in enumerate(pontos_y):
                    for i,x in enumerate(pontos_x):
                        cinza=imagePixelColor(img,(x,y))
                        if cinza==None:
                            cinza=1
                        else:
                            cinza=cinza[0]
                        car=int(cinza//(1/len(ordem)))
                        if car==len(ordem):
                            car=len(ordem)-1
                        car=ordem[car]
                        pontos.append([car,x,y,i,j])

                save()
                translate(-m0,-m0)

                for c,camada in enumerate(ordem[:-1]):
                    car_c=playmode(vezes,pontos,[camada,],c,ajuste_txt,car_c=car_c)
            
                if texto in [2,4]:
                    car_c+=nm
                if texto in [3,4] and not f:
                    car0=car_c+len(pontos_y)

                restore()
        
                # desenha quadrados rosas da modulacao fora da pagina
                if not ry and f%2:
                    if cmyk:
                        cmykStroke(*cor('m',cmyk=cmyk))
                    else:
                        fill(*cor('m',cmyk=cmyk))
                    rect(f*fw,ph+10,fw,1*cm)
            
            
            
            translate(0,-ph)
        restore()
        translate(pw,0)
    restore()


        # # # # # salvar
        # # ordem=str(gif)
        # # ordem=(3-len(ordem))*'0'+ordem
        # # pasta='7'
        # # nome='gif/%s/%s_playmode.pdf' % (pasta,ordem)
        # # path_save=os.path.join( path,nome )
        # # saveImage(path_save, multipage=False)
        # # print('gif salvo >>>')
        # # print(path_save)
        
        
        # if gif>=40:
        #     gif+=10
        # elif gif>=20:
        #     gif+=5
        # else:
        #     gif+=1


# grid
if grid:
    fill(None)
    if cmyk:
        cmykStroke(*cor('w',cmyk=cmyk))
    else:
        stroke(*cor('w',cmyk=cmyk))
    for i in range(faixas):
        if i:
            line((fw*i,0),(fw*i,ph*repete_y))

##########################################################

print('\n---------------------')
for img in imagens:
    print("    '%s' : {" % img)
    for i in imagens[img]:
        print("        '%s' : %s," % (i,str(imagens[img][i])))
    print('    },')
    print()
print('---------------------')

##########################################################
##########################################################
##########################################################

end = time.time()
print('\n>>>', end-start, 's')
