import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from styles import get_app_style
from manipular_json import manipularJson
import json
import os


class PantallaCredenciales(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs) -> None:
        super().__init__(master,*args, **kwargs)
        self.title('PA - Credenciales')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        estilo = get_app_style()
        #Variables globales para almcenar la informacion
        self.nombre_profesor = tk.StringVar()
        self.nombre_materia = tk.StringVar()
        self.grupo_curso = tk.StringVar()
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.cedula = tk.StringVar()
        self.departamento = tk.StringVar()
        self.ruta_tareas = tk.StringVar()
        self.facultad = tk.StringVar()
        self.facultad.set('Selecciona tu facultad')
        self.carrera = tk.StringVar()
        self.carrera.set('Selecciona tu carrera')
        self.intereses = tk.StringVar()
        self.FACULTADES = self.obtener_facultades()
        self.CARRERAS = ['']
        #titulo
        tk.Label(self, text='Credenciales', font=('Inter Bold', 16)).pack()
        #Funcion para buscar imagen
        self.boton_buscar_imagen()
        #Funcion para cargar la imagen por defecto
        self.cargar_imagen_default()
        self.boton_ayuda()
        self.boton_guardar_cambios()    
        self.entrada_credenciales()
        self.checkbox()
        tk.Button(self, text='Volver', command=self.volver_inicio).pack()

    def entrada_credenciales(self):
        tk.Label(self,text='Selecciona tu facultad', font=('Inter Bold',14)).pack(ipady=5)
        combobox_facultades = ttk.Combobox(self, values=self.FACULTADES, 
                            state='readonly', 
                            width=max(len(facultad) for facultad in self.FACULTADES), 
                            textvariable=self.facultad)
        combobox_facultades.pack()
        combobox_facultades.bind('<<ComboboxSelected>>',self.actualizar_carreras)
        tk.Label(self,text='Selecciona tu carrera', font=('Inter Bold',14)).pack(ipady=5)
        self.combobox_carrera = ttk.Combobox(self, values=self.CARRERAS, 
                            state='readonly', 
                            width= 27, 
                            textvariable=self.carrera)
        self.combobox_carrera.pack()
        tk.Label(self,text='Introduce el nombre de la materia', font=('Inter Bold',14)).pack(ipadx=75)
        tk.Entry(self, textvariable=self.nombre_materia).pack(ipadx=75)
        tk.Label(self,text='Introduce tu grupo', font=('Inter Bold',14)).pack(ipadx=75)
        tk.Entry(self, textvariable=self.grupo_curso).pack(ipadx=75)
        tk.Label(self,text='Introduce el nombre del profesor', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.nombre_profesor).pack(ipadx=75)
        tk.Label(self,text='Introduce tu nombre', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.nombre).pack(ipadx=75)
        tk.Label(self,text='Introduce tu apellido', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.apellido).pack(ipadx=75)
        tk.Label(self, text='Introduce la cedula', font=('Inter Bold',14)).pack()
        tk.Entry(self, textvariable=self.cedula).pack(ipadx=75)
        tk.Label(self, text='Introduce tus intereses', font=('Inter Bold',14)).pack(ipady=5)
        tk.Entry(self, textvariable=self.intereses).pack(ipadx=75, ipady=15)

        #Mensaje de ayuda para mostrarle al usuario como se usa el programa.

    def boton_buscar_imagen(self):
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

    def boton_ayuda(self):
        #Texto que indica ayuda
        tk.Label(self, text="¿Necesitas ayuda? ¡Pulsa este boton!").place(x=1000, y=14)
        #Configuracion del boton imagen
        self.imagen_ayuda = tk.PhotoImage(file = r'.\Portafolio\imagenes\info_button.png')
        tk.Button(self,image=self.imagen_ayuda, 
                command= self.funcion_boton_ayuda, 
                width= 38, height=38).place(x=1200, y=0)
        
    def boton_guardar_cambios(self):
        self.imagen_check = tk.PhotoImage(file = r'.\Portafolio\imagenes\check.png')
        self.boton_guardar_cambios = ttk.Button(
            self,
            text='Guardar cambios',
            style='BotonGuardarCambios.TButton',
            image=self.imagen_check,
            compound='left',
            command=lambda: self.guardar_cambios({
                'Credenciales': {
                    'Nombre': self.convertir(self.nombre),
                    'Apellido': self.convertir(self.apellido),
                    'Cedula': self.convertir(self.cedula),
                    'Materia': self.convertir(self.nombre_materia),
                    'Grupo': self.convertir(self.grupo_curso),
                    'Departamento': self.seleccion_departamento(),
                    'Profesor': self.convertir(self.nombre_profesor),
                    'Facultad': self.convertir(self.facultad),
                    'Carrera': self.convertir(self.carrera),
                },
                'Subcarpeta_actividades':{
                    'Tareas': self.convertir(self.variable_checkboxes[0]),
                    'Trabajos en clase': self.convertir(self.variable_checkboxes[1]),
                    'Proyectos': self.convertir(self.variable_checkboxes[2]),
                    'Laboratorios': self.convertir(self.variable_checkboxes[3]),
                    'Talleres': self.convertir(self.variable_checkboxes[4])
                }
            })
        )
        self.boton_guardar_cambios.place(x=75, y=320)


    def funcion_boton_ayuda(self):
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
            self.cargar_imagen_default()

    #Metodo para manipular la informacion de los credenciales con el json
    def guardar_cambios(self, credenciales):
        archivo_json = manipularJson()
        if os.path.exists(archivo_json.ruta_completa):
            archivo_json.actualizar_json(credenciales)
        else:
            archivo_json.crear_json(credenciales)

    def checkbox(self):
        self.variable_checkboxes = []
        opciones = ('Tareas', 'Trabajos en clase', 'Proyectos', 'Laboratorios', 'Talleres')
        for opcion in opciones:
            respuesta = tk.BooleanVar()
            self.variable_checkboxes.append(respuesta)
            ttk.Checkbutton(self, text=opcion, variable=respuesta).pack()

    def volver_inicio(self):
        self.destroy()
        self.master.deiconify()

    def convertir(self, dato):
        if isinstance(dato, tk.StringVar):
            return str(dato.get())
        elif isinstance(dato, tk.BooleanVar):
            return bool(dato.get())

    def obtener_facultades(self):
        lista_facultades = []
        with open(r'.\Portafolio\recursos\datos_universidad.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        for facultad in datos['Facultades']:
            lista_facultades.append(facultad)
        return lista_facultades
    
    def actualizar_carreras(self, event):
            facultad_seleccionada = self.facultad.get()
            self.obtener_carreras(facultad_seleccionada)
            return
    
    def seleccion_departamento(self):
        with open (r'.\Portafolio\recursos\datos_universidad.json', 'r', encoding='utf-8')as archivo:
            datos = json.load(archivo)
        facultad_seleccionada = self.facultad.get()
        carrera_seleccionada = self.carrera.get()
        carreras = list(datos['Carreras'][facultad_seleccionada])
        departamentos = list(datos['Departamentos'])
        if facultad_seleccionada =='Facultad de Ingeniería de Sistemas Computacionales':
            try:
                if carrera_seleccionada in [carreras[8], carreras[4]]:
                    return str(departamentos[1])
                elif carrera_seleccionada in [carreras[2], carreras[5], carreras[7]]:
                    return str(departamentos[0])
                elif carrera_seleccionada == carreras[3]:
                    return str(departamentos[2])
                elif carrera_seleccionada in [carreras[6], carreras[11], carreras[10], carreras[12]]:
                    return str(departamentos[3])
                elif carrera_seleccionada in [carreras[0], carreras[1], carreras[9]]:
                    return str(departamentos[4])
            except Exception as e:
                print (e)
        else:
            return None
    
    def obtener_carreras(self,facultad_seleccionada):
        with open (r'.\Portafolio\recursos\datos_universidad.json', 'r', encoding='utf-8')as archivo:
            datos_carrera = json.load(archivo)

        if facultad_seleccionada == 'Selecciona tu facultad':
            return
        else:
            self.CARRERAS.clear()
            self.CARRERAS.extend(datos_carrera['Carreras'][facultad_seleccionada])
            self.combobox_carrera['values'] = self.CARRERAS
            self.combobox_carrera['width'] = int(max(len(carrera) for carrera in self.CARRERAS)) - 8
        
        #Comprobacion del estado de la informacion
    def comprobacion(self):

        try:
            if len(self.nombreMateria.get()) == 0:
                messagebox.showwarning('Error!', 'Debes introducir el nombre de la materia que estas cursando.').pack()
                return
            elif len(self.nombre.get()) == 0:
                messagebox.showwarning('Error!', 'Debes introducir tu nombre antes de guardar los cambios.').pack()
                return
            elif len(self.apellido.get()) == 0:
                messagebox.showwarning('Error!', 'Debes introducir tu apellido antes de guardar los cambios.').pack()
                return
            elif len(self.grupo_curso.get()) == 0:
                messagebox.showwarning('Error!', 'Debes introducir el grupo del curso en el que te encuentras antes de continuar.').pack()
                return
            elif len(self.nombre_profesor.get()) == 0:
                messagebox.showwarning('Error!', '¡Necesitamos saber el nombre de tu profesor para hacer el portafolio!.').pack()
                return
            elif len(self.facultad.get()) == 'Selecciona tu facultad':
                messagebox.showwarning('Error!', 'Debes elegir una de las facultades para poder continuar.').pack()
                return
            elif len(self.carrera.get()) == 'Selecciona tu carrera':
                messagebox.showwarning('Error!', 'Debes elegir una de las carreras para poder continuar.').pack()
                return
            #Comprobar que la carrera esta dentro de la facultad que se eligió
            else:
                with open (r'.\Portafolio\recursos\datos_universidad.json', 'r', encoding='utf-8')as archivo:
                    datos = json.load(archivo)
                facultad_seleccionada = self.facultad.get()
                carrera_seleccionada = self.carrera.get()
                carreras = list(datos['Carreras'][facultad_seleccionada])
                if not carrera_seleccionada in carreras:
                    messagebox.showerror('ERROR', 'Intenta elegir una carrera dentro de tu facultad')
                    return
        except Exception as e:
            messagebox.showerror('ERROR', f'Hubo un error inesperado, reinicia el programa :(.{e}')
