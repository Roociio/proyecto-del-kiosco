"""from proveedores import Proveedores """
import sqlite3
conexion = sqlite3.connect("miDB.db")  
cursor = conexion.cursor() #declare el cursor 
class Productos: #aca cree la clase
    def __init__(self, _nombre="" , _vencimiento="" , _marca ="", _lote="", _proveedores=""): #creacion del constructor con sus respectivos atributos
        self.nombre = _nombre
        self.vencimiento = _vencimiento
        self.marca = _marca
        self.lote = _lote
        self.proveedores = _proveedores
    def crear (self): #creacion de metodo
        cursor.execute(f"INSERT INTO producto ( nombre, vencimiento , marca, lote, proveedores) VALUES ('{self.nombre}','{self.vencimiento}','{self.marca}','{self.lote}', '{self.proveedores}'") #rellena la tabla con los datos que vamos a agregar despues
        conexion.commit() # commit que guarda los cambios
        conexion.close() # para cerrar la bd
    def leer (self):
        res = cursor.execute("SELECT * FROM producto") #selecciona toda la tabla proveedor y la guarda en res 
        resultados = res.fetchall()  # devuelve los datos como una tupla 
        for item in resultados: 
                print (item) #hago un for y un print para que se imprima la tabla
    def actualizar (self, id_producto):
        cursor.execute( (f'  UPDATE producto SET nombre = "{self.nombre}", vencimiento = "{self.vencimiento}" , marca= "{self.marca}" , lote = "{self.lote}" WHERE id_producto = ?'),(id_producto,)) #actualiza los datos de la tabla
        conexion.commit () 
    def eliminar (self,id_producto):
        cursor.execute (f''' DELETE FROM producto WHERE id_producto = ?''',(id_producto,)) #elimina los datos de la tabla
    conexion.commit()
    conexion.close()
    print() 
     

    






        