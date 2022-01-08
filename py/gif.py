import time
start = time.time()

import os

# caminho da pasta do playmode
pasta=os.path.dirname(os.getcwd())
# path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])+'/'

def deleta(item,lista):
    if item in lista:
        lista.remove(item)
    return lista

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
path_gif = os.path.join(pasta, 'gif')
os.chdir(path_gif)
gif_lista = sorted(filter(os.path.isdir, os.listdir('.')))

# gif_lista = os.listdir(path_gif)
# # somente pastas
# x=[]
# for i in gif_lista:
#     if os.path.isdir(path_gif+i):
#         x.append(i)
# gif_lista=x
# # gif_lista=deleta('.DS_Store',gif_lista)
# gif_lista.sort()

gifs=['-','ps']+gif_lista


Variable([
    dict(name="gif", ui="PopUpButton", args=dict(items=gifs)),
    dict(name="frame_time", ui="EditText", args=dict(text='4')),
    dict(name="inverte_ordem", ui="CheckBox", args=dict(value=False)),
], globals())
    
s=var(frame_time,tipo='numero')
s=s/10

gif=var(gif,lista=gifs)
if gif == 'ps':
    path_gif=os.path.join(pasta, gif)
    path_pdf=os.path.join(pasta, 'pdf/0')
else:
    path_gif=os.path.join(path_gif, gif)

print(path_gif,'\n')
# os.chdir(path_gif)
# img_lista = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)

img_lista=deleta('.DS_Store',img_lista)

img_lista=os.listdir(path_gif)
img_lista.sort()

if gif == 'ps':
    # os.chdir(path_pdf)
    # pdf_lista = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)

    pdf_lista=os.listdir(path_gif)
    pdf_lista=deleta('.DS_Store',img_lista)
    pdf_lista.sort()
    
if inverte_ordem:
    img_lista.reverse()

imgw,imgh=0,0
pw,ph=0,0
for img in img_lista:
    print(img)
    img_path= os.path.join(path_gif,img)
    imgw,imgh=imageSize(img_path)
    if gif in ['3','4','5','6']:
        newPage(1500,1000)
        translate( ( width()-imgw ) /2, ( height()-imgh ) /2 )
    else:
        if imgw<pw or imgh<ph:
            newPage(pw,ph)
            # image(img2,(0,0))
            rect(0,0,width(),height())
            translate( ( width()-imgw ) /2, ( height()-imgh ) /2 )
        else:
            newPage(imgw,imgh)
            pw,ph=imgw,imgh
            img2=img_path
    frameDuration(s)
    image(img_path,(0,0))


# # # para salvar antere o valor de n e descomente as linhas abaixo
# path_save=os.path.join(pasta,'gif/gif_%s_%ss.mp4' % (gif,s))
# saveImage(path_save)
# print('\ngif salvo >>>')
# print(path_save)


end = time.time()
print('\n>>>', end-start, 's')

