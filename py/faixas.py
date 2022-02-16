import time
start = time.time()

##########################################################
import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

##########################################################

tipo_i=1
img_i=4

##########################################################

def cria_pasta(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print('>>> pasta criada \n>>>',path)

tipo=[
    ('entrada',19), #0
    ('cortina',8), #1
]

nome,n=tipo[tipo_i]

# imagens
path_img = os.path.join(path,'img/painel/%s' % nome)
img_lista = [img for img in os.listdir(path_img) if img[0]not in ['.','_']]
img_lista.sort()

# expo
path_expo = os.path.join(path,'img/expo/%s' % nome)
cria_pasta(path_expo)


img=img_lista[img_i]

path_fx = os.path.join(path_expo,img.split('.')[0])
path_fx_ = os.path.join(path_expo,'_'+img.split('.')[0])

if os.path.isdir(path_fx) or os.path.isdir(path_fx_):
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
