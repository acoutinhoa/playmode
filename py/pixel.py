import os

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidade
cm=72/2.54
mm=cm/10

# fonte
from fontes import font
from base import pixel

px_lista=['#','o','t','x']
 
def redefine(pattern):
    for j,y in enumerate(pattern):
        linha=''
        for i,x in enumerate(y):
            if x == '#':
                if tipo_px == 3:
                    x='o'
                elif tipo_px == 4:
                    x='t'
                elif tipo_px == 5:
                    x='x'
                else:
                    x=choice(px_lista)
            linha+=x
        pattern[j]=linha
    return pattern

def letra(car,layer=px_lista):
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
fontes=['👀']+[n for n in font.keys()]

# opcoes de itens coloridos
colore = ['👀','','p','pm','mode','play','playmode']

# cores
cor_modes = [
    '0_rgb',
    '1_cmyk',
]

# pixel
tipos = [
    '?',
    '1_randomico',
    '2_quadrado',
    '3_circulo',
    '4_triangulo',
    '5_xis',
    '6_colorido',
]


Variable([
    dict(name="x", ui="Slider", args=dict(value=10, minValue=0, maxValue=100)),    
    dict(name="y", ui="Slider", args=dict(value=40, minValue=0, maxValue=100)),    
    dict(name="palavra", ui="EditText", args=dict(text='playmode')),
    dict(name="modulo", ui="EditText", args=dict(text='17')),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes)),
    dict(name="tipo_px", ui="PopUpButton", args=dict(items=tipos)),
    dict(name="entreletra", ui="EditText", args=dict(text='1')),
    dict(name="cor_mode", ui="PopUpButton", args=dict(items=cor_modes)),
    dict(name="colorido", ui="EditText", args=dict(text='+')),
    dict(name="cor1", ui="EditText", args=dict(text='')),
    dict(name="cor2", ui="EditText", args=dict(text='')),
    dict(name="cor3", ui="EditText", args=dict(text='')),
    dict(name="cor4", ui="EditText", args=dict(text='')),
    dict(name="degrade", ui="CheckBox", args=dict(value=False)),
    dict(name="degrade_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="cores_quebradas", ui="CheckBox", args=dict(value=False)),
], globals())
    

w=1000
h=w/2
newPage(w,h)

m=var(modulo,10,tipo='numero')
tipo_px=var(tipo_px,randint(1,len(tipos)-1))

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
# contraste
if tipo_px==6 and degrade:
    if not cor1:
        cor1=()
        if cor_mode == 0:
            while 0 not in cor1:
                cor1=var('',tipo='cor')
        elif cor_mode == 1:
            while 1 not in cor1:
                cor1=var('',tipo='cor')
    else:
        cor1=var(cor1,tipo='cor')
    cor4=var(cor4,tipo='cor')
    cor3=var(cor3,dgd(cor1,cor4,2,4),tipo='cor')
    cor2=var(cor2,dgd(cor1,cor4,1,4),tipo='cor')
else:
    cor1=var(cor1,tipo='cor')
    cor2=var(cor2,tipo='cor')
    cor3=var(cor3,tipo='cor')
    cor4=var(cor4,tipo='cor')
            

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


strokeWidth(m/10)
miterLimit(m/10)
lineJoin("bevel")
# lineCap("square")

save()
translate(x0,y0)
margem0x,margem0y = x0,y0
linha=0

for n,car in enumerate(palavra):
    pattern=font[fonte][car].split()
    pattern.reverse()

    # recalcula pattern
    if tipo_px != 2:
        pattern=redefine(pattern)
        
    if tipo_px == 6:
        for px in px_lista:
            if car in colorido:
                def_cor(None,'stroke')
                if px == '#':
                    def_cor(cor1)
                elif px == 'o':
                    def_cor(cor2)
                elif px == 't':
                    def_cor(cor3)
                elif px == 'x':
                    def_cor(cor4)
            else:
                def_cor(None)
                if px == '#':
                    def_cor(cor1,'stroke')
                elif px == 'o':
                    def_cor(cor2,'stroke')
                elif px == 't':
                    def_cor(cor3,'stroke')
                elif px == 'x':
                    def_cor(cor4,'stroke')

            desenho,dw,dh=letra(pattern,layer=[px,])
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

        desenho,dw,dh=letra(pattern)
        drawPath(desenho)

    largura=dw+entreletra*m
    translate(largura,0)
       
restore()


    