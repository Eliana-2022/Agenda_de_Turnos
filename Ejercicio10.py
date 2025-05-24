#Escribir un programa que pide al usuario un caracter y muestre por pantalla si es una letra mayuscula, una letra minuscula, un numero o un caracter
#alt+z para poder ver la oracion en toda la pantalla

caracter = input("ingrese un caracter:")

if caracter.islower():
    print("minuscula")
elif caracter.isupper():
    print("mayuscula")
elif caracter.isdigit():
    print("numero")
else:
    print("caracter especial")
    