#Ejercicio 1: Crear una clase Persona
#Objetivo: Crear una clase simple con atributos y mostrar su uso.

"""class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1= Persona("camila", 34)
print(f"la persona se llama {persona1.nombre} y tiene {persona1.edad}")"""

#Ejercicio 2: Agregar un método a la clase
#Objetivo: Añadir un comportamiento a la clase con un método.
    
"""class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad}")

persona1= Persona("camila", 34)
print(f"la persona se llama {persona1.nombre} y tiene {persona1.edad}")
persona1.presentarse()"""

#Ejercicio 3: Crear una clase Producto
#Objetivo: Práctica con clases, atributos y lógica básica.

"""class Producto: 
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"nombre: {self.nombre}- $ : {self.precio}- cantidad {self.stock}")

    def vender(self):
        if self.stock > 0:
           self.stock -= 1
           print(f"producto vendido. Quedan {self.stock} unidades")
        else:  
           print(f"no hay stock disponible")
        
producto1= Producto("samsung", 1000, 2)
producto1.mostrar_info()
producto1.vender()"""

#Ejercicio 4: Herencia básica - clase Estudiante
#Objetivo: Crear una subclase que herede de otra.

"""class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        self.nombre= nombre
        self.edad = edad
        self.carrera= carrera

    def datos_estudiante (self):
        print(f"soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}")
Estudiante1= Estudiante("Jose", 34, "arquitectura")
Estudiante1.datos_estudiante()"""

#Ejercicio 5: Usar `super()` en la subclase
#Objetivo: Utilizar `super()` para inicializar atributos del padre.
        
"""class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera= carrera

    def datos_estudiante (self):
        print(f"soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}")
Estudiante1= Estudiante("Jose", 34, "arquitectura")
Estudiante1.datos_estudiante()"""

#Ejercicio 6: Clase Vehiculo y subclases
#Objetivo: Aplicar herencia para crear distintos tipos de objetos.

"""class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar (self):
        print(f"El vehiculo esta en marcha")

Vehiculo1 = Vehiculo ("BMW", 1986)
Vehiculo1.arrancar()

class Auto (Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def tocar_bocina (self):
        print(f"Beep Beep")

class Moto (Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def hacer_wheelie (self):
        print(f"haciendo wheelie")

auto_1= Auto("toyota", 2020)
moto_1= Moto("susuki", 100)

auto_1.arrancar()
auto_1.tocar_bocina()

moto_1.arrancar()
moto_1.hacer_wheelie()"""

#Ejercicio 7: Polimorfismo simple
#Objetivo: Entender cómo distintas clases pueden tener métodos con el mismo nombre pero distinto comportamiento.

"""class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar (self):
        print(f"El vehiculo esta en marcha")

Vehiculo1 = Vehiculo ("BMW", 1986)
Vehiculo1.arrancar()

class Auto (Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def tocar_bocina (self):
        print(f"Beep Beep")
    
    def tipo_vehiculo (self):
        print(f"soy un auto")

class Moto (Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def hacer_wheelie (self):
        print(f"haciendo wheelie")

    def tipo_vehiculo (self):
        print(f"soy una moto")

auto_1= Auto("toyota", 2020)
moto_1= Moto("susuki", 100)

Vehiculo= [auto_1, moto_1]

for vehiculo in Vehiculo:
    vehiculo.tipo_vehiculo ()"""

#Ejercicio 8: Bonus - Inventario de productos (integrador)
#Objetivo: Integrar varios conceptos.

class Producto: 
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
class Inventario:
    def __init__(self):
        self.productos []

    def agregar_producto (self, producto):
        self.productos.append(producto)
        print(f"producto {producto.nombre} agregado al inventario")

    def mostrar_producto (self, nombre):
        if not self.productos:
            print(f"No hay productos para mostrar")
        else:
            print(f"productros encontrados en el inventario")
            for producto in self.productos:
                print(producto)
    
    