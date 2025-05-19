#------------------------------------------
#Proyecto - Fundamentos de Progarmacion 01
#------------------------------------------

#------------------------------------------
#Integrantes  
# - Humberto Inope Benites
##------------------------------------------

#Es necesario importar las depencendias necesarias
import datetime

def ingresar_fecha_manual():
    """
    Permite al usuario ingresar una fecha manualmente y la retorna como objeto datetime.
    """
    while True:
        fecha_str = input("Ingrese la fecha (YYYY-MM-DD): ")
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Ingreso mal fecha...!!")


#------------------------------------------
#clase - SEDE
##------------------------------------------
class Sede:
    def __init__ (self,cod, nombre,dire,tele):
        self.cod = cod
        self.nom = nombre
        self.dire = dire 
        self.tele = tele
        
#Coleccion - SEDE 
listaSede = []

#Cargando Data Sede
listaSede.append(Sede(0,"---","      ---","          ---"))
listaSede.append(Sede(1,"PRINCIPAL","JESUS MAIA 350","940122221"))
listaSede.append(Sede(2,"SEDE NORTE","OLIVOS 345","981012450"))
listaSede.append(Sede(3,"SEDE SUR","VILLA EL SALVADOR 890","960245800"))

#Medodo Listar Sedes
def MostrarSedes():
    print("--------------------------------")
    print("******* Listar Sedes *******")
    print("-----------------------------------------------")
    print("Cod NombreSede  Direccion           Telefono")
    print("-----------------------------------------------")
    s = 1
    while s < len(listaSede):
        print(listaSede[s].cod, " ",listaSede[s].nom, " ",listaSede[s].dire, " ",listaSede[s].tele)
        s+=1
#-----------------------------------------------------------------------------------------------------

#------------------------------------------
#clase - Vehiculos
##------------------------------------------
class Vehiculo:
    def __init__ (self,cod, placa,marca,color,tipocombus):
        self.cod = cod
        self.placa = placa
        self.marca = marca
        self.color= color
        self.tipocombus = tipocombus

#Coleccion - Vehiculo
listaVehiculo = []

#Cargando Data Vehiculos
listaVehiculo.append(Vehiculo(0,"---","    ---","     ---","   ---"))
listaVehiculo.append(Vehiculo(1,"BDG-584","KIA","NEGRO","REGULAR"))
listaVehiculo.append(Vehiculo(2,"AAA-541","HYUNDAI","BLANCO","PREMIUM"))
listaVehiculo.append(Vehiculo(3,"FGR-584","TOYOTA","PLATA","REGULAR"))
listaVehiculo.append(Vehiculo(4,"HTR-894","KIA","NEGRO","PREMIUM"))
listaVehiculo.append(Vehiculo(5,"PLI-321","KIA","PLATA","REGULAR"))
listaVehiculo.append(Vehiculo(6,"AZT-123","TOYOTA","NEGRO","PREMIUM"))
listaVehiculo.append(Vehiculo(7,"ATR-567","TOYOTA","BLANCO","PREMIUM"))
listaVehiculo.append(Vehiculo(8,"UHT-582","HYUNDAI","BLANCO","PREMIUM"))
listaVehiculo.append(Vehiculo(9,"BHN-124","HYUNDAI","PLATA","PREMIUM"))

#Medodo Listar Sedes
def MostrarVehiculos():
    print("--------------------------------" )
    print("******* Listar Vehiculos *******")
    print("-----------------------------------------------")
    print("Cod Placa  Marca    Color  TipoCombustible ")
    print("-----------------------------------------------")
    s = 1
    while s < len(listaVehiculo):
        print(listaVehiculo[s].cod, " ",listaVehiculo[s].placa, " ",listaVehiculo[s].marca, " ",listaVehiculo[s].color, " ",listaVehiculo[s].tipocombus)
        s+=1
#-----------------------------------------------------------------------------------------------------    
#------------------------------------------
#clase - SedeVehiculos
##------------------------------------------
class SedeVehiculo:
    def __init__ (self,cod,codSede, codVehi):
        self.cod = cod
        self.codSede = codSede
        self.codVehi = codVehi
       

