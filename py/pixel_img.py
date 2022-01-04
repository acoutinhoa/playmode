
import os

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])


# desenho=BezierPath()
# desenho.traceImage(img, threshold=threshold, blur=None, invert=False, turd=2, tolerance=0.2, offset=None)
# gaussianBlur(radius=None)    

def pixel(car,bezier,i,j,m,var=1):
    x=i*var
    y=j*var
    if car != ' ':
        bezier.translate(-x,-y)
        bezier.appendPath(formas[car])
        bezier.translate(x,y)
    return bezier

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
path_img = path+'/img/0/'
img_lista = os.listdir(path_img)
img_lista.sort()
imgs=['?']+img_lista

# visualizar
opcoes = [
    '0_textura',
    '1_imagem',
    '2_grayscale',
    ]

fontes_do_pc = ['?',]+installedFonts()

# tipos de texto
tipos_txt=[
    '0_caracteres randomicos',
    '1_texto alinhado',
    '2_texto deslocado',
    '3_texto contado',
    ]

Variable([
    dict(name="img", ui="PopUpButton", args=dict(items=imgs)),
    dict(name="modulo", ui="EditText", args=dict(text='20')),
    dict(name="contraste", ui="Slider", args=dict(value=1, minValue=1, maxValue=3)),
    dict(name="brilho", ui="Slider", args=dict(value=0, minValue=-1, maxValue=1)),
    dict(name="inverte", ui="CheckBox", args=dict(value=False)),
    dict(name="cor", ui="EditText", args=dict(text='')),
    dict(name="ver", ui="PopUpButton", args=dict(items=opcoes)),
    dict(name="com_linha", ui="CheckBox", args=dict(value=False)),
    dict(name="caracteres", ui="EditText", args=dict(text='')),
    dict(name="fonte_pixel", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="fonte_size", ui="EditText", args=dict(text='')),
    dict(name="quadrado", ui="CheckBox", args=dict(value=True)),
    dict(name="circulo", ui="CheckBox", args=dict(value=True)),
    dict(name="triangulo", ui="CheckBox", args=dict(value=True)),
    dict(name="xis", ui="CheckBox", args=dict(value=True)),
    dict(name="texto", ui="PopUpButton", args=dict(items=tipos_txt)),
], globals())
    

m=var(modulo,randint(5,50),tipo='numero')
m=int(m)

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

cor_mode=0
cor=var(cor,(0,),tipo='cor')

# imagem
img=var(img,lista=imgs)
print('img =', img)
img=path_img+img
imgw,imgh=imageSize(img)

# fonte pixel
fonte_px=var(fonte_pixel,lista=fontes_do_pc)
fs=var(fonte_size,m,tipo='numero')

#caracteres
if texto:
    px_lista.append('texto')
else:
    px_lista+=[car for car in caracteres]


##############################################
##############################################
##############################################

# redefine variaveis
#img='' #'nome da imagem entre aspas'
#modulo=20 #numero inteiro
#costraste=0 #numero decimal entre 1 e 3
#brilho=0 #numero decimal entre -1 e 1
#cor=(0,0,0) #(0-1,0-1,0-1)
# fonte_px=15 #numero inteiro

##############################################
##############################################
##############################################


print('imgw =', imgw, 'px')
print('imgh =', imgh, 'px')
print()
print('contraste =', round(contraste,2))
print('brilho =', round(brilho,2))
print()
print('fonte_pixel =', fonte_px)
print('fonte_size =', fs)
print()
print('modulo =', m, 'px')


img=ImageObject(img)
img.colorMonochrome(color=(1,1,1,1), intensity=None)
img.colorControls(saturation=None, brightness=brilho, contrast=contraste)
if inverte:
    img.colorInvert()

pw=(imgw//m)*m
if imgw%m:
    pw+=m
ph=(imgh//m)*m
if imgh%m:
    ph+=m
    
newPage(pw,ph)
strokeWidth(m/10)
miterLimit(m/10)
# lineJoin("bevel")
# lineCap("square")


# cria dicionario com formas basicas formas basicas
formas={}
formas_txt={}
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

if ver==1:
    image(img,(0,0))

else:
    if com_linha:
        vezes=2
        px_lista2=px_lista.copy()
        px_lista2.reverse()
        ordem=px_lista+px_lista2+[' ']
    else:
        vezes=1
        ordem=px_lista+[' ']
    print('ordem =',ordem)

    cores=[]
    for j,y in enumerate(range(0,imgh,m)):
        cores.append([])
        for i,x in enumerate(range(0,imgw,m)):
            cinza=imagePixelColor(img,(x,y))
            if ver==2:
                fill(*cinza)
                rect(x,y,m,m)
            else:
                c=int(cinza[0]//(1/len(ordem)))
                if c==len(ordem):
                    c=len(ordem)-1
                car=ordem[c]
                cores[j]+=[(car,x,y,c,i,j),]
    
    for n in range(vezes):
        desenho=BezierPath()
        
        car_c=0
        for linha in cores:
            for ponto in linha:
                car,x,y,c,i,j = ponto
                
                if car=='texto':
                    if texto == 1:
                        car_n=i%len(caracteres)
                    elif texto == 2:
                        car_n=(i-j)%len(caracteres)
                    elif texto == 3:
                        car_n=car_c%len(caracteres)
                        car_c+=1
                    car=caracteres[car_n]
                    
                if com_linha:
                    if n==0 and c<len(px_lista):
                        desenho=pixel(car,desenho,x,y,m)
                    elif n==1 and c>=len(px_lista):
                        desenho=pixel(car,desenho,x,y,m)
                else:
                    desenho=pixel(car,desenho,x,y,m)
        if n==1:
            desenho.removeOverlap()
        if ver==0:
            if n==0:
                fill(*cor)
                stroke(None)
            elif n==1:
                fill(None)
                stroke(*cor)
            drawPath(desenho)
