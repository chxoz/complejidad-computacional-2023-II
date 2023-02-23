filename = str(input('Archivo:'))
try:
    with open(filename) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "el arichivo " + filename + " no existe"
    print(msg)
else: 
    large_string = ''
    for line in lines:
        large_string += line.strip()
    k = "\\\"
    if k in large_string:
        print("Valor de K "+ )
  
