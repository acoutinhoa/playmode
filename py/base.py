from random import choice,randint


def var(v,v0=None,lista=[],tipo='',cor_mode=0):
    if not v:
        if not v0:
            if lista:
                if tipo == 'lista':
                    v=randint(1,len(lista)-1)
                else:
                    v=choice(lista[1:])
            elif tipo in ['int','float']:
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
        if lista and tipo!='lista':
            v=lista[v]
        elif tipo=='int':
            v=int(v)
        elif tipo=='float':
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

def car_texto(car,car_c,i,j,texto,ajuste=0):
    if texto == 2:
        car_n=(car_c+i+ajuste)%len(car)
    elif texto == 3:
        car_n=(car_c+i+j+ajuste)%len(car)
    elif texto == 4:
        car_n=car_c%len(car)
        car_c+=1
    car=car[car_n]
    return car,car_c

def pixel(ponto,m,car_c,bezier,formas,texto,ajuste_txt=0):
    car,x,y,i,j = ponto

    if car not in formas.keys():
        car,car_c=car_texto(car,car_c,i,j,texto,ajuste_txt)
    
    bezier.translate(-x,-y)
    bezier.appendPath(formas[car])
    bezier.translate(x,y)

    return bezier,car_c

def cor(cores,cor_repetida=None):
    if type(cores) == type(''):
        c_lista=[c for c in cores]
        c=choice(c_lista)
        if c == 'r':
            c=(1,0,0)
        elif c == 'g':
            c=(0,1,0)
        elif c == 'b':
            c=(0,0,1)
        elif c == 'c':
            c=(0,1,1)
        elif c == 'm':
            c=(1,0,1)
        elif c == 'y':
            c=(1,1,0)
        elif c == 'k':
            c=(0,0,0)
        elif c == 'w':
            c=(1,1,1)
        else:
            c='cor nao definida'
        
        while c == cor_repetida:
            c=cor(cores,cor_repetida)
    elif type(cores) == []:
        c=choice(cores)
    else:
        c=cores
        
    return c
