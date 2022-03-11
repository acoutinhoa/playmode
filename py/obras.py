import time
start = time.time()

import os
from base import var,cor
from string import digits

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

#########################################

# unidades
cm = 72/2.54
mm = cm/10

#########################################

# img
path_img = os.path.join(path,'pdf/grafica/0/obras/0')
img_lista = [img for img in os.listdir(path_img) if img[0] not in ['.','_']]

#########################################

# txt
path_txt = os.path.join(path,'_/txt')

txt = os.path.join(path_txt,'obras.txt')
with open(txt, encoding="utf-8") as file:
    txt = file.read()

# eixos
txt=txt.split('EIXO')

linguas=['pt','en']

# organiza texto
base_obras={}
for i,eixo in enumerate(txt):
    if i:
        base_obras[i]={}
    n=1
    nome=0
    obra=0
    lang=linguas[0]
    autor=1
    aviso=0

    eixo=eixo.split('\n')[1:]
    for j,linha in enumerate(eixo):
        palavras=linha.split()
        if palavras:
            if autor==1:
                if n not in base_obras[i]:
                    base_obras[i][n]={'pt':{},'en':{},}
                obra=base_obras[i][n]

                autor=' '.join(palavras)
                obra[lang]['autor']=autor
                autor=0

            # editar
            elif linha[:2]=='**':
                obra[lang]['info_extra']=linha
            
            elif linha[0]=='*':
                obra[lang]['info_autor']=linha
                aviso=1
            
            elif aviso:
                obra[lang]['aviso']=linha

                if lang == linguas[0]:
                    lang = linguas[1]
                else:
                    lang=linguas[0]
                    n+=1
                autor=1
                aviso=0
                
            elif len(linha)<200:
                # print(linha)
                if 'info' not in obra[lang]:
                    obra[lang]['info']=[]
                obra[lang]['info'].append(linha)
            else:
                if 'texto' not in obra[lang]:
                    obra[lang]['texto']=[]
                if linha[-1]==' ':
                    linha=linha[:-1]
                obra[lang]['texto'].append(linha)
                
# # imprime dicionario    
# for eixo in base_obras:
#     print('>>>>>>>>', eixo)
#     dic=base_obras[eixo]
#     for obra in dic:
#         print(obra)
#         dic2=dic[obra]
#         for item in dic2:
#             dic3=dic2[item]
#             if type(dic3) == type(dic2):
#                 print('___ %s :'%item)
#                 for i in dic3:
#                     print('    %s :'%i,dic3[i])
#             else:
#                 print(dic3)
#     print()


#edita texto
obras_lista=[]
for e in base_obras:
    eixo=base_obras[e]
    for n in eixo:
        obra=eixo[n]
        numero=(e,n)
        for lang in linguas:
            
            if 'info' in obra[lang]:
                for i,item in enumerate(obra[lang]['info']):
                    
                    if item[0]==' ':
                        print('>>>>>>>')

                    item=item.replace('**','*')
                    item=item.replace('–','-')
    
                    # quebra linha no ;
                    if not ('Cortesia' in item or 'Courtesy' in item):
                        item=item.replace('; ',';')
                        item=item.split(';')
                    
                        for j,item in enumerate(item):
                            item=item[0].upper()+item[1:]
                            if not j:
                                obra[lang]['info'][i]=item
                            else:
                                obra[lang]['info'].insert(j+i,item)
                    else:
                        item=item[0].upper()+item[1:]
                        obra[lang]['info'][i]=item

            if 'info_autor' in obra[lang]:
                info=obra[lang]['info_autor']
                autor=obra[lang]['autor']
                
                # lista de obras
                if lang == 'pt':
                    obras_lista.append('%s_%s_%s'%(e,n,autor.replace('*','')))
            

                autor=autor.replace(' e ','\ne ')
                autor=autor.replace(' and ','\nand ')
                autor=autor.replace(', ',',\n')
                autor=autor.replace('*','')

                info=info.replace(', ',',') # padroniza a virgula
                info=info.replace(',',', ') # acrescenta espaço
                info=info.replace('*','')
                info=info.replace('.','')
                info=info.replace('–','-')

                if info[0]==' ':
                    info=info[1:]

                if numero in [(1,2),(1,3),(1,6),(2,6),(2,8),(2,10),]:

                    autor_=autor.replace(',','')
                    autor_=autor_.replace('\ne ','\n')
                    autor_=autor_.replace('and ','')
                    autor_=autor_.split('\n')
                    
                    info=info.split('; ')
                    
                    if numero == (1,6):
                        for j,item in enumerate(info):
                            item=item.split(', ')
                            nome=item.pop(0)
                            item=', '.join(item)
                            info[j]=item
                            autor_.append(nome)
                        info.insert(0,'')

                    elif numero == (2,6): #TALE OF TALES
                        autor_=[autor_[-1]]
                    
                    elif numero == (2,10): #TALE OF TALES
                        autor_=[autor_[0]]

                    for j,item in enumerate(info):
                        info[j]=[autor_[j],item]

                else:
                    info=[[autor,info]]
                
                obra[lang]['info_autor']=info
                obra[lang]['autor']=autor

            if 'info_extra' in obra[lang]:
                info=obra[lang]['info_extra']
                info=info.replace('** ','*')
                extra=info+' '
                obra[lang]['info_extra']=extra
                
            if 'texto' in obra[lang]:
                txt=obra[lang]['texto']
                for p,par in enumerate(txt):
                    par=par.replace('–','-')
                    par=par.replace('**','*')
                    txt[p]=par
                
