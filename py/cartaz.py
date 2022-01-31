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

# imagens
path_img = os.path.join(path,'img/cartaz')
img_lista = [img for img in os.listdir(path_img) if img[0] not in ['.','_']]
img_lista.sort()
imgs=['?']+img_lista

# cria pasta drawbot
path_drawbot=os.path.join(path_img,'_drawbot')
if not os.path.isdir(path_drawbot):
    os.mkdir(path_drawbot)

alinhamentos=[
    '?',
    '1_centralizado',
    '2_esquerda',
    '3_direita',
    '4_randomico',
    ]


Variable([
    dict(name="w_cm", ui="EditText", args=dict(text='42')),
    dict(name="h_cm", ui="EditText", args=dict(text='59.4')),
    dict(name="margem_sup_cm", ui="EditText", args=dict(text='5')),
    dict(name="margem_inf_cm", ui="EditText", args=dict(text='5')),
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="n_modulos", ui="EditText", args=dict(text='')),
    dict(name="zoom", ui="EditText", args=dict(text='1.6')),
    dict(name="alinha", ui="PopUpButton", args=dict(items=alinhamentos)),
], globals())
    
alinha=var(alinha,lista=alinhamentos,tipo='lista')

n=var(n_modulos,6,tipo='int')
e=var(zoom,1.4,tipo='float')

# margem
m_sup=var(margem_sup_cm,tipo='float')*cm
m_inf=var(margem_inf_cm,tipo='float')*cm

#painel
pw=var(w_cm,42,tipo='float')*cm
ph=var(h_cm,59.4,tipo='float')*cm

w=pw
h=ph-m_sup-m_inf

# imagem
img=var(img,lista=imgs)

print('modulos =', n)
print()
print('img =', img)

img=os.path.join(path_img,img)
imgw,imgh=imageSize(img)

# escala
e0=pw/imgw

# modulos
mh=h/n
mw=w


size(pw,ph)


imgs_path=[]
for i in range(n):
    ei=e**i

    translate(0,m_inf)
    save()
    translate(0,h-(i+1)*mh)
    iw=imgw*e0*ei
    ih=imgh*e0*ei
    if alinha == 1:
        x=(mw-iw)/2
    if alinha == 2:
        x=0
    if alinha == 3:
        x=mw-iw
    if alinha == 4:
        x=-randint(0,int(iw-mw))
    y=(mh-ih)/2
    translate(x,y)
    scale(e0*ei)
    image(img,(0,0))
    restore()

    mascara=BezierPath()
    mascara.rect(0,-m_inf,w,ph)
    mascara.rect(0,h-i*mh,mw,-mh)
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
