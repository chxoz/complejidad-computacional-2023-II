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
        aux = str(lines[0].replace('#' ,""))
        int_k = int(aux)
        if int_k == 2: 
            str_s = str(lines[1]).replace('$',"").replace("\n", "")
            list_s = str_s.split(",")
            str_c = str(lines[2]).replace('\\',"").replace("\n", "")
            list_c = str_c.split("%") 
            aux_c1 = ''
            aux_c2 = ''
            l=0
            equal = ''
            length_c = len(list_c)
            for i in range(0,length_c):
                aux_c1 = list_c[i]
                l+=1
                for j in range(l,length_c):
                    aux_c2 = list_c[j]
                    aux_cover = aux_c1 + "," + aux_c2
                    cover = aux_cover.split(",")
                    if cover == list_s: 
                        equal = 1
            if equal == 1:            
                print("SI")
                print("S = " + str(list_s).replace("[","{").replace("]","}"))
                print("c1 = {" + str(aux_c1) + "}\n" + "c2 = {" + "" +str(aux_c2)+"}")            
            else: 
                print("NO")    
    else:
        aux = str(lines[0].replace('#' ,""))
        print("El valor de K es:" + aux + " este algoritmo es para K = 2")