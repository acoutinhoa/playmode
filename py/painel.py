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

# painel
painel=1

# medidas em cm
if painel == 1:
    pw=25*cm
    ph=19*cm

# ajuste
p0x=-pw
p0y=0

###############################

# imagens
path_img = os.path.join(path,'img/painel/%s' % painel)
img_lista = [img for img in os.listdir(path_img) if img[0] not in ['.','_']]
img_lista.sort()
imgs=['?']+img_lista+['-']

# cria pasta drawbot
path_drawbot=os.path.join(path,'img/painel/_drawbot')
if not os.path.isdir(path_drawbot):
    os.mkdir(path_drawbot)

tipos=[
    '?',
    '1_vertical',
    '2_horizontal',
    '3_quadrado',
    ]


Variable([
    dict(name="img1", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="img2", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="img3", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="img4", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="img5", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="img6", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="n_modulos", ui="EditText", args=dict(text='')),
    dict(name="tipo", ui="PopUpButton", args=dict(items=tipos)),
], globals())
    
#modulo
tipo=var(tipo,1,lista=tipos,tipo='lista')

# imagem
if painel == 1:
    n=var(n_modulos,15,tipo='int')
    
    img1=var(img1,lista=imgs)
    img2=var(img2,lista=imgs)
    img3=var(img3,lista=imgs)
    img4=var(img4,lista=imgs)
    img5=var(img5,lista=imgs)
    img6=var(img6,lista=imgs)

elif painel == 2:
    # tamanho a partir da imagem
    p_img=os.path.join(path_img,imgs[-2])
    pw,ph=imageSize(p_img)

    n=var(n_modulos,15,tipo='int')
    
    img1=var(img1,imgs[1],lista=imgs)
    img2=var(img2,imgs[-1],lista=imgs)
    img3=var(img3,imgs[3],lista=imgs)
    img4=var(img4,imgs[-1],lista=imgs)
    img5=var(img5,imgs[5],lista=imgs)
    img6=var(img6,imgs[-1],lista=imgs)

print('modulos =', n)
print()
print('img1 =', img1)
print('img2 =', img2)
print('img3 =', img3)
print('img4 =', img4)
print('img5 =', img5)
print('img6 =', img6)

imgs=[img1,img2,img3,img4,img5,img6]
while '-' in imgs:
    imgs.remove('-')

imgs_path=[]

ordem=[]
vezes=len(imgs)-1
if tipo == 3:
    mw=pw/n
    nh=round(ph/mw)
    mh=ph/nh
    
    for j in range(nh):
        ordem.append([])
        for i in range(n):
            ordem[j].append(randint(0,vezes))
else:
    if tipo == 1:
        mw=pw/n
    elif tipo == 2:
        mh=ph/n
        
    for i in range(n):
        ordem.append(randint(0,vezes))


size(pw,ph)

for i,img in enumerate(imgs):
    img=os.path.join(path_img,img)
    imgw,imgh=imageSize(img)
    # #imagem centralizada
    # image(img,((pw-imgw)/2,(ph-imgh)/2))
    #imagem alinhada 0,0
    image(img,(p0x,p0y))

    mascara=BezierPath()
    mascara.rect(0,0,pw,ph)
    
    if tipo == 1:
        for j,modulo in enumerate(ordem):
            if modulo == i:
                mascara.rect((j+1)*mw,0,-mw,ph)
    elif tipo == 2:
        for j,modulo in enumerate(ordem):
            if modulo == i:
                mascara.rect(0,(j+1)*mh,pw,-mh)
    elif tipo == 3:
        for j,linha in enumerate(ordem):
            for m,modulo in enumerate(linha):
                if modulo == i:
                    mascara.rect(m*mw,(j+1)*mh,mw,-mh)

    mascara.removeOverlap()
    fill(1)
    drawPath(mascara)

    # salva
    nome="img-%s.pdf" % i
    path_save=os.path.join( path_drawbot,nome )
    saveImage(path_save, multipage=False)
    imgs_path.append(path_save)
    
    newDrawing()
    size(pw,ph)

# junta tudo
blendMode("multiply")

for i,img in enumerate(imgs_path):
    image(img,(0,0))
    

end = time.time()
print('\n>>>', end-start, 's')
