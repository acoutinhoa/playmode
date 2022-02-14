import time
start = time.time()

##########################################################
import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

##########################################################

tipo_i=0
img_i=2

##########################################################

def cria_pasta(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print('>>> pasta criada \n>>>',path)

tipo=[
    ('entrada',19), #0
    ('cortina',9), #1
]

nome,n=tipo[tipo_i]

# imagens
path_img = os.path.join(path,'img/painel/%s' % nome)
img_lista = [img for img in os.listdir(path_img) if img[0]!='.']
img_lista.sort()

# texto
path_txt = os.path.join(path,'img/txt/%s' % nome)
cria_pasta(path_txt)


img=img_lista[img_i]

path_fx = os.path.join(path_txt,img.split('.')[0])

if os.path.isdir(path_fx):
    print('pasta ok')

else:
    cria_pasta(path_fx)

    img = os.path.join(path_img,img)
    
    pw,ph=imageSize(img)
    fw=pw/n

    for i in range(n):
        newPage(fw,ph)

        im=ImageObject()
        with im:
            size(fw,ph)
            image(img,(-i*fw,0))

        image(im,(0,0))
        
        # save
        path_save = os.path.join(path_fx,'%s.pdf' % str(i))
        saveImage(path_save, multipage=False)        


##########################################################

end = time.time()
print('\n>>>', end-start, 's')
