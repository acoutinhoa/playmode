import time
start = time.time()

##########################################################

import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

##########################################################

faixas=10 # numero de faixas
modulos=list(range(1,20,5))
cores='rgbk'
cores_bg='kw'

# imagem
imgs=[
    # 'paciencia.jpeg',
    'painel_1.png',
    'painel_3.png',
    # 'playmode_2_BodoniSvtyTwoITCTT-BookIta.png',
]

# com_linhas
sw=0.5 #espessura da linha

##########################################################

print('faixas = ', faixas)
print('modulos = ', modulos)
print()
print('imgs =', imgs)

##########################################################

# # # CMYK

# # # varicao das faixas:
# # #     zomm
# # #     texto
    
# # # questoes:
# # #     outras formas? seta?
# # #     ajuste_texto?
# # #     contraste/brilho - no menu?


##########################################################

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
            cor_=dgd(cor1,cor2,c,len(ordem)-1)
            if n==0:
                fill(*cor_)
                stroke(None)
            elif n==1:
                fill(None)
                stroke(*cor_)
                strokeWidth(sw)
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
            bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
            bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
        base[c]=bezier
    # caracteres
    for c in caracteres:
        bezier=BezierPath()
        bezier.textBox(c, (-m/2,-m+fs-m,2*m,2*m), font=fonte, fontSize=fs, align='center',)
        base[c]=bezier
    return base

def cor(cores,cor_repetida=None):
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
        
    return c

##########################################################

# imagens
path_img = os.path.join(path,'img/1')
# crias pasta 1
if not os.path.isdir(path_img):
    os.mkdir(path_img)
    print('>>> pasta criada \n>>>',path_img)

# visualizar
opcoes = [
    '0_textura',
    '1_imagem',
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
    # dict(name="contraste", ui="Slider", args=dict(value=1, minValue=1, maxValue=3)),
    # dict(name="brilho", ui="Slider", args=dict(value=0, minValue=-1, maxValue=1)),
    dict(name="inverte_cores", ui="CheckBox", args=dict(value=False)),
    dict(name="com_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="caracteres", ui="EditText", args=dict(text='PLAYMODE')),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="texto", ui="PopUpButton", args=dict(items=tipos_txt)),
    dict(name="quadrado", ui="CheckBox", args=dict(value=True)),
    dict(name="circulo", ui="CheckBox", args=dict(value=True)),
    dict(name="triangulo", ui="CheckBox", args=dict(value=True)),
    dict(name="xis", ui="CheckBox", args=dict(value=True)),
    dict(name="cor1", ui="EditText", args=dict(text='')),
    dict(name="cor2", ui="EditText", args=dict(text='')),
    dict(name="degrade", ui="CheckBox", args=dict(value=False)),
    dict(name="faixas_randomicas", ui="CheckBox", args=dict(value=False)),
    dict(name="bg", ui="EditText", args=dict(text='100 100 100')),
    dict(name="bg_randomico", ui="CheckBox", args=dict(value=False)),
    dict(name="grid", ui="CheckBox", args=dict(value=False)),
], globals())

px_lista=[]
#formas geometricas
if quadrado:
    px_lista.append('quadrado')
if circulo:
    px_lista.append('circulo')
if triangulo:
    px_lista.append('triangulo')
if xis:
    px_lista.append('xis')

# cores
cor1=var(cor1,cor(cores),tipo='cor')
if degrade:
    cor2=var(cor2,cor(cores),tipo='cor')
else:
    cor2=cor1
bg=var(bg,cor(cores_bg,cor1),tipo='cor')

# fonte
fonte_px=var(fonte,'CourierNewPS-BoldMT', lista=fontes_do_pc)

#caracteres
texto=var(texto,lista=tipos_txt,tipo='lista')
ajuste_txt=0

if texto>1 and caracteres:
    if texto==4:
        px_lista.append(caracteres)
    else:
        px_lista+=caracteres.split(' ')
else:
    px_lista+=[car for car in caracteres]

print('fonte =', fonte_px)
print('cor1 =', cor1)
print('cor2 =', cor2)
print('bg =', bg)
print('texto =', tipos_txt[texto])

##########################################################

# cria dicionario de imagens
pw=0
ph=0

imagens={}

for i,img in enumerate(imgs):
    imagens[i]={}
    
    img=os.path.join(path_img,img)
    imgw,imgh=imageSize(img)
    
    imagens[i]['path']=img
    imagens[i]['w']=imgw
    imagens[i]['h']=imgh
    
    if imgw > pw:
        pw=imgw
    if imgh > ph:
        ph=imgh

# posicao e tamanho das imagens
for i in imagens:
    i=imagens[i]
    
    img_path=i['path']
    imgw=i['w']
    imgh=i['h']
    
    e=1 #escala
    
    # centraliza imagem
    x=(pw-imgw*e)/2
    y=(ph-imgh*e)/2
    
    img = ImageObject()
    with img:
        size(pw,ph)
        fill(1)
        rect(0,0,pw,ph)
        translate(x,y)
        scale(e)
        image(img_path,(0,0))
        
    img.colorMonochrome(color=(1,1,1,1), intensity=None)
    # img.colorControls(saturation=None, brightness=brilho, contrast=contraste)
    if inverte_cores:
        img.colorInvert()
    
    i['img']=img
    i['xy']=(x,y)
    i['escala']=e


# visualiza imagens
if ver==1:
    for i in imagens:
        img=imagens[i]
        newPage(pw,ph)
        image(img['img'],(0,0))

else:
    # faixas
    fw=pw/faixas
    
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

    newPage(pw,ph)

    if bg and not faixas_randomicas:
        fill(*bg)
        rect(0,0,pw,ph)
    
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
        print('n_modulos =', nm)
        print('modulos/faixa =', m)
        print('imagem =', imagens[img_i]['path'])
        
        # cores
        if faixas_randomicas:
            cor1=cor(cores)
            if degrade:
                cor2=cor(cores)
            else:
                cor2=cor1
        if bg_randomico:
            bg=cor(cores_bg,cor1)
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
        
        restore()

# grid
if grid:
    fill(None)
    stroke(0)
    for i in range(faixas):
        if i:
            line((fw*i,0),(fw*i,ph))

# # # # salvar
# m_str=str(m)
# if len(m_str)==1:
#      m_str='00'+m_str
# elif len(m_str)==2:
#      m_str='0'+m_str
# painel='seta'
# nome=os.path.join(path,'img/painel/2/seta-%s.pdf' % m_str)
# path_save=os.path.join( path,nome )
# saveImage(path_save, multipage=False)
# print('gif salvo >>>')
# print(path_save)


##########################################################

end = time.time()
print('\n>>>', end-start, 's')
