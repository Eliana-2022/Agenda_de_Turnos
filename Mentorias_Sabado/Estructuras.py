#1- Crea una lista con los números del 1 al 5. Muestra el contenido de la lista por pantalla.

# lista= [1 ,2 ,3 ,4 ,5 ]
# print(lista[3])

#2- Crea una lista vacía. Agrega los nombres "Ana", "Luis" y "Carlos" usando el método append() y luego imprime la lista.

#  nombres=[]
#  nombres.append('Ana')
#  nombres.append('Luis')
#  nombres.append('Carlos')

#  for nombre in nombres:
#      print(nombre)


#3- Dada la lista frutas = ["manzana", "banana", "naranja"], cambia el segundo elemento por "pera" y muestra la lista modificada.

# frutas = ["manzana", "banana", "naranja"]
# print(frutas)
# frutas[1] = "pera"
# print(frutas)

#4- Crea una tupla con tres colores: "rojo", "verde", "azul". Muestra el segundo color.

# colores =("rojo", "verde", "azul")
# print(colores[1])

#5- Dada la tupla datos = (10, 20, 30), conviértela en una lista, agrega el número 40, y vuelve a convertirla en tupla.

# datos = (10, 20, 30)
# lista_datos = list (datos)
# lista_datos.append(40)
# datos= tuple(lista_datos)
# print(datos)

#6- Dada la tupla numeros = (1, 2, 2, 3, 4, 2), cuenta cuántas veces aparece el número 2.

# numeros = (1, 2, 2, 3, 4, 2)
# contador= 0
# for numero in numeros:
#     if numero == 2:
#         contador += 1
# print(f"el numero dos aparecio {contador} veces")

#otra forma para hacer lo mismo de arriba
#numeros = (1, 2, 2, 3, 4, 2)
#print(numeros.count(2))

#7- Crea un conjunto a partir de la lista nombres = ["Ana", "Luis", "Ana", "Carlos"] y muestra el resultado.
#Los conjuntos no repiten valores

# nombres = ["Ana", "Luis", "Ana", "Carlos"]
# conjunto_nombres = set(nombres)
# print(conjunto_nombres)

#8- Crea un conjunto con los números del 1 al 5. Pregunta si el número 3 está en el conjunto.

# conjunto = {1, 2, 3, 4, 5}
# print(3 in conjunto)

#9- Dado A = {1, 2, 3} y B = {3, 4, 5}, muestra la intersección de ambos conjuntos.

# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a.intersection(b))

#10- Crea un diccionario con claves "nombre", "edad" y "ciudad", con tus propios datos. Muestra el valor de "ciudad".

# datos = {'nombre': "eliana", 'edad': 34, 'ciudad':"resistencia"}
# print(datos['ciudad'])

#11- Dado el diccionario alumno = {"nombre": "Lucía", "nota": 7}, cambia la nota a 9 y agrega la clave "aprobado" con el valor True.}

# alumno = {"nombre": "Lucía", "nota": 7}
# alumno["nota"]= 9
# alumno["aprobado"]= True
# print(alumno)

#12- Dado el diccionario colores = {"rojo": "red", "azul": "blue", "verde": "green"}, muestra todas las claves y valores uno a uno

# colores = {"rojo": "red", "azul": "blue", "verde": "green"}
# for clave, valor in colores.items():
#     print(f"{clave}, {valor}")

#Para mostrar solo los valores

# colores = {"rojo": "red", "azul": "blue", "verde": "green"}
# for valor in colores.values():
#     print(f"{valor}")

#Para mostrar solo las claves

# colores = {"rojo": "red", "azul": "blue", "verde": "green"}
# for clave in colores:
#     print(f"{clave}")