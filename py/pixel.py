import os

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# fonte
from fontes import font as fonts


def pixel(car,bezier,i,j,m,var=1):
    x=i*var
    y=j*var
    if car != ' ':
        bezier.translate(-x,-y)
        bezier.appendPath(formas[car])
        bezier.translate(x,y)
    return bezier

def redefine(pattern,px_lista):
    for j,y in enumerate(pattern):
        linha=[]
        for i,x in enumerate(y):
            if x == '#':
                x=choice(px_lista)
            linha.append(x)
        pattern[j]=linha
    return pattern

def letra(car,layer):
    desenho=BezierPath()
    for j,y in enumerate(car):
        for i,x in enumerate(y):
            if x in layer:
                desenho = pixel(x,desenho,i,j,m,var=m)
    desenho.removeOverlap()
    w=(i+1)*m
    h=(j+1)*m
    return desenho,w,h
    
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
                    if cores_quebradas:
                        v+=(randint(0,100)/100,)
                    else:
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


# fontes
fontes=['👀']+[n for n in fonts.keys()]

# opcoes de itens coloridos
colore = ['👀','','p','pm','mode','play','playmode']

# cores
cor_modes = [
    '0_rgb',
    '1_cmyk',
]

fontes_do_pc = ['?',]+installedFonts()

Variable([
    dict(name="x", ui="Slider", args=dict(value=10, minValue=0, maxValue=100)),    
    dict(name="y", ui="Slider", args=dict(value=40, minValue=0, maxValue=100)),    
    dict(name="palavra", ui="EditText", args=dict(text='playmode')),
    dict(name="modulo", ui="EditText", args=dict(text='17')),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes)),
    dict(name="entreletra", ui="EditText", args=dict(text='1')),
    dict(name="cor_mode", ui="PopUpButton", args=dict(items=cor_modes)),
    dict(name="colorido", ui="EditText", args=dict(text='+')),
    dict(name="cor1", ui="EditText", args=dict(text='')),
    dict(name="cor2", ui="EditText", args=dict(text='')),
    dict(name="cor3", ui="EditText", args=dict(text='')),
    dict(name="cor4", ui="EditText", args=dict(text='')),
    dict(name="pixel_colorido", ui="CheckBox", args=dict(value=False)),
    dict(name="degrade", ui="CheckBox", args=dict(value=False)),
    dict(name="degrade_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="cores_quebradas", ui="CheckBox", args=dict(value=False)),
    dict(name="caracteres", ui="EditText", args=dict(text='')),
    dict(name="fonte_pixel", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="fonte_size", ui="EditText", args=dict(text='')),
    dict(name="quadrado", ui="CheckBox", args=dict(value=True)),
    dict(name="circulo", ui="CheckBox", args=dict(value=True)),
    dict(name="triangulo", ui="CheckBox", args=dict(value=True)),
    dict(name="xis", ui="CheckBox", args=dict(value=True)),
], globals())
    

w=1000
h=w/2
newPage(w,h)

px_lista=[]
#formas geometricas
if quadrado:
    px_lista.append('quadrado')
if circulo:
    px_lista.append('circulo')
if triangulo:
    px_lista.append('triangulo')
if xis:
    px_lista.append('xis')
#caracteres
px_lista+=[car for car in caracteres]

m=var(modulo,10,tipo='numero')

# fonte
fonte=var(fonte,'sem buraco',lista=fontes)
# fonte colorida
colorido=var(colorido,choice(colore[1:]))
if colorido == '+':
    colorido=palavra
elif colorido == '-':
    colorido=''
colorido=[car for car in colorido]

# espaco entre os caracteres
entreletra=var(entreletra,randint(0,2),tipo='numero')

# posicao inicial
x0=x*width()/100
y0=y*height()/100

# cor
cor1=var(cor1,tipo='cor')
cor2=var(cor2,tipo='cor')

