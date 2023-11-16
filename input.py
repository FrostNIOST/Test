def ingrese_fecha (fecha):
    while True:
        fecha =input("Ingrese una fecha con el formato mm/aaaa (con'/' incluido): ") 
        m, a = separar_fecha(fecha)
        
        if m != 0:
            break
        else:
            print("Ingrese la fecha con el formato requerido!")
    return m, a  
def separar_fecha(fecha):
    while True:        
        try:                 
            m=int(fecha[0:2])
            a=int(fecha[3:7])
        except:
            m=0
            a=0
        if m < 1 or m > 12 :
            m = 0
        return m, a