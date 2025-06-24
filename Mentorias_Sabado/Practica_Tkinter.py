from tkinter import Tk, Entry, Button, END

#Funcion que agrega el numero presionando al Entry
def agregar_valor(valor):
    datos.insert(END, valor)

#Tamaño de la calculadora

ventana = Tk()
ventana.title("Calculadora TK")
ventana.configure(background="grey")
ventana.geometry("350x350")
ventana.resizable(False,False)

#Display calculadora
datos= Entry(ventana)
datos.grid(columnspan=15, ipadx=150, ipady=10)

#Botones
boton1 = Button(ventana, text="1", fg= 'black', bg= 'white', height="2", width="6", command=lambda: agregar_valor("1"))
boton1.grid(columnspan=2, ipadx=1, ipady=0)

ventana.mainloop()