#Coleccion - Vehiculo
listaSedeVehiculo = []

#Cargando Data Vehiculos por sede
listaSedeVehiculo.append(SedeVehiculo(0,0,0))
listaSedeVehiculo.append(SedeVehiculo(1,1,1))
listaSedeVehiculo.append(SedeVehiculo(2,1,2))
listaSedeVehiculo.append(SedeVehiculo(3,1,3))
listaSedeVehiculo.append(SedeVehiculo(4,2,4))
listaSedeVehiculo.append(SedeVehiculo(5,2,6))
listaSedeVehiculo.append(SedeVehiculo(6,2,8))
listaSedeVehiculo.append(SedeVehiculo(7,3,5))
listaSedeVehiculo.append(SedeVehiculo(8,3,7))
listaSedeVehiculo.append(SedeVehiculo(9,3,9))



#Medodo Listar Sedes
def MostrarSedeVehiculos():
    print("-----------------------------------------------")
    print("******* Listar Sedes x Vehiculos *******")
    print("-----------------------------------------------")
    print("Cod Sede       Placa  TipoCombustible ")
    print("-----------------------------------------------")
    s = 1
    while s < len(listaSedeVehiculo):
        print(listaSedeVehiculo[s].cod, " ",listaSede[listaSedeVehiculo[s].codSede].nom," ",listaVehiculo[listaSedeVehiculo[s].codVehi].placa
              , " ",listaVehiculo[listaSedeVehiculo[s].codVehi].tipocombus)
        s+=1
#-----------------------------------------------------------------------------------------------------    
#------------------------------------------
#clase - Proveedor
##------------------------------------------
class Proveedor:
    def __init__ (self,cod,ruc, razonso, correo, tele):
        self.cod = cod
        self.ruc = ruc
        self.razonso = razonso
        self.correo = correo
        self.tele = tele
       

#Coleccion - Proveedor
listaProveedor = []

#Cargando Data Proveedores 
listaProveedor.append(Proveedor(0,"---","---","---","---"))
listaProveedor.append(Proveedor(1,"10409668670","PETROPERU","PETROPERU@PETROPERU.COM","987654321"))
listaProveedor.append(Proveedor(2,"10458795100","PRIMAX","PRIMAX@PRIMAX.COM","985421500"))
listaProveedor.append(Proveedor(3,"10547812000","PETROMAX","PETROMAX@PETROMAX.COM","968451111"))


#Medodo Listar Proveedor
def MostrarProveedor():
    print("------------------------------------------------------------------------")
    print("******* Listar Proveedores *******")
    print("------------------------------------------------------------------------")
    print("Cod RUC           RAZON SOCIAL       CORREO                  TELEFONO ")
    print("------------------------------------------------------------------------")
    s = 1
    while s < len(listaProveedor):
        print(listaProveedor[s].cod, " ",listaProveedor[s].ruc, "      ",listaProveedor[s].razonso, " ",listaProveedor[s].correo, "         ",listaProveedor[s].tele)
        s+=1

#-----------------------------------------------------------------------------------------------------    
#------------------------------------------
#clase - Operaciones - Donde gestionamos las compras y el consumo de las unidades
#el comsumo se mide en litros 
#Conversion 1 Galon = 3.78 Litros
##------------------------------------------
class Operacines:
    def __init__ (self,cod,tipoopera,codSede, codProvee,tipoCombus,codVehi,fecha,compConsu):
        self.cod        = cod
        self.tipoopera  = tipoopera
        self.codSede    = codSede
        self.codProvee  = codProvee
        self.tipoCombus = tipoCombus
        self.codVehi    = codVehi
        self.fech       = fecha
        self.compConsu  = compConsu
       
#Coleccion - Operaciones
listaOperaciones = []

#Cargando Data Operaciones 
listaOperaciones.append(Operacines(0,"---",1,1,"",1,"",0.00))

