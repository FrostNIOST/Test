#---------------------------------------Funciones--------------------------------------------------
def ingrese_fecha (fecha):
    while True:
        fecha=input("Ingrese una fecha con el formato mm/aaaa (con'/' incluido): ") 
        m, a = separar_fecha(fecha)
        
        if m != 0:
            break
        else:
            print("Ingrese la fecha con el formato requerido!")
    return m, a    
#------------------------------------Separar fecha--------------------------------------------------
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
#------------------------------------------Zeller----------------------------------------------------
def algoritmoZeller(dd, mm, aaaa):
    a = int((14 - mm) / 12)
    y = aaaa - a
    m = int(mm + (12 * a) - 2)
    d = int(dd + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
    return d
#--------------------------------------Programa principal--------------------------------------------
tabla = [0, 31, 29, 31, 30, 31, 31, 30, 31, 30, 31] #ultimos dias de los meses
nombres_mes = ["", "Enero", "Febrero", "Marzo", "abril",
              "Mayo","Junio", "Julio","Agosto",
              "Septiembre","Octubre", "Diciembre"
              ]
#--------------------------------Ingresar fecha, separando mes y anio---------------------------------
mm, aaaa = ingrese_fecha()
#--------------------buscar eltumo dia del mes y anio (pendiente de anio bisiesto----------------------
primerDia = algoritmoZeller (1, mm, aaaa)
ultimoDia = tabla [mm]
#---------------------------------------Dibujar tablas------------------------------------------------
linea = "├─────┼─────┼─────┼─────┼─────┼─────┼─────┤"
print ()
print(f"{nombres_mes[mm]} de {aaaa}")
print("┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐") 
print("│  Dom│  Lun│  Mar│  Mie│  Jue│  Vie│  Sab│")
print(linea)
#------------------------------------------Columna actual-----------------------------------------------
col=0
#--------------------------------------Dibujas cajas vacias---------------------------------------------
linea2 = "|"
for i in range (0, primerDia):
    linea2 += "    |"
    col +=1
#---------------------------------Dibujar cajas con numero de dia---------------------------------------
for i in range (1, ultimoDia + 1):
    linea2 += ""+str(i)
    if i > 9:
        linea2 += "|"
    else:
        linea2 += " |"
    col +=1 
    if col > 6:
        print (linea2)
        print (linea)
        linea2 = "|"
        col = 0 
#----------------------------------Dibujar cierre de caja--------------------------------------------------
if col > 0:
    for i in range (col, 7):
        linea2 += "    |"
    print(linea2)
#------------------------------------Dibujar cierres de caja-------------------------------------------------        
print ("└─────┴─────┴─────┴─────┴─────┴─────┴─────┘")