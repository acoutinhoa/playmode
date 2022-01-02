#########################################
# criar uma pasta pattern
# dentro da pasta imagens
# playmode/img/pattern
#########################################


import os
import string

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

def var(v,v0=0,lista=[],tipo='',):
    if not v:
        if not v0:
            if lista:
                v=choice(lista[1:])
            elif tipo == 'numero':
                v=0
        else:
            v=v0
    else:
        if lista:
            v=lista[v]
        elif tipo == 'numero':
            v=int(v)
    if tipo == 'upper':
        v=v.upper()
    if tipo == 'lower':
        v=v.lower()
    return v

def limpa(padrao):
    for i in range(2):
        for l,linha in enumerate(padrao):
            if '#' in linha:
                break
        padrao=padrao[l:]
        padrao.reverse()

    cmin=len(padrao[0])
    cmax=0
    for c in range(cmin):
        for linha in padrao:
            if linha[c] == '#':
                if c<cmin:
                    cmin=c
                if c>cmax:
                    cmax=c
    for l,linha in enumerate(padrao):
        padrao[l]=linha[cmin:cmax+1]

    return padrao

def pattern(img):
    grid=BezierPath()

    desenho=BezierPath()
    desenho.traceImage(img)

    padrao=[]
    for y in range(ajuste,imgh+m,m):
        linha=''
        for x in range(ajuste,imgw+m,m):
            ponto=m/5
            grid.oval(x-ponto/2,y-ponto/2,ponto,ponto)

            if desenho.pointInside((x,y)):
                linha+='#'
            else:
                linha+='-'
        padrao+=[linha,]

    padrao=limpa(padrao)

    padrao.reverse()
    padrao='\n'.join(padrao)
    
    return padrao,desenho,grid


################################################

# imagens
path_img = path+'/img/pattern/'
imgs=['?']+os.listdir(path_img)


Variable([
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="modulo", ui="EditText", args=dict(text='50')),
    dict(name="ajuste_grid", ui="EditText", args=dict(text='')),
    dict(name="contraste", ui="Slider", args=dict(value=1, minValue=1, maxValue=3)),
    dict(name="brilho", ui="Slider", args=dict(value=0, minValue=-1, maxValue=1)),
    dict(name="ver_imagem", ui="CheckBox", args=dict(value=False)),
    dict(name="print_fonte", ui="CheckBox", args=dict(value=False)),
], globals())

# imagem
imagem=var(img,lista=imgs)
path=path_img+imagem
imgw,imgh=imageSize(path)

img=ImageObject(path)
img.colorControls(saturation=None, brightness=brilho, contrast=contraste)

ajuste=var(ajuste_grid,0,tipo='numero')

m=var(modulo,tipo='numero')


################################################


padrao,desenho,grid=pattern(img)

if ver_imagem:
    pw=imgw
    ph=imgh
    newPage(pw,ph)
    drawPath(desenho)
    fill(1,0,1)
    drawPath(grid)

else:
    grafico=padrao.split()
    grafico.reverse()
    pw=len(grafico[0]*m)
    ph=len(grafico*m)
    newPage(pw,ph)
    # desenha fonte pixel:
    fill(0)
    for j,linha in enumerate(grafico):
        for i,car in enumerate(linha):
            if car == '#':
                rect(i*m,j*m,m,m)
        
if print_fonte:
    txt="    '%s':{"
    print(txt % 'imagem')
    txt="        '%s':'''\n%s\n''',"
    print(txt % (imagem,padrao))
    print('    },')
else:
    print('img =', imagem)
    print('modulo =', m, 'px')
    print()
    print(padrao)
    

