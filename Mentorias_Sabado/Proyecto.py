"""import tkinter as tk

ventana = tk.Tk()
ventana.title('Agenda de Turnos')
ventana.geometry('400x200')
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)


barra_menu.add_cascade(label =
'Elija su día', menu=menu_principal)
submenu = tk.Menu(menu_principal)

menu_principal.add_cascade(label =
'Lunes', menu=submenu)
menu_principal.add_cascade(label =
'Martes', menu=submenu)
menu_principal.add_cascade(label =
'Miercoles', menu=submenu)
menu_principal.add_cascade(label =
'Jueves', menu=submenu)
menu_principal.add_cascade(label =
'Viernes', menu=submenu)

submenu.add_command(label = '8 - 9')
submenu.add_command(label = '9 - 10')
submenu.add_command(label = '10 - 11')
submenu.add_command(label = '11 - 12')
submenu.add_command(label = '12 - 13')
submenu.add_command(label = '13 - 14')
submenu.add_command(label = '14 - 15')
submenu.add_command(label = '15 - 16')
submenu.add_command(label = '16 - 17')
submenu.add_command(label = '17 - 18')
submenu.add_command(label = '18 - 19')
submenu.add_command(label = '19 - 20')

ventana.mainloop()"""

#Otro codigo
"""import tkinter as tk
from tkinter import simpledialog, messagebox
class App:
     def ___init__(self, root):
        self.root = root
        root.title("Gestor de Turnos")

        self.turnos = [
            "2025-06-21 09:00",
            "2025-06-21 10:00",
            "2025-06-21 11:00",
        ]
        self.reservas = {}  # turno -> cliente

        self.listbox = tk.Listbox(root, height=10, width=30)
        self.listbox.pack(pady=10)
        self.update_listbox()

        self.btn = tk.Button(root, text="Reservar turno", command=self.reserve)
        self.btn.pack(pady=5)

     def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for t in self.turnos:
            estado = self.reservas.get(t, "Disponible")
            self.listbox.insert(tk.END, f"{t} — {estado}")

     def reserve(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccioná un turno")
            return
        turno = self.turnos[sel[0]]
        if turno in self.reservas:
            messagebox.showinfo("Info", "Ese turno ya está reservado")
            return

        nombre = simpledialog.askstring("Cliente", "Nombre del cliente:")
        if nombre:
            self.reservas[turno] = nombre
            self.update_listbox()

if __name__== "__main__":
    print("ejecutando ventana")
    root = tk.Tk()
    app = App(root)
    root.mainloop()"""

#Ultima integrada
"""import tkinter as tk
from tkinter import simpledialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        root.title("Agenda de Turnos")
        root.geometry("450x300")

        # Diccionario de turnos reservados: clave = (día, hora), valor = (nombre, servicio)
        self.reservas = {}

        # Menú principal superior
        barra_menu = tk.Menu(root)
        root.config(menu=barra_menu)

        menu_dias = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Elegí el Día", menu=menu_dias)

        self.horarios = [
            "8 - 9", "9 - 10", "10 - 11", "11 - 12", "12 - 13",
            "13 - 14", "14 - 15", "15 - 16", "16 - 17", "17 - 18",
            "18 - 19", "19 - 20"
        ]
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        for dia in self.dias:
            submenu = tk.Menu(menu_dias, tearoff=0)
            for hora in self.horarios:
                submenu.add_command(
                    label=hora,
                    command=lambda d=dia, h=hora: self.reservar_turno(d, h)
                )
            menu_dias.add_cascade(label=dia, menu=submenu)

        # Selector de servicios
        tk.Label(root, text="Seleccioná el servicio:").pack(pady=5)
        self.servicios = ["Corte de pelo", "Coloración", "Manicura", "Depilación"]
        self.servicio_var = tk.StringVar(value=self.servicios[0])
        tk.OptionMenu(root, self.servicio_var, *self.servicios).pack()

        # Lista para mostrar las reservas
        self.lista = tk.Listbox(root, width=50, height=10)
        self.lista.pack(pady=10)

        self.actualizar_lista()

    def reservar_turno(self, dia, hora):
        turno = f"{dia} {hora}"

        if turno in self.reservas:
            messagebox.showinfo("Turno reservado", f"Este turno ya fue reservado por {self.reservas[turno][0]}")
            return

        nombre = simpledialog.askstring("Nombre", "¿Cuál es tu nombre?")
        if not nombre:
            return

        servicio = self.servicio_var.get()
        self.reservas[turno] = (nombre, servicio)
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for turno, (cliente, servicio) in sorted(self.reservas.items()):
            self.lista.insert(tk.END, f"{turno} - {cliente} ({servicio})")

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()"""

