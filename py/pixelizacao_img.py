import os
from base import var

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# imagens
path_img = os.path.join(path,'img/pixelizacao')
img_lista = [img for img in os.listdir(path_img) if img[0]!='.']
img_lista.sort()
imgs=['?']+img_lista


Variable([
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="escala", ui="Slider", args=dict(value=10, minValue=1, maxValue=100)),
], globals())

# imagem
img=var(img,lista=imgs)
print('img =', img)
img=os.path.join(path_img,img)
imgw,imgh=imageSize(img)

pw=imgw
ph=imgh

e=escala
print(e)


newPage(pw, ph)

im = ImageObject()
with im:
    size(pw/e,ph/e)
    scale(1/e)
    image(img, (0,0))

scale(e)
image(im, (0,0))


# ##########################################
# # pra salvar outras imagens:
# # mudar o valor de n
# ##########################################

# n=1
# path_img=path + '/img/1/banner_%s.png' % (n)
# saveImage(path_img)
# print('img salva >>>')
# print(path_img)

            
    