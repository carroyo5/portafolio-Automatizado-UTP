import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog
from tkinter import messagebox
from styles import get_app_style
from ventana_credenciales import PantallaCredenciales
from ventana_creacion import PantallaCreacion
import json
from manipular_json import manipularJson
import _tkinter
from crear_portafolio import crearPortafolio

class PantallaInicio(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title('PA - Portafolio Automatizado')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.funcion_boton_salir)
        self.carpeta_seleccionada = ''
        #Obtener los estilos del archivo styles
        estilo = get_app_style()
        #Titulo
        tk.Label(self, text= 'Portafolio Automatizado', font=('Inter Bold',16)).pack()
        #imagen del logo
        self.imagen_logo = tk.PhotoImage(file = r'.\Portafolio\imagenes\Logo.png')
        ttk.Label(self, image = self.imagen_logo).place(x=570, y=150)
        #Salto
        tk.Label(text='').pack()
        self.seleccionar_ruta_portafolio()
        #Cargar credenciales del usuario
        self.boton_crear_portafolio()
        self.boton_credenciales()
        self.boton_salir()

    def seleccionar_ruta_portafolio(self):
        #Configuracion completa del boton de seleccion de carpeta
        self.imagen_buscador = tk.PhotoImage(file = r'.\Portafolio\imagenes\imagen_buscador.png')
        self.boton_portafolio = ttk.Button(self, text='Selecciona la ruta donde quieres guardar tu portafolio',
           style='BotonPersonalizado.TButton',
           image=self.imagen_buscador,
           compound='left', 
           command= lambda: self.seleccion_carpeta())
        self.boton_portafolio.pack()
        self.ruta = tk.Label(self, text='')
        self.ruta.pack()

    def boton_crear_portafolio(self):
            self.imagen_nuevo_portafolio = tk.PhotoImage(file= r'.\Portafolio\imagenes\nuevo_archivo.png')
            #Boton para crear un portafolio nuevo
            self.boton_nuevo_portafolio = ttk.Button(text='Crear nuevo portafolio',
                        style= 'EstiloBotonesInferiores.TButton',
                        image= self.imagen_nuevo_portafolio,
                        compound='left', command= self.crear_carpetas).place(x=80, y=200)

    def boton_credenciales(self):
           #Imagen de las credenciales
        self.imagen_credenciales = tk.PhotoImage(file= r'.\Portafolio\imagenes\credenciales.png')
        #Boton para crear llenar la informacion de los credenciales
        self.boton_nuevo_credenciales = ttk.Button(text='Mis credenciales',
            style= 'EstiloBotonesInferiores.TButton',
            image= self.imagen_credenciales,
            command= self.pantalla_credenciales,
            compound='left').place(x=80, y=300)

    def boton_salir(self):
        #Imagen para salir
        self.imagen_salir = tk.PhotoImage(file= r'.\Portafolio\imagenes\salir2.png')
        self.boton_salir = ttk.Button(text='Salir',
            style= 'EstiloBotonesInferiores.TButton',
            image= self.imagen_salir,
            compound='left', command= self.funcion_boton_salir).place(x=80, y=400)
        tk.Label(text='Hecho por y para estudiantes con mucho ♥', font=('Inter Regular',12)).place(x=30,y=680)

    #Funcion de seleccion de carpeta
    def seleccion_carpeta(self):
        self.carpeta_seleccionada = filedialog.askdirectory()
        if self.carpeta_seleccionada:
            self.ruta.config(text=f'Ruta seleccionada: {self.carpeta_seleccionada}', 
                        font=('Inter Bold', 12), 
                        foreground='#75AD3C')
        else:
            self.ruta.config(text='No se ha seleccionado ninguna carpeta.',
                        font=('Inter Bold', 12), 
                        foreground='red')

    def crear_carpetas(self):
            crear= crearPortafolio(self.carpeta_seleccionada)

    #Funcion del boton salir y cerrar la pantalla
    def funcion_boton_salir(self):
        self.destroy()
        manipulador = manipularJson()
        manipulador.borrar_json()

    def pantalla_creacion(self):
        self.withdraw()
        pantalla_creacion = PantallaCreacion(self)
        pantalla_creacion.mainloop()
        self.deiconify()

    def pantalla_credenciales(self):
        try:
            self.withdraw()
            pantalla_credenciales = PantallaCredenciales(self)
            pantalla_credenciales.mainloop()
            self.deiconify()
        except _tkinter.TclError as wm_command:
            print(wm_command)

if __name__ == '__main__':
    PantallaInicio().mainloop()