#Cargando Data COMPRA MES DE ABRIL de todas la sedes
listaOperaciones.append(Operacines(1,"COMPRA",1,1,"REGULAR",0,"2025-04-01 00:00:00",200.00))
listaOperaciones.append(Operacines(2,"COMPRA",1,1,"PREMIUM",0,"2025-04-01 00:00:00",200.00))
listaOperaciones.append(Operacines(3,"COMPRA",2,2,"REGULAR",0,"2025-04-02 00:00:00",200.00))
listaOperaciones.append(Operacines(4,"COMPRA",2,2,"PREMIUM",0,"2025-04-02 00:00:00",200.00))
listaOperaciones.append(Operacines(5,"COMPRA",3,1,"REGULAR",0,"2025-04-05 00:00:00",200.00))
listaOperaciones.append(Operacines(6,"COMPRA",3,1,"PREMIUM",0,"2025-04-05 00:00:00",200.00))

#Cargando Data DEL COMUSO MES DE ABRIL - SEDE PRINCIPAL
listaOperaciones.append(Operacines(7,"CONSUMO",0,0,"",1,"2025-04-10 00:00:00",20.00))
listaOperaciones.append(Operacines(8,"CONSUMO",0,0,"",1,"2025-04-19 00:00:00",20.00))
listaOperaciones.append(Operacines(9,"CONSUMO",0,0,"",1,"2025-04-30 00:00:00",20.00))

listaOperaciones.append(Operacines(10,"CONSUMO",0,0,"",2,"2025-04-09 00:00:00",20.00))
listaOperaciones.append(Operacines(11,"CONSUMO",0,0,"",2,"2025-04-20 00:00:00",20.00))
listaOperaciones.append(Operacines(12,"CONSUMO",0,0,"",2,"2025-04-28 00:00:00",20.00))

listaOperaciones.append(Operacines(13,"CONSUMO",0,0,"",3,"2025-04-08 00:00:00",20.00))
listaOperaciones.append(Operacines(14,"CONSUMO",0,0,"",3,"2025-04-17 00:00:00",20.00))
listaOperaciones.append(Operacines(15,"CONSUMO",0,0,"",3,"2025-04-25 00:00:00",20.00))

#Cargando Data DEL COMUSO MES DE ABRIL - SEDE NORTE
listaOperaciones.append(Operacines(16,"CONSUMO",0,0,"",4,"2025-04-10 00:00:00",20.00))
listaOperaciones.append(Operacines(17,"CONSUMO",0,0,"",4,"2025-04-19 00:00:00",20.00))
listaOperaciones.append(Operacines(18,"CONSUMO",0,0,"",4,"2025-04-30 00:00:00",20.00))

listaOperaciones.append(Operacines(19,"CONSUMO",0,0,"",6,"2025-04-09 00:00:00",20.00))
listaOperaciones.append(Operacines(20,"CONSUMO",0,0,"",6,"2025-04-20 00:00:00",20.00))
listaOperaciones.append(Operacines(21,"CONSUMO",0,0,"",6,"2025-04-28 00:00:00",20.00))

listaOperaciones.append(Operacines(22,"CONSUMO",0,0,"",8,"2025-04-08 00:00:00",20.00))
listaOperaciones.append(Operacines(23,"CONSUMO",0,0,"",8,"2025-04-17 00:00:00",20.00))
listaOperaciones.append(Operacines(24,"CONSUMO",0,0,"",8,"2025-04-25 00:00:00",20.00))

#Cargando Data DEL COMUSO MES DE ABRIL - SEDE SUR
listaOperaciones.append(Operacines(25,"CONSUMO",0,0,"",5,"2025-04-10 00:00:00",20.00))
listaOperaciones.append(Operacines(26,"CONSUMO",0,0,"",5,"2025-04-19 00:00:00",20.00))
listaOperaciones.append(Operacines(27,"CONSUMO",0,0,"",5,"2025-04-30 00:00:00",20.00))

listaOperaciones.append(Operacines(28,"CONSUMO",0,0,"",7,"2025-04-09 00:00:00",20.00))
listaOperaciones.append(Operacines(29,"CONSUMO",0,0,"",7,"2025-04-20 00:00:00",20.00))
listaOperaciones.append(Operacines(30,"CONSUMO",0,0,"",7,"2025-04-28 00:00:00",20.00))

