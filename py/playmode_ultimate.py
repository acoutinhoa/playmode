import time
start = time.time()

##########################################################
import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
cm = 72/2.54
mm = cm/10

# _____________________________________
# _____________________________________
# _____________________________________

repete_x=3
repete_y=1

ajuste_texto=0

# # logo
# pw=1000
# ph=300
# faixas=10
# modulos=[2**i for i in range(0,6)] # n_modulos/faixa

# # cartaz
# pw=42*cm
# ph=60*cm
# faixas=4
# modulos=[2**i for i in range(1,7)] # n_modulos/faixa

# # painel entrada
# faixas=19
# pw=faixas*200
# ph=2500
# modulos=[2**i for i in range(0,6)] # n_modulos/faixa

# # texto abertura
# pw=800
# ph=2200
# # ph=350
# faixas=2
# modulos=[1,]+[2**i for i in range(0,6)] # n_modulos/faixa

# cortina
faixas=9
pw=600*faixas
ph=2500
modulos=[2**i for i in range(1,6)] # n_modulos/faixa


caracteres='PLAYMODE PLAYMODE'

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
    #     'x':'r',
    #     'y':'c',
    #     'zoom':'w',
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

    # 'bh cortina':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/playmode_2_BodoniSvtyTwoITCTT-BookIta.png',
    #     'x':'r',
    #     'y':'r',
    #     'zoom':randint(20,60),
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

    # 'bh2':{
    #     'path':'/Users/alien/x3/x/qdd/playmode/img/1/playmode_2_BodoniSvtyTwoITCTT-BookIta.png',
    #     'x':'r',
    #     'y':'r',
    #     'zoom':randint(3,6),
    #     'inverte_cores':False,
    #     'brilho':0,
    #     'contraste':1,
    # },

    # 'c_painel':{
    #     'path':'pixel_c_100.png',
    #     'x' : -476,
    #     'y' : -1307,
    #     'zoom' : 18,
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

    'obra_bandeira_2x1_cortina':{
        'path':'/Users/alien/x3/x/qdd/playmode/img/obras/bandeira.jpeg',
        'x' : 'r',
        'y' : 'r',
        'zoom' : randint(30,50)/10,
        'inverte_cores':False,
        'brilho':-0.0,
        'contraste':1,
    },

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

    'obra_taca_2x1_cortina':{
        'path':'/Users/alien/x3/x/qdd/playmode/img/obras/taca.jpeg',
        'x' : 'r',
        'y' : 'r',
        'zoom' : randint(20,40)/10,
        'inverte_cores':False,
        'brilho':-0.10,
        'contraste':1,
    },

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
        if n==1:
            desenho.removeOverlap()
        if ver==0:
            if txt_colorido and layer[0] not in ps2:
                cor_=cor(cor_txt)
            else:
                cor_=dgd(cor0,cor1,c,len(ordem)-1)
                
            if n==0:
                fill(*cor_)
                stroke(None)
            elif n==1:
                fill(None)
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

def cor(cores,cor_repetida=None):
    if type(cores) == type(''):
        c_lista=[c for c in cores]
        c=choice(c_lista)
        if c == 'r':
            c=(1,0,0)
        elif c == 'g':
            c=(0,1,0)
        elif c == 'b':
            c=(0,0,1)
        elif c == 'c':
            c=(0,1,1)
        elif c == 'm':
            c=(1,0,1)
        elif c == 'y':
            c=(1,1,0)
        elif c == 'k':
            c=(0,0,0)
        elif c == 'w':
            c=(1,1,1)
        else:
            c='cor nao definida'
        
        while c == cor_repetida:
            c=cor(cores,cor_repetida)
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
    '2_texto alinhado',
    '3_texto horizontal+vertical',
    '4_texto corrido',
    ]

Variable([
    # dict(name="CMYK", ui="CheckBox", args=dict(value=False)),
    dict(name="ver", ui="PopUpButton", args=dict(items=opcoes)),
    dict(name="grid", ui="CheckBox", args=dict(value=False)),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="texto", ui="PopUpButton", args=dict(items=tipos_txt)),
    dict(name="quadrado", ui="CheckBox", args=dict(value=True)),
    dict(name="circulo", ui="CheckBox", args=dict(value=True)),
    dict(name="triangulo", ui="CheckBox", args=dict(value=True)),
    dict(name="xis", ui="CheckBox", args=dict(value=True)),
    dict(name="com_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="degrade", ui="CheckBox", args=dict(value=False)),
    dict(name="faixas_randomicas", ui="CheckBox", args=dict(value=False)),
    dict(name="bg_randomico", ui="CheckBox", args=dict(value=False)),
    dict(name="txt_colorido", ui="CheckBox", args=dict(value=False)),
], globals())

