#Comparar dos numeros y decir cual es mayor

numero1 = int(input("ingrese primer numero"))
numero2 = int(input("ingrese segundo numero"))

if numero1 > numero2:
    print("el primer numero es mayor")
elif numero1 < numero2:
    print("tu primer numero es menor")
else:
    print("tus numeros son iguales")