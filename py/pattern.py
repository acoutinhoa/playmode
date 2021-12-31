import string

# # # # # # import sys
# # # # # # sys.path.append('../')
# # # # # # import numeros.irracionais
# # # # # from id import var

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

def pattern(letra,letras,print_fonte=False):
    fontes={}
    chave='%s_%s_%s' % (fonte,str(fs),cases[case])
    fontes[chave]={}
    
    grid=BezierPath()
    
    espacow=0
    espacoh=0
    for car in letras:
        desenho=BezierPath()
        desenho.text(car, font=fonte, fontSize=fs*m,offset=(fs*m/1.5,fs*m))
    
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
        fontes[chave][car.lower()]=padrao
    
    #cria caracter pro espaco
    if print_fonte:
        espacow=int(espacow/len(letras))
        espacoh=int(espacoh/len(letras))
        fontes[chave][' ']=espacoh*(espacow*'-'+'\n')
    
    #desenha grid
    fill(1,0,1)
    drawPath(grid)
    
    return fontes,chave


fonts=[
    '?',
    '.ArabicUIDisplay-Medium', #23
    '.DamascusPUABold', #40
    '.HelveticaNeueDeskInterface-Bold', #52
    '.Keyboard', #74
    '.LucidaGrandeUI-Bold', #77
    '.PingFangTC-Semibold', #111
    '.SFCompactDisplay-Black', #114
    '.SFCompactRounded-Black', #123
    '.SFNS-HeavyG1', #169
    '.SFNSMono-Heavy', #227
    '.SFNSRounded-Bold', #238
    'AmericanTypewriter-Bold', #297
    'Arial-Black', #325
    'ArialRoundedMTBold', #340
    'Avenir-Black', #346
    'BodoniSvtyTwoOSITCTT-Bold', #400
    'BodoniSvtyTwoSCITCTT-Book', #403
    'ComicSansMS-Bold', #423
    'Courier-Bold', #430
    'CourierNewPS-BoldMT', #434
    'Futura-Bold', #461
    'GillSans-UltraBold', #486
    'HelveticaNeue-Bold', #503
    'HelveticaNeue-CondensedBlack', #505
    'Impact', #556
    'LastResort', #603
    'MyanmarSangamMN-Bold', #640
    'Noteworthy-Bold', #646
    'Optima-Bold', #759
    'Optima-ExtraBlack', #761
    'PTMono-Bold', #768
    'PTSans-CaptionBold', #773
    'PTSans-Narrow', #775
    'PTSans-NarrowBold', #776
    'PTSerif-Bold', #778
    'PTSerif-BoldItalic', #779
    'Palatino-Bold', #784
    'Phosphate-Inline', #790
    'PingFangTC-Semibold', #807
    'Rockwell-Bold', #813
    'Seravek-Bold', #862
    'Silom', #877
    'Skia-Regular_Black', #883
    'SnellRoundhand-Black', #893
    'SukhumvitSet-Bold', #895
    'Superclarendon-Black', #901
    'Tahoma-Bold', #911
    'Times-Bold', #923
    'Verdana-Bold', #938
    'Wingdings-Regular', #944
    'Wingdings2', #945
    'Wingdings3', #946
    'Zapfino', #948
    ]

cases = [
    'upper',
    'lower',
    ]

fontes_do_pc = ['-','?',]+installedFonts()

Variable([
    dict(name="fonte_do_pc", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fonts)),
    dict(name="case", ui="PopUpButton", args=dict(items=cases)),
    dict(name="letra", ui="EditText", args=dict(text='')),
    dict(name="altura", ui="EditText", args=dict(text='')),
    dict(name="ajuste_grid", ui="EditText", args=dict(text='')),
    dict(name="print_fonte", ui="CheckBox", args=dict(value=False)),
], globals())

if fonte_do_pc:
    fonte=var(fonte_do_pc,lista=fontes_do_pc)
    if fonte=='?':
        fonte=choice(fontes_do_pc[2:])
else:
    fonte=var(fonte,lista=fonts)

if case == 0:
    letras=string.ascii_uppercase
elif case == 1:
    letras=string.ascii_lowercase
letras=[l for l in letras]
letra=var(letra,choice(letras),tipo=cases[case])

fs=var(altura,10,tipo='numero')
ajuste=var(ajuste_grid,0,tipo='numero')

m=10

ph=3*fs*m
pw=4*fs*m

if print_fonte:
    fontes,chave = pattern(letra,letras,print_fonte)
else:
    fontes,chave = pattern(letra,[letra,],print_fonte)

# desenha fonte pixel:
fill(0)
padrao = fontes[chave][letra.lower()].split()
padrao.reverse()
translate(2.2*fs*m,fs*m)
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
            print(txt % (car,fontes[fonte][car.lower()]))
        print('    },')

else:
    print('letra =', letra)
    print('fonte =', fonte)
    print('altura =', fs)
    print()
    print(fontes[chave][letra.lower()])



