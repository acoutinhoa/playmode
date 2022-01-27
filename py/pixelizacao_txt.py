import os
from base import var

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

fontes_do_pc = ['?',]+installedFonts()
pm= ['playmode','PLAYMODE', 'PlayMode', 'playMode','play_mode', 'play-mode']

Variable([
    dict(name="w", ui="EditText", args=dict(text='1000')),
    dict(name="h", ui="EditText", args=dict(text='500')),
    dict(name="y", ui="Slider", args=dict(value=1, minValue=0.1, maxValue=4)),
    dict(name="escala", ui="Slider", args=dict(value=10, minValue=1, maxValue=100)),
    dict(name="palavra", ui="EditText", args=dict(text='PLAYMODE')),
    dict(name="fonte", ui="PopUpButton", args=dict(items=fontes_do_pc)),
    dict(name="fonte_size", ui="Slider", args=dict(value=0.30, minValue=0, maxValue=2)),
    # dict(name="salva_imagem", ui="CheckBox", args=dict(value=False)),
], globals())

pw=var(w,tipo='int')
ph=var(h,tipo='int')
e=escala

palavra=var(palavra,choice(pm))
fonte=var(fonte,lista=fontes_do_pc)
fs=(fonte_size/e)*ph

print(palavra)
print()
print('fonte =', fonte)
print()


newPage(pw, ph)

im = ImageObject()
with im:
    size(pw/e,ph/e)
    fill(1)
    rect(0,0,width(),height())
    fill(0)
    font(fonte)
    fontSize(fs)
    text(palavra, (width()/2, (height()-fs/y)/2), align='center')


# # # # # # ########################################

# # # # # # # unidades
# # # # # # # 1 inch = 2.54 cm
# # # # # # # cm = dpi/2.54
# # # # # # # cm = 72/2.54
# # # # # # cm = 36/2.54
# # # # # # mm = cm*10

# # # # # # # banner
# # # # # # pw=230*cm
# # # # # # ph=312*cm

# # # # # # palavra='''PLAY
# # # # # # MODE'''

# # # # # # fs=80



# # # # # # newPage(pw, ph)

# # # # # # im = ImageObject()
# # # # # # with im:
# # # # # #     size(pw/e,ph/e)
# # # # # #     fill(1)
# # # # # #     rect(0,0,width(),height())
# # # # # #     fill(0)
# # # # # #     font(fonte)
# # # # # #     lineHeight(fs-10)
# # # # # #     fontSize(fs)
# # # # # #     text(palavra, (15*cm/e, 190*cm/e), align='left')

# # # # # # ########################################

scale(e)
image(im, (0,0))


# ##########################################
# # pra salvar outras imagens:
# # mudar o valor de n
# ##########################################

# n=1
# path_img=path + '/img/1/playmode_%s_%s.png' % (n,fonte)
# saveImage(path_img)
# print('img salva >>>')
# print(path_img)

            
    