listaOperaciones.append(Operacines(31,"CONSUMO",0,0,"",9,"2025-04-08 00:00:00",20.00))
listaOperaciones.append(Operacines(32,"CONSUMO",0,0,"",9,"2025-04-17 00:00:00",20.00))
listaOperaciones.append(Operacines(33,"CONSUMO",0,0,"",9,"2025-04-25 00:00:00",20.00))

#Cargando Data COMPRA MES DE ABRIL de todas la sedes
listaOperaciones.append(Operacines(34,"COMPRA",1,1,"REGULAR",0,"2025-05-01 00:00:00",100.00))
listaOperaciones.append(Operacines(35,"COMPRA",1,1,"PREMIUM",0,"2025-05-01 00:00:00",100.00))
listaOperaciones.append(Operacines(36,"COMPRA",2,2,"REGULAR",0,"2025-05-02 00:00:00",100.00))
listaOperaciones.append(Operacines(37,"COMPRA",2,2,"PREMIUM",0,"2025-05-02 00:00:00",100.00))
listaOperaciones.append(Operacines(38,"COMPRA",3,1,"REGULAR",0,"2025-05-05 00:00:00",100.00))
listaOperaciones.append(Operacines(39,"COMPRA",3,1,"PREMIUM",0,"2025-05-05 00:00:00",100.00))

#Cargando Data DEL COMUSO MES DE MAYO - SEDE PRINCIPAL 
listaOperaciones.append(Operacines(40,"CONSUMO",0,0,"",1,"2025-05-10 00:00:00",20.00))
listaOperaciones.append(Operacines(41,"CONSUMO",0,0,"",1,"2025-05-19 00:00:00",20.00))
listaOperaciones.append(Operacines(42,"CONSUMO",0,0,"",1,"2025-05-30 00:00:00",20.00))

listaOperaciones.append(Operacines(43,"CONSUMO",0,0,"",2,"2025-05-09 00:00:00",20.00))
listaOperaciones.append(Operacines(44,"CONSUMO",0,0,"",2,"2025-05-20 00:00:00",20.00))
listaOperaciones.append(Operacines(45,"CONSUMO",0,0,"",2,"2025-05-28 00:00:00",20.00))

listaOperaciones.append(Operacines(46,"CONSUMO",0,0,"",3,"2025-05-08 00:00:00",20.00))
listaOperaciones.append(Operacines(47,"CONSUMO",0,0,"",3,"2025-05-17 00:00:00",20.00))
listaOperaciones.append(Operacines(48,"CONSUMO",0,0,"",3,"2025-05-25 00:00:00",20.00))

#Cargando Data DEL COMUSO MES DE ABRIL - SEDE NORTE
listaOperaciones.append(Operacines(49,"CONSUMO",0,0,"",4,"2025-05-10 00:00:00",20.00))
listaOperaciones.append(Operacines(50,"CONSUMO",0,0,"",4,"2025-05-19 00:00:00",20.00))
listaOperaciones.append(Operacines(51,"CONSUMO",0,0,"",4,"2025-05-30 00:00:00",20.00))

listaOperaciones.append(Operacines(52,"CONSUMO",0,0,"",6,"2025-05-09 00:00:00",20.00))
listaOperaciones.append(Operacines(53,"CONSUMO",0,0,"",6,"2025-05-20 00:00:00",20.00))
listaOperaciones.append(Operacines(54,"CONSUMO",0,0,"",6,"2025-05-28 00:00:00",20.00))

listaOperaciones.append(Operacines(55,"CONSUMO",0,0,"",8,"2025-05-08 00:00:00",20.00))
listaOperaciones.append(Operacines(56,"CONSUMO",0,0,"",8,"2025-05-17 00:00:00",20.00))
listaOperaciones.append(Operacines(57,"CONSUMO",0,0,"",8,"2025-05-25 00:00:00",20.00))

#Cargando Data DEL COMUSO MES DE ABRIL - SEDE SUR
listaOperaciones.append(Operacines(58,"CONSUMO",0,0,"",5,"2025-05-10 00:00:00",20.00))
listaOperaciones.append(Operacines(59,"CONSUMO",0,0,"",5,"2025-05-19 00:00:00",20.00))
listaOperaciones.append(Operacines(60,"CONSUMO",0,0,"",5,"2025-05-30 00:00:00",20.00))

