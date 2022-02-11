import time
start = time.time()

import os
from base import var, dgd, pixel

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

# unidades
cm = 72/2.54
mm = cm/10

###############################
###############################
###############################

ordem=[
    ('Produção',1.5), #0
    ('',2.7), #1
    ('Apoio',2), #2
    ('Patrocínio',3), #3
    ('Realização',3), #4
]

# linhas
ordem_linhas={
    '1':[[0,1,2,3,4]],
    '3':[[0],[1,2],[3,4]],
    }

###############################
###############################
###############################

# imagens
path_img = os.path.join(path,'img/logos')

fontes_do_pc = ['?',]+installedFonts()

n_linhas=list(ordem_linhas.keys())

Variable([
    dict(name="linhas", ui="PopUpButton", args=dict(items=n_linhas)),
    dict(name="altura_ccbb_mm", ui="EditText", args=dict(text='30')),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="fonteSize_px", ui="EditText", args=dict(text='12')),
], globals())

#linhas
n_linhas=n_linhas[linhas]
linhas=ordem_linhas[n_linhas]

# fonte
fonte=var(fonte,'CourierNewPS-BoldMT', lista=fontes_do_pc)
fs=var(fonteSize_px,tipo='float')

# logos
h=var(altura_ccbb_mm,tipo='float')*mm

#_____________________________________________
print('linhas =', n_linhas)
print('altura bb =', h/mm, 'mm')
print()
print('fonte =', fonte)
print('fonte size =', fs, 'px')
#_____________________________________________

m=h/3
h_linha=6*m

if n_linhas == '1':
    pw=105*m
elif n_linhas == '3':
    pw=44*m
ph=len(linhas)*h_linha+2*m

size(pw,ph)
translate(2*m,2*m)

linhas.reverse()
for linha in linhas:

    save()
    for n in linha:
        txt,nm=ordem[n]

        path_logos= os.path.join(path_img,str(n))
        logos = [img for img in os.listdir(path_logos) if img[0]!='.']
        logos.sort()
    
        # texto
        if txt:
            txt+=':'
    
        font(fonte)
        fontSize(fs)
        cmykFill(0,0,0,1)
        textBox(txt,( 0 , 3*m , fs*len(txt) , m*1.5 ))
    
        # logos
        for logo in logos:
            logo=os.path.join(path_logos,logo)
            lw,lh=imageSize(logo)
        
            e=(nm*m)/(lh/2)
        
            save()
            scale(e)
            image(logo,(0,-lh/4))
            restore()
        
            translate(lw*e+m,0)

        translate(m,0)

    restore()
    translate(0,h_linha)

end = time.time()
print('\n>>>', end-start, 's')
