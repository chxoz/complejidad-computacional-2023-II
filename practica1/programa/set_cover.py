filename = str(input('Archivo:'))
try:
    with open(filename + ".txt") as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "el arichivo " + filename + " no existe"
    print(msg)
else: 
    large_string = ''
    for line in lines:
        large_string += line.strip()
    s = "$" 
    c = "\\"
    k = "#"
    if s in large_string:
        str_s = str(lines[1]).replace('$',"").replace("\n", "")
        list_s = str_s.split(",")
        l = len(list_s)
        if l >=11:
            aux = l - 5
            first = list_s[0:5]
            last = list_s[aux:l]
            print("los primeros 5 y los ultimos 5 elementos de S son :" + str(first) + str(last))
        else:
            print("elementos del conjunto S: "+ str(list_s))
            
        
    if k in large_string:
        print("Valor de K = " + str(lines[0].replace('\\' ,"")))
    else:
        print("no se encontro el valor de K en la codificacion")
  
