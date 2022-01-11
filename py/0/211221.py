import os

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-2])


# fonte
from fontes import font
from base import pixel

def letra(car):
    desenho=BezierPath()
    px=font[fonte][car].split()
    px.reverse()
    for j,y in enumerate(px):
        for i,x in enumerate(y):
            if x == '#' and pixel_randomico:
                x=choice(['#','o','t','x'])
            pixel(x,desenho,i,j,m,var=m)
    desenho.removeOverlap()
    w=(i+1)*m
    h=(j+1)*m
    # ponto de conexao
    ponto=0
    for i,car in enumerate(px[0]):
        if car == '#':
            ponto=i*m
            break
    return desenho,w,h,ponto

def def_cor(cor,tipo='fill'):
    if tipo == 'stroke':
        if not cor:
            if cor_mode==0:
                stroke(None)
            if cor_mode==1:
                cmykStroke(None)
        else:
            if cor_mode==0:
                stroke(*cor)
            if cor_mode==1:
                cmykStroke(*cor)
    elif tipo == 'fill':
        if not cor:
            if cor_mode==0:
                fill(None)
            if cor_mode==1:
                cmykFill(None)
        else:
            if cor_mode==0:
                fill(*cor)
            if cor_mode==1:
                cmykFill(*cor)

def dgd(cor1,cor2,p,repete):
    c=()
    for nc in range(len(cor1)):
        c1=cor1[nc]
        c2=cor2[nc]
        if c1 == c2:
            c3=c1
        else:
            if repete-1 == 0:
                c3=c2
            else:
                c3=c1-((c1-c2)/(repete-1))*p
        c+=(c3,)
    return c

def inverte_cor(cor):
    c=()
    for i in range(3):
        c+=(1-cor[i],)
    if cor_mode == 1:
        c+=(0,)
    return c


def pm(m,w,h,colorido,fonte,tipo,x0,y0,repete_min,repete_max,buraco):    
    save()
    translate(x0,y0)
    margem0x,margem0y = x0,y0
    linha=0
    # pal=2*choice([i for i in palavra])
    for n,car in enumerate(palavra):
        desenho,dw,dh,ponto=letra(car)

        if tipo in [1,2,3]:
            if car in colorido or colore_linha:
                if degrade:
                    def_cor(dgd(cor1,cor2,n,len(palavra)))
                else:
                    def_cor(cor1)
                def_cor(linha,'stroke')
            else:
                def_cor(cor_)
                if degrade_linha:
                    def_cor(dgd(cor1,cor2,n,len(palavra)),'stroke')
                else:
                    def_cor(linha_,'stroke')

        if tipo in [1,2]:
            save()
            x=randint(m,int(w-dw-m))
            y=randint(m,int(h-dh-m))
            if linha and tipo==2:
                save()
                if colore_linha:
                    if degrade_linha:
                        def_cor(dgd(cor1,cor2,n,len(palavra)),'stroke')
                    else:
                        def_cor(linha_,'stroke')
                    
                line((linha),(x+ponto,y))
                restore()

            translate(x,y)
            drawPath(desenho)
            if tipo==2:
                linha=(x+ponto,y)
            restore()

        elif tipo == 3:
            if buraco and randint(0,1):
                pass
            else:
                drawPath(desenho)

            largura=dw+entreletra*m
            translate(largura,0)
           
        elif tipo in [4,5,6]:
            # calcula o inicio
            if tipo in [5,6]:
                x=choice([-1,1])
                y=choice([-1,1])
                cx=x0
                cy=y0
            repete=randint(repete_min,repete_max)

            save()
            for p in range(repete):
                if tipo in [5,6]:
                    if (cx+dw > w) or (cx < 0):
                        x=x*-1
                        translate(2*x*m,0)
                    if (cy+dh > h) or (cy < 0):
                        y=-1*y
                        translate(0,2*y*m)

                if car in colorido:
                    if degrade:
                        def_cor(dgd(cor1,cor2,p,repete))
                    else:
                        def_cor(cor1)
                    def_cor(linha,'stroke')
                else:
                    def_cor(cor_)
                    if degrade_linha:
                        def_cor(dgd(cor1,cor2,p,repete),'stroke')
                    else:
                        def_cor(linha_,'stroke')

                if buraco and randint(0,1):
                    pass
                else:
                    drawPath(desenho)

                if tipo in [5,6]:
                    dx=x*entrelinha*m
                    dy=y*entrelinha*m
                    translate(dx,dy)
                    cx+=dx
                    cy+=dy
                else:
                    translate(0,entrelinha*m)
            
            if tipo == 4:
                if contraste > 2:
                    if car in colorido or colore_linha:
                        def_cor(cor3)
                        def_cor(linha,'stroke')
                    else:
                        def_cor(cor_)
                        if degrade_linha:
                            def_cor(cor3,'stroke')
                        else:
                            def_cor(linha_,'stroke')
                elif colore_linha and (car not in colorido):
                    def_cor(cor1)
                    def_cor(linha,'stroke')
                    
                if contraste in [2,4,6]:
                    translate(0,-randint(0,repete)*entrelinha*m)
                drawPath(desenho)
            restore()
            
            largura=dw+entreletra*m
            if tipo in [5,6]:
                x0+=largura
                cy+=y*m
            translate(largura,0)
    restore()
    if tipo == 5:
        tipo=3
        pm(m,w,h,colorido,fonte,tipo,margem0x,margem0y,0,0,False)
    elif tipo == 6:
        tipo=4
        pm(m,w,h,colorido,fonte,tipo,margem0x,margem0y,1,randint(1,8),False)

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
            v=int(v)
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
path_img = path+'/img/0/'
imgs=['','👀']+os.listdir(path_img)