listaOperaciones.append(Operacines(61,"CONSUMO",0,0,"",7,"2025-05-09 00:00:00",20.00))
listaOperaciones.append(Operacines(62,"CONSUMO",0,0,"",7,"2025-05-20 00:00:00",20.00))
listaOperaciones.append(Operacines(63,"CONSUMO",0,0,"",7,"2025-05-28 00:00:00",20.00))

listaOperaciones.append(Operacines(64,"CONSUMO",0,0,"",9,"2025-05-08 00:00:00",20.00))
listaOperaciones.append(Operacines(65,"CONSUMO",0,0,"",9,"2025-05-17 00:00:00",20.00))
listaOperaciones.append(Operacines(66,"CONSUMO",0,0,"",9,"2025-05-25 00:00:00",20.00))

#Medodo Listar Operaciones 
def MostrarOperaciones():
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("******* Listar Operaciones *******")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Cod TIPOOPERA    SEDE               PROVEEDOR        TIPOCOMBUS     CODVEHI           FECHA                     CANTIDAD LITROS ")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    s = 1
    while s < len(listaOperaciones):
        if listaOperaciones[s].codSede == 0:
            print(
            listaOperaciones[s].cod," ",
            listaOperaciones[s].tipoopera,"    ",
            "-----------",
            "    -----------     ",
            "   -----------    ",
            listaOperaciones[s].codVehi,"-",listaVehiculo[int(listaOperaciones[s].codVehi)].placa,"  ",
            listaOperaciones[s].fech,"      ",
            listaOperaciones[s].compConsu)    
        else:      
            print(
            listaOperaciones[s].cod," ",
            listaOperaciones[s].tipoopera,"     ",
            listaOperaciones[s].codSede,"-",listaSede[int(listaOperaciones[s].codSede)].nom," ",
            listaOperaciones[s].codProvee,"-",listaProveedor[int(listaOperaciones[s].codProvee)].razonso,"       ",
            listaOperaciones[s].tipoCombus,"        ",
            listaOperaciones[s].codVehi,"             ",
            listaOperaciones[s].fech,"      ",
            listaOperaciones[s].compConsu)   
        s+=1

#Medodo Listar Operaciones  
def MostrarCompraXSede(sede, mes):
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("******* Listar Operaciones *******")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Cod TIPOOPERA    SEDE               PROVEEDOR        TIPOCOMBUS     CODVEHI           FECHA                     CANTIDAD LITROS ")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    total = 0.00
    nomSede = ""
    s = 1
    while s < len(listaOperaciones):
        fech = format(listaOperaciones[s].fech)
        fecha = datetime.datetime.strptime(fech, "%Y-%m-%d %H:%M:%S") 
        if int(listaOperaciones[s].codSede) == int(sede) and int(fecha.month) == int(mes):
            nomSede = listaSede[int(listaOperaciones[s].codSede)].nom
            print(
            listaOperaciones[s].cod," ",
            listaOperaciones[s].tipoopera,"     ",
            listaOperaciones[s].codSede,"-",listaSede[int(listaOperaciones[s].codSede)].nom," ",
            listaOperaciones[s].codProvee,"-",listaProveedor[int(listaOperaciones[s].codProvee)].razonso,"       ",
            listaOperaciones[s].tipoCombus,"        ",
            listaOperaciones[s].codVehi,"             ",
            listaOperaciones[s].fech,"      ",
            listaOperaciones[s].compConsu)   
            total = total + int(listaOperaciones[s].compConsu)
        elif int(listaOperaciones[s].codSede) == int(sede) and int(mes) == 0:
            nomSede = listaSede[int(listaOperaciones[s].codSede)].nom
            print(
            listaOperaciones[s].cod," ",
            listaOperaciones[s].tipoopera,"     ",
            listaOperaciones[s].codSede,"-",listaSede[int(listaOperaciones[s].codSede)].nom," ",
            listaOperaciones[s].codProvee,"-",listaProveedor[int(listaOperaciones[s].codProvee)].razonso,"       ",
            listaOperaciones[s].tipoCombus,"        ",
            listaOperaciones[s].codVehi,"             ",
            listaOperaciones[s].fech,"      ",
            listaOperaciones[s].compConsu)   
            total = total + int(listaOperaciones[s].compConsu)
        s+=1
    print("--------------------------------------------------------------------------------------------------------------------------------")    
    print("******* TOTAL DE COMPRAS SEDE : ", nomSede , "                                             TOTAL LT. COMPRADOS  : " , total )
    print("--------------------------------------------------------------------------------------------------------------------------------")

