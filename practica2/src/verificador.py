file_entrada = str(input("Escribe con que ejemplar quieres trabajar\n"+
                         "Puedes escoger entre los siguientes archivos:\n"+
                         "ej1 \nej2\nej3"+"\nArchivo:"))# le pedimos al usuario un nombre de archivo

if file_entrada=="ej1":
   certificados="cer1 \ncer2\ncer3\ncer4\ncer5"+"\nArchivo:"

if file_entrada=="ej2":
   certificados="cer6 \ncer7\ncer8\ncer9\ncer10"+"\nArchivo:"

if file_entrada=="ej3":
   certificados="cer11 \ncer12\ncer13\ncer14\ncer15"+"\nArchivo:"   

file_cer=str(input("Escribe el archivo donde tienes el certificado\n"
                   +"Puedes escoger entre los siguientes archivos:\n"+
                   certificados))

try:#manejamos la ecepcion en caso de que no se ingrese un archivo existente
    with open(file_entrada + ".txt") as f_obj:#abrimos nuestro archivo a codificar
        lines = f_obj.readlines()#leemos todo el contenido del archivo
except FileNotFoundError:
    msg = "El archivo " + file_entrada + " no existe"#mensaje de error
    print(msg)
else:
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
        """if l >=11:#si es mayor o igual a 1 entonces imprimimos los primeros y ultimos 5 elementos
            aux = l - 5 #auxiliar para el indice de los ultimos elementos
            first = list_s[0:5]
            last = list_s[aux:l]
            print("los primeros 5 y los ultimos 5 elementos de S son :" + str(first) + str(last))
        else:#si es menor a 11 se imprimen todos los elementos de S
            print("elementos del conjunto S: "+ str(list_s))
     else: 
        print("No se encontro el conjunto S en la codificacion")"""
     if c in large_string:#si \\ esta en la cadena estamos por leer el conjunto C
        str_c = str(lines[2]).replace('\\',"").replace("\n", "")#limpiamos la cadena
        list_c = str_c.split("%")#se crea una lista de conjuntos que estaba separada por %
        l_c = len(list_c)#auxiliar para la longitud
        
        print("El numero de elementos de S es: "+str(len(list_s)))
        print("El numero de subconjuntos de C es: " + str(l_c))
     else:
        print("No se encontro el conjunto c en la codificacion")   
     if k in large_string:# si # esta en la cadena estamos por leer el valor de K
        print("Valor de K = " + str(lines[0].replace('#' ,"")))
     else:
        print("No se encontro el valor de K en la codificacion")
    
     f_obj.close()

     k=str(lines[0].replace('#' ,""))
     s=len(list_s)
     c=str(l_c)
     
     try:#manejamos la ecepcion en caso de que no se ingrese un archivo existente
      with open(file_cer + ".txt") as f:#abrimos nuestro archivo a codificar
        line = f.readline()#leemos todo el contenido del archivo
     except FileNotFoundError:
      msg = "El arichivo " + file_cer + " no existe"#mensaje de error
      print(msg)
     
     line=line.strip()
     l=len(line)
     subconjuntos=""
     
     for i in range(0,l):
        if line[i]=="1":
           if i==(l-1):
              subconjuntos+=list_c[i]
           else:   
              subconjuntos+=list_c[i]+","

     if(subconjuntos[len(subconjuntos)-1]==","):
       subconjuntos=subconjuntos[0:len(subconjuntos)-1]
     arr_subs=subconjuntos.split(",")  
     
     sin_reps=[]
     for i in range(0,len(arr_subs)):
        if arr_subs[i] not in sin_reps:
           sin_reps.append(arr_subs[i])

     print(sin_reps)
     print(list_s)

     if list_s==sin_reps:
        print("Si, los conjuntos tomados cumplen para ser una cubierta para S")
     else:
        print("No, los conjuntos tomados no cumplen para ser una cubierta para S")   