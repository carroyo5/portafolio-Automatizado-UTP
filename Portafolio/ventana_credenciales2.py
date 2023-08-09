import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from styles import get_app_style

class PantallaCredenciales(tk.Toplevel):
    def __init__(self, inicio)-> None:
        super().__init__(inicio)
        self.title('PA - Credenciales')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        estilo = get_app_style()
        self.DEPARTAMENTOS = ['Arquitectura y Redes de Computadoras']
        #Variables globales
        self.nombre_profesor = tk.StringVar()
        self.nombre_materia = tk.StringVar()
        self.grupo_curso = tk.StringVar()
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.departamento = tk.StringVar()
        self.ruta_tareas = tk.StringVar()
        #Texto que indica ayuda
        tk.Label(self, text="¿Necesitas ayuda? ¡Pulsa este boton!").place(x=1000, y=14)
        #Configuracion del boton imagen
        self.imagen_ayuda = tk.PhotoImage(file = r'.\Portafolio\imagenes\info_button.png')
        tk.Button(self,image=self.imagen_ayuda, 
                command= self.boton_ayuda, 
                width= 38, height=38).place(x=1200, y=0)
        #titulo
        tk.Label(self, text='Credenciales', font=('Inter Bold', 16)).pack()
        self.imagen_buscador = tk.PhotoImage(file = r'.\Portafolio\imagenes\imagen_buscador.png')
        #Label para mostrar la imagen
        self.mostrar_imagen = tk.Label(self, width=200, height=200)
        self.mostrar_imagen.place(x=95, y=50)

        self.boton_buscar_imagen = ttk.Button(self, text='Buscar una imagen...',
           style='BotonBuscarImagen.TButton',
           image=self.imagen_buscador,
           compound='left',
           command=self.seleccion_imagen)
        self.boton_buscar_imagen.place(x=75,y=265)

        #Funcion para cargar la imagen por defecto
        self.cargar_imagen_default()

        self.imagen_check = tk.PhotoImage(file = r'.\Portafolio\imagenes\check.png')
        self.boton_buscar_imagen = ttk.Button(self, text='Guardar cambios',
                style='BotonGuardarCambios.TButton',
                image=self.imagen_check,
                compound='left',
                command = lambda: self.guardar_cambios)
        self.boton_buscar_imagen.place(x=75,y=320)
        tk.Label(self,text='Introduce el nombre de la materia', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.nombre_materia).pack(ipadx=75)
        tk.Label(self,text='Introduce tu nombre', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.nombre).pack(ipadx=75)
        tk.Label(self,text='Introduce tu apellido', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.apellido).pack(ipadx=75)

    #Mensaje de ayuda para mostrarle al usuario como se usa el programa.
    def boton_ayuda(self):
        #Configuracion del mensaje
        self.ventana_ayuda = tk.Toplevel(self)
        self.ventana_ayuda.resizable(width=False, height=False)
        self.ventana_ayuda.title("Informacion sobre el uso del programa")
        #Mensaje
        self.mensaje = '''Este es un mensaje de ayuda
        es posible hacer esto?'''

        #configuracion del mensaje de ayuda
        tk.Message(self.ventana_ayuda, text=self.mensaje, width=300).pack()

    #Funcion para cargar la imagen por default
    def cargar_imagen_default(self):
        imagen_default = Image.open(r'.\Portafolio\imagenes\imagen_default.png')
        imagen_default = imagen_default.resize((200, 200))
        imagen_default = ImageTk.PhotoImage(image=imagen_default)
        self.mostrar_imagen.config(image=imagen_default)
        self.mostrar_imagen.image = imagen_default

    #Funcion para seleccionar carpetas
    def seleccion_imagen(self):
        imagen_seleccionada = filedialog.askopenfilename(filetypes=[('Imagenes', '*.png; *.jpg; *.jpeg')])
        if imagen_seleccionada:
            archivo_seleccionado = Image.open(imagen_seleccionada)
            archivo_seleccionado = archivo_seleccionado.resize((200, 200))
            archivo_seleccionado = ImageTk.PhotoImage(archivo_seleccionado)
            self.mostrar_imagen.config(image=archivo_seleccionado)
            self.mostrar_imagen.image = archivo_seleccionado
        else:
            self.cargar_imagen_default

    def guardar_cambios():
        pass
    #Comprobacion del estado de la informacion
    def comprobacion(self):
        try:
            if len(str(self.nombreMateria.get())) == 0:
                messagebox.showwarning('Error!', 'Debes introducir el nombre de la materia que estas cursando.').pack()
        except Exception as MensajeMateria:
            pass
    
if __name__ == '__main__':
    PantallaCredenciales().mainloop()
