#Pelota es esferica
#color negra y blanca
#peso
#textura
#rueda
#Un objeto es una instancia de clase


"""class Pelota:
    def __init__(self, color, marca, tamano, deporte):
        self.color = color
        self.marca = marca
        self.tamano = tamano
        self.deporte = deporte

    def rodar (self):
        print(f"la pelota {self.deporte} esta rodando")

mi_pelota1 = Pelota("blanca", "nike", 5, "futbol")
mi_pelota2 = Pelota("rojo", "adidas", 3, "futsal")

print(f"mi pelota es {mi_pelota1.marca}, y color {mi_pelota1.color}")
mi_pelota1.rodar()"""

class Calculadora:
 #Atributos-> como variables
    def __init__(self):
        pass
#Metodos-> como funciones
    def sumar (self, a,b):
        return a + b

    def restar (self, a,b):
        return a - b

    def multiplicar (self, a,b):
        return a * b

    def dividir (self, a,b):
        if b != 0:
           return a / b
        else: return "Error. Division por 0"

mi_calculadora = Calculadora()
print(f"Suma: {mi_calculadora.sumar(3,5)}")