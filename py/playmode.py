import time
start = time.time()

import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])


def playmode(vezes,pontos,layer,c=0,ajuste_txt=0):
    for n in range(vezes):
        desenho=BezierPath()
        car_c=0
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
            cor=dgd(cor1,cor2,c,len(ordem)-1)
            if n==0:
                fill(*cor)
                stroke(None)
            elif n==1:
                fill(None)
                stroke(*cor)
            drawPath(desenho)

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

###############################


# imagens
path_img = os.path.join(path,'img/1')
# crias pasta 1
if not os.path.isdir(path_img):
    os.mkdir(path_img)
    print('>>> pasta criada \n>>>',path_img)

img_lista = [img for img in os.listdir(path_img) if img[0]!='.']
img_lista.sort()
imgs=['?']+img_lista

# visualizar
opcoes = [
    '0_textura',
    '1_imagem',
    '2_grayscale',
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

# tipos
# tipos=[
#     '0_todas imagens',
#     ]

Variable([
    # dict(name="filtro", ui="PopUpButton", args=dict(items=tipos)),
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="ver", ui="PopUpButton", args=dict(items=opcoes)),
    dict(name="modulo", ui="EditText", args=dict(text='30')),
    dict(name="contraste", ui="Slider", args=dict(value=1, minValue=1, maxValue=3)),
    dict(name="brilho", ui="Slider", args=dict(value=0, minValue=-1, maxValue=1)),
    dict(name="inverte_cores", ui="CheckBox", args=dict(value=False)),
    dict(name="com_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="caracteres", ui="EditText", args=dict(text='PLAYMODE')),
    dict(name="fonte_pixel", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="texto", ui="PopUpButton", args=dict(items=tipos_txt)),
    dict(name="ajuste_texto", ui="Slider", args=dict(value=0, minValue=-10, maxValue=10)),
    # dict(name="fonte_size", ui="EditText", args=dict(text='')),
    dict(name="quadrado", ui="CheckBox", args=dict(value=True)),
    dict(name="circulo", ui="CheckBox", args=dict(value=True)),
    dict(name="triangulo", ui="CheckBox", args=dict(value=True)),
    dict(name="xis", ui="CheckBox", args=dict(value=True)),
    dict(name="cor1", ui="EditText", args=dict(text='0')),
    dict(name="cor2", ui="EditText", args=dict(text='0')),
    dict(name="degrade", ui="CheckBox", args=dict(value=True)),
    dict(name="bg", ui="EditText", args=dict(text='100 100 100')),
], globals())
    

m=var(modulo,randint(5,50),tipo='int')
# m=int(m)

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

cor1=var(cor1,tipo='cor')
cor2=var(cor2,tipo='cor')
bg=var(bg,tipo='cor')

# imagem
# if not img:
#     if filtro == 1:
#         imgs=[]
img=var(img,lista=imgs)
print('img =', img)
img=os.path.join(path_img,img)
imgw,imgh=imageSize(img)

# fonte pixel
fonte_px=var(fonte_pixel,lista=fontes_do_pc)
# fs=var(fonte_size,m,tipo='float')

#caracteres
texto=var(texto,lista=tipos_txt,tipo='lista')
ajuste_txt=round(ajuste_texto)

if texto>1 and caracteres:
    if texto==4:
        px_lista.append(caracteres)
    else:
        px_lista+=caracteres.split(' ')
else:
    px_lista+=[car for car in caracteres]


##############################################
##############################################
##############################################

# redefine variaveis
#img='' #'nome da imagem entre aspas'
#modulo=20 #numero inteiro
#costraste=0 #numero decimal entre 1 e 3
#brilho=0 #numero decimal entre -1 e 1
#fonte_px=15 #numero inteiro
#cor1=(0,0,0) #(0-1,0-1,0-1)
#cor2=(0,0,0) #(0-1,0-1,0-1)
#bg=(0,0,0) #(0-1,0-1,0-1)

##############################################
##############################################
##############################################


print('imgw =', imgw, 'px')
print('imgh =', imgh, 'px')
print('contraste =', round(contraste,2))
print('brilho =', round(brilho,2))
print('fonte_pixel =', fonte_px)
# print('fonte_size =', fs)
print('cor1 =', cor1)
print('cor2 =', cor2)
print('bg =', bg)
print('modulo =', m, 'px')
print('texto =', tipos_txt[texto])


img=ImageObject(img)
img.colorMonochrome(color=(1,1,1,1), intensity=None)
img.colorControls(saturation=None, brightness=brilho, contrast=contraste)
if inverte_cores:
    img.colorInvert()


# gerar varias paginas para fazer o gif
# pgs = lista de valores de modulo para cada pagina
pgs=[]
# pgs=list(range(15,101,5))+list(range(3,12))+[13,17]
# pgs=list(range(20,81,10))+list(range(3,12))+[13,17,140,120,100]+list(range(15,50,10))
if not pgs:
    pgs=[m,]


for pg in pgs:
    m=pg

    # ponto central do modulo para verificacao da cor
    p0=round(m/2)

    # lista pontos da vertical e horizontal
    pontos_y=list(range(p0,imgh,m))
    pontos_x=list(range(p0,imgw,m))
    # inverte a lista vertical para desenha de cima para baixo
    pontos_y.reverse()

    # pagina
    pw=len(pontos_x)*m
    ph=len(pontos_y)*m

    # if filtro==1:
    #     ah=(pw-ph)/2
    #     ph=pw
    
    # cria dicionario com formas basicas formas basicas
    base=formas(caracteres,m,fonte=fonte_px)

    newPage(pw,ph)
    sw=m/10
    strokeWidth(sw)
    miterLimit(sw)
    # lineJoin("bevel")
    # lineCap("square")

    if bg:
        fill(*bg)
        rect(0,0,pw,ph)
    # if filtro==1:
    #     translate(0,ah)
    if ver==1:
        image(img,(0,0))

    else:
        translate(-p0,-p0)
        
        if com_linha:
            vezes=2
            px_lista2=[px+'_' for px in px_lista]
            px_lista2.reverse()
            ordem=px_lista+px_lista2+['']
        else:
            vezes=1
            ordem=px_lista+['']
        print('ordem =',ordem)
        
        pontos=[]
        for j,y in enumerate(pontos_y):
            for i,x in enumerate(pontos_x):
                cinza=imagePixelColor(img,(x,y))
                if ver==2:
                    fill(*cinza)
                    rect(x,y,m,m)
                else:
                    car=int(cinza[0]//(1/len(ordem)))
                    if car==len(ordem):
                        car=len(ordem)-1
                    car=ordem[car]
                    pontos.append([car,x,y,i,j])

        if degrade:
            for c,camada in enumerate(ordem[:-1]):
                playmode(vezes,pontos,[camada,],c,ajuste_txt)
        else:
            playmode(vezes,pontos,ordem,ajuste_txt)

    # # # # salvar
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

end = time.time()
print('\n>>>', end-start, 's')
