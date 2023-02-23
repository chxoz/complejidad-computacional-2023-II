filename = str(input("puedes escoger entre los siguientes archivos:\n"+
                     "ej1 \nej2\nej3 \nej4\nej5"+"\nArchivo:"))# le pedimos al usuario un nombre de archivo
try:#manejamos la ecepcion en caso de que no se ingrese un archivo existente
    with open(filename + ".txt") as f_obj:#abrimos nuestro archivo a codificar
        lines = f_obj.readlines()#leemos todo el contenido del archivo
except FileNotFoundError:
    msg = "el arichivo " + filename + " no existe"#mensaje de error
    print(msg)
else: #si el archivo que nos dio es valido entonces se hacen los pasos del punto 2 de la practica
    large_string = ''#inicializamos una cadena vacia 
    for line in lines:
        large_string += line.strip() #llenamos la cadena previamente inicializada sin espacios en blanco
    s = "$" #el simbolo $ nos indica que estamos por leer el conjunto S
    c = "\\" #el simbolo \\ nos indica que estamos por leer el conjunto C
    k = "#" #el simbolo # nos indica que estamos por leer el valor de K
    if s in large_string:#si se encuentra el simbolo $ en la cadena entonces se siguio la codificacion y se puede continuar
        str_s = str(lines[1]).replace('$',"").replace("\n", "")# quitamos los datos que estorban
        list_s = str_s.split(",") #hacemos una lista para tener los elementos del conjunto S
        l = len(list_s) #variable auxiliar para determinar el tamaño de la lista anterior
        if l >=11:#si es mayor o igual a 1 entonces imprimimos los primeros y ultimos 5 elementos
            aux = l - 5 #auxiliar para el indice de los ultimos elementos
            first = list_s[0:5]
            last = list_s[aux:l]
            print("los primeros 5 y los ultimos 5 elementos de S son :" + str(first) + str(last))
        else:#si es menor a 11 se imprimen todos los elementos de S
            print("elementos del conjunto S: "+ str(list_s))
    else: 
        print("No se encontro el conjunto S en la codificacion")
    if c in large_string:#si \\ esta en la cadena estamos por leer el conjunto C
        str_c = str(lines[2]).replace('\\',"").replace("\n", "")#limpiamos la cadena
        list_c = str_c.split("%")#se crea una lista de conjuntos que estaba separada por %
        l_c = len(list_c)#auxiliar para la longitud
        print("el numero de miembros de c es: " + str(l_c))
    else:
        print("no se encontro el conjunto c en la codificacion")   
    if k in large_string:# si # esta en la cadena estamos por leer el valor de K
        print("Valor de K = " + str(lines[0].replace('#' ,"")))
    else:
        print("no se encontro el valor de K en la codificacion")
f_obj.close()
