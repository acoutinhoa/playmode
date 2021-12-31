
import os
# fonte
from fontes import font
from base import pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidade
cm=72/2.54
mm=cm/10

px_lista=['#','o','t','x']
 
def redefine(pattern):
    for j,y in enumerate(pattern):
        linha=''
        for i,x in enumerate(y):
            if x == '#':
                if tipo_px == 2:
                    x='o'
                elif tipo_px == 3:
                    x='t'
                elif tipo_px == 4:
                    x='x'
                else:
                    x=choice(px_lista)
            linha+=x
        pattern[j]=linha
    return pattern


def letra(car,layer=px_lista):
    desenho=BezierPath()
    for j,y in enumerate(car):
        for i,x in enumerate(y):
            if x in layer:
                desenho = pixel(x,desenho,i,j,m)
    
    desenho.removeOverlap()
    w=(i+1)*m
    h=(j+1)*m
    return desenho,w,h
    
def def_cor(cor,tipo='fill'):
    if tipo == 'stroke':
        if not cor:
            if cor_mode==0:
                stroke(None)
            if cor_mode==1:
                cmykStroke(None)
        else:
            if cor_mode==0:
                stroke(*cor)
            if cor_mode==1:
                cmykStroke(*cor)
    elif tipo == 'fill':
        if not cor:
            if cor_mode==0:
                fill(None)
            if cor_mode==1:
                cmykFill(None)
        else:
            if cor_mode==0:
                fill(*cor)
            if cor_mode==1:
                cmykFill(*cor)

def dgd(cor1,cor2,p,repete):
    c=()
    for nc in range(len(cor1)):
        c1=cor1[nc]
        c2=cor2[nc]
        if c1 == c2:
            c3=c1
        else:
            if repete-1 == 0:
                c3=c2
            else:
                c3=c1-((c1-c2)/(repete-1))*p
        c+=(c3,)
    return c

def var(v,v0=0,lista=[],tipo='',):
    if not v:
        if not v0:
            if lista:
                v=choice(lista[1:])
            elif tipo=='numero':
                v=randint(0,1)
            elif tipo=='cor':
                v=()
                for i in range(3):
                    v+=(randint(0,1),)
        else:
            if v0=='none':
                v=None
            else:
                v=v0
    else:
        if lista:
            v=lista[v]
        elif tipo=='numero':
            v=float(v)
        elif tipo=='cor':
            if v == 'none':
                v=None
            else:
                v_=v.split()
                v=()
                for i in v_:
                    v+=(int(i)/100,)
    if tipo == 'cor' and v:
        if cor_mode == 0:
            n=3
        elif cor_mode == 1:
            n=4
        for i in range(n-len(v)):
            v+=(0,)
    return v


###############################


# imagens
path_img = path+'/img/0/'
imgs=['?']+os.listdir(path_img)

# visualizar
opcoes = [
    '0_textura',
    '1_imagem',
    '2_grayscale',
    ]

# # fontes
# fontes=['👀']+[n for n in font.keys()]


Variable([
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="modulo", ui="EditText", args=dict(text='20')),
    # dict(name="contraste", ui="Slider", args=dict(value=1, minValue=1, maxValue=3)),
    # dict(name="brilho", ui="Slider", args=dict(value=0, minValue=-1, maxValue=1)),
    # dict(name="cor", ui="EditText", args=dict(text='')),
    # dict(name="ver", ui="PopUpButton", args=dict(items=opcoes)),
    # dict(name="com_linha", ui="CheckBox", args=dict(value=False)),
    # dict(name="fonte", ui="PopUpButton", args=dict(items=fontes)),
], globals())
    

m=var(modulo,randint(5,50),tipo='numero')
m=int(m)

# cor_mode=0
# cor=var(cor,(0,),tipo='cor')
# print(cor)

# imagem
img=var(img,lista=imgs)
print('img =', img)
img=path_img+img
imgw,imgh=imageSize(img)

img=ImageObject(img)
# img.colorControls(saturation=None, brightness=brilho, contrast=contraste)

# # fonte
# fonte=var(fonte,fontes[3],lista=fontes)

print('imgw =', imgw, 'px')
print('imgh =', imgh, 'px')
print()
print('modulo =', m, 'px')
# print('fonte =', fonte)



newPage(imgw,imgh)
strokeWidth(m/10)
miterLimit(m/10)
# lineJoin("bevel")
# lineCap("square")





# if ver==1:
#     image(img,(0,0))

# else:
#     if com_linha:
#         n=2
#         px_atsil=px_lista.copy()
#         px_atsil.reverse()
#         ordem=px_lista+px_atsil+['-']
#     else:
#         n=1
#         ordem=px_lista+['-']
#     print('ordem =',ordem)
    
#     for n in range(n):
#         desenho=BezierPath()
        
#         for j in range(0,imgh,m):
#             for i in range(0,imgw,m):
#                 cor_px=imagePixelColor(img,(i,j))
#                 cinza=(cor_px[0]+cor_px[1]+cor_px[2])/3
            
#                 if ver==2:
#                     fill(cinza)
#                     rect(i,j,m,m)
#                 else:
#                     c=int(cinza//(1/len(ordem)))
#                     if c==len(ordem):
#                         c=len(ordem)-1
#                     car=ordem[c]
                    
#                     if com_linha:
#                         if n==0 and c<4:
#                             desenho=pixel(car,desenho,i,j,m)
#                         elif n==1 and c>=4:
#                             desenho=pixel(car,desenho,i,j,m)
#                     else:
#                         desenho=pixel(car,desenho,i,j,m)
#         if n==1 and com_linha:
#             desenho.removeOverlap()
        
#         if ver==0:
#             if n==0:
#                 fill(*cor)
#                 stroke(None)
#                 drawPath(desenho)
#             elif n==1:
#                 fill(None)
#                 stroke(*cor)
#                 drawPath(desenho)

