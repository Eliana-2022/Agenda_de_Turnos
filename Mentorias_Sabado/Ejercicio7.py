#Crear un programa que pida al usuario y contraseña y en caso de ser incorrecto, volver a pedir
usuario = input ('ingrese su nombre de usuario')
contraseña = input ('ingrese su contraseña')

while usuario != 'Informatorio' and contraseña != 'Info 2025':
    print ('El usuario o contraseña ingresado son incorrectos. Intentá nuevamente')
    usuario = input ('ingrese su usuario:')
    contraseña = input ('ingrese su contraseña:')
else:
    print('Ingresaste correctamente.Bienvenido')