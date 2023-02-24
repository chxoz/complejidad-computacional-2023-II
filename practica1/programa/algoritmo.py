# le pedimos al usuario un nombre de archivo
filename = str(input("puedes escoger entre los siguientes archivos:\n"+
                     "ej1 \nej2\nej3 \nej4\nej5"+"\nArchivo:"))
#manejamos la ecepcion en caso de que no se ingrese un archivo existente
try:
    #abrimos nuestro archivo a codificar
    with open(filename + ".txt") as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "el arichivo " + filename + " no existe"#mensaje de error
    print(msg)
else:
    #si el archivo que nos dio es valido entonces se hacen los pasos del punto 3 de la practica
    #inicializamos una cadena vacia
    large_string = '' 
    #llenamos la cadena previamente inicializada sin espacios en blanco
    for line in lines:
        large_string += line.strip() 
    #el simbolo $ nos indica que estamos por leer el conjunto S
    s = "$" 
    #el simbolo \\ nos indica que estamos por leer el conjunto C
    c = "\\"
    #el simbolo # nos indica que estamos por leer el valor de K 
    k = "#" 
    #si se encuentra el simbolo # en la cadena entonces se siguio la codificacion y se puede continuar
    # si # esta en la cadena estamos por leer el valor de K
    if k in large_string:
        #se obtine la cadena que contiene al valor de k 
        aux = str(lines[0].replace('#' ,""))
        #cast de string a int
        int_k = int(aux)
        #si k es igual a dos entonces iniciamos con el algoritmo
        if int_k == 2: 
            #limpiamos la cadena que contiene al conjunto S
            str_s = str(lines[1]).replace('$',"").replace("\n", "")
            #hacemos una lista con los elementos de S
            list_s = str_s.split(",")
            int_s = [int (x) for x in list_s]
            int_s.sort()
            #limpiamos la cadena que contiene al conjunto C
            str_c = str(lines[2]).replace('\\',"").replace("\n", "")
            #hacemos una lista con los elementos de C
            list_c = str_c.split("%") 
            #auxiliar para guardar los valores de c1 en el ciclo for
            aux_c1 = ''
            #auxiliar para guardar los valores de c2 en el ciclo for
            aux_c2 = ''
            #variable para mutar dentro de la condicional del segundo for
            c1 = ''
            #variable para mutar dentro de la condicional del segundo for
            c2 = ''
            #auxiliar para hacer un rango dinamico en el range del for anidado
            l=0
            #auxiliar para guardar si hay solucion para el ejemplar o no
            equal = ''
            #variable para el rango 
            length_c = len(list_c)
            #cilo for que fija el primer subconjunto de c para comparar con los siguientes
            for i in range(0,length_c):
                #variable que guarda el subconjunto en la posicion i
                aux_c1 = list_c[i]
                #lista con elementos 'x'  con x un valor numerico hecho cadena
                list_c1 = aux_c1.split(",")
                #lista que se pasa a int para poder hacer un sort
                int_c1 = [int(x) for x in list_c1]
                #lista ordenada
                int_c1.sort()
                l+=1
                for j in range(l,length_c):
                    aux_c2 = list_c[j]
                    aux_cover = aux_c1 + "," + aux_c2
                    #aux_cover_reverse = aux_c2 + "," + aux_c1
                    #cover_reverse = aux_cover_reverse.split(",")
                    cover = aux_cover.split(",")
                    int_cover = [int (x) for x in cover]
                    int_cover.sort()
                    print(int_s)
                    print("++++++++++++++++++++")
                    print(int_cover)
                    if int_cover == int_s: 
                        equal = 1
                        c1 = aux_c1
                        c2 = aux_c2
            if equal == 1:            
                print("SI")
                print("S = " + str(list_s).replace("[","{").replace("]","}"))
                print("c1 = {" + str(c1) + "}\n" + "c2 = {" + "" +str(c2)+"}")            
            else: 
                print("NO")    
    else:
        aux = str(lines[0].replace('#' ,""))
        print("El valor de K es:" + aux + " este algoritmo es para K = 2")