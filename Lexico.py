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
            
def operaciones_relaciones(texto, linea):
    
    menor = r"\b<\b"
    menorigual = r"\b<=\b"
    mayor = r"\b>\b"
    mayorigual=r"\b>=\b"
    igualdad = r"\b==\b"
    distinto =r"\b!=\b"
    asignacion =r"\D="
    val1 = re.findall(menor, texto)
    val2 = re.findall(menorigual, texto)
    val3 = re.findall(mayor, texto)
    val4 = re.findall(mayorigual, texto)
    val5 = re.findall(igualdad, texto)
    val6 = re.findall(distinto, texto)
    val7 = re.findall(asignacion, texto)
    im(val1,linea,"Menor que: ")
    im(val2,linea,"Menor igual: ")
    im(val3,linea,"Mayor: ")
    im(val4,linea,"Mayor igual: ")
    im(val5,linea,"Igualdad: ")
    im(val6,linea,"Distinto: ")
    im(val7,linea,"Asignacion: ")
    
def bloques(texto, linea):
    #linea
    inicio_parentesis  = r"\("
    final_parentesis  = r"\)"

    inicio_corchete  = r'\['
    final_corchete  = r'\]'
    inicio_bloque   = r'{'
    final_bloque  = r'}'

    comillas_dobles    = r'\"'
    comillas_simples = r'\''

    val1 = re.findall(inicio_parentesis,texto)
    im(val1,linea,"Inicio parentesis: ")
    val2 = re.findall(final_parentesis,texto)
    im(val2,linea,"Fin parentesis: ")

    val3 = re.findall(inicio_corchete,texto)
    im(val3, linea, "Inicio corchetes: ")
    val4 = re.findall(final_corchete,texto)
    im(val4,linea,"Final corchetes: ")

    val5 = re.findall(inicio_bloque,texto)
    im(val5,linea,"Inicio bloque: ")
    val6 = re.findall(final_bloque,texto)
    im(val6,linea,"Final bloque: ")
    val7 = re.findall(comillas_dobles,texto)
    im(val7,linea,"Comillas dobles: ")
    val8 = re.findall(comillas_simples,texto)
    im(val8,linea,"Comillas simples: ")

def variables_va(texto, linea):
   
    variables_var = r"var*.[a-zA-Z_][a-zA-Z0_9]*"
    variables_let = r"let.[a-zA-Z_][a-zA-Z0_9]*"

    val1 = re.findall(variables_var,texto)
    val2 = re.findall(variables_let,texto)
    respuesta  = val1+val2
    im(respuesta,linea,"Variable: ")


def datos(text, linea):
    #linea
    entero_decimales = r"[+-]?\d+\.?\d*"
    cadena_caracteres = r"[\b\",\b\']\w.+[\"\b,\'\b]"
    boleanos = r"true|false"
    array = r"\[[\W,\w].+\]"
    
    
    numero= re.findall(entero_decimales, text)
    
    cadena = re.findall(cadena_caracteres,text)
    bolean = re.findall(boleanos,text)
    array_data = re.findall(array, text)
    
    im(numero,linea,"Numero: ")
    im(cadena, linea, "Cadena: ")
    im(bolean ,linea,"Boleano: ")
    #im(array_data,linea,"Array: ")
           

print("Ingresa 1 para palabras reservadas")
print("Ingresa 2 para operadores aritmeticos")
print("Ingresa 3 para operadores relacionales")
print("Ingresa 4 para bloques")
print("Ingresa 5 para variables")
print("Ingresa 6 para tipos de datos")
texto = int(input("Digita: "))

while texto != 0: 
    if texto == 1:
        print("\nPalabras reservadas")
        i = 0
        archivo = open("texto.js","r")
        for ii in archivo:
            i+=1
            palabras_reservadas(ii,i)
        archivo.close()
    
    
    if texto == 2:
        print("\nOperadores aritmeticos")
        i = 0
        archivo = open("texto.js", "r")

        for ii in archivo:
            i+=1
            operadores_aritmeticos(ii,i)
        archivo.close()
    
    if texto == 3:
        print("\nOperadores relacionales")
        
        archivo = open("texto.js","r")
        i = 0
        for ii in archivo:
            i+=1
            operaciones_relaciones(ii,i)
        archivo.close()

    if texto == 4:
        print("\nBloques")
        archivo = open("texto.js","r")
        i = 0
        for ii in archivo:
            i+=1
            bloques(ii,i)
        archivo.close()

    if texto == 5:
        print("\nVariables")
        archivo = open("texto.js","r")
        i = 0
        for ii in archivo:
            i+=1
            variables_va(ii,i)
        archivo.close()
    if texto == 6:
        print("\nTipos de datos")
        archivo = open("texto.js","r")
        i = 0
        for ii in archivo:
            i+=1
            datos(ii,i)
            
        archivo.close()
       
    if texto != 1 or texto != 2 or texto !=3 or texto !=4 or texto != 5 or texto != 6:
        print("\n***Ingresa un digito valido***")

    print("Ingresa 1 para palabras reservadas")
    print("Ingresa 2 para operadores aritmeticos")
    print("Ingresa 3 para operadores relacionales")
    print("Ingresa 4 para bloques")
    print("Ingresa 5 para variables")
    print("Ingresa 6 para tipos de datos")
    print("0 para salir")
    texto = int(input("Digita: "))
    

    

