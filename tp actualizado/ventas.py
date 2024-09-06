import sqlite3
conexion = sqlite3.connect("miDB.db")
cursor = conexion.cursor()

class Ventas:
    def __init__(self, _producto="" , _precio ="", _cantidad="" , _fecha="", _manejoVentas="", _ventas="") -> None:
        self.producto = _producto
        self.precio = _precio
        self.cantidad = _cantidad
        self.fecha = _fecha
        self.manejoVentas = _manejoVentas
        self.ventas = _ventas


    def crear (self):
        cursor.execute(f"INSERT INTO venta ( producto, precio , cantidad, fecha, manejoVentas, ventas) VALUES ('{self.producto}','{self.precio}','{self.cantidad}','{self.fecha}' , '{self.manejoVentas}', '{self.ventas}')")
        conexion.commit()
        conexion.close
    def leer (self):
        res = cursor.execute("SELECT * FROM venta") #"""selecciona toda la tabla proveedor y la guarda en res """
        resultados = res.fetchall()  #""" devuelve los datos como una lista de tuplas """ 
        for item in resultados:
                print (item)
    def actualizar (self, id_venta):
        cursor.execute( (f'  UPDATE venta SET producto = "{self.producto}", precio = "{self.precio}",  cantidad= "{self.cantidad}", fecha = "{self.fecha}", manejoventas = "{self.manejoVentas}", ventas = "{self.ventas}" WHERE id_venta = ?'),(id_venta,))
        conexion.commit ()
        print ()
    def eliminar (self,id_venta):
        cursor.execute (''' DELETE FROM venta WHERE id_venta = ?''',(id_venta,)) 
        conexion.commit()
        conexion.close()
        print()
        