#Medodo Listar Comsumo mensual  
def MostrarComsumoxMes(mes):
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("******* Listar Operaciones *******")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Cod TIPOOPERA    SEDE               TIPOCOMBUS        CODVEHI           FECHA                     CANTIDAD LITROS ")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    total = 0.00
    nomSede = ""
    s = 1
    v = 1
    while s < len(listaOperaciones):
        fech = format(listaOperaciones[s].fech)
        fecha = datetime.datetime.strptime(fech, "%Y-%m-%d %H:%M:%S") 
        if listaOperaciones[s].codSede == 0 and int(fecha.month) == int(mes):     

            while v < len(listaSedeVehiculo):
                    if listaOperaciones[s].codVehi == listaSedeVehiculo[v].codVehi:
                         nomSede = str(listaSedeVehiculo[v].codSede) + " - " +listaSede[int(listaSedeVehiculo[v].codSede)].nom
                    v+=1
            print(
            listaOperaciones[s].cod," ",
            listaOperaciones[s].tipoopera,"     ",          
            nomSede,"     ",
            listaVehiculo[int(listaOperaciones[s].codVehi)].tipocombus,"        ",
            listaOperaciones[s].codVehi,"-",listaVehiculo[int(listaOperaciones[s].codVehi)].placa,"  ",
            listaOperaciones[s].fech,"      ",
            listaOperaciones[s].compConsu)   
            total = total + int(listaOperaciones[s].compConsu)
        elif listaOperaciones[s].codSede == 0 and int(mes)==0:               
            while v < len(listaSedeVehiculo):
                    if listaOperaciones[s].codVehi == listaSedeVehiculo[v].codVehi:
                         nomSede = str(listaSedeVehiculo[v].codSede) + " - " +listaSede[int(listaSedeVehiculo[v].codSede)].nom
                    v+=1
            print(
            listaOperaciones[s].cod," ",
            listaOperaciones[s].tipoopera,"     ",          
            nomSede,"     ",
            listaVehiculo[int(listaOperaciones[s].codVehi)].tipocombus,"        ",
            listaOperaciones[s].codVehi,"-",listaVehiculo[int(listaOperaciones[s].codVehi)].placa,"  ",
            listaOperaciones[s].fech,"      ",
            listaOperaciones[s].compConsu)   
            total = total + int(listaOperaciones[s].compConsu)
        v=1
        s+=1
    print("--------------------------------------------------------------------------------------------------------------------------------")    
    print("******* TOTAL DE COMPRAS     :                                      TOTAL LT. COMPRADOS  : " , total )
    print("--------------------------------------------------------------------------------------------------------------------------------")


#------------------------------------------
# MENU DEL SISTEMA
##------------------------------------------
i=0