#########################################

# qctx
def qctx(fs,enter=0,espaco=0,alinha=None):
    x=randint(0,3)
    t=FormattedString()
    if alinha:
        t.align(alinha)
    if x==0:
        t.append(' ◼︎',fontSize=fs,font=fontes[0],tracking=elq,)
    elif x==1:
        t.append(' ●',fontSize=fs,font=fontes[0],tracking=elq,)
    elif x==2:
        t.append(' ▲',fontSize=fs,font=fontes[0],tracking=elq,)
    elif x==3:
        t.append(' ⨯',fontSize=fs*1.2,font=fontes[0],tracking=elq*6,)
    if espaco:
        t.append(' ',tracking=elq,)
    if enter:
        t.append('\n')
    return t

#########################################

obras_lista+=['tudo','autoportante','info_extra','varios_autores']

pesos=['bold','light']

Variable([
    dict(name = "ver", ui = "PopUpButton", args = dict(items = obras_lista)),
    dict(name = "escala_real", ui = "CheckBox", args = dict(value = False)),
    dict(name = "grafica", ui = "CheckBox", args = dict(value = False)),
    dict(name = "peso", ui = "PopUpButton", args = dict(items = pesos)),
    dict(name = "curvas", ui = "CheckBox", args = dict(value = False)),
    dict(name = "salvar", ui = "CheckBox", args = dict(value = False)),
], globals())

#########################################

fontes=[
    'Courier', # 0
    'Courier-Bold', # 1
    'Courier-BoldOblique', # 2
    'Courier-Oblique', # 3
    'CourierNewPS-BoldItalicMT', # 4
    'CourierNewPS-BoldMT', # 5
    'CourierNewPS-ItalicMT', # 6
    'CourierNewPSMT', # 7
]

if not peso:
    # versao bold
    f_autor=fontes[5]
    f_obra=fontes[5]
    f_info=fontes[0]
    f_cortesia=fontes[3]
    f_txt_it=fontes[4]
    f_txt={
        'pt':fontes[5],
        'en':fontes[5],
    }
elif peso==1:
    # versao light
    f_autor=fontes[5]
    f_obra=fontes[5]
    f_info=fontes[7]
    f_cortesia=fontes[6]
    f_txt_it=fontes[3]
    f_txt={
        'pt':fontes[0],
        'en':fontes[0],
    }

f_aviso=fontes[5]

# fontSize
fs=1.0*cm
fst=1.36*cm #titulo
fsa=0.85*cm #aviso

#lineHeight
lh=1.5*cm
lhi=1.4*cm #info
lhi1=lhi*1.5 #espaco info1
lhi2=lhi*.5 #espaco info2
lht=2.0*cm #titulo
lht2=lht*.8 #espaco
lha=1.2*cm #aviso

#align
a=['right','left']

#paragrafo
pti=0.0*cm
pt=lh*.9 #texto

#entreletra
elt=2 #titulo
el=-0.5 #normal
elq=-1 #qctx
elc=-1 #condensed
ela=1.5 #aviso

