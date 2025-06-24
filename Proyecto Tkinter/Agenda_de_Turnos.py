import tkinter as tk
from tkinter import messagebox, ttk , simpledialog           # Módulos para mostrar cuadros de diálogos y widgets.
from tkcalendar import DateEntry                             # Calendario desplegable.
from datetime import datetime, time, timedelta               # Se usa para manejar fechas y horas. 

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

    def __str__(self):
        return f"{self.servicio.nombre} | {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} | {self.estado}"


# DATOS -> Lista de servicios 

servicios = [
    Servicio(1, "Musicoterapia", 60),
    Servicio(2, "Consulta clínica", 30),
    Servicio(3, "Kinesiología", 60),
    Servicio(4, "Fisiatría", 60),
    Servicio(5, "Traumatología", 30),
    Servicio(6, "Odontología", 60)
]

usuario_actual = Usuario("Equipo 7", "equipo7@mail.com")  # Usuario ficticio "logueado".

# INTERFAZ GRÁFICA CON TKINTER

class AppTurnos: # Clase gestora de la ventana principal y sus interacciones.
    def __init__(self, root):  # Constructor que recibe la ventana raíz (root) y configura la interfaz.
        self.root = root
        self.root.title("Agenda de Turnos")

        self.frame_menu = tk.Frame(root, padx=20, pady=20) # Frame -> Contenedor para agrupar widgets.
        self.frame_menu.pack() # pack() -> Método de posicionamiento automático (uno debajo del otro).

        tk.Label(self.frame_menu, text=f"Bienvenid@ {usuario_actual.nombre}", font=("Roboto", 16)).pack(pady=10) # Mensaje de bienvenida.
        
        # Botones de menú principal.
        # command=self.metodo -> Cada botón llama a un método diferente al hacer click.
        
        tk.Button(self.frame_menu, text="Servicios Disponibles", width=25,bg= "lightblue1", command=self.mostrar_servicios).pack(pady=5) # Muestra una lista.
        tk.Button(self.frame_menu, text="Reservar Turno", width=25,bg= "lightblue1", command=self.abrir_reserva).pack(pady=5)    # Abre un formulario.
        tk.Button(self.frame_menu, text="Ver Mis Turnos", width=25,bg= "lightblue1", command=self.mostrar_turnos).pack(pady=5)   # Muestra los turnos reservados.
        tk.Button(self.frame_menu, text="Cancelar Turno", width=25,bg= "lightblue1", command=self.cancelar_turno).pack(pady=5)   # Cancelación de turnos.
        tk.Button(self.frame_menu, text="Salir", width=25,bg= "lightblue1", command=root.quit).pack(pady=5)                      # Cierra la app.

    # MÉTODOS DE LA INTERFAZ

    def mostrar_servicios(self):
        top = tk.Toplevel(self.root) # Toplevel -> Crea una ventana secundaria.
        top.title("Servicios Disponibles")
        for s in servicios:
            tk.Label(top, text=f"{s.nombre} - {s.duracion} min", padx=10, pady=5).pack() # Label -> Etiquetas de los servicios disponibles.

    def abrir_reserva(self): 
        reserva_win = tk.Toplevel(self.root)
        reserva_win.title("Reservar Turno")

        tk.Label(reserva_win, text="Seleccione servicio:").pack(pady=(10,0)) # Selección del servicio
        servicio_var = tk.StringVar() # StringVar -> Variable que captura texto en interfaces.
        servicio_combo = ttk.Combobox(reserva_win, textvariable=servicio_var, state="readonly") # Combobox -> Menú desplegable de los servicios.
        servicio_combo['values'] = [s.nombre for s in servicios]
        servicio_combo.pack(pady=(10,0))

        tk.Label(reserva_win, text="Seleccione una fecha:").pack() # Calendario para la fecha
        fecha_cal = DateEntry(reserva_win, date_pattern='dd/MM/yyyy', mindate=datetime.now().date())
        fecha_cal.pack(pady=(0,10))
                
        tk.Label(reserva_win, text="Seleccione una hora:").pack() # Selección del horario en franjas 
        hora_var = tk.StringVar()
        horarios = [] # Franjas de los horarios
        
        t = time(8,0) # Turnos entre las 8 y las 12 horas.
        while t < time(12,0):
            horarios.append(t.strftime("%H:%M"))
            dt = datetime.combine(datetime.today(), t) + timedelta(minutes=30)
            t = dt.time()
        
        t= time(14,0) # Turnos entre las 14 y las 18 horas.
        while t < time(18,0):
            horarios.append(t.strftime("%H:%M"))
            dt = datetime.combine(datetime.today(), t) + timedelta(minutes=30)
            t = dt.time()
            
        hora_combo = ttk.Combobox(reserva_win, textvariable=hora_var, values=horarios, state="readonly")
        hora_combo.pack(pady=(0,10))
        
        def confirmar_reserva():
            nombre_servicio = servicio_var.get() # get() -> Obtiene el valor seleccionado.
            servicio = next((s for s in servicios if s.nombre == nombre_servicio), None) # next(...) -> Busca el servicio en la lista.
            if not servicio:
                messagebox.showerror("Error", "Seleccione un servicio.")
                return

            fecha_sel = fecha_cal.get_date() # Captura y combinación de fecha/hora.
            try:
                hora_sel = datetime.strptime(hora_var.get(), "%H:%M").time() # Convierte la cadena ingresada en objeto datetime.
            except ValueError:
                messagebox.showerror("Error", "Seleccione una fecha válida.")
                return
            
            fecha_hora = datetime.combine(fecha_sel, hora_sel)
                
            if fecha_hora < datetime.now(): # Validaciones de lógica.
                    messagebox.showerror("Error", "La fecha y hora debe ser futuras.") # Muestra mensaje de error si se ingresa una fecha pasada.
                    return
            if fecha_hora.weekday() == 6:
                    messagebox.showerror("Error", "Los días domingos no hay turnos disponibles.")
                    return
            
            nombre_apellido = simpledialog.askstring("Datos del cliente", "Ingrese su nombre y apellido:")
            if not nombre_apellido or not nombre_apellido.strip():
                messagebox.showwarning("Falta información", "Debe ingresar su nombre y apellido.")
                return
            
            turno = Turno(fecha_hora, servicio) # Creación y guardado del turno.
            turno.cliente_nombre = nombre_apellido.strip ()

            usuario_actual.reservar_turno(turno)
            messagebox.showinfo("Éxito", "Turno reservado.")
            reserva_win.destroy()
            
        tk.Button(reserva_win, text="Confirmar", command=confirmar_reserva).pack(pady=10)

    def mostrar_turnos(self): # Ventana que muestra los turnos del usuario.
        top = tk.Toplevel(self.root)
        top.title("Mis Turnos")

        if not usuario_actual.turnos:
            tk.Label(top, text="No tenés turnos reservados.").pack(pady=10)
            return

        for t in usuario_actual.turnos:
            tk.Label(top, text=str(t)).pack(padx=10, pady=5)
    
    def cancelar_turno(self):
        if not usuario_actual.turnos:
            messagebox.showinfo("Aviso", "No hay turnos para cancelar.")
            return

        cancelar_win = tk.Toplevel(self.root)
        cancelar_win.title("Cancelar Turno")

        tk.Label(cancelar_win, text="Seleccione un turno para cancelar:").pack(pady=5)

        turno_var = tk.StringVar()
        opciones = [f"{i+1}. {str(t)}" for i, t in enumerate(usuario_actual.turnos)]
        turno_combo = ttk.Combobox(cancelar_win, textvariable=turno_var, values=opciones, state="readonly", width=60)
        turno_combo.pack(pady=5)

        def confirmar_cancelacion():
            eleccion = turno_var.get()
            if not eleccion:
                messagebox.showerror("Error", "Debe seleccionar un turno.")
                return
            indice = int(eleccion.split(".")[0]) - 1
            turno_cancelado = usuario_actual.turnos.pop(indice)
            messagebox.showinfo("Cancelado", f"Turno cancelado:\n{turno_cancelado}")
            cancelar_win.destroy()

        tk.Button(cancelar_win, text="Confirmar Cancelación", command=confirmar_cancelacion).pack(pady=10)


# EJECUCIÓN DEL PROGRAMA

if __name__ == "__main__": # Se ejecuta al correr el archivo.
    root = tk.Tk()         # Crea de la ventana principal.
    app = AppTurnos(root)  # Inicializa la instancia de la interfaz.
    root.mainloop()        # Inicia el bucle manteniendo la ventana abierta para los eventos.