if pixel_colorido and degrade:
    cor3=var(cor3,dgd(cor1,cor2,1,len(px_lista)),tipo='cor')
    cor4=var(cor4,dgd(cor1,cor2,2,len(px_lista)),tipo='cor')
else:
    cor3=var(cor3,tipo='cor')
    cor4=var(cor4,tipo='cor')

# fonte pixel
fonte_px=var(fonte_pixel,lista=fontes_do_pc)
fs=var(fonte_size,m,tipo='numero')
            

print('modulo =', m, 'px')
print('fonte =', fonte)
print('entreletra =', entreletra)
print()
print('colorido =', colorido)
print('+ => todos')
print('- => nenhum')
print()
print('cor1 =', cor1, '>>> cor quadrado /// inicio degrade')
print('cor2 =', cor2, '>>> cor circulo /// fim degrade')
print('cor3 =', cor3, '>>> cor triangulo')
print('cor4 =', cor4, '>>> cor x')
print()
print('fonte_pixel =', fonte_px)
print('fonte_size =', fs)


strokeWidth(m/10)
miterLimit(m/10)
lineJoin("bevel")
# lineCap("square")


# cria dicionario com formas basicas formas basicas
formas={}
# formas geometricas
car_lista=['#','o','t','+','x','X',]
for c in car_lista:
    x,y=0,0
    bezier=BezierPath()
    if c == '#':
        c='quadrado'
        bezier.rect(x,y,m,m)
    elif c == 'o':
        c='circulo'
        bezier.oval(x,y,m,m)
    elif c == 't':
        c='triangulo'
        bezier.polygon((x,y),(x+m/2,y+m),(x+m,y))
    elif c == '+':
        c='cruz'
        bezier.rect(x+m/4,y,m/2,m)
        bezier.rect(x,y+m/4,m,m/2)
    elif c == 'X':
        c='xis2'
        n=3
        bezier.polygon((x,y),(x+m/n,y),(x+m,y+m),(x+m-m/n,y+m))
        bezier.polygon((x+m-m/n,y),(x+m,y),(x+m/n,y+m),(x,y+m),)
    elif c == 'x':
        c='xis'
        n=4
        bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
        bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
    formas[c]=bezier
# caracteres
for c in caracteres:
    bezier=BezierPath()
    bezier.textBox(c, (-m/2,-m+fs-m,2*m,2*m), font=fonte_px, fontSize=fs, align='center',)
    formas[c]=bezier



save()
translate(x0,y0)
margem0x,margem0y = x0,y0
linha=0

for n,car in enumerate(palavra):
    pattern=fonts[fonte][car].split()
    pattern.reverse()

    # recalcula pattern
    pattern=redefine(pattern,px_lista)
        
    if pixel_colorido:
        for px in px_lista:
            if car in colorido:
                def_cor(None,'stroke')
                tipo_cor='fill'
            else:
                def_cor(None)
                tipo_cor='stroke'

            if px == px_lista[0]:
                def_cor(cor1,tipo=tipo_cor)
            elif px == px_lista[1]:
                def_cor(cor2,tipo=tipo_cor)
            elif px == px_lista[2]:
                def_cor(cor3,tipo=tipo_cor)
            elif px == px_lista[3]:
                def_cor(cor4,tipo=tipo_cor)

            desenho,dw,dh=letra(pattern,[px,])
            drawPath(desenho)
       
    else:
        if car in colorido:
            if degrade:
                def_cor(dgd(cor1,cor2,n,len(palavra)))
            else:
                def_cor(cor1)
            def_cor(None,'stroke')
        else:
            def_cor(None)
            if degrade_linha:
                def_cor(dgd(cor1,cor2,n,len(palavra)),'stroke')
            else:
                def_cor(cor1,'stroke')

        desenho,dw,dh=letra(pattern,px_lista)
        drawPath(desenho)

    largura=dw+entreletra*m
    translate(largura,0)
       
restore()

    