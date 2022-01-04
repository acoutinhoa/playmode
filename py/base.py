from random import choice

def pixel(car,bezier,i,j,m,var=1):
    x=i*var
    y=j*var
    if car == '#':
        bezier.rect(x,y,m,m)
    elif car == 'o':
        bezier.oval(x,y,m,m)
    elif car == 't':
        bezier.polygon((x,y),(x+m/2,y+m),(x+m,y))
    elif car == '+':
        bezier.rect(x+m/4,y,m/2,m)
        bezier.rect(x,y+m/4,m,m/2)
    elif car == 'X':
        n=3
        bezier.polygon((x,y),(x+m/n,y),(x+m,y+m),(x+m-m/n,y+m))
        bezier.polygon((x+m-m/n,y),(x+m,y),(x+m/n,y+m),(x,y+m),)
    elif car == 'x':
        n=4
        bezier.polygon((x+m/n,y),(x+m,y+m-m/n),(x+m-m/n,y+m),(x,y+m/n))
        bezier.polygon((x,y+m-m/n),(x+m-m/n,y),(x+m,y+m/n),(x+m/n,y+m))
    return bezier


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

