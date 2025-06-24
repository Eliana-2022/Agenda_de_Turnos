import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime

# MODELOS - Clases base del sistema

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.turnos = []

    def reservar_turno(self, turno):
        self.turnos.append(turno)


class Servicio:
    def __init__(self, id_servicio, nombre, duracion):
        self.id = id_servicio
        self.nombre = nombre
        self.duracion = duracion


class Turno:
    def __init__(self, fecha_hora, servicio):
        self.fecha_hora = fecha_hora
        self.servicio = servicio
        self.estado = "Reservado"
        self.cliente_nombre = "Sin nombre"  # valor por defecto

    def __str__(self):
        return f"{self.servicio.nombre} | {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} | {self.estado} | {self.cliente_nombre}"


# DATOS -> Lista de servicios 

servicios = [
    Servicio(1, "Musicoterapia", 60),
    Servicio(2, "Consulta médica", 45),
    Servicio(3, "Kinesiología", 60)
]

usuario_actual = Usuario("Equipo 7", "equipo7@mail.com")  # Usuario ficticio "logueado".

# INTERFAZ GRÁFICA CON TKINTER

class AppTurnos:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Turnos")

        self.frame_menu = tk.Frame(root, padx=20, pady=20)
        self.frame_menu.pack()

        tk.Label(self.frame_menu, text=f"Bienvenid@ {usuario_actual.nombre}", font=("Roboto", 16)).pack(pady=10)
        tk.Button(self.frame_menu, text="Servicios Disponibles", width=25, command=self.mostrar_servicios).pack(pady=5)
        tk.Button(self.frame_menu, text="Reservar Turno", width=25, command=self.abrir_reserva).pack(pady=5)
        tk.Button(self.frame_menu, text="Ver Mis Turnos", width=25, command=self.mostrar_turnos).pack(pady=5)
        tk.Button(self.frame_menu, text="Salir", width=25, command=root.quit).pack(pady=5)

    def mostrar_servicios(self):
        top = tk.Toplevel(self.root)
        top.title("Servicios Disponibles")
        for s in servicios:
            tk.Label(top, text=f"{s.nombre} - {s.duracion} min", padx=10, pady=5).pack()

    def abrir_reserva(self): 
        reserva_win = tk.Toplevel(self.root)
        reserva_win.title("Reservar Turno")

        tk.Label(reserva_win, text="Seleccione servicio:").pack()
        servicio_var = tk.StringVar()
        servicio_combo = ttk.Combobox(reserva_win, textvariable=servicio_var, state="readonly")
        servicio_combo['values'] = [s.nombre for s in servicios]
        servicio_combo.pack()

        tk.Label(reserva_win, text="Fecha y hora (DD/MM/AAAA HH:MM):").pack()
        fecha_entry = tk.Entry(reserva_win)
        fecha_entry.pack()

        def confirmar_reserva():
            nombre_servicio = servicio_var.get()
            servicio = next((s for s in servicios if s.nombre == nombre_servicio), None)
            if not servicio:
                messagebox.showerror("Error", "Seleccione un servicio.")
                return

            try:
                fecha = datetime.strptime(fecha_entry.get(), "%d/%m/%Y %H:%M")
                if fecha < datetime.now():
                    messagebox.showerror("Error", "La fecha debe ser futura.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha inválido.")
                return

            nombre_apellido = simpledialog.askstring("Datos del cliente", "Ingrese su nombre y apellido:")
            if not nombre_apellido or not nombre_apellido.strip():
                messagebox.showwarning("Falta información", "Debe ingresar su nombre y apellido.")
                return

            turno = Turno(fecha, servicio)
            turno.cliente_nombre = nombre_apellido.strip()

            usuario_actual.reservar_turno(turno)
            messagebox.showinfo("Éxito", f"Turno reservado para {nombre_apellido.strip()}.")
            reserva_win.destroy()

        tk.Button(reserva_win, text="Confirmar", command=confirmar_reserva).pack(pady=10)

    def mostrar_turnos(self):
        top = tk.Toplevel(self.root)
        top.title("Mis Turnos")

        if not usuario_actual.turnos:
            tk.Label(top, text="No tenés turnos reservados.").pack(pady=10)
            return

        for t in usuario_actual.turnos:
            tk.Label(top, text=str(t)).pack(padx=10, pady=5)

# EJECUCIÓN DEL PROGRAMA

if __name__ == "__main__":
    root = tk.Tk()
    app = AppTurnos(root)
    root.mainloop()