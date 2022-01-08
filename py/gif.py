import time
start = time.time()

import os

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])


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
path_gif = path+'/gif/'
gif_lista = os.listdir(path_gif)
x=[]
for i in gif_lista:
    if os.path.isdir(path_gif+i):
        x.append(i)
gif_lista=x
        
# gif_lista=deleta('.DS_Store',gif_lista)
gif_lista.sort()
gifs=['-']+gif_lista


Variable([
    dict(name="gif", ui="PopUpButton", args=dict(items=gifs)),
    dict(name="frame_time", ui="EditText", args=dict(text='4')),
], globals())
    
s=var(frame_time,tipo='numero')
s=s/10

gif=var(gif,lista=gifs)
path_gif+='%s/'%gif
img_lista=os.listdir(path_gif)
img_lista=deleta('.DS_Store',img_lista)
img_lista.sort()
img_lista.reverse()
print(gif)

for img in img_lista:
    print(img)
    img_path=path_gif+img
    imgw,imgh=imageSize(img_path)
    if gif in ['3','4','5','6']:
        newPage(1500,1000)
        translate( ( width()-imgw ) /2, ( height()-imgh ) /2 )
    else:
        newPage(imgw,imgh)
    frameDuration(s)
    image(img_path,(0,0))


# # # para salvar antere o valor de n e descomente as linhas abaixo
# path_save=path + "/gif/gif%s_f-%s.mp4" % (gif,s)
# saveImage(path_save)
# print('gif salve >>>')
# print(path_save)


end = time.time()
print('\n>>>', end-start, 's')