fmt_tit = FormattedString(
    fontSize=fst, 
    lineHeight=lht,
    align=a[0],
    cmykFill=(0,0,0,1),
    tracking=elt,
)
fmt_txt = FormattedString(
    fontSize=fs, 
    lineHeight=lhi,
    align=a[1],
    paragraphTopSpacing=pti,
    cmykFill=(0,0,0,1),
    tracking=el,
)
fmt_aviso = FormattedString(
    fontSize=fsa, 
    lineHeight=lha,
    align=a[1],
    cmykFill=(0,0,0,0),
    tracking=ela,
    font=f_aviso,
)

# formata texto
txt_obras={}
for eixo in base_obras:
    if eixo not in txt_obras:
        txt_obras[eixo]={}

    for n in base_obras[eixo]:
        numero=(eixo,n)
        if n not in txt_obras[eixo]:
            txt_obras[eixo][n]={}
        
        obra=txt_obras[eixo][n]
        b_obra=base_obras[eixo][n]
        
        for l in linguas:
            obra[l]={}
            
            obra[l]['titulo']=fmt_tit.copy()
            
            autor=b_obra[l]['autor'].upper()

            # # arquivo imagem:
            # obra[l]['titulo'].append('%s-%s-%s\n'%(eixo,n,l),font=f_autor,align=a[0],cmykFill=(1,0,0,0),)
            
            obra[l]['titulo'].append(autor,font=f_autor,align=a[0],cmykFill=(0,0,0,1),)
            obra[l]['titulo'].append('\n',lineHeight=lht2,)
            
            obra[l]['texto']=fmt_txt.copy()
            
            if 'info' in b_obra[l]:
                alinha=a[1]
                novo=0
                for i,info in enumerate(b_obra[l]['info']):
                    # titulo da obra
                    if not i or ', 19' in info or ', 20' in info:
                        if novo:
                            alinha=a[0]
                            obra[l]['texto'].append('\n',lineHeight=lhi1,)
                            novo=0
                        info=info.split(', ')
                        
                        if len(info)==1:
                            info.append('')
                        elif len(info)>2:
                            info=[', '.join(info[:-1]),info[-1]]
                        
                        if numero in [(3,3),(1,12)]: #isamu
                            el_=elc
                        else:
                            el_=el

                        obra[l]['texto'].append(info[0].upper(),font=f_obra,align=alinha,lineHeight=lhi,tracking=el_)
                        obra[l]['texto'].append(qctx(fs,enter=0,espaco=1,alinha=alinha),)
                        obra[l]['texto'].append(info[1]+'\n',font=f_info,align=alinha,tracking=el_,)
                    
                    elif 'Cortesia' in info or 'Courtesy' in info:
                        obra[l]['texto'].append(info+'\n',font=f_cortesia,align=alinha,tracking=el)
                    
                    else:
                        if novo==0:
                            novo=1
                            obra[l]['texto'].append('\n',lineHeight=lhi2,)
                        obra[l]['texto'].append(info+'\n',font=f_info,align=alinha,lineHeight=lh,tracking=el,)
            obra[l]['texto'].append('\n',lineHeight=lhi2,tracking=el)

            if 'texto' in b_obra[l]:
                for p,par in enumerate(b_obra[l]['texto']):
                    #italico
                    par=par.split('%%')
                    for it,par in enumerate(par):
                        if it%2:
                            obra[l]['texto'].append(par,font=f_txt_it,align=a[1],lineHeight=lh,paragraphTopSpacing=pt,)
                        else:
                            obra[l]['texto'].append(par,font=f_txt[l],align=a[1],lineHeight=lh,paragraphTopSpacing=pt,)
                    # if p == len(b_obra[l]['texto'])-1:
                    #     obra[l]['texto'].append(qctx(fs,enter=0,espaco=0))
                    obra[l]['texto'].append('\n',font=f_txt[l],align=a[1],lineHeight=lh,paragraphTopSpacing=pt,)
    
            if 'info_extra' in b_obra[l]:
                info=b_obra[l]['info_extra']
                # underline
                info=info.split('&&')
                for un,info in enumerate(info):
                    if un%2:
                        obra[l]['texto'].append(info,font=f_info,align=a[1],lineHeight=lhi,underline='single')
                    else:
                        obra[l]['texto'].append(info,font=f_info,align=a[1],lineHeight=lhi,underline=None)
                obra[l]['texto'].append('\n',lineHeight=lhi2,tracking=el,)

            obra[l]['texto'].append('\n',lineHeight=lhi,tracking=el,)

            if 'info_autor' in b_obra[l]:
                if numero in [(3,5)]:
                    el_=elc*2
                else:
                    el_=el
                    
                for info in b_obra[l]['info_autor']:
                    obra[l]['texto'].append(info[0],font=f_obra,align=a[0],lineHeight=lhi,paragraphTopSpacing=pti,tracking=el_,)
                    if info[1]:
                        obra[l]['texto'].append(qctx(fs,enter=0,espaco=1))
                        obra[l]['texto'].append(info[1]+'\n',font=f_info,align=a[0],lineHeight=lhi,paragraphTopSpacing=pti,tracking=el_,)
                    else:
                        obra[l]['texto'].append('\n',font=f_obra,align=a[0],tracking=el_)

            # aviso
            obra[l]['aviso']=fmt_aviso.copy()
            if 'aviso' in b_obra[l]:
                aviso=b_obra[l]['aviso']
                aviso=aviso.replace('.',' ')
                obra[l]['aviso'].append(aviso.upper())

