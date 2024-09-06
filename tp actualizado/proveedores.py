import sqlite3
conexion = sqlite3.connect("miDB.db")
cursor = conexion.cursor()
class Proveedores:
    def __init__(self, _nombre = "" , _empresa =" " , _marca ="", _manejoProveedores ="" ) -> None:
        self.nombre = _nombre
        self.empresa = _empresa
        self.marca = _marca
        self.manejoProveedores= _manejoProveedores
    def crear (self):
        cursor.execute(f"INSERT INTO proveedor ( nombre, empresa , marca, manejoProveedores) VALUES ('{self.nombre}','{self.empresa}','{self.marca}','{self.manejoProveedores}')")
        conexion.commit()
        conexion.close()
    def leer (self):
        res = cursor.execute("SELECT * FROM proveedor") #"""selecciona toda la tabla proveedor y la guarda en res """
        resultados = res.fetchall()  #""" devuelve los datos como una lista de tuplas """ 
        for item in resultados:
                print (item)
    def actualizar (self, id_proveedor):
        cursor.execute( (f'  UPDATE proveedor SET nombre = "{self.nombre}", empresa = "{self.empresa}" , marca= "{self.marca}" , manejoProveedores = "{self.manejoProveedores}" WHERE id_proveedor = ?') ,(id_proveedor,))
        conexion.commit ()
    def eliminar (self, id_proveedor):
        cursor.execute (f''' DELETE FROM proveedor WHERE id_proveedor =  ?''',(id_proveedor,)) 
        conexion.commit()
        conexion.close()
        print()
        

