#Escribe un programa que solicite al usuario su peso y su altura y luego calcule e imprima su indice de masa corporal (inc)
#INC= peso / estatura

peso = float(input("ingrese su peso en kilogramo"))
altura= float(input("ingrese su altura en metros"))
inc = peso / altura ** 2 

print ("su inc es:", inc)