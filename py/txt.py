import time
start = time.time()

import os
from base import var,cor
from docx import Document

# caminho da pasta do playmode
path='/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])

#-------------------

#https://python-docx.readthedocs.io/en/latest/index.html

# https://www.geeksforgeeks.org/python-working-with-docx-module/

# https://automatetheboringstuff.com/chapter13/

#-------------------

#####################################

# visualizar atributos do objeto
# nao ta funcionando mais :(
def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

# ver texto sem formatacao
def getText(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#########################################

# unidades
cm = 72/2.54
mm = cm/10
print('>>> 1px == 1cm')

# docx
doc_path = os.path.join(path,'_/txt/Textos.docx')
doc = Document(doc_path)

#########################################

# # # # aberturas = os.path.join(path_txt,'aberturas.txt')
# # # # with open(aberturas, encoding="utf-8") as file:
# # # #     aberturas = file.read()

# # # # # textos
# # # # aberturas=aberturas.split('###')
# # # # aberturas={i:txt.split('___') for i,txt in enumerate(aberturas)}

# fontes_do_pc = ['?',]+installedFonts()

# Variable([
#     dict(name = "tipo", ui = "PopUpButton", args = dict(items = tipos)),
#     dict(name = "altura_randomica", ui = "CheckBox", args = dict(value = True)),
#     dict(name = "autoportante", ui = "CheckBox", args = dict(value = True)),
#     dict(name = "modulor", ui = "CheckBox", args = dict(value = False)),
#     dict(name = "fonte", ui = "PopUpButton", args = dict(items = fontes_do_pc)),
#     dict(name = "cor_suporte", ui="EditText", args=dict(text='k')),
#     dict(name = "alturas", ui = "CheckBox", args = dict(value = False)),
#     dict(name = "gira", ui = "CheckBox", args = dict(value = True)),
#     dict(name = "imagem", ui = "CheckBox", args = dict(value = True)),
#     dict(name = "estampa", ui = "CheckBox", args = dict(value = False)),
# ], globals())
    
# fonte=var(fonte,'HelveticaNeue',lista=fontes_do_pc)
# print('fonte =', fonte)

#########################################

# # print the list of paragraphs in the document
# print('List of paragraph objects:->>>')
# print(doc.paragraphs)
  
# # print the list of the runs 
# # in a specified paragraph
# print('\nList of runs objects in 1st paragraph:->>>')
# print(doc.paragraphs[0].runs)
  
# # print the text in a paragraph 
# print('\nText in the 1st paragraph:->>>')
# print(doc.paragraphs[0].text)
  
# # for printing the complete document
# print('\nThe whole content of the document:->>>\n')
# for para in doc.paragraphs:
#     print(para.text)

#########################################

for p,para in enumerate(doc.paragraphs):
    print('##############')
    print(p)
    # print(para.paragraph_format.left_indent)

    # # # for attr in dir(para):
    # # #     print("obj.%s = %r" % (attr, getattr(para, attr)))

    for r,run in enumerate(para.runs):
        txt=run.text
        
        if txt:
            print('    ',r)
            print(txt)
        
        if run.bold:
            print('    bold')
        if run.italic:
            print('    italico')
        if run.underline:
            print('    --------underline')
        # if str(run.font.color.rgb) == '0070C0':
        if run.font.color.rgb:
            print('    >>>>>>>>>>>>>>>>>>>>>>>>>>', run.font.color.rgb)
        # print(type(run.font.color.rgb))

        # # # for attr in dir(run):
        # # #     print("obj.%s = %r" % (attr, getattr(run, attr)))

    
#########################################

end = time.time()
print('\n>>>', end-start, 's')
