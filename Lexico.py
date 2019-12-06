import re


datos_re = []

def im(lista, numero, texto):
    if lista != []:
        for i in lista:
            print(str(texto) +str(i)+ " Linea "+str(numero))
    
    

def recibe(indice, lista,dt):
    #INDECE , Texto, Dato
    datos_re.append([indice,dt,lista])

def palabras_reservadas(texto, linea):
    palabras_reservadas_patron =r"\bconsole\b|\blog\b|\blet\b|\bvar\b|\bconst\b|\bpush\b|\bpop\b|\bunshift\b|\bshift\b|\bslice\b|\bsplice\b|\breverse\b|\bsplit\b|\bjoin\b|\bsort\b|\bindexOf\b|\bfindIndex\b|\bfind\b|\bnew\b|\bSet\b|\bof\b|\bforEach\b|\bsome\b|\bevery\b|\blenght\b|\bmap\b|\bfilter\b|\breduce\b|\btoFixed\b|\bparseInt\b|\bparseFloat\b|\bMath.random\b|\bthis\b|\bdelete\b|\bObject.getPrototypeOf\b|\bObject.assign\b|\bString.prototype\b|\bhasOwnProperty\b|\blegs\b|\blastIndex\b|\bincludes\b|\bstartsWith\b|\bendsWith\b|\breplace\b|\bsubstr\b|\breturn\b|\bprompt\b|\balert\b|\bArray\b|\bbreak\b|\bcase\b|\bcatch\b|\bclass\b|\bdefault\b|\bdo\b|\belse\b|\belseif\b|\bendsswitch\b|\beval\b|\bextends\b|\bfor\b|\bfunction\b|\bif\b|\bimplements\b|\binclude\b|\binstanceof\b|\binterface\b|\bprint\b|\bprivate\b|\bprotected\b|\bpublic\b|\brequire\b|\bstatic\b|\bswitch\b|\bthrow\b|\btry\b|\buse\b|\bwhile\b|\btrue\b|\bfalse\b"
    respuesta = re.findall(palabras_reservadas_patron, texto)
    im(respuesta,linea,"Palabra reservada: ")
def operadores_aritmeticos(texto, linea):
    operadores_aritmeticos_patron = r"\d+.[-,+,/,*,%,(**)]\d+"
    operadores_aritmeticoss_patron =r"[a-zA-Z_][a-zA-Z0_9]*.[-,+,/,*,%,**][a-zA-Z_][a-zA-Z0_9]*"
    val1 = re.findall(operadores_aritmeticos_patron, texto)
    val2 = re.findall(operadores_aritmeticoss_patron,texto)
    respuesta = val1+val2
    if respuesta != []:
        for i in respuesta:
            print("Operadores aritmeticos: ",i, " Linea: ",linea)
    

