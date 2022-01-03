import string

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
    # if tipo == 'upper':
    #     v=v.upper()
    # if tipo == 'lower':
    #     v=v.lower()
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

def pattern(letra,letras,print_fonte=False):
    fontes={}
    chave='%s_%s' % (fonte,str(fs))
    fontes[chave]={}
    
    grid=BezierPath()
    
    espacow=0
    espacoh=0
    for car in letras:
        desenho=BezierPath()
        desenho.text(car, font=fonte, fontSize=fs*m,offset=(margem_x,fsh*m/4+margem_y))
    
        if car==letra:
            newPage(pw,ph)
            drawPath(desenho)

        padrao=[]
        for y in range(0,ph,m):
            linha=''
            for x in range(0,pw,m):
                if car == letra:
                    ponto=m/5
                    grid.oval(x+ajuste-ponto/2,y+ajuste-ponto/2,ponto,ponto)

                if desenho.pointInside((x+ajuste,y+ajuste)):
                    linha+='#'
                else:
                    linha+='-'
            padrao+=[linha,]

        padrao=limpa(padrao)

        espacow+=len(padrao[0])
        espacoh+=len(padrao)

        padrao.reverse()
        padrao='\n'.join(padrao)
        fontes[chave][car]=padrao
    
    #cria espaco
    if print_fonte:
        espacow=int(espacow/len(letras))
        espacoh=int(espacoh/len(letras))
        fontes[chave][' ']=espacoh*(espacow*'-'+'\n')
    
    #desenha grid
    fill(1,0,1)
    drawPath(grid)
    
    return fontes,chave


fontes_do_pc = ['?',]+installedFonts()

Variable([
    dict(name="fonte_do_pc", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    # dict(name="case", ui="PopUpButton", args=dict(items=cases)),
    dict(name="uppercase", ui="CheckBox", args=dict(value=True)),
    dict(name="lowercase", ui="CheckBox", args=dict(value=False)),
    dict(name="digits", ui="CheckBox", args=dict(value=False)),
    dict(name="punctuation", ui="CheckBox", args=dict(value=False)),
    dict(name="letra", ui="EditText", args=dict(text='')),
    dict(name="altura", ui="EditText", args=dict(text='10')),
    dict(name="ajuste_grid", ui="EditText", args=dict(text='')),
    dict(name="margem_x", ui="Slider", args=dict(value=3, minValue=-10, maxValue=30)),    
    dict(name="margem_y", ui="Slider", args=dict(value=2, minValue=-10, maxValue=30)),    
    dict(name="print_fonte", ui="CheckBox", args=dict(value=False)),
], globals())

fonte=var(fonte_do_pc,lista=fontes_do_pc)

letras=[]
if uppercase:
    letras+=list(string.ascii_uppercase)
if lowercase:
    letras+=list(string.ascii_lowercase)
if digits:
    letras+=list(string.digits)
if punctuation:
    letras+=list(string.punctuation)
letra=var(letra,choice(letras))

fs=var(altura,10,tipo='numero')
ajuste=var(ajuste_grid,0,tipo='numero')

m=10
margem_x=margem_x*m
margem_y=margem_y*m

font(fonte,fs)
fsw,fsh=textSize(letra, align=None, width=None, height=None)

pw=int(3*margem_x+2*fsw*m)
ph=int(1.5*margem_y+fsh*m)

if print_fonte:
    fontes,chave = pattern(letra,letras,print_fonte)
else:
    fontes,chave = pattern(letra,[letra,],print_fonte)

# desenha fonte pixel:
fill(0)
padrao = fontes[chave][letra].split()
padrao.reverse()
translate(pw-margem_x-fsw*m,(ph-len(padrao)*m)/2)
for j,linha in enumerate(padrao):
    for i,car in enumerate(linha):
        if car == '#':
            rect(i*m,j*m,m,m)
        

if print_fonte:
    for fonte in fontes:
        txt="    '%s':{"
        print(txt % fonte)
        for car in fontes[fonte]:
            txt="        '%s':'''\n%s\n''',"
            print(txt % (car,fontes[fonte][car]))
        print('    },')

else:
    print('letra =', letra)
    print('fonte =', fonte)
    print('altura =', fs)
    print()
    print(fontes[chave][letra])



