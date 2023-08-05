import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import styles

#Configuración de la Ventana principal
credenciales = tk.Tk()
credenciales.title('PA- Portafolio automatizado')
credenciales.geometry('1280x720')
credenciales.resizable(width=False, height=False)
credenciales.style = styles.get_app_style()

DEPARTAMENTOS = ['Arquitectura y Redes de Computadoras', ]

#Variables globales
nombreProfesor = tk.StringVar()
nombreMateria = tk.StringVar()
grupoCurso = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
departamento = tk.StringVar()
rutaTareas = tk.StringVar()


#Mensaje de ayuda para mostrarle al usuario como se usa el programa.
def boton_ayuda():
    #Configuracion del mensaje
    ventana_ayuda = tk.Toplevel(credenciales)
    ventana_ayuda.resizable(width=False, height=False)
    ventana_ayuda.title("Informacion sobre el uso del programa")

    #Mensaje
    mensaje = '''Este es un mensaje de ayuda
    es posible hacer esto?'''

    #configuracion del mensaje de ayuda
    tk.Message(ventana_ayuda, text=mensaje, width=300).pack()

#Funcion para cargar la imagen por default
def cargar_imagen_default():
    imagen_default = Image.open(r'.\Portafolio\imagenes\imagen_default.png')
    imagen_default = imagen_default.resize((200, 200))
    imagen_default = ImageTk.PhotoImage(image=imagen_default)
    mostrar_imagen.config(image=imagen_default)
    mostrar_imagen.image = imagen_default

#Funcion para seleccionar carpetas
def seleccion_imagen():
    imagen_seleccionada = filedialog.askopenfilename(filetypes=[('Imagenes', '*.png; *.jpg; *.jpeg')])
    if imagen_seleccionada:
        archivo_seleccionado = Image.open(imagen_seleccionada)
        archivo_seleccionado = archivo_seleccionado.resize((200, 200))
        archivo_seleccionado = ImageTk.PhotoImage(archivo_seleccionado)
        mostrar_imagen.config(image=archivo_seleccionado)
        mostrar_imagen.image = archivo_seleccionado
    else:
        cargar_imagen_default()

def guardar_cambios():
    pass

#Texto que indica ayuda
tk.Label(credenciales, text="¿Necesitas ayuda? Pulsa este boton!").place(x=1000, y=14)
#Configuracion del boton imagen
imagen_ayuda = tk.PhotoImage(file = r'.\Portafolio\imagenes\info_button.png')
tk.Button(credenciales,image=imagen_ayuda, 
          command= boton_ayuda, 
          width= 38, height=38).place(x=1200, y=0)
#titulo
tk.Label(credenciales, text='Credenciales', font=('Inter Bold', 16)).pack()
imagen_buscador = tk.PhotoImage(file = r'.\Portafolio\imagenes\imagen_buscador.png')
#Label para mostrar la imagen
mostrar_imagen = tk.Label(credenciales, width=200, height=200)
mostrar_imagen.place(x=95, y=50)
#Funcion para cargar la imagen por defecto
cargar_imagen_default()
#Configuracion del boton buscar imagen
botonBuscarImagen = ttk.Style()
botonBuscarImagen.configure('BotonBuscarImagen.TButton', 
                 relief='flat', 
                 foreground='#555454', 
                 background='#B3D5EE',
                 width=20, 
                 height=20, 
                 borderwidth=20, font=('Inter Bold', 12))

boton_buscar_imagen = ttk.Button(credenciales, text='Buscar una imagen...',
           style='BotonBuscarImagen.TButton',
           image=imagen_buscador,
           compound='left',
           command=seleccion_imagen)
boton_buscar_imagen.place(x=75,y=265)

#Configuracion del boton de guardar cambios
botonGuardarCambios = ttk.Style()
botonGuardarCambios.configure('BotonGuardarCambios.TButton', 
                 relief='flat', 
                 foreground='#000000', 
                 background='#8EFF9A',
                 width=20, 
                 height=20, 
                 borderwidth=20, font=('Inter Bold', 12))

imagen_check = tk.PhotoImage(file = r'.\Portafolio\imagenes\check.png')
boton_buscar_imagen = ttk.Button(credenciales, text='Guardar cambios',
           style='BotonGuardarCambios.TButton',
           image=imagen_check,
           compound='left',
           command = lambda: guardar_cambios)
boton_buscar_imagen.place(x=75,y=320)

#Input nombre de la materia
tk.Label(text='Introduce el nombre de la materia', font=('Inter Bold',14)).pack(ipady=5)
tk.Entry(credenciales, textvariable=nombreMateria).pack(ipadx=75)

tk.Label(text='Introduce tu nombre', font=('Inter Bold',14)).pack(ipady=5)
tk.Entry(credenciales, textvariable=nombre).pack(ipadx=75)

tk.Label(text='Introduce tu apellido', font=('Inter Bold',14)).pack(ipady=5)
tk.Entry(credenciales, textvariable=apellido).pack(ipadx=75)

#Boton para crear Portafolio y comprobar la informacion proporcionada
ttk.Button(text='Crear Portafolio',command=lambda: comprobacion(), style= 'EstiloBotonesInferiores.TButton',).pack(side=tk.LEFT, padx=75)

#Comprobacion del estado de la informacion
def comprobacion():
    try:
        if len(str(nombreMateria.get())) == 0:
            messagebox.showwarning('Error!', 'Debes introducir el nombre de la materia que estas cursando.').pack()
    except Exception as MensajeMateria:
        pass

credenciales.mainloop()