#########################################

def desenha_texto(texto,meio_texto,numero):
    hyphenation(False)
    
    col=1 # colunas
    ec=0 # entrecolunas
    
    tit=texto['titulo']
    txt=texto['texto']
    aviso=texto['aviso']
    line_h=lh
        

    tit.append('\n\n')

    w=(pw-me-md-(col-1)*ec)/col
    tw,th=textSize(txt, width=w)
    th=(th/col)/2
    
    outline=BezierPath()
    
    save()
    translate(me,meio_texto)

    for n in range(col):
        if curvas:
            outline.textBox(txt,((tw+ec)*n,-th,tw,2*th))
        else:
            textBox(txt,((tw+ec)*n,-th,tw,2*th))
            
    twt,tht=textSize(tit, width=w)
    if curvas:
        outline.textBox(tit,(0,th,w,tht))
    else:
        textBox(tit,(0,th,w,tht))
        
    if curvas:
        cmykFill(0,0,0,1)
        drawPath(outline)
    
    # aviso
    m2=1*cm
    w=tw/2-2*m2
    aw,ah=textSize(aviso, width=w)
    
    save()
    translate(m2,-th-ah-5*cm)
    cmykFill(0,0,0,1)
    rect(-m2,-m2/2,aw+2*m2,ah+m2)
    
    if curvas:
        outline=BezierPath()
        outline.textBox(aviso,(0,0,aw,ah))
        cmykFill(0,0,0,0)
        drawPath(outline)
    else:
        textBox(aviso,(0,0,aw,ah))
    
    restore()
    
    # imagem
    if numero not in imagens:
        numero=(0,0)
    
    img=imagens[numero][lang]
    imgw,imgh=imageSize(img)
    
    escala=pw/imgw
    save()
    translate(-me,th+tht+10*cm)
    scale(escala)
    image(img, (0,0))
    restore()

    restore()

#########################################

#pagina
pw=30*cm
# ph=90*cm

#margem
me=3.0*cm
md=me

#meio
meio=140*cm

#suportes
#largura do apoio do tecido
# if escala_real:
#     apoio=3
# else:
#     apoio=0
apoio=4
base_min=50
base_max=90

suporte={
    'autoportante':{
        'altura':220+apoio/2,
        'total':0,
    },
    'bandeira':{
        'altura':250+apoio/2,
        'total':0,
    },
}
# calcula o tamanho total do tecido
for tipo in suporte:
    tipo=suporte[tipo]
    altura=tipo['altura']
    media=((altura-base_min)+(altura-base_max))/2
    tipo['total']=2*media

print(suporte)
#imagens
imagens={}
for img in img_lista:
    nome=img.split('.')[0]
    nome=nome.split('-')
    numero=(int(nome[0]),int(nome[1]))
    lang=nome[2]
    if numero not in imagens:
        imagens[numero]={}
    imagens[numero][lang]= os.path.join(path_img,img)

sala=[(1,1),(1,2),(1,3),]

if ver == len(obras_lista)-1:
    ver=[(1,2),(1,3),(1,6),(2,6),(2,8),(2,10),]
