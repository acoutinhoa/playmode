
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