# fontes
fontes=['👀']+[n for n in font.keys()]

# opcoes de itens coloridos
colore = ['👀','','p','pm','mode','play','playmode']

# tipos
tipos = [
    '👀',
    '1_randomico sem linha',
    '2_randomico com linha',
    '3_linear',
    '4_empilhado',
    '5_paciencia',
    '6_paciencia empilhada',
]

# cores
cor_modes = [
    '0_rgb',
    '1_cmyk',
]

# contraste
contrastes = [
    '👀',
    '1_sem contraste',
    '2_sem contraste randomico',
    '3_contraste cor2 ultimo',
    '4_contraste cor2 randomico',
    '5_contraste cor3 ultimo',
    '6_contraste cor3 randomico',
]


Variable([
    dict(name="x0", ui="EditText", args=dict(text='')),
    dict(name="y0", ui="EditText", args=dict(text='')),
    dict(name="painel", ui="CheckBox", args=dict(value=False)),
    dict(name="palavra", ui="EditText", args=dict(text='playmode')),
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="divisao_w", ui="EditText", args=dict(text='')),
    dict(name="divisao_h", ui="EditText", args=dict(text='')),
    dict(name="modulo", ui="EditText", args=dict(text='')),
    dict(name="colorido", ui="PopUpButton", args=dict(items=colore)),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes)),
    dict(name="tipo", ui="PopUpButton", args=dict(items=tipos)),
    dict(name="buraco", ui="CheckBox", args=dict(value=False)),
    dict(name="pixel_randomico", ui="CheckBox", args=dict(value=False)),
    dict(name="entreletra", ui="EditText", args=dict(text='')),
    dict(name="entrelinha", ui="EditText", args=dict(text='')),
    dict(name="repete_min", ui="EditText", args=dict(text='')),
    dict(name="repete_max", ui="EditText", args=dict(text='')),
    dict(name="cor_mode", ui="PopUpButton", args=dict(items=cor_modes)),
    dict(name="cor1", ui="EditText", args=dict(text='')),
    dict(name="cor2", ui="EditText", args=dict(text='')),
    dict(name="cor3", ui="EditText", args=dict(text='')),
    dict(name="linha", ui="EditText", args=dict(text='')),
    dict(name="cor_", ui="EditText", args=dict(text='')),
    dict(name="linha_", ui="EditText", args=dict(text='')),
    dict(name="contraste", ui="PopUpButton", args=dict(items=contrastes)),
    dict(name="transparente", ui="CheckBox", args=dict(value=False)),
    dict(name="degrade", ui="CheckBox", args=dict(value=True)),
    dict(name="degrade_linha", ui="CheckBox", args=dict(value=True)),
    dict(name="colore_linha", ui="CheckBox", args=dict(value=False)),
], globals())
    

