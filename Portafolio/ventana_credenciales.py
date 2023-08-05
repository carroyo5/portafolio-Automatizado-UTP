import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
#Configuración de la Ventana principal
credenciales = tk.Tk()
credenciales.title('PA- Portafolio automatizado')
credenciales.geometry('1280x720')
credenciales.resizable(width=False, height=False)

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
        archivo_seleccionado = tk.PhotoImage(file=imagen_seleccionada)
        mostrar_imagen.config(image=archivo_seleccionado)
        mostrar_imagen.image = archivo_seleccionado
    else:
        cargar_imagen_default()

#Texto que indica ayuda
tk.Label(credenciales, text="¿Necesitas ayuda? Pulsa este boton!").place(x=1000, y=14)
#Configuracion del boton imagen
imagen_ayuda = tk.PhotoImage(file = r'.\Portafolio\imagenes\info_button.png')
tk.Button(credenciales,image=imagen_ayuda, 
          command= boton_ayuda, 
          width= 38, height=38).place(x=1200, y=0)
#titulo
tk.Label(credenciales, text='Portafolio Automatizado', font=('Arial', 16)).pack()
imagen_buscador = tk.PhotoImage(file = r'.\Portafolio\imagenes\imagen_buscador.png')
#Label para mostrar la imagen
mostrar_imagen = tk.Label(credenciales, width=400, height=400)
mostrar_imagen.pack()
#Funcion para cargar la imagen por defecto
cargar_imagen_default()
#Configuracion del boton buscar imagen
boton_buscar_imagen = ttk.Button(credenciales, text='Buscar una imagen...',
           style='BotonPersonalizado.TButton',
           image=imagen_buscador,
           compound='left', 
           command=seleccion_imagen)
boton_buscar_imagen.pack()

#Input nombre de la materia
tk.Label(text='Introduce el nombre de la materia').pack()
tk.Entry(credenciales, textvariable=nombreMateria).pack()

tk.Label(text='Introduce tu nombre').pack()
tk.Entry(credenciales, textvariable=nombre).pack()

tk.Label(text='Introduce tu apellido').pack()
tk.Entry(credenciales, textvariable=apellido).pack()


#Boton para crear Portafolio y comprobar la informacion proporcionada
tk.Button(text='Crear Portafolio',
          height=2,
          width=20,
          command=lambda: comprobacion()).pack()

#Comprobacion del estado de la informacion
def comprobacion():
    try:
        if len(str(nombreMateria.get())) == 0:
            messagebox.showwarning('Error!', 'Debes introducir el nombre de la materia que estas cursando.').pack()
    except Exception as MensajeMateria:
        pass

credenciales.mainloop()