while i == 0:
    print("------------------------------")
    print("Menu del sistemas Inicializado")
    print("------------------------------")
    print("1.Registrar Sede")
    print("2.Consultar Sedes")
    print("3.Registrar Vehiculo")
    print("4.Consultar Vehiculos")
    print("5.Registrar Sede x Vehiculo")
    print("6.Consultar Sede x Vehiculo")
    print("7.Registrar Proveedor")
    print("8.Consultar Proveedor")    
    print("9.Registrar Operaciones")
    print("10.Consultar Operaciones")
    print("11.Reporte TipoComsumo x Sede")
    print("12.Reporte de Comsumo x Mes")
    print("13.Salir")
    print("------------------------------")
    
    opcion = int(input())
    if opcion == 1:
        print("****** Registrar Sede *******" )
        cod = len(listaSede) 
        nom = input("Ingrese el nombre de la Sede :"  )
        dire = input("Ingrese el direccion de la Sede :"  )
        tele = input("Ingrese el telefono de la Sede :"  )
        sede = Sede(cod,nom,dire,tele)
        listaSede.append(sede)
        print("--------------------------------")
        print("Se registro la Sede : ",nom )
    elif opcion == 2:

        MostrarSedes()

    elif opcion == 3:
        print("****** Registrar Vehilculo *******" )
        cod = len(listaVehiculo) 
        placa = input("Ingrese la placa del vehiculo :"  )
        marca = input("Ingrese la marca del vehiculo :"  )
        color = input("Ingrese el color del vahiculo :"  )
        tipocombus = input("Ingrese el tipo de combus del vahiculo :"  )
        vehi = Vehiculo(cod,placa,marca,color,tipocombus)
        listaVehiculo.append(vehi)
        print("--------------------------------" )
        print("Se registro el Vehiculo : ",placa )
    elif opcion == 4:
       
        MostrarVehiculos()

    elif opcion == 5:
        print("****** Registrar Sede Vehiculo *******" )
        cod = len(listaSedeVehiculo) 
        codsede = int(input("Ingrese la codSede del vehiculo :"  ))
        codvehi = int(input("Ingrese la codVehi del vehiculo :"  ))
        sedevehi = SedeVehiculo(cod,codsede,codvehi)
        listaSedeVehiculo.append(sedevehi)
        print("--------------------------------")
        print("Se registro la Sede / Vehiculo : ",listaSede[codsede].nom, " - ",listaVehiculo[codvehi].placa)
    elif opcion == 6:
        
        MostrarSedeVehiculos()

    elif opcion == 7:
        print("****** Registrar Proveedor *******" )
        cod = len(listaProveedor) 
        ruc = input("Ingrese el ruc del proveedor :"  )
        razonso = input("Ingrese la Rezon Social del Proveedor :"  )
        correo = input("Ingrese el correo del proveedor :"  )
        tele = input("Ingrese el telefono del Proveedor :"  )
        prove = Proveedor(cod,ruc,razonso,correo,tele)
        listaProveedor.append(prove)
        print("--------------------------------")
        print("Se registro el Proveedor RUC/RAZON SOCIAL : ", ruc , "-",razonso )

    elif opcion == 8:

        MostrarProveedor()
        
    elif opcion == 9:
        print("****** Registrar Operaciones *******" )
        cod = len(listaOperaciones) 
        tipoopera = input("Ingrese el TipoOperacion TIPOS : COMPRA / CONSUMO :"  )       
        #Logica para validar el tipo de operacion COMPRA / CONSUMO
        if tipoopera == "COMPRA":
            codVehi = 0 
            codSede = input("Ingrese el codSede :"  )
            codProvee = input("Ingrese el CodProveedor :"  )
            tipoCombus = input("Ingrese el Tipo de Combustible :"  )
            fecha = ingresar_fecha_manual()
        elif tipoopera == "CONSUMO":
            codVehi = input("Ingrese el codVehiculo :"  )
            codSede = 0
            codProvee = 0
            tipoCombus = " "
            fecha = ingresar_fecha_manual()
        compConsu = input("Ingrese la cantida en Litros :"  )
        opera = Operacines(cod,tipoopera,codSede,codProvee,tipoCombus,codVehi,fecha,compConsu)
        listaOperaciones.append(opera)
        print("--------------------------------")
        print("Se registro la Operacion : ", tipoopera , 
              " Sede : ",listaSede[int(codSede)].nom, 
              " Proveedor : ",listaProveedor[int(codProvee)].razonso,
              " Placa : ",listaVehiculo[int(codVehi)].placa," Cant.Litros : ",compConsu )
    elif opcion == 10:    
        MostrarOperaciones()
    elif opcion == 11:    
        codSede = input("Ingrese el codSede :"  )
        codmes = input("Ingrese el mes :"  )
        MostrarCompraXSede(codSede,codmes)
    elif opcion == 12:    
        codmes = input("Ingrese el mes :"  )
        MostrarComsumoxMes(codmes)
    elif opcion == 13:
        exit()
      