# imagens
if img==1:
    img=randint(2,len(imgs)-2)
if img:
    img=imgs[img]
    img=path_img+img
    imgw,imgh=imageSize(img)
    newPage(imgw,imgh)
    image(img,(0,0))

# repeticao dos graficos
if painel:
    palavra_painel=[i for i in palavra]
    divisao_w=var(divisao_w,10,tipo='numero')
    divisao_h=var(divisao_h,10,tipo='numero')
else:
    divisao_w=var(divisao_w,1,tipo='numero')
    divisao_h=var(divisao_h,1,tipo='numero')
w=width()/divisao_w
h=height()/divisao_h
# modulo da fonte
if painel:
    m=var(modulo,randint(5,8),tipo='numero')
else:
    m=var(modulo,randint(10,15),tipo='numero')
# fonte
fonte=var(fonte,lista=fontes)
# fonte colorida
colorido=var(colorido,lista=colore)
colorido=[car for car in colorido]
# tipo
tipo=var(tipo,randint(2,len(tipos)-1))
# espaco entre as repeticoes
entrelinha=var(entrelinha,randint(1,2),tipo='numero')
# espaco entre os caracteres
entreletra=var(entreletra,randint(0,2),tipo='numero')

# numero de repeticao
# define os numero padroes da rapeticao em funcao do tipo
if tipo == 4:
    repete_min=var(repete_min,1,tipo='numero')
    repete_max=var(repete_max,13,tipo='numero')
elif tipo in [5,6]:
    repete_min=var(repete_min,1,tipo='numero')
    repete_max=var(repete_max,9,tipo='numero')
else:
    repete_min=var(repete_min,0,tipo='numero')
    repete_max=var(repete_max,0,tipo='numero')

# # # # cores
# # # cor=var(cor, randint(1,len(cores)-1))

# posicao inicial
if tipo in [1,2]:
    x0=var(x0,0,tipo='numero')
    y0=var(y0,0,tipo='numero')
elif tipo in [5,6]:
    x0=var(x0,int(w/4),tipo='numero')
    y0=var(y0,int(h/2),tipo='numero')
else:
    x0=var(x0,randint(10,50),tipo='numero')
    y0=var(y0,choice(range(0,int(h/2))),tipo='numero')

# cor
# contraste
contraste=var(contraste,randint(1,len(contrastes)-1))
cor1=var(cor1,tipo='cor')
cor2=var(cor2,tipo='cor')
if contraste in [2,3]:
    cor3=var(cor3,inverte_cor(cor1),tipo='cor')
elif contraste in [4,5]:
    cor3=var(cor3,inverte_cor(cor1),tipo='cor')
linha=var(linha,'none',tipo='cor')

if cor_mode == 0:
    cor_=var(cor_,(1,1,1),tipo='cor')
elif cor_mode == 1:
    cor_=var(cor_,(0,0,0,0),tipo='cor')
linha_=var(linha_,cor1, tipo='cor')

if transparente:
    cor_=None
            
print('divisao_w =', divisao_w )
print('divisao_h =', divisao_h )
print('modulo =', m)
print('colorido =', colorido)
print('fonte =', fonte)
print('tipo =', tipos[tipo])
print('entrelinha =', entrelinha)
print('entreletra =', entreletra)
print()
print('>>> cores fonte colorida')
print('cor1 =', cor1, '>>> cor inicial do degrade')
print('cor2 =', cor2, '>>> cor final do degrade')
print('cor3 =', cor3, '>>> cor contraste do degrade')
print('linha =', linha)
print('>>> cores fonte nao colorida')
print('cor_ =', cor_)
print('linha_ =', linha_)




strokeWidth(m/10)
miterLimit(m/10)
# lineJoin("bevel")
# lineCap("square")

for nh in range(divisao_h):
    save()
    for nw in range(divisao_w):
        if painel:
            palavra=choice(palavra_painel)
        pm(m,w,h,colorido,fonte,tipo,x0,y0,repete_min,repete_max,buraco)
        translate(w,0)
    restore()
    translate(0,h)
    
    