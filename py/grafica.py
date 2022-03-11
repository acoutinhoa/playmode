import time
start = time.time()

##########################################################
import os
from random import shuffle
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

def barra(d=1*cm,m=3*cm,y=0,n=3,fundo=True,info='',outline=True):
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
    
    if outline:
        t=BezierPath()
        t.text(txt,(m+2*cm,d*.2))
        drawPath(t)
    else:
        text(txt,(m+2*cm,d*.2))
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

def save_file(nome):
    path_save=os.path.join( path,nome )
    saveImage(path_save, multipage=False)
    print('salvo', randint(2,19)*choice(['>','=']))
    print(path_save)

##########################################################

tipos=[
    'janelas',
    'entrada',
    'portas',
    'obras',
    'obras-duplo',
    'barra',
    # ('entrada',19), #0
    # ('cortina',8), #1
]

Variable([
    dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
    dict(name = "faixas", ui = "CheckBox", args = dict(value = False)),
    dict(name = "ver", ui = "EditText", args = dict(text = '')),
    dict(name = "ilhos_cm", ui = "EditText", args = dict(text = '1')),
    dict(name = "salvar", ui = "CheckBox", args = dict(value = False)),
], globals())

tipo=tipos[tipo]
ilhos=float(ilhos_cm)*cm
costura=6*cm

if tipo == 'barra':
    for w in [70,80]:
        pw=w*cm
        newPage(pw,ilhos)
        barra(d=ilhos, m=3*cm, y=0, n=5, fundo=True, info='painel-%s'%w,outline=False)

else:
    if tipo in ['obras','obras-duplo',]:
        path_img = os.path.join(path,'pdf/grafica/0/obras/1')
    else:
        if faixas:
            path_img = os.path.join(path,'pdf/grafica/0/%s/0' % tipo)
        else:
            path_img = os.path.join(path,'pdf/grafica/0/%s/1' % tipo)

    #imagens
    img_lista = [img for img in os.listdir(path_img) if img[0] not in ['.','_']]
    imagens={}
    for img in img_lista:
        nome=img.split('.')[0]
        nome=nome.split('-')
        lado=nome.pop(-1)
        nome='-'.join(nome)
        if nome not in imagens:
            imagens[nome]={}
        imagens[nome][lado]= os.path.join(path_img,img)
        # else:
        #     imagens[nome]= os.path.join(path_img,img)

    if faixas and tipo in ['entrada','janelas']:
        # mistura paineis
        # duas cortinhas randomicas
        
        # medidas
        suporte=2
        if tipo == 'entrada':
            altura=250+suporte/2
            bmin=15
            bmax=bmin
            largura=20
        elif tipo == 'janelas':
            altura=220+suporte/2
            bmin=15
            bmax=60
            largura=60
        altura_total=(altura-(bmin+bmax)/2)*2
        
        faixas_ordem={}
        for i in imagens:
            paineis=list(imagens[i].keys())
            n=int(i)
            for faixa in range(n):
                mistura=paineis.copy()
                shuffle(mistura)

                for painel in range(2):
                    if painel not in faixas_ordem:
                        faixas_ordem[painel]={}

                    faixas_ordem[painel][faixa]=[]
                    for lado in range(2):
                        if not lado:
                            h=altura-randint(bmin,bmax)
                            h=[h,altura_total-h]
                        faixas_ordem[painel][faixa].append([mistura.pop(),largura,h[lado]])
            
            faixas_mix={}
            for painel in faixas_ordem:
                for faixa in faixas_ordem[painel]:
                    for l,lado in enumerate(faixas_ordem[painel][faixa]):
                        lado,largura,altura=lado
                        if not lado in faixas_mix:
                            faixas_mix[lado]={}
                        faixas_mix[lado][faixa]=[painel,l,largura,altura]
            
    if ver:
        info=imagens[ver]
        imagens={}
        imagens[ver]=info

    for i in imagens:
        print(i)
        for j in imagens[i]:
            print('    ',j, imagens[i][j])
    
    if faixas:
        for painel in imagens:
            n=int(painel.split('-')[-1])
            for i in imagens[painel]:
                img=imagens[painel][i]
                imgw,imgh=imageSize(img)

                fw=imgw/n
                ph=round(imgh)
            
                if tipo == 'portas':
                    ordem=painel.split('-')[0]
                else:
                    ordem=n*'1'
            
                w0=0
                for j,o in enumerate(ordem):
                    
                    # dpi=200/72
                    if tipo == 'portas':
                        pw=round(int(o)*fw)
                        e=1
                    elif tipo in ['entrada','janelas']:
                        nome,lado,largura,altura=faixas_mix[i][j]
                        ph=round(altura*cm)
                        pw=round(largura*cm)
                        e=pw/fw
                        
                    newPage(pw,ph)
                    
                    # im = ImageObject()
                    # with im:
                    #     size(pw*dpi,ph*dpi)
                    #     scale(e)
                    #     scale(dpi)
                    #     image(img,(-w0,0))
                    
                    # scale(1/dpi)
                    # image(im,(0,0))

                    scale(e)
                    image(img,(-w0,0))

                    w0+=pw/e
                
                    #salvar
                    if tipo=='portas':
                        nome=painel[:-1]+str(j)
                        nome='pdf/grafica/0/%s/1/%s-%s.pdf' % (tipo,nome,i)
                    elif tipo in ['entrada','janelas']:
                        nome='%s-%s-%s' % (nome,j,lado)
                        nome='pdf/grafica/0/%s/1/%s.pdf' % (tipo,nome)
                
                    if salvar:
                        save_file(nome)

    else:
        for painel in imagens:
            i0=imagens[painel]['0']
            i1=imagens[painel]['1']

            i0w,i0h=imageSize(i0)
            i1w,i1h=imageSize(i1)

            pw=i0w
            if tipo=='obras-duplo':
                ph=(i0h+i1h)*2+ilhos
            else:
                ph=i0h+i1h
            
            #escala da grafica
            eg=0.25
            
            newPage(pw*eg,ph*eg)
            scale(eg)

            save()
            if tipo=='obras-duplo':
                translate(0,i0h+ilhos/2)
            
            image(i0,(0,0))

            save()
            translate(pw,i0h+i1h)
            scale(-1,-1)
            image(i1,(0,0))
            restore()

            #ilhos
            info='%s-%s' % (tipo,painel)

            #centro
            if tipo=='portas':
                translate(0,i0h)
                barra(d=ilhos, m=3*cm, y=-ilhos/2, n=0, fundo=True, info=info)
                #costura
                for i in range(2):
                    i=((-1)**(i+1))*costura
                    lineDash(None)
                    cmykStroke(0,0,0,0)
                    for j in range(2):
                        line((0,i),(pw,i))
                        cmykStroke(0,0,0,1)
                        lineDash(.5*cm,.5*cm)
            else:
                barra(d=ilhos, m=3*cm, y=i0h-ilhos/2, n=3, fundo=True, info=info)
        
            restore()

            if tipo=='obras-duplo':
                #barra1
                barra(d=ilhos, m=3*cm, y=0, n=3, fundo=True, info=info)
                #barra2
                barra(d=ilhos, m=3*cm, y=ph-ilhos, n=3, fundo=True, info=info)
        
            # salvar
            nome='pdf/grafica/1/%s/playmode_%s-%s_%sx%scm.pdf' % (tipo,tipo,painel,round(pw/cm,1),round(ph/cm,1))

            if salvar:
                save_file(nome)

##########################################################

end = time.time()
print('\n>>>', end-start, 's')
print('\n>>>', (end-start)/60, 'min')
