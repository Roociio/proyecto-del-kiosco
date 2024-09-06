from productos import Productos #aca importe los archivos al main
from ventas import Ventas 
from proveedores import Proveedores
menu = input("Elija que desea modificar (Ventas, Proveedores o Productos):  ") #declaro la variable menu q voy a utilizar para la eleccion de los archivos
eleccion =""
if menu == "Ventas": #aplico un condicional en caso que el usuario elija la opcion ventas
        eleccion = input("Elija que desea realizar:")  
        if eleccion == "Crear": # aplico condicional para la eleccion de algun metodo del crud
                producto = input ("Ingrese nombre del producto: ") #aca puse inputs para ingresar los valores a la tabla
                precio = int (input("Ingrese precio: "))
                cantidad = int (input("Ingrese la cantidad: "))
                fecha = (input("Ingrese la fecha (dd/mm/aaaa): "))
                manejoVentas = input ("Ingrese el manejo de las ventas: ")
                ventas = input ("Ingrese las ventas: ")
                ventas = Ventas (producto , precio , cantidad , fecha , manejoVentas , ventas ) #aca cree del objeto
                ventas.crear() # aca llame al metodo crear
        elif eleccion == "Leer": 
                ventas = Ventas () #no le pase los atributos porque no hacen falta para el metodo que vamos a usar
                ventas.leer()
        elif eleccion == "Actualizar":
                producto = input ("Ingrese nombre del producto: ")
                precio = int (input("Ingrese precio: "))
                cantidad = int (input("Ingrese la cantidad: "))
                fecha = (input("Ingrese la fecha (dd/mm/aaaa): "))
                manejoVentas = input ("Ingrese el manejo de las ventas: ")
                ventas = input ("Ingrese las ventas: ")
                id_ingresada = int(input("ingrese la id de la venta a actualizar: "))#se ingresa la id de la fila q se va a actualizar
                ventas=Ventas (producto, precio, cantidad, fecha, manejoVentas, ventas)
                ventas.actualizar (id_ingresada) #id esta aca porque es un dato necesario para el metodo
        elif eleccion == "Eliminar": 
                id_ingresada = int(input("ingrese la id de la venta que desee eliminar: "))
                ventas = Ventas( )
                ventas.eliminar(id_ingresada)
elif menu== "Productos":
        eleccion = input("Ingrese que desea realizar: ")
        if eleccion == "Crear":
                nombre = input ("Ingrese nombre del producto: ")
                vencimiento = (input("Ingrese la fecha de vencimiento (dd/mm/aaaa): "))
                marca = input("Ingrese la marca: ")
                lote = int (input("Ingrese el lote: "))
                proveedores = input ("Ingrese los proveedores: ")
                producto = Productos (nombre , vencimiento , marca , lote , proveedores)
                producto.crear()
        elif eleccion == "Leer":
                producto = Productos ()
                producto.leer()
        elif eleccion == "Actualizar":
                producto = input ("Ingrese nombre del producto: ")
                precio = int (input("Ingrese precio: "))
                cantidad = int (input("Ingrese la cantidad: "))
                fecha = (input("Ingrese la fecha (dd/mm/aaaa): "))
                ventas = input ("Ingrese las ventas: ")
                manejoVentas = input ("Ingrese el manejo de las ventas: ")
                id_ingresada = int(input("ingrese la id de la venta a actualizar: "))
                producto= Productos (producto, precio, cantidad, fecha, ventas, manejoVentas)
                producto.actualizar (id_ingresada)
        elif eleccion == "Eliminar": 
                id_ingresada = int(input("ingrese la id del producto que desee eliminar: "))
                producto = Productos ( )
                producto.eliminar(id_ingresada)   
elif menu== "Proveedores":
         eleccion = input("elija que desea realizar:")
         if eleccion== "Crear":
                nombre= input("ingrese nombre: ")
                empresa= input("ingrese empresa: ")
                marca= input ("ingrese marca: ")
                manejoProveedores= input ("ingrese el manejo de proveedores:")
                proveedor = Proveedores(nombre , empresa , marca , manejoProveedores )
                proveedor.crear()
         elif eleccion== "Leer":
                proveedor = Proveedores()
                proveedor.leer()
         elif eleccion== "Actualizar":
                nombre= input("ingrese nombre: ")
                empresa= input("ingrese empresa: ")
                marca= input ("ingrese marca: ")
                manejoProveedores= input ("ingrese el manejo de proveedores: ")
                id_ingresada = int(input("ingrese la id del proveedor a actualizar: "))
                proveedor = Proveedores(nombre , empresa , marca , manejoProveedores)
                proveedor.actualizar(id_ingresada)
         elif eleccion == "Eliminar": 
                id_ingresada = int(input("ingrese la id del proveedor a eliminar: "))
                proveedor = Proveedores( )
                proveedor.eliminar(id_ingresada)






        