#formas geometricas
ps1=[quadrado,circulo,triangulo,xis]
ps2=['quadrado','circulo','triangulo','xis',]

px_lista=[]
for i,botao in enumerate(ps1):
    if botao:
        px_lista.append(ps2[i])

# cores
cor0=cor(cor_0)
if degrade:
    cor1=cor(cor_1)
else:
    cor1=cor0
bg=cor(cor_bg,cor0)

# fonte
fonte_px=var(fonte,'CourierNewPS-BoldMT', lista=fontes_do_pc)

#caracteres
texto=var(texto,lista=tipos_txt,tipo='lista')
ajuste_txt=ajuste_texto

if texto>1 and caracteres:
    if texto==4:
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

# # # # # # imagens
# # # # # w=0
# # # # # h=0
# # # # # for i in imagens:
# # # # #     i=imagens[i]

# # # # #     img=i['path']
# # # # #     e=i['zoom']
    
# # # # #     if len(img.split('/')) == 1:
# # # # #         img=os.path.join(path_img,img)
# # # # #         i['path']=img
        
# # # # #     imgw,imgh=imageSize(img)
# # # # #     i['w']=imgw
# # # # #     i['h']=imgh

# # # # #     if e not in ['w','h']:
# # # # #         imgw=imgw*e
# # # # #         imgh=imgh*e
# # # # #         if not pw and imgw > w:
# # # # #             w=imgw
# # # # #         if not ph and imgh > h:
# # # # #             h=imgh

# # # # # # define pagina
# # # # # if not pw:
# # # # #     pw=w
# # # # # if not ph:
# # # # #     ph=h
# # # # # print('pagina = %spx x %spx' % (pw,ph) )


# largura da faixa
fw=pw/faixas

# estampa
ph=ph/repete_y
pw=pw/repete_x

for i in imagens:
    i=imagens[i]
    
    i_path=i['path']
    # img=i['path']
    # e=i['zoom']
    
    if len(i_path.split('/')) == 1:
        i_path=os.path.join(path_img,i_path)
        i['path']=i_path
        
    imgw,imgh=imageSize(i_path)
    i['w']=imgw
    i['h']=imgh


    # # # i_path=i['path']
    # # # imgw=i['w']
    # # # imgh=i['h']
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
        fill(1)
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
        fill(*bg)
        rect(0,0,pw*repete_x,ph*repete_y)
    
    save()
    for rx in range(repete_x):
        save()
        for ry in range(repete_y):
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
                    cor0=cor(cor_0)
                    if degrade:
                        cor1=cor(cor_1)
                    else:
                        cor1=cor0
                if bg_randomico:
                    bg=cor(cor_bg,cor0)
                    fill(*bg)
                    rect(f*fw,0,fw,ph)
        
                # formas
                base=bases[nm]
        
                # cria lista de pontos
                pontos_x=[f*fw+m0+m*x for x in range(nm)]
                pontos_y=[m0*(y+1) for y in range(round(ph/m0)) if not y%2]
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
        
                car_c+=nm
                restore()
            
                # desenha quadrados rosas da modulacao fora da pagina
                if ry==repete_y-1 and f%2:
                    fill(1,0,1)
                    rect(f*fw,ph+10,fw,fw)

            translate(0,ph)
        restore()
        translate(pw,0)
    restore()

# grid
if grid:
    fill(None)
    stroke(0)
    for i in range(faixas):
        if i:
            line((fw*i,0),(fw*i,ph*repete_y))

##########################################################

print('\n---------------------')
for img in imagens:
    print("    '%s' :" % img)
    for i in imagens[img]:
        print("        '%s' : %s," % (i,str(imagens[img][i])))
    print()
print('---------------------')

##########################################################
##########################################################
##########################################################

end = time.time()
print('\n>>>', end-start, 's')
