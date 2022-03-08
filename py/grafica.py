import time
start = time.time()

##########################################################
import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

##########################################################

# unidades
cm = 72/2.54
mm = cm/10

##########################################################

def cria_pasta(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print('>>> pasta criada \n>>>',path)

def barra(d=1*cm,m=3*cm,y=0,n=3,fundo=True,info=''):
    dist=(pw-2*m)/(n-1)
    
    save()        
    translate(0,y)

    if fundo:
        cmykFill(0,0,0,0)
        cmykStroke(0,0,0,1)
        rect(0,0,pw,d)
    
    #info
    save()
    cmykFill(0,0,0,1)
    cmykStroke(None)

    txt=FormattedString()
    txt.append(info.upper(),font='Helvetica-Bold',fontSize=d*.8)
    
    t=BezierPath()
    t.text(txt,(m+2*cm,d*.2))
    drawPath(t)
    restore()

    translate(m,0)
    for i in range(n):
        save()
        translate(-d/2,0)
        oval(0,0,d,d)
        line((0,d/2),(d,d/2))
        line((d/2,0),(d/2,d))
        restore()
        translate(dist,0)
    restore()

##########################################################

tipos=[
    'obrascr',
    'obras-duplo',
    # ('entrada',19), #0
    # ('cortina',8), #1
]

Variable([
    dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
    dict(name = "ver", ui = "EditText", args = dict(text = '')),
    dict(name = "ilhos_cm", ui = "EditText", args = dict(text = '1')),
    dict(name = "salvar", ui = "CheckBox", args = dict(value = False)),
], globals())

ilhos=float(ilhos_cm)*cm

# obras
if tipo in [0,1]:
    # img
    path_img = os.path.join(path,'pdf/grafica/0/obras/txt')
    img_lista = [img for img in os.listdir(path_img) if img[0] not in ['.','_']]

    #imagens
    imagens={}
    for img in img_lista:
        nome=img.split('.')[0]
        nome=nome.split('-')
        lang=nome.pop(2)
        nome='-'.join(nome)
        if nome not in imagens:
            imagens[nome]={}
        imagens[nome][lang]= os.path.join(path_img,img)
    
    if ver:
        info=imagens[ver]
        imagens={}
        imagens[ver]=info
    
    print(imagens)
    for obra in imagens:
        pt=imagens[obra]['pt']
        en=imagens[obra]['en']
        
        ptw,pth=imageSize(pt)
        enw,enh=imageSize(en)
        
        pw=ptw
        if tipo==0:
            ph=pth+enh
        elif tipo==1:
            ph=(pth+enh)*2+ilhos
            
        newPage(pw,ph)
        
        save()
        if tipo==1:
            translate(0,pth+ilhos/2)
                    
        image(pt,(0,0))
        
        save()
        translate(pw,pth+enh)
        scale(-1,-1)
        image(en,(0,0))
        restore()

        #ilhos
        info='%s-%s' % (tipos[tipo],obra)
        
        #centro
        barra(d=ilhos, m=3*cm, y=pth-ilhos/2, n=3, fundo=True, info=info)
        restore()
        
        if tipo==1:
            #barra1
            barra(d=ilhos, m=3*cm, y=0, n=3, fundo=True, info=info)
            #barra2
            barra(d=ilhos, m=3*cm, y=ph-ilhos, n=3, fundo=True, info=info)
        
        if salvar:
            nome='pdf/grafica/1/%s/playmode_%s-%s_%scm-%scm.pdf' % ('obras',tipos[tipo],obra,round(pw/cm,1),round(ph/cm,1))
            
            

##########################################################

if salvar:
    path_save=os.path.join( path,nome )
    saveImage(path_save, multipage=False)
    print('salvo', randint(2,19)*choice(['>','=']))
    print(path_save)

##########################################################



# nome,n=tipo[tipo_i]

# # imagens
# path_img = os.path.join(path,'img/painel/%s' % nome)
# img_lista = [img for img in os.listdir(path_img) if img[0]not in ['.','_']]
# img_lista.sort()

# # grafica
# path_grafica = os.path.join(path,'pdf/_grafica/%s' % nome)
# cria_pasta(path_grafica)


# img=img_lista[img_i]

# path_fx = os.path.join(path_grafica,img.split('.')[0])
# path_fx_ = os.path.join(path_grafica,'_'+img.split('.')[0])

# if os.path.isdir(path_fx) or os.path.isdir(path_fx_):
#     print('pasta ok')

# else:
#     cria_pasta(path_fx)

#     img = os.path.join(path_img,img)
    
#     pw,ph=imageSize(img)
#     fw=pw/n

#     for i in range(n):
#         newPage(fw,ph-250)

#         # im=ImageObject()
#         # with im:
#         #     size(fw,ph)
#         image(img,(-i*fw,0))

#         # image(im,(0,0))
        
#         # save
#         path_save = os.path.join(path_fx,'%s.pdf' % str(i))
#         saveImage(path_save, multipage=False)        


##########################################################

end = time.time()
print('\n>>>', end-start, 's')