elif ver == len(obras_lista)-2:
    ver=[(1,11),(1,12)]
elif ver == len(obras_lista)-3:
    ver=sala
elif ver == len(obras_lista)-4:
    ver=(0,0)
else:
    ver=obras_lista[ver].split('_')
    ver=( int(ver[0]),int(ver[1]) )

for eixo in txt_obras:
    if eixo == ver[0] or ver[0]==0 or type(ver)==type([]):
        newPage(pw,50)
        fill(0,1,1)
        rect(0,0,width(),height())
        fill(0)
        fontSize(height())
        text(str(eixo),(width()/2,0),align='center')
    
        for obra in txt_obras[eixo]:
            numero=(eixo,obra)
            
            if type(ver) == type([]):
                if numero in ver:
                    v=numero
                else:
                    v=(4,20)
            else:
                v=ver
            
            if obra == v[1] or v[1]==0:
                if numero in sala:
                    tipo='autoportante'
                else:
                    tipo='bandeira'
                
                altura=suporte[tipo]['altura']*cm
                total=suporte[tipo]['total']*cm
                
                if not escala_real:
                    zoom=0.10
                    newPage(300*cm*zoom,320*cm*zoom)
                    # fundo
                    fill(.85)
                    rect(0,0,width(),height())
                    scale(zoom)
                    #meio
                    fill(.3)
                    fontSize(4*cm)
                    txt='%s cm'%round(meio/cm,1)
                    text(txt,(7*cm,meio+70))
                    stroke(.3)
                    lineDash(20, 40)
                    line( (0,meio),(width()/zoom,meio) )
                    stroke(None)

                for l,lang in enumerate(linguas):

                    pdf='pdf/grafica/0/obras/1/%s-%s-%s.pdf' % (eixo,obra,l)

                    if grafica:
                        if not os.path.isfile(pdf):
                            pdf='pdf/grafica/0/obras/1/%s-%s-%s.pdf' % (0,0,l)
                        pdf=os.path.join( path,pdf )
                        
                        imgw,imgh=imageSize(pdf)
                        ph=imgh
                        base=altura-ph
                        
                    else:
                        if not l:
                            base=randint(base_min,base_max)*cm
                            # base=base_max*cm
                            ph=altura-base
                            h2=total-ph
                        else:
                            ph,h2=h2,ph
                            base=altura-ph
                    
                    # nome
                    nome='%s_%s' % (eixo,obra)
                    for item in obras_lista:
                        if item[:3] == nome:
                            nome=item
                            break

                    print()
                    print(nome, lang)
                    print('tecido = %scm x %s cm' % (round(pw/cm,1),round(ph/cm-apoio/2,1)))
                    print('apoio_largura = %scm' % (round(apoio,1)))
                    print('altura = %scm' % (round(base/cm,1)))
                    
                    meio_texto=meio-base
                    
                    if escala_real:
                        newPage(pw,ph)
                    else:
                        dist=58*cm
                        save()
                        if not l:
                            fill(0)
                            rect(0,altura,90*cm,-2*cm)
                            translate(dist,base)
                        else:
                            translate(width()/zoom,0)
                            fill(0)
                            rect(0,altura,-90*cm,-2*cm)
                            translate(-dist-pw,base)
                        save()
                        fill(1)
                        rect(0,0,pw,ph)
                        restore()
                    
                    if grafica:
                        image(pdf,(0,0))
                    else:
                        desenha_texto(txt_obras[eixo][obra][lang],meio_texto,numero)
                    
                    if escala_real:
                        if salvar:
                            path_save=os.path.join( path,pdf )
                            saveImage(path_save, multipage=False)
                            print('salvo', randint(2,19)*choice(['>','=']))
                            print(path_save)
                    else:
                        restore()

                if not escala_real:
                    fill(.85)
                    rect(0,altura,width()/zoom,height()/zoom-altura)

                    # modulor
                    blendMode('darken')
                    for i in range(randint(1,1)):
                        modulor = os.path.join(path,'img/escala/modulor%s.pdf' % randint(0,3))
                        save()
                        translate(width()/zoom/2,0)
                        scale(choice([-1,1]),1)
                        scale(cm)
                        image(modulor,(0,0))
                        restore()

#########################################

end = time.time()
print('\n>>>', end-start, 's')
