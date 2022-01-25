import time
start = time.time()

import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
# 1 inch = 2.54 cm
# cm = dpi/2.54
# cm = 72/2.54
cm = 36/2.54
mm = cm*10

def playmode(pontos,layer,c=0):
    desenho=BezierPath()
    car_c=0
    for linha in pontos:
        for pt in linha:
            if pt[0] in layer:
                desenho,car_c=pixel(pt,m,car_c,desenho,base,texto)
    cor=dgd(cor1,cor2,c,len(ordem)-1)
    fill(*cor)
    stroke(None)
    drawPath(desenho)

def formas(caracteres):
    base={}
    # formas geometricas
    car_lista=['#','o','t','+','x','X',]
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
        elif c == 'X':
            c='xis2'
            n=3
            bezier.polygon((x,y),(x+m/n,y),(x+m,y+m),(x+m-m/n,y+m))
            bezier.polygon((x+m-m/n,y),(x+m,y),(x+m/n,y+m),(x,y+m),)
        elif c == 'x':
            c='xis'
            n=4
            bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
            bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
        base[c]=bezier
    # caracteres
    for c in caracteres:
        bezier=BezierPath()
        bezier.textBox(c, (-m/2,-m+fs-m,2*m,2*m), font=fonte_px, fontSize=fs, align='center',)
        base[c]=bezier
    return base

###############################


# imagens
path_img = os.path.join(path,'img/1')
img_lista = [img for img in os.listdir(path_img) if img[0]!='.']
img_lista.sort()
imgs=['?']+img_lista

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
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="fonte_pixel", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="texto", ui="PopUpButton", args=dict(items=tipos_txt)),
], globals())
    

# fonte pixel
fonte_px=var(fonte_pixel,lista=fontes_do_pc)

contraste=1.1 #numero decimal entre 1 e 3
brilho=0 #numero decimal entre -1 e 1

# imagem
img=var(img,lista=imgs)
print('img =', img)
img=os.path.join(path_img,img)
imgw,imgh=imageSize(img)

#caracteres
caracteres='PLAYMODE'

#formas geometricas
px_lista=['quadrado','circulo','triangulo','xis']

texto=var(texto,lista=tipos_txt,tipo='indice')
if texto>1 and caracteres:
    if texto==4:
        px_lista.append(caracteres)
    else:
        px_lista+=caracteres.split(' ')
else:
    px_lista+=[car for car in caracteres]

cor1=(0,)
cor2=(0,)
bg=None

#banner
pw=230*cm
ph=312*cm


##############################################
##############################################
##############################################

# redefine variaveis
#img='' #'nome da imagem entre aspas'
#modulo=20 #numero inteiro
#costraste=0 #numero decimal entre 1 e 3
#brilho=0 #numero decimal entre -1 e 1
#cor=(0,0,0) #(0-1,0-1,0-1)
# fonte_px=15 #numero inteiro

##############################################
##############################################
##############################################



img=ImageObject(img)
img.colorMonochrome(color=(1,1,1,1), intensity=None)
img.colorControls(saturation=None, brightness=brilho, contrast=contraste)


ordem=px_lista+['']
print('ordem =',ordem)

newPage(pw,ph)

# barra de logos
translate(0,ph/10)

#marge
margem=6*cm
translate(margem,0)

modulos_ordem=[5,10,20,30,50,110]
colunas=2
modulos=[]
modulos_ordem.reverse()
for i in range(colunas):
    modulos.append([])
    for j in range(i,len(modulos_ordem),colunas):
        modulos[i].append(modulos_ordem[j])
modulos.reverse()
print(modulos)

largura=(pw-2*margem)/colunas

for lista in modulos:
    save()
    for m in lista:
        save()
        fs=m

        # cria dicionario com formas basicas formas basicas
        base=formas(caracteres)

        # ponto central do modulo para verificacao da cor
        p0=round(m/2)

        # lista pontos da vertical e horizontal
        pontos_y=list(range(p0,imgh,m))
        pontos_x=list(range(p0,imgw,m))
        # inverte a lista vertical para desenha de cima para baixo
        pontos_y.reverse()

        # dimensoes
        iw=len(pontos_x)*m
        ih=len(pontos_y)*m

        # e=ph/(3*ih)
        e=largura/iw


        scale(e)

        if bg:
            fill(*bg)
            rect(0,0,pw,ph)


        translate(-p0,-p0)
        pontos=[]
        for j,y in enumerate(pontos_y):
            pontos.append([])
            for i,x in enumerate(pontos_x):
                cinza=imagePixelColor(img,(x,y))
                car=int(cinza[0]//(1/len(ordem)))
                if car==len(ordem):
                    car=len(ordem)-1
                car=ordem[car]
                pontos[j]+=[[car,x,y,i,j],]

        for c,camada in enumerate(ordem[:-1]):
            playmode(pontos,[camada,],c)
        restore()
        translate(0,ih*e)
    restore()
    translate(largura,0)

# # # # para salvar antere o valor de n e descomente as linhas abaixo
# m_str=str(m)
# if len(m_str)==1:
#      m_str='00'+m_str
# elif len(m_str)==2:
#      m_str='0'+m_str
# gif=6
# nome="gif/%s/%s_m-%s.pdf" % (gif,img_nome.split('.')[0],m_str)
# path_save=os.path.join( path,nome )
# saveImage(path_save, multipage=False)
# print('gif salvo >>>')
# print(path_save)


print('imgw =', imgw, 'px')
print('imgh =', imgh, 'px')
print('contraste =', round(contraste,2))
print('brilho =', round(brilho,2))
print('fonte_pixel =', fonte_px)
print('fonte_size =', fs)
print('cor1 =', cor1)
print('cor2 =', cor2)
print('bg =', bg)
print('modulo =', m, 'px')
print('texto =', tipos_txt[texto])


end = time.time()
print('\n>>>', end-start, 's')
